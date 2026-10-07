#!/usr/bin/env python3
"""D5 comparator-1 SKEPTIC check: is Tier-1 eps_R of BRI1 at a single time (k = 1) just a constant times the
normalized third-cumulant (Kubo) response?

Two protocols {P0, P1}, k = 1, T_R1 = affine maps of R.  P0 is exactly symmetric, so (Theorem F, F2)
    eps_R = (1/2) d_BL(std P1, std P0),     d_BL with |f| <= 1, Lip f <= 1.
Formal leading order: std P1 - std P0 = (gamma1/6) H3 phi + o(1/N_B)  =>  eps_R = (V*/12)|gamma1| + o(1/N_B),
gamma1 = K(t)/(N_B m2^{3/2}) + O(N_B^-2), K(t) = Kubo response of x^3 - 3 m2 x.
Exact finite-N_B laws: F = N_B^{-1/2} sum_j X_j^eps(t), eps = N_B^{-1/2}, X_j i.i.d.; CDF of std F by Gil-Pelaez
from phi_X(v) (trapezoid Gibbs nodes pushed through the forced flow); d_BL by LP on a fine grid.
"""
import json, sys
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import diags, vstack

PI = np.pi; VSTAR = 0.943578
def s5(u): return 10*u**3 - 15*u**4 + 6*u**5
h = 0.05
xs = h*np.arange(-int(4.5/h), int(4.5/h)+1); ps = h*np.arange(-int(8.5/h), int(8.5/h)+1)
X0, P0 = [a.ravel() for a in np.meshgrid(xs, ps, indexing="ij")]
W = np.exp(-(P0**2/2 + X0**2/2 + X0**4/4)); W /= W.sum()
m2 = W @ X0**2
tstar = PI; NST = 3000; dt = tstar/NST

def x_at(eps):
    x, p = X0.copy(), P0.copy()
    f = lambda t, x, p: (p, -x - x**3 + eps*s5(min(t/PI, 1.0)))
    for n in range(NST):
        t = n*dt
        k1 = f(t, x, p); k2 = f(t+dt/2, x+dt/2*k1[0], p+dt/2*k1[1])
        k3 = f(t+dt/2, x+dt/2*k2[0], p+dt/2*k2[1]); k4 = f(t+dt, x+dt*k3[0], p+dt*k3[1])
        x = x + dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]); p = p + dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
    return x

L, hz = 9.0, 0.004
edges = np.arange(-L, L + hz/2, hz)
du, U = 0.01, 14.0
us = du*np.arange(1, int(U/du)+1)

def std_cdf(xv, NB):
    eps = NB**-0.5
    mu = W @ xv; c = xv - mu; var = W @ c**2
    sig = np.sqrt(var)           # sd of F = sd of X^eps
    k3 = W @ c**3
    gamma1 = NB**-0.5 * k3 / sig**3
    # phi_{std F}(u) = phi_c(eps u / sig)^NB, phi_c = char. fn of centred X
    phis = np.empty(us.size, complex)
    for i0 in range(0, us.size, 50):
        v = eps*us[i0:i0+50, None]/sig
        phis[i0:i0+50] = (np.exp(1j*v*c[None, :]) @ W)**NB
    # Gil-Pelaez: F(z) = 1/2 - (1/pi) int_0^inf Im(e^{-iuz} phi(u))/u du ; u -> 0 limit of integrand is -z
    integ = np.imag(np.exp(-1j*np.outer(edges, us))*phis[None, :])/us[None, :]
    I = du*(integ.sum(1) - 0.5*integ[:, -1]) + du*0.5*(-edges)
    return 0.5 - I/PI, gamma1

def dbl(cp, cq):
    mu = np.diff(cp) - np.diff(cq)
    mu[0] += cp[0] - cq[0]; mu[-1] += (1 - cp[-1]) - (1 - cq[-1])
    n = mu.size
    D = diags([-np.ones(n-1), np.ones(n-1)], [0, 1], shape=(n-1, n))
    A = vstack([D, -D]).tocsr(); b = np.full(2*(n-1), hz)
    r = linprog(-mu, A_ub=A, b_ub=b, bounds=[(-1, 1)]*n, method="highs")
    assert r.status == 0
    return -r.fun

out = {"t": "pi", "m2": m2, "V_star": VSTAR, "rows": []}
x0 = x_at(0.0)
for NB in [int(a) for a in sys.argv[1:]] or [8, 16, 32, 64]:
    x1 = x_at(NB**-0.5)
    c0, g0 = std_cdf(x0, NB); c1, g1 = std_cdf(x1, NB)
    d = dbl(c1, c0)
    epsR = 0.5*d
    lo = VSTAR/12*abs(g1)
    out["rows"].append({"N_B": NB, "gamma1_P0": g0, "gamma1_P1": g1, "N_B*gamma1_P1": NB*g1,
                        "eps_R": epsR, "(V*/12)|gamma1|": lo, "ratio": epsR/lo,
                        "N_B*eps_R": NB*epsR, "cdf_P0_symmetry_check": float(np.max(np.abs(c0 + c0[::-1] - 1)))})
    print(json.dumps(out["rows"][-1]), flush=True)
out["limit_(V*/12)|K|/m2^1.5_using_archived_K_P1(pi)=-0.14878490"] = VSTAR/12*0.1487849002590415/m2**1.5
print(json.dumps(out, indent=1))
