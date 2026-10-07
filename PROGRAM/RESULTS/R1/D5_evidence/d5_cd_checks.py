"""Exact sanity checks for the D5 questions C and D (scratch; evidence only, not results).

(K1) Prefix-tree causal linear representation (Theorem D2): three protocols on a
     2-time grid; P1 and P2 share the prefix through t1 (non-anticipating family).
     Build the tree latent (node variables, children conditionally independent given
     ancestors), 0/1 selection readouts; check h_a#mu == P_a exactly and that row j of
     h_a depends only on the prefix class [a]_j.
(K2) Plain product latent (Theorem D1) on the same family: exact, but row 1 of h_1
     and h_2 differ although P1, P2 share the prefix -> not causal.
(K3) Excess-e gluing (Prop C3), k = 2, e = 1: P0, P1 on Z^2 (finite support) with a
     common 1-D linear marginal; glue along it; check the latent lives on a
     3-dim subspace and the two coordinate projections reproduce P0, P1 exactly.
(K4) Atom-count step of Theorem C1 (necessity): two readouts with different level
     sets give laws with different atom counts under a two-point environment law.
(K5) Symmetry route (Prop C4): a centrally symmetric latent read through
     non-injective, protocol-dependent linear maps gives centrally symmetric records;
     E2's asymmetric latent does not.
"""
from fractions import Fraction as Fr
from itertools import product
from collections import defaultdict
import json, sys

out = {}

def law_add(d, key, w):
    d[key] = d.get(key, Fr(0)) + w

# ---------------- K1/K2: non-anticipating family on grid (t1, t2) ----------------
# protocols: a0 (prefix class A at t1), a1, a2 (share prefix class B at t1; differ at t2)
# records: Y = (Y1, Y2) with small finite supports
P = {
    "a0": {(0, 0): Fr(1, 2), (1, 1): Fr(1, 4), (-1, 1): Fr(1, 4)},
    "a1": {(0, 1): Fr(1, 3), (0, -1): Fr(1, 6), (2, 0): Fr(1, 2)},
    "a2": {(0, 3): Fr(1, 6), (0, 0): Fr(1, 3), (2, 5): Fr(1, 4), (2, -5): Fr(1, 4)},
}
prefix = {"a0": ("A", "A0"), "a1": ("B", "B1"), "a2": ("B", "B2")}  # class at level 1, level 2

def marg1(p):
    m = {}
    for (y1, y2), w in p.items():
        law_add(m, y1, w)
    return m

# non-anticipation check: a1, a2 share first-coordinate law
out["K1_nonanticipating_first_marginal_equal"] = marg1(P["a1"]) == marg1(P["a2"])

# tree latent: level-1 node per class at level 1; level-2 node per class at level 2.
# Z = (Z_A, Z_B, Z_A0, Z_B1, Z_B2). Z_A ~ P_a0 first marginal; Z_B ~ P_a1 first marginal.
# Z_{child} | Z_{parent} ~ conditional of Y2 given Y1 under any protocol in the child class.
def cond2(p):
    m1 = marg1(p)
    c = defaultdict(dict)
    for (y1, y2), w in p.items():
        law_add(c[y1], y2, w / m1[y1])
    return c

lvl1 = {"A": marg1(P["a0"]), "B": marg1(P["a1"])}
lvl2 = {"A0": ("A", cond2(P["a0"])), "B1": ("B", cond2(P["a1"])), "B2": ("B", cond2(P["a2"]))}
nodes = ["A", "B", "A0", "B1", "B2"]

mu = {}
for zA, wA in lvl1["A"].items():
    for zB, wB in lvl1["B"].items():
        for zA0, wA0 in lvl2["A0"][1][zA].items():
            for zB1, wB1 in lvl2["B1"][1][zB].items():
                for zB2, wB2 in lvl2["B2"][1][zB].items():
                    law_add(mu, (zA, zB, zA0, zB1, zB2), wA * wB * wA0 * wB1 * wB2)
out["K1_mu_total_mass"] = str(sum(mu.values()))

# 0/1 selection readouts: row j picks the node of a's class at level j
H = {a: [nodes.index(prefix[a][0]), nodes.index(prefix[a][1])] for a in P}
ok_exact = True
for a, rows in H.items():
    img = {}
    for z, w in mu.items():
        law_add(img, (z[rows[0]], z[rows[1]]), w)
    img = {k: v for k, v in img.items() if v != 0}
    ok_exact &= (img == P[a])
out["K1_tree_selection_exact_for_all_protocols"] = ok_exact
# causality: row 1 of h_a1 == row 1 of h_a2 (same level-1 class)
out["K1_row1_shared_by_prefix_class"] = H["a1"][0] == H["a2"][0]

# K2: plain product latent: Z = (Y^{a0}, Y^{a1}, Y^{a2}) independent; h_a = projection onto copy a
mu_prod = {}
for (y0, w0), (y1, w1), (y2, w2) in product(P["a0"].items(), P["a1"].items(), P["a2"].items()):
    law_add(mu_prod, (y0, y1, y2), w0 * w1 * w2)
ok = True
for i, a in enumerate(["a0", "a1", "a2"]):
    img = {}
    for z, w in mu_prod.items():
        law_add(img, z[i], w)
    ok &= (img == P[a])
out["K2_product_projection_exact"] = ok
# causality fails: the time-1 coordinate read under a1 is copy-1's, under a2 copy-2's (different latent coords)
out["K2_row1_differs_between_a1_a2_despite_shared_prefix"] = True  # by construction: pi_{a1,1} != pi_{a2,1}

# ---------------- K3: excess-1 gluing, k = 2 ----------------
# P0: centrally symmetric on Z^2; P1: skewed; common 1-D marginal: l0(y) = y[0] for P0, l1(y) = y[0] for P1
P0 = {(1, 1): Fr(1, 4), (-1, -1): Fr(1, 4), (1, -2): Fr(1, 8), (-1, 2): Fr(1, 8), (0, 0): Fr(1, 4)}
P1 = {(1, 3): Fr(1, 4), (1, 0): Fr(1, 8), (-1, 0): Fr(1, 8), (-1, -4): Fr(1, 4), (0, 2): Fr(1, 4)}
def lin_marg(p, f):
    m = {}
    for y, w in p.items():
        law_add(m, f(y), w)
    return m
l0 = lambda y: y[0]
l1 = lambda y: y[0]
out["K3_common_marginal"] = lin_marg(P0, l0) == lin_marg(P1, l1)
def third_central(p):
    m = [sum(w * y[i] for y, w in p.items()) for i in range(2)]
    return [sum(w * (y[i] - m[i]) ** 3 for y, w in p.items()) for i in range(2)]
out["K3_P0_third_central_moments"] = [str(x) for x in third_central(P0)]
out["K3_P1_third_central_moments"] = [str(x) for x in third_central(P1)]
# glue: (Y0, Y1) conditionally independent given r = l0(Y0) = l1(Y1)
R = lin_marg(P0, l0)
mu3 = {}
for y0, w0 in P0.items():
    for y1, w1 in P1.items():
        if l0(y0) == l1(y1):
            r = l0(y0)
            law_add(mu3, (y0[0], y0[1], y1[1]), w0 * w1 / R[r])  # latent z = (r, y0_2, y1_2) in R^3
out["K3_latent_dim"] = 3
out["K3_mass"] = str(sum(mu3.values()))
img0 = lin_marg(mu3, lambda z: (z[0], z[1]))
img1 = lin_marg(mu3, lambda z: (z[0], z[2]))
out["K3_h0_exact"] = {k: v for k, v in img0.items() if v} == P0
out["K3_h1_exact"] = {k: v for k, v in img1.items() if v} == P1
out["K3_kernels_differ"] = True  # ker h0 = span(e3), ker h1 = span(e2)

# ---------------- K4: atom counting ----------------
h_b = lambda z: z % 2          # identifies z and z+2
h_a = lambda z: z              # injective
mu4 = {0: Fr(1, 2), 2: Fr(1, 2)}
out["K4_atoms_h_a_vs_h_b"] = [len(lin_marg(mu4, h_a)), len(lin_marg(mu4, h_b))]

# ---------------- K5: symmetry route ----------------
# latent in Z^3, centrally symmetric; readouts: protocol 0 reads z1, protocol 1 reads z1 + z3 (non-injective, mode-selecting)
muS = {}
base = {(1, 0, 2): Fr(1, 6), (0, 1, 1): Fr(1, 6), (2, -1, 0): Fr(1, 6)}
for z, w in base.items():
    law_add(muS, z, w)
    law_add(muS, tuple(-x for x in z), w)
def sym1(p):
    return all(p.get(-y, 0) == w for y, w in p.items())
r0 = lin_marg(muS, lambda z: z[0])
r1 = lin_marg(muS, lambda z: z[0] + z[2])
out["K5_symmetric_latent_records_symmetric"] = [sym1(r0), sym1(r1)]
# E2-type asymmetric latent: S symmetric, U skewed independent; read S vs S+U
S = {1: Fr(1, 2), -1: Fr(1, 2)}
U = {2: Fr(1, 3), -1: Fr(2, 3)}  # mean 0, skewed
rS = S
rSU = {}
for s, ws in S.items():
    for u, wu in U.items():
        law_add(rSU, s + u, ws * wu)
out["K5_E2_records_symmetric"] = [sym1(rS), sym1(rSU)]

json.dump(out, sys.stdout, indent=1, default=str)
print()
