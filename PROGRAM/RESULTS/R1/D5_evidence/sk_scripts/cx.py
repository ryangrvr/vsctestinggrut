import numpy as np
from scipy import integrate, stats
phi = stats.norm.pdf
# (1) k=1: P = N(0,1), Q = law of Z^3/sqrt(15) (standardized). Both centrally symmetric -> I_Z2 = 0 for both,
# and Z -> Z^3 is an odd (Z2-covariant) bijection, so J-S's Z2 covariance quasi-order relates them both ways.
# T_R1 at k=1 = affine maps; quotient residual group O(1) = {+1,-1}; both laws symmetric so sign irrelevant.
f = lambda x: np.exp(-x**2/2)          # even, sup=1, Lip = e^{-1/2} < 1 -> ||f||_BL = 1
EP = integrate.quad(lambda z: f(z)*phi(z), -np.inf, np.inf)[0]
EQ = integrate.quad(lambda z: f(z**3/np.sqrt(15))*phi(z), -np.inf, np.inf)[0]
print("(1) E_P f =", EP, " E_Q f =", EQ, " d_q^BL >=", abs(EP-EQ), " eps_R = d_q/2 >=", abs(EP-EQ)/2)
# kurtosis check
print("    kurtosis P = 3, kurtosis Q =", 10395/15**2)
# (2) k=2 Gaussian copulas rho=0.3 vs 0.6: radially symmetric (U =d 1-U), so reference information for the
# total reflection is 0 for both; but |rho| differs -> different R-orbits -> eps_R^mono > 0 (M1).
def Eg(rho, n=120):
    x, w = np.polynomial.hermite_e.hermegauss(n); w = w/np.sqrt(2*np.pi)
    X, Y = np.meshgrid(x, x, indexing='ij'); W = np.outer(w, w)
    # n2 = rho*n1 + sqrt(1-rho^2)*e
    return np.sum(W*np.tanh(X)*np.tanh(rho*X+np.sqrt(1-rho**2)*Y))
a, b = Eg(0.3), Eg(0.6)
print("(2) E tanh tanh: rho=0.3 ->", a, " rho=0.6 ->", b, " eps_R^mono >=", abs(abs(a)-abs(b))/(2*np.sqrt(2)))
