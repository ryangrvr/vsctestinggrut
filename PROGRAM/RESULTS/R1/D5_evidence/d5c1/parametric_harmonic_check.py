#!/usr/bin/env python3
"""D5 comparator-1 control (illustrative, exact up to ODE tolerance).

Harmonic bath oscillator (H0 = p^2/2 + x^2/2, Gibbs beta = 1 => (x0, p0) ~ N(0, I)), with
(a) linear coupling  H_int = -q(t) x        -> force record F = x      (BRI1-type; harmonic control)
(b) parametric coupling H_int = (a/2) q(t) x^2 -> force record F = -(a/2) x^2.
In both cases the bath dynamics are linear, so x(t) is Gaussian under every protocol.

(a): x_q(t) = x_0(t) + deterministic shift  => every protocol is a translate of P0: eps_R = 0 (both tiers).
(b): x_q(t) is centred Gaussian with protocol-dependent covariance; for a centred Gaussian pair,
     Corr(x1^2, x2^2) = rho^2, and the copula of (x1^2, x2^2) is fixed by |rho|.
     If |rho_P1| != |rho_P0| the copulas lie in different reflection orbits (Tier 2 escape), and
     affine maps preserving the image cone of (x1^2, x2^2) are positive diagonal scalings (or the
     swap) plus shifts, which preserve Corr(x1^2, x2^2), so Tier 1 escapes too.
Protocol q: the frozen BRI1 P1 profile; grid (pi, pi + 1) (nondegenerate; (pi, 2pi) is singular for omega = 1).
"""
import json

import numpy as np
from scipy.integrate import solve_ivp

PI = np.pi


def smooth(u):
    return 10 * u**3 - 15 * u**4 + 6 * u**5


def q1(t):
    return smooth(t / PI) if t <= PI else 1.0


def fundamental(a, proto, times):
    """Phi(t) (2x2) for x'' = -(1 + a q(t)) x  (parametric); returns {t: Phi}."""
    def rhs(t, s):
        k = 1 + (a * q1(t) if proto == 1 else 0.0)
        M = s.reshape(2, 2)
        A = np.array([[0, 1], [-k, 0]])
        return (A @ M).ravel()
    sol = solve_ivp(rhs, (0, max(times)), np.eye(2).ravel(), t_eval=times, rtol=1e-12, atol=1e-12,
                    method="DOP853")
    return {t: sol.y[:, i].reshape(2, 2) for i, t in enumerate(sol.t)}


def main():
    times = [PI, PI + 1.0]
    out = {}
    for a in (0.3, 0.6):
        res = {}
        for proto in (0, 1):
            Ph = fundamental(a, proto, times)
            C = np.array([[(Ph[ti] @ Ph[tj].T)[0, 0] for tj in times] for ti in times])  # Sigma0 = I
            rho = C[0, 1] / np.sqrt(C[0, 0] * C[1, 1])
            res[f"P{proto}"] = {"var_x": [C[0, 0], C[1, 1]], "rho_x": rho,
                                "corr_of_force_x2": rho**2}
        out[f"a={a}"] = res
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
