"""Comparator-10 counterexample checks (evidence only).
M1: memoryless finite-alphabet mode-selection channel Y_t = S_t + x_t U_t (S uniform +-1, U ~ Bern(p)).
M2: memoryless translation channel Y_t = S_t + x_t.
k = 1 grid; T_R1 = affine maps of R; d_q^BL = min over O in {+1,-1} of d_BL(P~, O#Q~).
d_BL between finitely supported laws on R computed exactly by LP over f values on the union support:
  max sum f_i (p_i - q_i)  s.t. |f_i| <= 1, |f_i - f_j| <= |x_i - x_j|.
(On R, Lipschitz extension from a finite set preserves both bounds, so the LP value is d_BL.)
eps_R = 1/2 d_q^BL for two protocols (Theorem F2).
"""
import itertools, json
import numpy as np
from scipy.optimize import linprog

def standardize(atoms):
    x = np.array([a for a, _ in atoms], float); w = np.array([b for _, b in atoms], float)
    mu = (w * x).sum(); sd = np.sqrt((w * (x - mu) ** 2).sum())
    return [((xi - mu) / sd, wi) for xi, wi in zip(x, w)]

def d_bl(P, Q):
    pts = sorted(set([round(a, 12) for a, _ in P] + [round(a, 12) for a, _ in Q]))
    idx = {v: i for i, v in enumerate(pts)}
    c = np.zeros(len(pts))
    for a, w in P: c[idx[round(a, 12)]] += w
    for a, w in Q: c[idx[round(a, 12)]] -= w
    A, b = [], []
    for i, j in itertools.combinations(range(len(pts)), 2):
        row = np.zeros(len(pts)); row[i], row[j] = 1, -1
        A.append(row); b.append(abs(pts[i] - pts[j]))
        A.append(-row); b.append(abs(pts[i] - pts[j]))
    res = linprog(-c, A_ub=np.array(A), b_ub=np.array(b), bounds=[(-1, 1)] * len(pts), method="highs")
    return -res.fun

def dq(P, Q):
    Pt, Qt = standardize(P), standardize(Q)
    return min(d_bl(Pt, [(s * a, w) for a, w in Qt]) for s in (1, -1))

def law_sum(A, B):
    out = {}
    for a, wa in A:
        for b, wb in B:
            out[a + b] = out.get(a + b, 0) + wa * wb
    return sorted(out.items())

S = [(-1.0, 0.5), (1.0, 0.5)]
res = {}
for p in (0.25, 0.1):
    U = [(0.0, 1 - p), (1.0, p)]
    P0, P1 = S, law_sum(S, U)
    x = np.array([a for a, _ in P1]); w = np.array([b for _, b in P1])
    mu = (w * x).sum(); var = (w * (x - mu) ** 2).sum(); k3 = (w * (x - mu) ** 3).sum()
    res[f"M1_p={p}"] = {"P1_atoms": P1, "gamma1_P1": k3 / var ** 1.5,
                        "gamma_exact": p * (1 - p) * (1 - 2 * p) / (1 + p * (1 - p)) ** 1.5,
                        "eps_R_TR1": 0.5 * dq(P0, P1)}
P1t = [(a + 1.0, w) for a, w in S]
res["M2_translation"] = {"eps_R_TR1": 0.5 * dq(S, P1t)}
print(json.dumps(res, indent=1, default=float))
