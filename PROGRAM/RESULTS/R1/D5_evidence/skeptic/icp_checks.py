import numpy as np
from scipy import stats
rng = np.random.default_rng(7)
n = 20000

def irdt(Y, X, env):
    """ICP 'invariant residual distribution test' (nonlinear ICP Alg. 5 / PBM Method II style):
    pooled OLS of Y on X (with intercept), then KS of residuals env e vs rest, Bonferroni."""
    A = np.column_stack([np.ones(len(Y))] + ([X] if X is not None else []))
    beta, *_ = np.linalg.lstsq(A, Y, rcond=None)
    R = Y - A @ beta
    envs = np.unique(env)
    pv = min(stats.ks_2samp(R[env == e], R[env != e]).pvalue for e in envs[:1])
    return min(1.0, pv)

def sym(n):   # symmetric, non-Gaussian latent
    return rng.laplace(size=n)
def skw(n):
    return (rng.gamma(2.0, size=n) - 2.0) / np.sqrt(2.0)

out = {}
# E-A: unchanged environment Z, calibrated interface t_a in T_R1 (k=1): Y0 = Z, Y1 = 2Z + 1
Z0, Z1 = sym(n), sym(n)
Y = np.r_[Z0, 2 * Z1 + 1]; X = np.r_[Z0, Z1]; env = np.r_[np.zeros(n), np.ones(n)]
out['E-A  S={Z}'] = irdt(Y, X, env); out['E-A  S=empty'] = irdt(Y, None, env)
# E-B: unchanged environment Z=(S,U), mode selection h0=(1,0), h1=(1,1)
S0, U0, S1, U1 = sym(n), skw(n), sym(n), skw(n)
Y = np.r_[S0, S1 + U1]; X = np.column_stack([np.r_[S0, S1], np.r_[U0, U1]])
out['E-B  S={S,U}'] = irdt(Y, X, env); out['E-B  S=empty'] = irdt(Y, None, env)
# E-C: responding environment, one readout h = id; Law(Z) changes (symmetric -> skewed)
Z0, Z1 = sym(n), skw(n)
Y = np.r_[Z0, Z1]; X = np.r_[Z0, Z1]
out['E-C  S={Z}'] = irdt(Y, X, env); out['E-C  S=empty'] = irdt(Y, None, env)
for k, v in out.items():
    print(f'{k:16s} p = {v:.3g}  -> {"accept" if v > 0.05 else "REJECT"}')

# Per-environment symmetric whitening WITHOUT the O(k) minimization falsely separates a T_R1 orbit
W = np.column_stack([skw(n), sym(n)])            # whitened-ish law P
K = np.array([[1.0, 2.0], [0.0, 1.0]])           # GL(2) interface
Q = W @ K.T + np.array([3.0, -1.0])              # Q = t#P, same T_R1 orbit
def symwhiten(Y):
    C = np.cov(Y.T); w, V = np.linalg.eigh(C); Wm = V @ np.diag(w ** -0.5) @ V.T
    return (Y - Y.mean(0)) @ Wm.T
Pw, Qw = symwhiten(W), symwhiten(Q)
print('coordinate-1 skewness after per-env symmetric whitening: P %.3f  Q %.3f' % (stats.skew(Pw[:, 0]), stats.skew(Qw[:, 0])))
print('KS p (coord 1, no O(k) min):', stats.ks_2samp(Pw[:, 0], Qw[:, 0]).pvalue)
# Mardia sqrt(beta1) (O(k)-invariant) agrees
def mardia(Yw):
    T = np.einsum('ni,nj,nk->ijk', Yw, Yw, Yw) / len(Yw); return np.sqrt((T ** 2).sum())
print('O(k)-invariant sqrt(beta1): P %.4f  Q %.4f' % (mardia(Pw), mardia(Qw)))
