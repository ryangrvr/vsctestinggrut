#!/usr/bin/env python3
"""SKEPTIC re-check of the analyst's parametric-harmonic control (independent code).
Bath x'' = -(1 + a q(t)) x, (x0, p0) ~ N(0, I); record F = -(a/2) x^2 on grid (pi, pi+1).
(i) rho_x under P0 (exact cos 1) and P1 via Radau (different integrator from the analyst's DOP853);
(ii) reflection-safe Tier-2 invariants of the copula of (x1^2, x2^2): Spearman rho_S (invariant under the joint
     reflection, sign-flipped by single reflections) and |rho^N| (normal-score correlation), by Monte Carlo;
(iii) Tier-1: Pearson Corr(x1^2, x2^2) = rho^2 (Isserlis), invariant under the only affine bijections of the
     quadrant (positive diagonal scalings, swap).
"""
import json
import numpy as np
from scipy.integrate import solve_ivp
from scipy.stats import norm, rankdata

PI = np.pi
def s5(u): return 10*u**3 - 15*u**4 + 6*u**5
def q1(t): return s5(t/PI) if t <= PI else 1.0

def rho_x(a, driven):
    def rhs(t, s):
        k = 1 + (a*q1(t) if driven else 0.0)
        M = s.reshape(2, 2); return (np.array([[0, 1], [-k, 0]]) @ M).ravel()
    sol = solve_ivp(rhs, (0, PI+1), np.eye(2).ravel(), t_eval=[PI, PI+1], method="Radau", rtol=1e-11, atol=1e-13)
    Ph = [sol.y[:, i].reshape(2, 2) for i in range(2)]
    C = np.array([[(Ph[i] @ Ph[j].T)[0, 0] for j in range(2)] for i in range(2)])
    return C[0, 1]/np.sqrt(C[0, 0]*C[1, 1])

rng = np.random.default_rng(20261007)
def copula_stats(r, n=4_000_000):
    z1 = rng.standard_normal(n); z2 = r*z1 + np.sqrt(1-r*r)*rng.standard_normal(n)
    u = rankdata(z1**2)/(n+1); v = rankdata(z2**2)/(n+1)
    rhoS = np.corrcoef(u, v)[0, 1]
    rhoN = np.corrcoef(norm.ppf(u), norm.ppf(v))[0, 1]
    return float(rhoS), float(rhoN)

out = {"rho_P0_exact_cos1": float(np.cos(1.0))}
for a in (0.3, 0.6):
    r0, r1 = rho_x(a, False), rho_x(a, True)
    s0 = copula_stats(abs(r0)); s1 = copula_stats(abs(r1))
    out[f"a={a}"] = {"rho_P0": r0, "rho_P1": r1, "Corr_x2_P0": r0**2, "Corr_x2_P1": r1**2,
                     "spearman_P0": s0[0], "spearman_P1": s1[0], "abs_rhoN_P0": abs(s0[1]), "abs_rhoN_P1": abs(s1[1])}
print(json.dumps(out, indent=1))
