#!/usr/bin/env python3
"""R1 T-ladder, numerical sanity checks (Claude Code). See R1_T_LADDER.md.

These are checks of identities and inequalities that are proved in the note. They are
not results. A failure means a bug in the note or in this script.

  (L1) T_caus equivariance: Cholesky innovations of K*Y equal sign*innovations of Y,
       for random invertible lower-triangular K. Exact identity, also for empirical laws.
  (L2) T_lin equivariance: whitened K*Y = O * whitened Y with O orthogonal; Mardia
       skewness beta_1 is invariant. Exact identity.
  (L3) Mardia witness inequality (Prop B2):
         | sqrt(b1(P)) - sqrt(b1(Q)) | <= W3(W_P, h W_Q) * (mu_P^2 + mu_P mu_Q + mu_Q^2)
       for EVERY orthogonal h (so in particular for the minimizing one). W3 between
       equal-size empirical measures in R^k is computed exactly by assignment.
  (L4) Symmetry obstruction (Thm C1): any linear image of an exactly centrally
       symmetric empirical law has zero third central moments in every coordinate and
       beta_1 = 0, to rounding. Contrast: protocol-dependent filters of a shared skewed
       driver (the C2-F mechanism) change single-time skewness but leave beta_1
       unchanged, i.e. they stay in one T_lin orbit.
  (L5) Normal-score witness inequality (Prop D3):
         | |E_P N_i^2 N_j| - |E_Q N_i^2 N_j| | <= 3 m^2 * W3(N_P, s N_Q)
       for every sign vector s, where N are normal scores and m = ||N_i||_3.
  (L6) Mode selection (Prop E2, owner ruling G2-01 item 3b): a two-mode exogenous
       environment (S symmetric, U skewed, independent; law protocol-independent).
       Protocol 0 reads S, protocol 1 reads S + U. The maps are linear but not
       injective (R^2 -> R^1). The reference is exactly symmetric, the driven law is
       skewed, and the Mardia/skewness witness is > 0, with no back-reaction. This is
       outside Theorem C's hypothesis, not a counterexample to it.
"""
import json

import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.stats import norm

rng = np.random.default_rng(20261006)
out = {}


def center(y):
    return y - y.mean(axis=0)


def cov(y):
    c = center(y)
    return c.T @ c / len(y)


def innovations(y):
    L = np.linalg.cholesky(cov(y))
    return np.linalg.solve(L, center(y).T).T


def whiten(y):
    w, V = np.linalg.eigh(cov(y))
    return center(y) @ V @ np.diag(w ** -0.5) @ V.T


def mardia_sqrt_b1(wh):
    n, k = wh.shape
    t = np.einsum("ni,nj,nl->ijl", wh, wh, wh) / n
    return float(np.sqrt((t ** 2).sum()))


def w3(a, b):
    c = np.linalg.norm(a[:, None, :] - b[None, :, :], axis=2) ** 3
    r, s = linear_sum_assignment(c)
    return float(c[r, s].mean() ** (1 / 3))


def mu3(a):
    return float((np.linalg.norm(a, axis=1) ** 3).mean() ** (1 / 3))


def random_orthogonal(k):
    q, r = np.linalg.qr(rng.standard_normal((k, k)))
    return q @ np.diag(np.sign(np.diag(r)))


def sample(kind, n, k):
    if kind == "gauss_corr":
        A = rng.standard_normal((k, k))
        return rng.standard_normal((n, k)) @ A.T
    if kind == "gamma_mix":
        A = rng.standard_normal((k, k))
        return rng.gamma(0.8, 1.0, (n, k)) @ A.T
    if kind == "lognormal":
        return np.exp(0.5 * rng.standard_normal((n, k))) @ rng.standard_normal((k, k)).T
    if kind == "student":
        return rng.standard_t(7, (n, k)) @ rng.standard_normal((k, k)).T
    raise ValueError(kind)


# (L1) T_caus equivariance. Deviations are reported relative to cond(Cov(K*Y)) * machine
# eps: the identity is exact, and its floating-point error is set by the conditioning of
# the covariance that gets factored.
EPS = np.finfo(float).eps
dev1, rel1 = 0.0, 0.0
for _ in range(50):
    k = int(rng.integers(2, 6))
    y = sample("gamma_mix", 2000, k)
    K = np.tril(rng.standard_normal((k, k)))
    K[np.diag_indices(k)] = rng.choice([-1, 1], k) * rng.uniform(0.2, 3.0, k)
    yp = y @ K.T + rng.standard_normal(k)
    u, up = innovations(y), innovations(yp)
    s = np.sign(np.diag(K))
    d = float(np.abs(up - u * s).max())
    dev1, rel1 = max(dev1, d), max(rel1, d / (np.linalg.cond(cov(yp)) * EPS))
out["L1_Tcaus_innovation_equivariance_maxdev"] = dev1
out["L1_maxdev_over_condcov_eps"] = rel1

# (L2) T_lin equivariance and Mardia invariance
dev2, dmardia, rel2 = 0.0, 0.0, 0.0
for _ in range(50):
    k = int(rng.integers(2, 6))
    y = sample("gamma_mix", 2000, k)
    K = rng.standard_normal((k, k))
    yp = y @ K.T + rng.standard_normal(k)
    w, wp = whiten(y), whiten(yp)
    O, *_ = np.linalg.lstsq(w, wp, rcond=None)
    d = max(float(np.abs(O.T @ O - np.eye(k)).max()), float(np.abs(w @ O - wp).max()))
    dev2, rel2 = max(dev2, d), max(rel2, d / (np.linalg.cond(cov(yp)) * EPS))
    dmardia = max(dmardia, abs(mardia_sqrt_b1(w) - mardia_sqrt_b1(wp)))
out["L2_Tlin_whitening_orthogonal_maxdev"] = dev2
out["L2_maxdev_over_condcov_eps"] = rel2
out["L2_Tlin_mardia_invariance_maxdev"] = dmardia

# (L3) Mardia witness inequality
kinds = ["gauss_corr", "gamma_mix", "lognormal", "student"]
worst3, trials3 = 0.0, 0
for _ in range(60):
    k = int(rng.integers(2, 4))
    k1, k2 = rng.choice(kinds, 2, replace=False)
    a, b = whiten(sample(k1, 300, k)), whiten(sample(k2, 300, k))
    lhs = abs(mardia_sqrt_b1(a) - mardia_sqrt_b1(b))
    lam = mu3(a) ** 2 + mu3(a) * mu3(b) + mu3(b) ** 2
    for h in [np.eye(k), random_orthogonal(k), random_orthogonal(k)]:
        rhs = w3(a, b @ h.T) * lam
        worst3 = max(worst3, lhs / rhs)
        trials3 += 1
out["L3_trials"] = trials3
out["L3_max_lhs_over_rhs"] = worst3
out["L3_inequality_holds"] = bool(worst3 <= 1 + 1e-12)

# (L4) symmetry obstruction vs the C2-F mechanism
k, n = 40, 4000
x = rng.gamma(0.5, 1.0, (n, k)) - 0.5
sym = np.vstack([x, -x])                          # exactly centrally symmetric
K = rng.standard_normal((k, k))                   # dense, non-causal linear map
img = sym @ K.T + rng.standard_normal(k)
c3 = (center(img) ** 3).mean(axis=0)
out["L4_symmetric_image_max_abs_third_moment"] = float(np.abs(c3).max())
out["L4_symmetric_image_sqrt_b1"] = mardia_sqrt_b1(whiten(img))
drv = rng.gamma(0.5, 1.0, (n, k))                 # shared skewed driver, k time points
dt = 0.05


def filt(tau):
    tt = np.arange(k) * dt
    F = np.tril(np.exp(-(tt[:, None] - tt[None, :]) / tau))
    return F * dt / tau + np.eye(k) * 1e-3        # causal, invertible


ya, yb = drv @ filt(0.05).T, drv @ filt(0.20).T
ga = ((center(ya)[:, -1]) ** 3).mean() / ya[:, -1].std() ** 3
gb = ((center(yb)[:, -1]) ** 3).mean() / yb[:, -1].std() ** 3
out["L4_C2F_like_last_time_skewness_a_b"] = [float(ga), float(gb)]
out["L4_C2F_like_sqrt_b1_a_b"] = [mardia_sqrt_b1(whiten(ya)), mardia_sqrt_b1(whiten(yb))]

# (L5) normal-score witness inequality
def normal_scores(y):
    n = len(y)
    r = np.argsort(np.argsort(y, axis=0), axis=0)
    return norm.ppf((r + 0.5) / n)


worst5, trials5 = 0.0, 0
for _ in range(60):
    k1, k2 = rng.choice(kinds, 2, replace=False)
    a, b = normal_scores(sample(k1, 300, 2)), normal_scores(sample(k2, 300, 2))
    m = float((np.abs(a[:, 0]) ** 3).mean() ** (1 / 3))   # identical for every column
    lhs = max(abs(abs((a[:, i] ** 2 * a[:, j]).mean()) - abs((b[:, i] ** 2 * b[:, j]).mean()))
              for i, j in [(0, 1), (1, 0)])
    for s in [np.array([1, 1]), np.array([1, -1]), np.array([-1, 1]), np.array([-1, -1])]:
        rhs = 3 * m * m * w3(a, b * s)
        worst5 = max(worst5, lhs / rhs)
        trials5 += 1
out["L5_trials"] = trials5
out["L5_max_lhs_over_rhs"] = worst5
out["L5_inequality_holds"] = bool(worst5 <= 1 + 1e-12)

def m3s(x):
    z = (x - x.mean()) / x.std()
    return float((np.abs(z) ** 3).mean() ** (1 / 3))


# (L6) two-mode mode selection: symmetric reference, skewed driven, no back-reaction
n = 200000
S = rng.standard_normal(n)
S = np.concatenate([S, -S])                       # exactly symmetric mode
U = rng.gamma(2.0, 1.0, 2 * n) - 2.0              # skewed mode, independent of S
F0, F1 = S, S + U                                  # projections (1,0) and (1,1) of (S,U)
g = lambda x: float(((x - x.mean()) ** 3).mean() / x.std() ** 3)
out["L6_two_mode_skew_reference_driven"] = [g(F0), g(F1)]
out["L6_two_mode_exact_skew_driven"] = 4.0 / 3.0 ** 1.5   # kappa3(U)=2k=4, Var = 1 + 2 = 3
out["L6_two_mode_E2pm_witness_lower_bound"] = abs(abs(g(F0)) - abs(g(F1))) / (
    2 * (m3s(F0) ** 2 + m3s(F0) * m3s(F1) + m3s(F1) ** 2))

print(json.dumps(out, indent=1))
json.dump(out, open(__file__.replace(".py", "_output.json"), "w"), indent=1)
