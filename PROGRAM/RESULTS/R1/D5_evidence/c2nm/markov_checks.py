"""D5 comparator 2 (non-Markovianity) checks. Evidence only.
(1) C2-F as implemented: is each record an AR(1) Markov chain? Exact linear-predictor coefficients.
(2) C2-F' (two-exponential calibrated filter): non-Markov record, still one GL(k) orbit.
(3) Markov environment examples: tilted quartic law kappa3 (exact quadrature);
    stationary overdamped quartic diffusion: 2-time copula radial asymmetry (Tier 2) via a
    reversible finite-volume generator (evidence grade)."""
import numpy as np
from scipy.linalg import expm
from scipy.stats import norm
from scipy.integrate import quad

np.set_printoptions(precision=4, suppress=True)

def filt_exp(n, dt, tau):
    K = np.zeros((n, n))
    for k in range(n):
        for j in range(k + 1):
            K[k, j] = np.exp(-(k - j) * dt / tau)
    return K

def filt_2exp(n, dt, t1, t2, w=0.5):
    K = np.zeros((n, n))
    for k in range(n):
        for j in range(k + 1):
            K[k, j] = w * np.exp(-(k - j) * dt / t1) + (1 - w) * np.exp(-(k - j) * dt / t2)
    return K

def predictor_coeffs(K, k):
    """E[F_k | F_0..F_{k-1}] = c . xi_{<k} with c = K[k,:k] (xi i.i.d. mean 0, independent of xi_k).
    In F-coordinates: c^T (K[:k,:k])^{-1} F_{<k}. Exact (no Gaussianity used)."""
    c = K[k, :k]
    return np.linalg.solve(K[:k, :k].T, c)

n, dt = 64, 0.01
print("== (1) C2-F as implemented: exact predictor weights on (F_{k-3},F_{k-2},F_{k-1}) at k=10 ==")
for tau in (0.05, 0.20):
    a = predictor_coeffs(filt_exp(n, dt, tau), 10)
    print(f"tau={tau}: weights on last 4 = {a[-4:]}, max |weight| on F_<k-1 = {np.max(np.abs(a[:-1])):.2e}, r=exp(-dt/tau)={np.exp(-dt/tau):.6f}")
print("== (2) C2-F' two-exponential filters (tau=0.05,0.40), (0.02,0.20) ==")
for (t1, t2) in ((0.05, 0.40), (0.02, 0.20)):
    K = filt_2exp(n, dt, t1, t2)
    a = predictor_coeffs(K, 10)
    print(f"taus=({t1},{t2}): weights on last 4 = {a[-4:]}, max |weight| on F_<k-1 = {np.max(np.abs(a[:-1])):.3e}; unit diag -> invertible: det={np.prod(np.diag(K)):.1f}")

print("\n== (3a) tilted quartic law pi_lam ∝ exp(-(z^2/2+z^4/4) + lam z), D=1: exact kappa3 ==")
U = lambda z: z**2/2 + z**4/4
def cumulants(lam):
    m = [quad(lambda z: z**p * np.exp(-U(z) + lam*z), -12, 12, epsabs=1e-14, epsrel=1e-13)[0] for p in range(4)]
    m = [x / m[0] for x in m]
    mu = m[1]; v = m[2] - mu**2; k3 = m[3] - 3*mu*m[2] + 2*mu**3
    return mu, v, k3, k3 / v**1.5
m0 = [quad(lambda z: z**p*np.exp(-U(z)), -12, 12, epsabs=1e-14)[0] for p in (0,2,4)]
k4_0 = m0[2]/m0[0] - 3*(m0[1]/m0[0])**2
print(f"kappa4(pi_0) = {k4_0:.6f} (nonzero => kappa3(pi_lam) = kappa4*lam + O(lam^3) != 0 for small lam != 0)")
for lam in (0.0, 0.1, 0.5, 1.0, 2.0):
    mu, v, k3, g = cumulants(lam)
    print(f"lam={lam}: mean={mu:+.6f} var={v:.6f} kappa3={k3:+.3e} gamma1={g:+.6f}")

print("\n== (3b) stationary overdamped quartic diffusion, 2-time copula odd witness (Tier 2 evidence) ==")
def gen(lam, L=4.0, M=801):
    z = np.linspace(-L, L, M); h = z[1] - z[0]
    V = U(z) - lam*z
    Q = np.zeros((M, M))
    for i in range(M - 1):
        dV = V[i+1] - V[i]
        Q[i, i+1] = np.exp(-dV/2) / h**2     # reversible (SG-type) rates, D=1
        Q[i+1, i] = np.exp(+dV/2) / h**2
    Q -= np.diag(Q.sum(axis=1))
    pi = np.exp(-(V - V.min())); pi /= pi.sum()
    return z, Q, pi

def witness(lam, tau, M=801):
    z, Q, pi = gen(lam, M=M)
    P = expm(Q * tau)
    J = pi[:, None] * P                     # joint law of (z(0), z(tau))
    F = np.cumsum(pi) - pi/2                # mid-CDF
    N = norm.ppf(np.clip(F, 1e-15, 1-1e-15))
    t = np.tanh(N)
    g = (t**2)[:, None] * t[None, :]        # odd bounded witness tanh(n1)^2 tanh(n2)
    Eg = np.sum(J * g)
    E3 = np.sum(J * ((N**2)[:, None] * N[None, :]))
    rhoN = np.sum(J * (N[:, None] * N[None, :])) / np.sum(pi * N**2)
    return Eg, E3, rhoN, np.max(np.abs(J - J.T))

for M in (401, 801):
    for lam in (0.0, 1.0):
        for tau in (0.25, 1.0):
            Eg, E3, rhoN, asym = witness(lam, tau, M)
            print(f"M={M} lam={lam} tau={tau}: E[tanh(N1)^2 tanh(N2)]={Eg:+.4e}  E[N1^2 N2]={E3:+.4e}  rho^N={rhoN:+.4f}  max|J-J^T|={asym:.1e}")
