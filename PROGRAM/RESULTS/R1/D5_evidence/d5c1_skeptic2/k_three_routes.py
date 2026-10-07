#!/usr/bin/env python3
"""D5 comparator-1 SKEPTIC check (scratch; independent of the analyst's kubo_check.py).

K(t) := d/d eps kappa_3(X^eps(t))|_0 for one Duffing oscillator (H0 = p^2/2 + x^2/2 + x^4/4, beta = 1),
driven by +eps q(t) (BRI1 convention), computed three independent ways:
  (1) FD   : kappa_3(eps)/eps of the FULL nonlinear forced dynamics (kappa_3 odd in eps), eps = d, 2d, Richardson;
  (2) FDT4 : K(t) = G(0) q(t) - int_0^t G(t-s) q'(s) ds, with G(tau) = kappa(x_tau,x_tau,x_tau,x_0) the connected
             equilibrium 4-point function (this is the integrated-by-parts form of int R_A q with
             R_A(tau) = -dG/dtau; G(0) = m4 - 3 m2^2).
  (3) compared to the archived K_A06 diagonal (wo002_results.json / pf4q archive values via the analyst output).
Grid: trapezoid h = 0.07 on [-4.5,4.5] x [-8.5,8.5]; RK4 with 4000 steps per 2 pi (different from the analyst's
h = 0.08, 8000 steps).
"""
import json
import numpy as np

PI = np.pi
def s5(u): return 10*u**3 - 15*u**4 + 6*u**5
def ds5(u): return 30*u**2 - 60*u**3 + 30*u**4
def q(proto, t):
    t = np.asarray(t, float)
    a = s5(np.clip(t/PI, 0, 1))
    if proto == 1: return np.where(t <= PI, a, 1.0)
    return np.where(t <= PI, a, 1.0 + s5(np.clip((t-PI)/PI, 0, 1)))
def dq(proto, t):
    t = np.asarray(t, float)
    a = ds5(np.clip(t/PI, 0, 1))/PI*(t <= PI)
    if proto == 1: return a
    return a + (t > PI)*ds5(np.clip((t-PI)/PI, 0, 1))/PI

h = 0.07
xs = h*np.arange(-int(4.5/h), int(4.5/h)+1); ps = h*np.arange(-int(8.5/h), int(8.5/h)+1)
X0, P0 = [a.ravel() for a in np.meshgrid(xs, ps, indexing="ij")]
W = np.exp(-(P0**2/2 + X0**2/2 + X0**4/4)); W /= W.sum()
m2 = W @ X0**2; m4 = W @ X0**4
NST = 4000; T = 2*PI; dt = T/NST
obs_idx = {"pi": NST//2, "3pi/2": 3*NST//4, "2pi": NST}

def integrate(eps, proto, record_G=False):
    x, p = X0.copy(), P0.copy()
    out = {}; G = np.zeros(NST+1)
    def f(t, x, p): return p, -x - x**3 + eps*q(proto, t)
    for n in range(NST+1):
        t = n*dt
        if record_G:
            G[n] = W @ (x**3 * X0) - 3*m2*(W @ (x*X0))
        for nm, k in obs_idx.items():
            if n == k:
                mu = W @ x; c = x - mu
                out[nm] = W @ c**3
        if n == NST: break
        k1 = f(t, x, p); k2 = f(t+dt/2, x+dt/2*k1[0], p+dt/2*k1[1])
        k3 = f(t+dt/2, x+dt/2*k2[0], p+dt/2*k2[1]); k4 = f(t+dt, x+dt*k3[0], p+dt*k3[1])
        x = x + dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]); p = p + dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
    return out, G

res = {"m2": m2, "G0_m4_minus_3m2sq": m4 - 3*m2**2}
_, G = integrate(0.0, 1, record_G=True)
ts = np.linspace(0, T, NST+1)
d = 1e-3
for proto in (1, 2):
    kp1, _ = integrate(d, proto); kp2, _ = integrate(2*d, proto)   # kappa_3 is exactly odd in eps (parity)
    fd, fdt = {}, {}
    for nm, k in obs_idx.items():
        D1 = kp1[nm]/d; D2 = kp2[nm]/(2*d)
        fd[nm] = (4*D1 - D2)/3
        s = ts[:k+1]
        integrand = G[k::-1][:k+1]*dq(proto, s)
        fdt[nm] = float(G[0]*q(proto, ts[k]) - np.trapezoid(integrand, s))
    res[f"P{proto}"] = {"K_FD_full_dynamics": fd, "K_FDT_4point": fdt}
print(json.dumps(res, indent=1))
