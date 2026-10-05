#!/usr/bin/env python3
"""S2 consistency check: numerical K(t) = 3 c(t) versus the leading small-time
formula K_lead(t) = 3 C7 t^7, C7 = -Var(x0^2)/(28 pi^3).

Fresh code, written for this build. It shares nothing with the record's
numerical scripts beyond the model definition:
    x0'' = -x0 - x0^3                      (unforced Duffing, Gibbs initial data, beta = 1)
    y1'' + (1 + 3 x0^2) y1 = q(t),  y1(0) = y1'(0) = 0,   q(t) = s(t/pi)
    c(t) = Cov(x0(t)^2, y1(t)).
Two independent quadrature/integrator combinations are run:
    A: probabilists' Gauss-Hermite tensor grid (Gibbs factor exp(-a^4/4) in the
       weights) + fixed-step classical RK4, at two grid sizes and two step sizes;
    B: Gauss-Legendre tensor grid on [-L, L]^2 with the full Gibbs weight +
       adaptive DOP853 (scipy), rtol = atol = 1e-13.
A third, semi-analytic, comparison sums the exact series sum_{k=7}^{14} C_k t^k.
Output: data/t7_check.json. The times are those requested for S2.
"""
import os

import numpy as np
from scipy.integrate import solve_ivp

from common import DATA, dump_json, load_json, tool_ref

TIMES = [0.1, 0.2, 0.25, 0.5]


def q(t):
    u = t / np.pi
    return 10 * u ** 3 - 15 * u ** 4 + 6 * u ** 5     # valid on [0, pi]; all TIMES < pi


def rk4_states(a, b, times, dt):
    """Integrate (x, p, y, v) on arrays from t = 0 through the sorted times."""
    x, p = a.copy(), b.copy()
    y, v = np.zeros_like(a), np.zeros_like(a)
    t, out = 0.0, []

    def f(t, x, p, y, v):
        return p, -x - x ** 3, v, -(1 + 3 * x ** 2) * y + q(t)

    for T in times:
        n = max(1, int(round((T - t) / dt)))
        h = (T - t) / n
        for _ in range(n):
            k1 = f(t, x, p, y, v)
            k2 = f(t + h / 2, *(s + h / 2 * k for s, k in zip((x, p, y, v), k1)))
            k3 = f(t + h / 2, *(s + h / 2 * k for s, k in zip((x, p, y, v), k2)))
            k4 = f(t + h, *(s + h * k for s, k in zip((x, p, y, v), k3)))
            x, p, y, v = (s + h / 6 * (c1 + 2 * c2 + 2 * c3 + c4)
                          for s, c1, c2, c3, c4 in zip((x, p, y, v), k1, k2, k3, k4))
            t += h
        out.append((x.copy(), y.copy()))
    return out


def dop853_states(a, b, times):
    n = a.size

    def rhs(t, z):
        x, p, y, v = z[:n], z[n:2 * n], z[2 * n:3 * n], z[3 * n:]
        return np.concatenate([p, -x - x ** 3, v, -(1 + 3 * x ** 2) * y + q(t)])

    z0 = np.concatenate([a, b, np.zeros(n), np.zeros(n)])
    sol = solve_ivp(rhs, (0.0, max(times)), z0, method="DOP853", t_eval=times,
                    rtol=1e-13, atol=1e-13)
    return [(sol.y[:n, i], sol.y[2 * n:3 * n, i]) for i in range(len(times))]


def cov(w, x, y):
    ex2 = np.sum(w * x * x)
    return np.sum(w * x * x * y) - ex2 * np.sum(w * y)


def grid_hermite(n):
    z, wz = np.polynomial.hermite_e.hermegauss(n)     # weight exp(-z^2/2)
    A, B = np.meshgrid(z, z, indexing="ij")
    W = np.outer(wz * np.exp(-z ** 4 / 4), wz)
    return A.ravel(), B.ravel(), (W / W.sum()).ravel()


def grid_legendre(n, L=6.0):
    z, wz = np.polynomial.legendre.leggauss(n)
    z, wz = L * z, L * wz
    A, B = np.meshgrid(z, z, indexing="ij")
    W = np.outer(wz, wz) * np.exp(-A ** 2 / 2 - A ** 4 / 4 - B ** 2 / 2)
    return A.ravel(), B.ravel(), (W / W.sum()).ravel()


def main():
    const = load_json(os.path.join(DATA, "constants.json"))
    Cn = {int(k): v for k, v in const["series"]["C_numeric"].items()}
    C7 = Cn[7]                             # = -Var(x0^2)/(28 pi^3) at the high-precision m2

    runs = {}
    for n in (64, 96):
        a, b, w = grid_hermite(n)
        for dt in (2e-4, 1e-4):
            st = rk4_states(a, b, TIMES, dt)
            runs[f"A_GH{n}_RK4dt{dt:g}"] = [cov(w, x, y) for x, y in st]
    a, b, w = grid_legendre(160)
    st = dop853_states(a, b, TIMES)
    runs["B_GL160_DOP853"] = [cov(w, x, y) for x, y in st]

    primary = "A_GH96_RK4dt0.0001"
    rows = []
    for i, t in enumerate(TIMES):
        c_vals = {k: v[i] for k, v in runs.items()}
        cA = c_vals[primary]
        lead = C7 * t ** 7
        series = sum(Cn[k] * t ** k for k in range(7, 15))
        spread = max(abs(v - cA) for v in c_vals.values())
        rows.append({
            "t": t,
            "K_numerical": 3 * cA,
            "K_leading": 3 * lead,
            "ratio": cA / lead,
            "ratio_method_B": c_vals["B_GL160_DOP853"] / lead,
            "ratio_series_t7_to_t14": series / lead,
            "max_abs_spread_c_across_runs": spread,
            "relative_spread": spread / abs(cA),
            "c_by_run": c_vals,
        })
        print(f"t={t:<5} K_num={3*cA: .6e}  K_lead={3*lead: .6e}  ratio={cA/lead:.6f}"
              f"  (B: {c_vals['B_GL160_DOP853']/lead:.6f}; series<=t^14: {series/lead:.6f};"
              f" rel. spread {spread/abs(cA):.1e})")

    dump_json({
        "times": TIMES,
        "primary_run": primary,
        "C7": C7,
        "rows": rows,
        "method": tool_ref("check_t7.py",
                           "Gauss-Hermite/RK4 (primary) and Gauss-Legendre/DOP853 (independent); "
                           "c(t) = Cov(x0(t)^2, y1(t)) by quadrature over the beta = 1 Gibbs law"),
        "note": "Computed by this build; the expected ratios quoted in the build prompt were not used.",
    }, os.path.join(DATA, "t7_check.json"))


if __name__ == "__main__":
    main()
