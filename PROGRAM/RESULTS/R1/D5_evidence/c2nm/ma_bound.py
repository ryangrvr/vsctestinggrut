"""Theorem F3 lower bound for the Markov example M-A / M-B single-time marginal:
eps_R^{T_R1}({P0,P1}) >= 1/2 * abs(E g(W)) / ||g||_BL, g odd, W = standardized z under pi_lam."""
import numpy as np
from scipy.integrate import quad
U = lambda z: z**2/2 + z**4/4
for lam in (0.5, 1.0):
    Z = quad(lambda z: np.exp(-U(z)+lam*z), -12, 12, epsabs=1e-14)[0]
    mu = quad(lambda z: z*np.exp(-U(z)+lam*z), -12, 12, epsabs=1e-14)[0]/Z
    v = quad(lambda z: (z-mu)**2*np.exp(-U(z)+lam*z), -12, 12, epsabs=1e-14)[0]/Z
    s = np.sqrt(v)
    best = 0
    for a in (0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0):
        g = lambda z: np.clip((z-mu)/s, -a, a)
        Eg = quad(lambda z: g(z)*np.exp(-U(z)+lam*z), -12, 12, epsabs=1e-14, limit=200)[0]/Z
        bound = 0.5*abs(Eg)/max(a, 1.0)
        best = max(best, bound)
        print(f"lam={lam} a={a}: E clip_a(W) = {Eg:+.6e}  -> eps_R >= {bound:.4e}")
    print(f"lam={lam}: best clip bound eps_R^(T_R1) >= {best:.4e}")
