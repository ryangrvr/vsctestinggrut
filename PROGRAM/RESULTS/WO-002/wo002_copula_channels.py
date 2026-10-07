#!/usr/bin/env python3
"""WO-002 — BRI1 against coordinatewise monotone interfaces (T_mono): leading-order copula
coordinates on the frozen grid tau = (pi, 3pi/2, 2pi). Built by Claude Code (VS Code paused).

NUMERICAL EVIDENCE ONLY — NOT CERTIFIED. The quadrature has no certified error budget.
This is the same grade as BRI1-PF4Q, whose machinery (`R1/pf4q_core.py`, byte-identical
to the BRI1 record) is reused here.

Object (R1_T_LADDER.md section 5; rulings G2-03 and G2-04). Under T_mono the invariant is
the copula, modulo coordinate reflections. P0's copula is radially symmetric. At order
1/N_B, the copula difference P1 − P0 has two kinds of coordinates (formal Edgeworth
order):
  odd  : A_abc = Kt_abc − (1/3)[Kt_aaa rho_ab rho_ac + Kt_bbb rho_ba rho_bc
                                + Kt_ccc rho_ca rho_cb],
         with Kt = K/m2^(3/2). This is the third-cumulant tensor modulo per-coordinate
         quadratic deformations; it has C(k+2,3) − k free components.
  even : Delta rho_ab = [C2_ab − (1/2) rho_ab (C2_aa + C2_bb)] / m2, where
         Cov X^eps = Cov x0 + eps^2 C2 + O(eps^4), and
         C2_ab = Cov(y1_a, y1_b) + (1/2)[Cov(x0_a, y2_b) + Cov(y2_a, x0_b)],
         with y2 solving y2'' + (1 + 3 x0^2) y2 = −6 x0 y1^2.
Both enter the copula difference as (coordinate)/N_B + O(N_B^-2).

Methods:
  A: variational equations (x0, y1, y2), trapezoid rules h = 0.08, 0.06, plus a
     Gauss–Hermite n = 192 cross-check.
  B: nonlinear dynamics at small eps, Richardson in eps^2 for C2, trapezoid
     h = 0.12, 0.08.
  Finite N_B: nonlinear dynamics at eps = N_B^(−1/2). F's covariance and third
     cumulant follow exactly from X^eps via kappa_n(F) = N_B^(1−n/2) kappa_n(X^eps).
     The cumulant-level coordinates of F are then multiplied by N_B.

Exact controls (each can fail):
  - A_aaa = 0 (exact on stationarity-preserving rules; reported per rule);
  - marginal-only synthetic control gives A = 0;
  - parity: Cov(x0, y1) = 0;
  - stationarity: E x0(t)^2 = m2 at every t in tau;
  - Gibbs identity m2 + m4 = 1;
  - harmonic bath: K = 0 and C2 = 0;
  - recomputed K matches the archived PF4Q K.
"""
import json
import os
import sys
from itertools import combinations_with_replacement

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "R1"))
import pf4q_core as C  # noqa: E402  (frozen BRI1 machinery)

TAU = C.TAU
IDX = list(combinations_with_replacement(range(3), 3))     # 10 components
PAIRS = [(0, 1), (0, 2), (1, 2)]
NAMES = ["pi", "3pi/2", "2pi"]


def lab(t):
    return "(" + ",".join(NAMES[i] for i in t) + ")"


# ------------------------------------------------------------------ dynamics
def variational2(X0, P0, times, harmonic=False, tol=1e-13):
    """Rows: x, p, then for each protocol q in (1, 2): y1, y1dot, y2, y2dot.
    y1'' = -(1 + 3x^2) y1 + q(t);  y2'' = -(1 + 3x^2) y2 - 6 x y1^2   (harmonic: no x^3)."""
    M = len(X0)
    c3 = 0.0 if harmonic else 1.0

    def rhs(t, s):
        s = s.reshape(10, M)
        x, p = s[0], s[1]
        k = 1 + 3 * c3 * x * x
        out = [p, -x - c3 * x ** 3]
        for j, proto in enumerate((1, 2)):
            y1, v1, y2, v2 = s[2 + 4 * j: 6 + 4 * j]
            out += [v1, -k * y1 + C.q_of(proto, t), v2, -k * y2 - 6 * c3 * x * y1 ** 2]
        return np.concatenate(out)

    y0 = np.concatenate([X0, P0, np.zeros(8 * M)])
    out = C._run(rhs, y0, times, tol)
    res = {}
    for t, v in out.items():
        v = v.reshape(10, M)
        res[t] = {"x": v[0], 1: (v[2], v[4]), 2: (v[6], v[8])}
    return res


def nonlinear(X0, P0, eps, proto, times, tol=1e-12):
    return C.nonlinear(X0, P0, eps, proto, times, tol)


# ------------------------------------------------------------------ statistics
def cov(W, a, b):
    return W @ (a * b) - (W @ a) * (W @ b)


def A_tensor(Kt, rho):
    A = {}
    for (a, b, c) in IDX:
        A[(a, b, c)] = Kt[(a, b, c)] - (Kt[(a, a, a)] * rho[a][b] * rho[a][c]
                                        + Kt[(b, b, b)] * rho[b][a] * rho[b][c]
                                        + Kt[(c, c, c)] * rho[c][a] * rho[c][b]) / 3.0
    return A


def method_A(X, P, W, harmonic=False):
    sol = variational2(X, P, list(TAU), harmonic=harmonic)
    x = [sol[t]["x"] for t in TAU]
    m2 = float(W @ (X * X))
    m4 = float(W @ X ** 4)
    rho = [[float(W @ (x[a] * x[b])) / m2 for b in range(3)] for a in range(3)]
    stat = max(abs(float(W @ (x[a] * x[a])) - m2) for a in range(3))
    out = {"m2": m2, "m2_plus_m4_minus_1": m2 + m4 - 1, "stationarity_maxdev": stat,
           "rho": rho, "proto": {}}
    for proto in (1, 2):
        y1 = [sol[t][proto][0] for t in TAU]
        y2 = [sol[t][proto][1] for t in TAU]
        K = {(a, b, c): (C.c_term(W, x[a], x[b], y1[c]) + C.c_term(W, x[a], x[c], y1[b])
                         + C.c_term(W, x[b], x[c], y1[a])) for (a, b, c) in IDX}
        Kt = {k: v / m2 ** 1.5 for k, v in K.items()}
        C2 = [[cov(W, y1[a], y1[b]) + 0.5 * (cov(W, x[a], y2[b]) + cov(W, y2[a], x[b]))
               for b in range(3)] for a in range(3)]
        drho = {(a, b): (C2[a][b] - 0.5 * rho[a][b] * (C2[a][a] + C2[b][b])) / m2 for (a, b) in PAIRS}
        parity = max(abs(cov(W, x[a], y1[b])) for a in range(3) for b in range(3))
        out["proto"][proto] = {"K": K, "Kt": Kt, "A": A_tensor(Kt, rho), "C2": C2, "drho": drho,
                               "parity_cov_x0_y1_max": parity}
    return out


def method_B(X, P, W, eps_pair=(1e-2, 5e-3)):
    """C2 by Richardson in eps^2 from the nonlinear flow; K by Richardson in eps^2 from kappa3/eps."""
    x0 = nonlinear(X, P, 0.0, 1, list(TAU))
    x0 = [x0[t] for t in TAU]
    m2 = float(W @ (X * X))
    rho = [[cov(W, x0[a], x0[b]) / m2 for b in range(3)] for a in range(3)]
    res = {"rho": rho, "proto": {}}
    for proto in (1, 2):
        D, Kd = [], []
        for eps in eps_pair:
            xe = nonlinear(X, P, eps, proto, list(TAU))
            xe = [xe[t] for t in TAU]
            D.append([[(cov(W, xe[a], xe[b]) - cov(W, x0[a], x0[b])) / eps ** 2 for b in range(3)]
                      for a in range(3)])
            Kd.append({k: C.k3(W, xe[k[0]], xe[k[1]], xe[k[2]]) / eps for k in IDX})
        C2 = [[(4 * D[1][a][b] - D[0][a][b]) / 3 for b in range(3)] for a in range(3)]
        K = {k: (4 * Kd[1][k] - Kd[0][k]) / 3 for k in IDX}
        Kt = {k: v / m2 ** 1.5 for k, v in K.items()}
        drho = {(a, b): (C2[a][b] - 0.5 * rho[a][b] * (C2[a][a] + C2[b][b])) / m2 for (a, b) in PAIRS}
        res["proto"][proto] = {"K": K, "A": A_tensor(Kt, rho), "C2": C2, "drho": drho}
    return res


def finite_NB(X, P, W, NBs=(4, 8, 16, 32, 64, 128)):
    """Cumulant-level copula coordinates of F at finite N_B, times N_B."""
    x0 = nonlinear(X, P, 0.0, 1, list(TAU))
    x0 = [x0[t] for t in TAU]
    c0 = [[cov(W, x0[a], x0[b]) for b in range(3)] for a in range(3)]
    r0 = [[c0[a][b] / np.sqrt(c0[a][a] * c0[b][b]) for b in range(3)] for a in range(3)]
    out = {}
    for proto in (1, 2):
        rows = []
        for N in NBs:
            eps = N ** -0.5
            xe = nonlinear(X, P, eps, proto, list(TAU))
            xe = [xe[t] for t in TAU]
            cN = [[cov(W, xe[a], xe[b]) for b in range(3)] for a in range(3)]
            sd = [np.sqrt(cN[a][a]) for a in range(3)]
            rN = [[cN[a][b] / (sd[a] * sd[b]) for b in range(3)] for a in range(3)]
            # kappa3(F) = eps * kappa3(X^eps); standardized by sd(F) = sd(X^eps)
            Kt = {k: eps * C.k3(W, xe[k[0]], xe[k[1]], xe[k[2]]) / (sd[k[0]] * sd[k[1]] * sd[k[2]])
                  for k in IDX}
            A = A_tensor(Kt, rN)
            rows.append({"N_B": N,
                         "N_B_times_A": {lab(k): N * A[k] for k in IDX},
                         "N_B_times_drho": {lab(p): N * (rN[p[0]][p[1]] - r0[p[0]][p[1]]) for p in PAIRS}})
        out[proto] = rows
    return out


def marginal_only_control(seed=7):
    rng = np.random.default_rng(seed)
    G = rng.standard_normal((3, 5))
    S = G @ G.T
    d = np.sqrt(np.diag(S))
    rho = (S / np.outer(d, d)).tolist()
    c = rng.standard_normal(3)
    Kt = {}
    for (a, b, cc) in IDX:
        Kt[(a, b, cc)] = 2 * (c[a] * rho[a][b] * rho[a][cc] + c[b] * rho[b][a] * rho[b][cc]
                              + c[cc] * rho[cc][a] * rho[cc][b])
    A = A_tensor(Kt, rho)
    return max(abs(v) for v in A.values())


def harmonic_control(h=0.08, Lx=8.0, Lp=8.0):
    xs = h * np.arange(-int(Lx / h), int(Lx / h) + 1)
    ps = h * np.arange(-int(Lp / h), int(Lp / h) + 1)
    X, P = np.meshgrid(xs, ps, indexing="ij")
    W = np.exp(-(X ** 2 + P ** 2) / 2)
    X, P, W = X.ravel(), P.ravel(), (W / W.sum()).ravel()
    r = method_A(X, P, W, harmonic=True)
    return {"max_abs_K": max(abs(v) for pr in (1, 2) for v in r["proto"][pr]["K"].values()),
            "max_abs_C2": max(abs(v) for pr in (1, 2) for row in r["proto"][pr]["C2"] for v in row)}


def main():
    arch = json.load(open(os.path.join(ROOT, "R1", "pf4q_results_archived.json")))
    runs = {}
    for h in (0.08, 0.06):
        X, P, W = C.rule_trap(h)
        runs[f"A_h{h}"] = method_A(X, P, W)
    X, P, W, _ = C.rule_gh(192)
    runs["A_GH192"] = method_A(X, P, W)
    for h in (0.12, 0.08):
        X, P, W = C.rule_trap(h)
        runs[f"B_h{h}"] = method_B(X, P, W)
    X, P, W = C.rule_trap(0.08)
    fin = finite_NB(X, P, W)

    prim = runs["A_h0.06"]
    report = {"grade": "NUMERICAL EVIDENCE ONLY — NOT CERTIFIED",
              "tau": NAMES, "m2": prim["m2"], "rho_free": prim["rho"],
              "controls": {}, "odd_channel_A": {}, "even_channel_drho": {}, "finite_NB": {}}
    ctl = report["controls"]
    # A_aaa = Kt_aaa (1 - rho_aa^2): exact zero iff rho_aa = 1, i.e. iff the rule preserves
    # stationarity. Reported per rule: GH192 is a cross-check rule with a known ~1e-6
    # stationarity error (PF4Q treats it the same way).
    ctl["A_aaa_max_abs_by_rule"] = {r: max(abs(runs[r]["proto"][p]["A"][(i, i, i)])
                                           for p in (1, 2) for i in range(3))
                                    for r in runs if r.startswith("A_")}
    ctl["marginal_only_control_max_abs_A"] = marginal_only_control()
    ctl["parity_cov_x0_y1_max"] = max(runs[r]["proto"][p]["parity_cov_x0_y1_max"]
                                      for r in runs if r.startswith("A_") for p in (1, 2))
    ctl["stationarity_maxdev_by_rule"] = {r: runs[r]["stationarity_maxdev"] for r in runs if r.startswith("A_")}
    ctl["gibbs_m2_plus_m4_minus_1"] = {r: runs[r]["m2_plus_m4_minus_1"] for r in runs if r.startswith("A_")}
    ctl["harmonic_control"] = harmonic_control()
    kdev = 0.0
    for p in (1, 2):
        for k in IDX:
            a = arch[f"P{p}{lab(k)}"]["K_A06"]
            kdev = max(kdev, abs(runs["A_h0.06"]["proto"][p]["K"][k] - a))
    ctl["K_recomputed_vs_archived_K_A06_maxdev"] = kdev

    for p in (1, 2):
        for k in IDX:
            if k[0] == k[1] == k[2]:
                continue
            vals = {r: runs[r]["proto"][p]["A"][k] for r in runs}
            v = vals["A_h0.06"]
            spread = max(abs(x - v) for r, x in vals.items() if r != "A_GH192")
            report["odd_channel_A"][f"P{p}{lab(k)}"] = {
                "value": v, "spread": spread, "GH192": vals["A_GH192"],
                "ratio_to_spread": abs(v) / spread if spread > 0 else None,
                "methods": vals}
        for pr in PAIRS:
            vals = {r: runs[r]["proto"][p]["drho"][pr] for r in runs}
            v = vals["A_h0.06"]
            spread = max(abs(x - v) for r, x in vals.items() if r != "A_GH192")
            report["even_channel_drho"][f"P{p}({NAMES[pr[0]]},{NAMES[pr[1]]})"] = {
                "value": v, "spread": spread, "GH192": vals["A_GH192"],
                "ratio_to_spread": abs(v) / spread if spread > 0 else None,
                "methods": vals}
        report["finite_NB"][f"P{p}"] = fin[p]

    # preregistered reading (WO-002): ESCAPE-ODD / ESCAPE-EVEN if some coordinate >= 1e2 x spread
    for p in (1, 2):
        odd = any(v["ratio_to_spread"] is not None and v["ratio_to_spread"] >= 1e2
                  for k, v in report["odd_channel_A"].items() if k.startswith(f"P{p}"))
        even = any(v["ratio_to_spread"] is not None and v["ratio_to_spread"] >= 1e2
                   for k, v in report["even_channel_drho"].items() if k.startswith(f"P{p}"))
        report[f"reading_P{p}"] = (["ESCAPE-ODD"] if odd else []) + (["ESCAPE-EVEN"] if even else []) \
            or ["LEADING-ORDER NULL"]

    def enc(o):
        if isinstance(o, dict):
            return {(lab(k) if isinstance(k, tuple) and len(k) == 3 else
                     (f"({NAMES[k[0]]},{NAMES[k[1]]})" if isinstance(k, tuple) else str(k))): enc(v)
                    for k, v in o.items()}
        if isinstance(o, list):
            return [enc(v) for v in o]
        return o

    json.dump(enc(report), open(os.path.join(HERE, "wo002_results.json"), "w"), indent=1)
    print(json.dumps(enc({k: report[k] for k in ("controls", "reading_P1", "reading_P2")}), indent=1))


if __name__ == "__main__":
    main()
