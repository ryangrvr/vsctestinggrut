import numpy as np
# Gauss-Hermite (probabilists') quadrature for X ~ N(0,1)
x, w = np.polynomial.hermite_e.hermegauss(200)
w = w / w.sum()
E = lambda g: float(np.sum(w * g(x)))

# (1) Data-processing violation of d_q^BL (k=1, quotient group {+-1} after whitening).
# P = N(0,1), Q = N(0,4) = law of 2X: same T_R1 orbit, so d_q^BL(P,Q) = 0.
# Apply phi(y) = y + y^3 to both: compare standardized laws of phi(X) and phi(2X).
def std_moments(a, b):
    g = lambda t: a*t + b*t**3
    m = E(g); v = E(lambda t: (g(t)-m)**2)
    kurt = E(lambda t: ((g(t)-m)/np.sqrt(v))**4)
    return m, v, kurt
_, v1, k1 = std_moments(1.0, 1.0)   # phi(X)
_, v2, k2 = std_moments(2.0, 8.0)   # phi(2X)
# Even BL witness f(z) = min(|z|, 1) - has ||f||_inf <= 1, Lip <= 1; even, so sign-quotient-safe.
f = lambda z: np.minimum(np.abs(z), 1.0)
Ef1 = E(lambda t: f((t + t**3)/np.sqrt(v1)))
Ef2 = E(lambda t: f((2*t + 8*t**3)/np.sqrt(v2)))
print("(1) kurtosis phi(X) =", round(k1,4), " phi(2X) =", round(k2,4))
print("    even-witness |E f| difference (lower bound on d_q^BL after phi) =", round(abs(Ef1-Ef2),6))

# (2) Memoryless nonlinear responding environment: F = xi + c*q*(xi^2 - 1), xi iid N(0,1).
c = 0.3
kappa3 = 6*c + 8*c**3; var = 1 + 2*c**2
gamma = kappa3/var**1.5
print("(2) c=0.3, q=1: skewness gamma =", round(gamma,4), "(q=0: 0 exactly)")
# Odd BL witness f(z) = clip(z,-1,1): ||f||_BL = 1. Theorem F3: eps_R >= 0.5*|E f(W1)|.
fo = lambda z: np.clip(z, -1, 1)
W = lambda t: (t + c*(t**2 - 1))/np.sqrt(var)
Efo = E(lambda t: fo(W(t)))
print("    E clip(W1) =", round(Efo,6), " => eps_R^(T_R1) >= ", round(0.5*abs(Efo),6))
