#!/usr/bin/env python3
"""G3 preregistered-property verification (Mansfield-Fritz Table (b), arXiv:1105.1819,
entries extracted verbatim from the LaTeX source): (1) exact normalization and
no-signalling of the probabilistic model; (2) possibilistic non-locality; (3) NO
coarse-grained Hardy paradox: for every pair of Alice settings, every pair of Bob
settings, and every binary coarse-graining (two nonempty blocks) of each involved
measurement's outcome set, the coarse-grained 2x2 binary support contains no Hardy
configuration under the full relabelling symmetry (setting swaps, party swap,
outcome flips). Exact Fractions."""
from fractions import Fraction as F
from itertools import product, combinations
A = ['a1', 'a2', 'a3']; B = ['b1', 'b2']; OA = {a: (0, 1) for a in A}; OB = {'b1': (0, 1), 'b2': (0, 1, 2)}
# rows: (alice setting, alice outcome); cols: b1 outcomes 0,1 | b2 outcomes 0,1,2  (verbatim LaTeX table (b))
rows = {('a1',0): [F(1,16), F(3,16), F(0), F(1,8), F(1,8)],
        ('a1',1): [F(3,16), F(9,16), F(1,2), F(1,8), F(1,8)],
        ('a2',0): [F(0), F(1,2), F(1,8), F(1,4), F(1,8)],
        ('a2',1): [F(1,4), F(1,4), F(3,8), F(0), F(1,8)],
        ('a3',0): [F(0), F(1,2), F(1,8), F(1,8), F(1,4)],
        ('a3',1): [F(1,4), F(1,4), F(3,8), F(1,8), F(0)]}
cols = [('b1',0), ('b1',1), ('b2',0), ('b2',1), ('b2',2)]
p = {(a, b): {} for a in A for b in B}
for (a, oa), vals in rows.items():
    for (b, ob), v in zip(cols, vals):
        p[(a, b)][(oa, ob)] = v
ok_norm = all(sum(p[c].values()) == 1 for c in p)
ok_ns = all(len({sum(v for (oa, ob), v in p[(a, b)].items() if oa == o) for b in B}) == 1 for a in A for o in (0, 1)) and \
        all(len({sum(v for (oa, ob), v in p[(a, b)].items() if ob == o) for a in A}) == 1 for b in B for o in OB[b])
S = {c: {k for k, v in p[c].items() if v > 0} for c in p}
print(f"(1) normalization exact: {ok_norm}; no-signalling exact: {ok_ns}; zero cells: {sum(1 for c in p for v in p[c].values() if v == 0)}")
glob = [g for g in product(*[OA[a] for a in A], *[OB[b] for b in B])
        if all((g[A.index(a)], g[3 + B.index(b)]) in S[(a, b)] for a in A for b in B)]
nonext = [(c, s) for c in S for s in S[c]
          if not any((g[A.index(c[0])], g[3 + B.index(c[1])]) == s for g in glob)]
print(f"(2) global sections: {len(glob)}; possible sections not extending: {len(nonext)} -> possibilistically non-local: {len(nonext) > 0}")
def blockings(outs):
    outs = list(outs); res = []
    for r in range(1, len(outs)):
        for blk in combinations(outs, r):
            if outs[0] in blk: res.append({o: 0 if o in blk else 1 for o in outs})
    return res
def has_hardy(T):  # T: dict (x,y)->set of (u,v) binary
    for sx, sy, sp, f in product((0,1), (0,1), (0,1), product((0,1), repeat=4)):
        def get(x, y):
            xx, yy = (x ^ sx, y ^ sy)
            src = T[(yy, xx)] if sp else T[(xx, yy)]
            out = set()
            for (u, v) in src:
                if sp: u, v = v, u
                out.add((u ^ f[x], v ^ f[2 + y]))
            return out
        if (0,0) in get(0,0) and (0,0) not in get(0,1) and (0,0) not in get(1,0) and (1,1) not in get(1,1):
            return True
    return False
found = 0; checked = 0
for (x0, x1) in combinations(A, 2):
    for (y0, y1) in [('b1', 'b2')]:
        for bx0, bx1, by0, by1 in product(blockings(OA[x0]), blockings(OA[x1]), blockings(OB[y0]), blockings(OB[y1])):
            T = {}
            for i, (xa, bx) in enumerate([(x0, bx0), (x1, bx1)]):
                for j, (yb, by) in enumerate([(y0, by0), (y1, by1)]):
                    T[(i, j)] = {(bx[u], by[v]) for (u, v) in S[(xa, yb)]}
            checked += 1
            if has_hardy(T): found += 1
print(f"(3) coarse-grained 2x2 sub-tables checked: {checked}; containing a Hardy configuration: {found} -> NO coarse-grained Hardy paradox: {found == 0}")
