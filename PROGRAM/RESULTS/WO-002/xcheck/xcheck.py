#!/usr/bin/env python3
"""Independent cross-check of BRI1 (clamped Duffing) third-cumulant tensor K,
second-order covariance coefficient C2, A_abc and drho.

Written from scratch from the task spec only.

State per quadrature node (all integrated together, vectorised over nodes):
  0 x, 1 p                                  unforced orbit x0(t)
  for protocol k in {0,1} (P1,P2): base 2+4k
     y1, y1', y2, y2'                       first/second-order variational responses
  for protocol k, eps index e: base 10 + 2*(3k+e)
     d, d'   with d = X^eps - x0 (exact nonlinear deviation, no cancellation)
"""
import json
import sys
import time

import numpy as np
from numpy.polynomial.hermite_e import hermegauss
from scipy.integrate import solve_ivp
from scipy.integrate._ivp import dop853_coefficients as dc

PI = np.pi
TAU = (PI, 1.5 * PI, 2.0 * PI)
NAMES = ("pi", "3pi/2", "2pi")
EPS = (1e-2, 5e-3, 2.5e-3)
NE = len(EPS)
NC = 10 + 2 * 2 * NE
TRIPLES = [(a, b, c) for a in range(3) for b in range(a, 3) for c in range(b, 3)]
PAIRS = [(0, 1), (0, 2), (1, 2)]


def smooth(u):
    return u * u * u * (10.0 + u * (-15.0 + 6.0 * u))


def make_rhs(seg):
    """seg 0: t in [0,pi]; seg 1: t in [pi,2pi]."""
    epsv = np.array(EPS).reshape(1, NE, 1)

    def f(t, Y):
        N = Y.shape[-1]
        x = Y[0]
        out = np.empty_like(Y)
        x2 = x * x
        out[0] = Y[1]
        out[1] = -x - x * x2
        if seg == 0:
            s = smooth(t / PI)
            q = np.array([s, s])
        else:
            q = np.array([1.0, 1.0 + smooth((t - PI) / PI)])
        kk = 1.0 + 3.0 * x2
        Yv = Y[2:10].reshape(2, 4, N)
        Ov = out[2:10].reshape(2, 4, N)
        y1 = Yv[:, 0]
        Ov[:, 0] = Yv[:, 1]
        Ov[:, 1] = q[:, None] - kk * y1
        Ov[:, 2] = Yv[:, 3]
        Ov[:, 3] = -kk * Yv[:, 2] - 6.0 * x * y1 * y1
        Yd = Y[10:].reshape(2, NE, 2, N)
        Od = out[10:].reshape(2, NE, 2, N)
        d = Yd[:, :, 0]
        Od[:, :, 0] = Yd[:, :, 1]
        Od[:, :, 1] = epsv * q[:, None, None] - d - d * (3.0 * x2 + d * (3.0 * x + d))
        return out

    return f


_A = dc.A[:12, :12]
_B = dc.B
_C = dc.C[:12]


def rk8(f, t0, t1, Y, n):
    """Fixed-step 8th-order explicit RK (Dormand-Prince 8(5,3) main tableau)."""
    h = (t1 - t0) / n
    K = [None] * 12
    nz = [[j for j in range(s) if _A[s, j] != 0.0] for s in range(12)]
    nzb = [j for j in range(12) if _B[j] != 0.0]
    for i in range(n):
        t = t0 + i * h
        K[0] = f(t, Y)
        for s in range(1, 12):
            dY = (h * _A[s, nz[s][0]]) * K[nz[s][0]]
            for j in nz[s][1:]:
                dY += (h * _A[s, j]) * K[j]
            dY += Y
            K[s] = f(t + _C[s] * h, dY)
        dY = (h * _B[nzb[0]]) * K[nzb[0]]
        for j in nzb[1:]:
            dY += (h * _B[j]) * K[j]
        Y = Y + dY
    return Y


def propagate_rk8(X0, P0, n0):
    """n0 steps on [0,pi], n0/2 on [pi,3pi/2], n0/2 on [3pi/2,2pi]."""
    Y = np.zeros((NC, X0.size))
    Y[0] = X0
    Y[1] = P0
    out = []
    Y = rk8(make_rhs(0), 0.0, PI, Y, n0)
    out.append(Y.copy())
    Y = rk8(make_rhs(1), PI, 1.5 * PI, Y, n0 // 2)
    out.append(Y.copy())
    Y = rk8(make_rhs(1), 1.5 * PI, 2.0 * PI, Y, n0 // 2)
    out.append(Y.copy())
    return np.stack(out)  # (3, NC, N)


def propagate_dop853(X0, P0, tol):
    """scipy adaptive DOP853, segments [0,pi], [pi,2pi] (t_eval 3pi/2)."""
    N = X0.size
    Y = np.zeros((NC, N))
    Y[0] = X0
    Y[1] = P0
    out = []
    f0 = make_rhs(0)
    f1 = make_rhs(1)
    sol = solve_ivp(lambda t, y: f0(t, y.reshape(NC, N)).ravel(), (0.0, PI), Y.ravel(),
                    method="DOP853", rtol=tol, atol=tol)
    Y = sol.y[:, -1].reshape(NC, N)
    out.append(Y.copy())
    nfev = sol.nfev
    sol = solve_ivp(lambda t, y: f1(t, y.reshape(NC, N)).ravel(), (PI, 2 * PI), Y.ravel(),
                    method="DOP853", rtol=tol, atol=tol, t_eval=[1.5 * PI, 2 * PI])
    out.append(sol.y[:, 0].reshape(NC, N))
    out.append(sol.y[:, 1].reshape(NC, N))
    nfev += sol.nfev
    return np.stack(out), nfev


# ---------------------------------------------------------------- quadrature
def sym1(x, w):
    x = 0.5 * (x - x[::-1])
    w = 0.5 * (w + w[::-1])
    return x, w


def freud_gauss(n, L=10.0, M=40001):
    """Gauss rule for w(x)=exp(-x^2/2-x^4/4) via Lanczos (full reorth.) on a
    fine trapezoid discretisation of the measure, then Golub-Welsch."""
    t = np.linspace(-L, L, M)
    wt = np.exp(-t * t / 2 - t ** 4 / 4) * (t[1] - t[0])
    mu0 = wt.sum()
    Q = np.zeros((n + 1, M))
    q = np.sqrt(wt)
    q /= np.linalg.norm(q)
    Q[0] = q
    alpha = np.zeros(n)
    beta = np.zeros(n)
    for k in range(n):
        v = t * Q[k]
        alpha[k] = Q[k] @ v
        v -= alpha[k] * Q[k]
        if k > 0:
            v -= beta[k - 1] * Q[k - 1]
        for _ in range(2):
            v -= Q[: k + 1].T @ (Q[: k + 1] @ v)
        beta[k] = np.linalg.norm(v)
        Q[k + 1] = v / beta[k]
    alpha[:] = 0.0  # symmetric weight
    J = np.diag(alpha) + np.diag(beta[: n - 1], 1) + np.diag(beta[: n - 1], -1)
    ev, V = np.linalg.eigh(J)
    wx = mu0 * V[0] ** 2
    return sym1(ev, wx)


def tensor(x, wx, p, wp, prune=1e-30):
    X, P = np.meshgrid(x, p, indexing="ij")
    W = np.outer(wx, wp)
    X, P, W = X.ravel(), P.ravel(), W.ravel()
    keep = W > prune * W.max()
    dropped = W[~keep].sum() / W.sum()
    return X[keep], P[keep], W[keep] / W[keep].sum(), dropped


def rule_gh_x4(n, prune=1e-30):
    x, wx = sym1(*hermegauss(n))
    wx = wx * np.exp(-x ** 4 / 4)
    p, wp = sym1(*hermegauss(n))
    return tensor(x, wx, p, wp, prune)


def rule_freud(nx, npp, prune=1e-30):
    x, wx = freud_gauss(nx)
    p, wp = sym1(*hermegauss(npp))
    return tensor(x, wx, p, wp, prune)


def rule_trap(h, Lx=4.5, Lp=8.5, prune=1e-30):
    kx = int(np.floor(Lx / h + 1e-9))
    kp = int(np.floor(Lp / h + 1e-9))
    x = np.arange(-kx, kx + 1) * h
    p = np.arange(-kp, kp + 1) * h
    wx = np.exp(-x * x / 2 - x ** 4 / 4)
    wp = np.exp(-p * p / 2)
    return tensor(x, wx, p, wp, prune)


# ---------------------------------------------------------------- statistics
def analyse(X0, W, S):
    W = W / W.sum()

    def E(f):
        return f @ W

    def cov(u, v):
        return np.einsum("n,an,bn->ab", W, u, v) - np.outer(E(u), E(v))

    def k3(z):
        dz = z - E(z)[:, None]
        return np.einsum("n,an,bn,cn->abc", W, dz, dz, dz)

    m2 = E(X0 ** 2)
    m4 = E(X0 ** 4)
    x = S[:, 0, :]
    M = np.einsum("n,an,bn->ab", W, x, x)
    rho = M / m2
    res = {
        "m2": m2,
        "m4": m4,
        "m2+m4-1": m2 + m4 - 1.0,
        "E_x0": float(np.max(np.abs(E(x)))),
        "stationarity_dev": (np.diag(M) - m2).tolist(),
        "rho": rho.tolist(),
        "k3_x0_max": float(np.max(np.abs(k3(x)))),
    }
    k3x = k3(x)
    for k in range(2):
        tag = "P%d" % (k + 1)
        b = 2 + 4 * k
        y1 = S[:, b, :]
        y2 = S[:, b + 2, :]
        T = np.einsum("n,an,bn,cn->abc", W, x, x, y1) - np.einsum("ab,c->abc", M, E(y1))
        K = T + np.einsum("acb->abc", T) + np.einsum("bca->abc", T)
        C2 = cov(y1, y1) + 0.5 * (cov(x, y2) + cov(y2, x))
        parity = float(np.max(np.abs(cov(x, y1))))
        Kt = K / m2 ** 1.5
        A = np.zeros((3, 3, 3))
        for (a, bb, c) in TRIPLES:
            A[a, bb, c] = Kt[a, bb, c] - (Kt[a, a, a] * rho[a, bb] * rho[a, c]
                                          + Kt[bb, bb, bb] * rho[bb, a] * rho[bb, c]
                                          + Kt[c, c, c] * rho[c, a] * rho[c, bb]) / 3.0
        drho = [(C2[a, bb] - 0.5 * rho[a, bb] * (C2[a, a] + C2[bb, bb])) / m2 for (a, bb) in PAIRS]
        # nonlinear finite-eps method
        Knl, C2nl = [], []
        for e in range(NE):
            c = 10 + 2 * (k * NE + e)
            d = S[:, c, :]
            eps = EPS[e]
            Knl.append((k3(x + d) - k3x) / eps)
            C2nl.append((cov(x, d) + cov(d, x) + cov(d, d)) / eps ** 2)
        Knl = np.array(Knl)
        C2nl = np.array(C2nl)
        KR1 = (4 * Knl[1] - Knl[0]) / 3  # eps 1e-2, 5e-3
        KR1b = (4 * Knl[2] - Knl[1]) / 3  # eps 5e-3, 2.5e-3
        KR2 = (16 * KR1b - KR1) / 15
        CR1 = (4 * C2nl[1] - C2nl[0]) / 3
        CR1b = (4 * C2nl[2] - C2nl[1]) / 3
        CR2 = (16 * CR1b - CR1) / 15
        res[tag] = {
            "K": {f"({NAMES[a]},{NAMES[bb]},{NAMES[c]})": K[a, bb, c] for (a, bb, c) in TRIPLES},
            "K_full": K.tolist(),
            "C2": C2.tolist(),
            "parity_max": parity,
            "A": {f"({NAMES[a]},{NAMES[bb]},{NAMES[c]})": A[a, bb, c] for (a, bb, c) in TRIPLES},
            "drho": {f"({NAMES[a]},{NAMES[bb]})": v for (a, bb), v in zip(PAIRS, drho)},
            "nl": {
                "K_raw": Knl.tolist(),
                "C2_raw": C2nl.tolist(),
                "K_rich_1e-2_5e-3": KR1.tolist(),
                "K_rich3": KR2.tolist(),
                "C2_rich_1e-2_5e-3": CR1.tolist(),
                "C2_rich3": CR2.tolist(),
                "maxdiff_K_rich_vs_var": float(np.max(np.abs(KR1 - K))),
                "maxdiff_K_rich3_vs_var": float(np.max(np.abs(KR2 - K))),
                "maxdiff_C2_rich_vs_var": float(np.max(np.abs(CR1 - C2))),
                "maxdiff_C2_rich3_vs_var": float(np.max(np.abs(CR2 - C2))),
            },
        }
    return res


def run_rule(name, X, P, W, n0):
    t0 = time.time()
    S = propagate_rk8(X, P, n0)
    t1 = time.time()
    r = analyse(X, W, S)
    r["nodes"] = int(X.size)
    r["rk8_steps_per_pi"] = n0
    r["runtime_s"] = t1 - t0
    print(f"[{name}] nodes={X.size} n0={n0} time={t1-t0:.1f}s", flush=True)
    return r, S


if __name__ == "__main__":
    pass


def gh_gw(n):
    """Probabilists' Gauss-Hermite via Golub-Welsch (stable for large n)."""
    off = np.sqrt(np.arange(1, n, dtype=float))
    J = np.diag(off, 1) + np.diag(off, -1)
    ev, V = np.linalg.eigh(J)
    w = np.sqrt(2 * np.pi) * V[0] ** 2
    return sym1(ev, w)


def rule_gh_x4_gw(nx, npp=None, prune=1e-30):
    npp = nx if npp is None else npp
    x, wx = gh_gw(nx)
    wx = wx * np.exp(-x ** 4 / 4)
    p, wp = gh_gw(npp)
    return tensor(x, wx, p, wp, prune)


ARCH = "/tmp/claude-0/f0chain/R1/pf4q_results_archived.json"


def compare_archive(res):
    with open(ARCH) as fh:
        arch = json.load(fh)
    out = {}
    for tag in ("P1", "P2"):
        dev = {}
        for key, v in res[tag]["K"].items():
            dev[key] = v - arch[tag + key]["K_A06"]
        out[tag] = dev
    out["max_abs_dev"] = max(abs(v) for tag in ("P1", "P2") for v in out[tag].values())
    return out
