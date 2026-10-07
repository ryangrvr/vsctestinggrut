import numpy as np
from numpy.polynomial.hermite_e import hermegauss
# Gauss-Hermite (probabilists') quadrature for E over N(0,1)
x, w = hermegauss(200); w = w/w.sum()
E = lambda f: np.sum(w*f(x))
# (1) contamination example: P_eta = (1-eta) N(0,1) + eta delta_c, c = eta^(-1/2); compare to N(0,1)
for eta in [1e-2,1e-4,1e-6]:
    c = eta**-0.5
    m = eta*c
    s = np.sqrt((1-eta)*1 + eta*c**2 - m**2)
    # E cos(W) for standardized W, f = cos has sup-norm 1, Lip 1, even (so invariant under O(1)={+-1})
    Ecos = (1-eta)*E(lambda z: np.cos((z-m)/s)) + eta*np.cos((c-m)/s)
    gap = abs(Ecos - E(np.cos))
    print(f"eta={eta:g}: TV(P_eta,N)={eta:g}, d_q^BL >= {gap:.4f}, eps_R(two protocols)=d_q/2 >= {gap/2:.4f}")
print("limit e^{-1/4}-e^{-1/2} =", np.exp(-0.25)-np.exp(-0.5))
# (2) common bijection y->y^3 applied to {N(0,1), N(1,1)}: skewness of standardized (Z+1)^3 vs Z^3
def skew(f):
    mu = E(f); v = E(lambda z:(f(z)-mu)**2); return E(lambda z:(f(z)-mu)**3)/v**1.5
print("skew Z^3 =", skew(lambda z:z**3), " skew (Z+1)^3 =", skew(lambda z:(z+1)**3))
