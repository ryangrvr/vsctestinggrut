#!/usr/bin/env python3
"""D5 comparator-1 check (read-only w.r.t. the program repo).

Claim tested: BRI1's single-time witness coefficient
    K(t) := d/d eps kappa_3(X^eps(t)) |_{eps=0}   (= 3 Cov(x0(t)^2, y1(t)), archived K_P(t,t,t))
equals the classical Kubo linear-response coefficient of the cubic observable
A = x^3 - 3 m2 x to the perturbation H' = -eps q(s) x, i.e.
    K(t) = int_0^t R_A(t - s) q(s) ds,   R_A(tau) = beta < p(0) A(x(tau)) >_Gibbs,  beta = 1,
and R_A(tau) = -d/dtau kappa_4(x(tau), x(tau), x(tau), x(0)) (connected equilibrium 4-point
function). Harmonic control: kappa_4 == 0, so K == 0.

Same Gibbs measure and protocols as the frozen BRI1 machinery (copied definitions, not imported).
"""
import json
import sys

import numpy as np

PI = np.pi


def smooth(u):
    return 10 * u**3 - 15 * u**4 + 6 * u**5


def q_of(proto, t):
    if t <= PI:
        return smooth(t / PI)
    return 1.0 if proto == 1 else 1.0 + smooth((t - PI) / PI)


def rule_trap(h, Lx=4.5, Lp=8.5, harmonic=False):
    xs = h * np.arange(-int(Lx / h), int(Lx / h) + 1)
    ps = h * np.arange(-int(Lp / h), int(Lp / h) + 1)
    X, P = np.meshgrid(xs, ps, indexing="ij")
    V = X**2 / 2 + (0 if harmonic else X**4 / 4)
    W = np.exp(-(V + P**2 / 2))
    return X.ravel(), P.ravel(), (W / W.sum()).ravel()


def run(h, nsteps, harmonic=False):
    X, P, W = rule_trap(h, harmonic=harmonic)
    c3 = 0.0 if harmonic else 1.0
    m2 = W @ X**2
    T = 2 * PI
    dt = T / nsteps
    ts = np.linspace(0, T, nsteps + 1)
    # state: x, p, y1(P1), v1(P1), y1(P2), v1(P2)
    S = np.stack([X, P, 0 * X, 0 * X, 0 * X, 0 * X])

    def f(t, S):
        x, p, y1, v1, y2, v2 = S
        k = 1 + 3 * c3 * x * x
        return np.stack([p, -x - c3 * x**3, v1, -k * y1 + q_of(1, t), v2, -k * y2 + q_of(2, t)])

    R = np.zeros(nsteps + 1)         # R_A(tau) = < p0 * A(x0(tau)) >
    Kdir = {1: {}, 2: {}}
    obs = {round(PI, 12): "pi", round(1.5 * PI, 12): "3pi/2", round(2 * PI, 12): "2pi"}
    p0 = P.copy()
    for n in range(nsteps + 1):
        t = ts[n]
        x = S[0]
        A = x**3 - 3 * m2 * x
        R[n] = W @ (p0 * A)
        key = obs.get(round(t, 12))
        if key is None:
            for tt, nm in obs.items():
                if abs(t - tt) < 0.5 * dt:
                    key = nm
        if key is not None:
            for proto, yi in ((1, 2), (2, 4)):
                y = S[yi]
                Kdir[proto][key] = 3 * (W @ ((x * x - m2) * y) - (W @ (x * x - m2)) * (W @ y))
        if n == nsteps:
            break
        k1 = f(t, S)
        k2 = f(t + dt / 2, S + dt / 2 * k1)
        k3 = f(t + dt / 2, S + dt / 2 * k2)
        k4 = f(t + dt, S + dt * k3)
        S = S + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    # Kubo convolution K_FDT(t) = int_0^t R(t - s) q(s) ds (trapezoid on the same grid)
    Kfdt = {1: {}, 2: {}}
    for tt, nm in obs.items():
        n = int(round(tt / dt))
        s = ts[: n + 1]
        for proto in (1, 2):
            qs = np.array([q_of(proto, si) for si in s])
            integrand = R[n::-1][: n + 1] * qs
            Kfdt[proto][nm] = float(np.trapezoid(integrand, s))
    # also check R_A(tau) = -d/dtau kappa4(x_tau,x_tau,x_tau,x_0) at a few tau via finite differences
    return m2, Kdir, Kfdt, R, ts


def main():
    out = {}
    arch = json.load(open(sys.argv[1]))
    for harmonic in (False, True):
        m2, Kdir, Kfdt, R, ts = run(0.08, 8000, harmonic=harmonic)
        tag = "harmonic" if harmonic else "duffing"
        out[tag] = {"m2": m2, "K_direct": Kdir, "K_kubo": Kfdt, "max_abs_R": float(np.max(np.abs(R)))}
    out["archived_diag"] = {
        p: {nm: arch[f"P{p}({nm},{nm},{nm})"]["K_A06"] for nm in ("pi", "3pi/2", "2pi")} for p in (1, 2)}
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
