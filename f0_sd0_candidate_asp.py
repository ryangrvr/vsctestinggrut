#!/usr/bin/env python3
"""Anchored-Support Principle (ASP) -- candidate implementation + mechanical battery.

Scenario: vars (hashable names), contexts (tuples of vars), outcomes per var
implicit from supports. Support: dict ctx_tuple -> frozenset of outcome tuples
(aligned with ctx order), every context nonempty, pNS assumed/checkable.

LAW (ASP): S is admissible iff for EVERY nonempty U subseteq X, the induced
sub-realization S|U is ANCHORED: it has at least one possible event (U',s)
(section over a co-measurable set, possible in at least one context) whose
steering closure (per-variable arc-consistency fixpoint across all contexts)
terminates with no empty context restriction.
"""
from itertools import product, combinations
import sys, random

# ---------- core ----------
def var_sets(contexts, support):
    """Per-variable possibility sets (pNS: equal across contexts; take union+check)."""
    P = {}
    for ctx in contexts:
        for i, v in enumerate(ctx):
            vals = {t[i] for t in support[ctx]}
            if v in P:
                if P[v] != vals:
                    return None  # pNS violated
            else:
                P[v] = vals
    return P

def check_pns(contexts, support):
    return var_sets(contexts, support) is not None

def ac_consistent(contexts, support, seed, P0=None):
    """Steering closure from seed (dict var->val). True iff no contradiction."""
    P = {v: set(s) for v, s in (P0 or var_sets(contexts, support)).items()}
    for v, val in seed.items():
        if val not in P[v]:
            return False
        P[v] = {val}
    changed = True
    while changed:
        changed = False
        for ctx in contexts:
            R = [t for t in support[ctx]
                 if all(t[i] in P[ctx[i]] for i in range(len(ctx)))]
            if not R:
                return False
            for i, v in enumerate(ctx):
                vals = {t[i] for t in R}
                if vals != P[v]:
                    P[v] = vals
                    changed = True
    return True

def iter_events(contexts, support):
    """All possible events: nonempty U within a context, s in proj_U(S_C) for
    at least one C >= U. Deduped."""
    seen = set()
    for ctx in contexts:
        n = len(ctx)
        for r in range(1, n + 1):
            for idxs in combinations(range(n), r):
                secs = {tuple(t[i] for i in idxs) for t in support[ctx]}
                vs = tuple(ctx[i] for i in idxs)
                for s in secs:
                    key = frozenset(zip(vs, s))
                    if key in seen:
                        continue
                    seen.add(key)
                    yield dict(zip(vs, s))

def anchored(contexts, support):
    """Exists an event with consistent steering closure?"""
    P0 = var_sets(contexts, support)
    assert P0 is not None, "pNS violated"
    for ev in iter_events(contexts, support):
        if ac_consistent(contexts, support, ev, P0):
            return True
    return False

def event_stats(contexts, support):
    P0 = var_sets(contexts, support)
    tot = ok = 0
    for ev in iter_events(contexts, support):
        tot += 1
        if ac_consistent(contexts, support, ev, P0):
            ok += 1
    return ok, tot

def induced(contexts, support, U):
    """Induced sub-realization on variable set U (union-projection, maximal cover)."""
    U = set(U)
    inters = {}
    for ctx in contexts:
        D = tuple(sorted((v for v in ctx if v in U), key=str))
        if D:
            inters.setdefault(D, []).append(ctx)
    Ds = list(inters)
    maximal = [D for D in Ds
               if not any(set(D) < set(D2) for D2 in Ds)]
    sup = {}
    for D in maximal:
        cells = set()
        for ctx in inters[D]:
            pos = [ctx.index(v) for v in D]
            cells |= {tuple(t[i] for i in pos) for t in support[ctx]}
        sup[D] = frozenset(cells)
    return maximal, sup

def asp_admissible(contexts, support, variables=None, return_witness=False):
    """Hereditarily anchored? Checks every nonempty subset of variables."""
    if variables is None:
        variables = sorted({v for c in contexts for v in c}, key=str)
    n = len(variables)
    # check the full scenario first (cheap rejection for PR-like cores)
    for r in range(n, 0, -1):
        for Uc in combinations(variables, r):
            cx, sp = induced(contexts, support, Uc)
            if not anchored(cx, sp):
                return (False, Uc) if return_witness else False
    return (True, None) if return_witness else True

def classify_generic(contexts, support, variables=None):
    """local / logical / strong via exhaustive global sections."""
    if variables is None:
        variables = sorted({v for c in contexts for v in c}, key=str)
    P = var_sets(contexts, support)
    doms = [sorted(P[v], key=str) for v in variables]
    vi = {v: i for i, v in enumerate(variables)}
    globals_ok = []
    for g in product(*doms):
        if all(tuple(g[vi[v]] for v in ctx) in support[ctx] for ctx in contexts):
            globals_ok.append(g)
    if not globals_ok:
        return 'strong'
    for ctx in contexts:
        for s in support[ctx]:
            if not any(all(g[vi[ctx[i]]] == s[i] for i in range(len(ctx)))
                       for g in globals_ok):
                return 'logical'
    return 'local'

# ---------- scenario builders ----------
def table222_to_generic(S):
    """Recon dict {(x,y): frozenset{(o1,o2)}} -> generic."""
    contexts = [('a0', 'b0'), ('a0', 'b1'), ('a1', 'b0'), ('a1', 'b1')]
    sup = {}
    for (x, y) in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        sup[('a%d' % x, 'b%d' % y)] = frozenset(S[(x, y)])
    return contexts, sup

def ghz3_support():
    """GHZ (3,2,2): vars X1,Y1,X2,Y2,X3,Y3; 8 contexts (one var per party).
    Even #Y -> parity constraint (XXX:0; two-Y:1); odd #Y -> full."""
    contexts, sup = [], {}
    for t1 in 'XY':
        for t2 in 'XY':
            for t3 in 'XY':
                ctx = (t1 + '1', t2 + '2', t3 + '3')
                ny = (t1 + t2 + t3).count('Y')
                if ny % 2 == 0:
                    tgt = 0 if ny == 0 else 1
                    cells = {(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)
                             if a ^ b ^ c == tgt}
                else:
                    cells = set(product((0, 1), repeat=3))
                contexts.append(ctx)
                sup[ctx] = frozenset(cells)
    return contexts, sup

def ghz4_G1_support():
    """G1 (4,2,2): 8 contexts: XXXX parity0; six two-Y contexts parity1; YYYY parity0."""
    def ctx_of(types):
        return tuple(t + str(i + 1) for i, t in enumerate(types))
    def par(types):
        ny = types.count('Y')
        if types in ('XXXX', 'YYYY'):
            return 0
        if ny == 2:
            return 1
        return None
    contexts, sup = [], {}
    for types in ['XXXX', 'XXYY', 'XYXY', 'XYYX', 'YXXY', 'YXYX', 'YYXX', 'YYYY']:
        p = par(types)
        ctx = ctx_of(types)
        cells = {t for t in product((0, 1), repeat=4)
                 if (t[0] ^ t[1] ^ t[2] ^ t[3]) == p}
        contexts.append(ctx)
        sup[ctx] = frozenset(cells)
    return contexts, sup

def peres_mermin_support():
    """PM square: 9 vars o_rc; contexts 3 rows + 3 cols; outcomes 0/1 (=+1/-1 exp);
    row parities 0, col parities 0,0,1 (odd column = third)."""
    v = lambda r, c: 'o%d%d' % (r, c)
    contexts, sup = [], {}
    for r in range(3):
        ctx = (v(r, 0), v(r, 1), v(r, 2))
        contexts.append(ctx)
        sup[ctx] = frozenset(t for t in product((0, 1), repeat=3)
                             if t[0] ^ t[1] ^ t[2] == 0)
    for c in range(3):
        ctx = (v(0, c), v(1, c), v(2, c))
        contexts.append(ctx)
        tgt = 1 if c == 2 else 0
        sup[ctx] = frozenset(t for t in product((0, 1), repeat=3)
                             if t[0] ^ t[1] ^ t[2] == tgt)
    return contexts, sup

def magic_square_bipartite_support():
    """SD-K6: bipartite magic square pseudo-telepathy support.
    Alice A1..A3 (row assignments, parity 0 -> 4 outcomes as tuples),
    Bob B1..B3 (col assignments, parity 1), context (Ar,Bc): agree at cell (r,c)."""
    rows = [t for t in product((0, 1), repeat=3) if t[0] ^ t[1] ^ t[2] == 0]
    cols = [t for t in product((0, 1), repeat=3) if t[0] ^ t[1] ^ t[2] == 1]
    contexts, sup = [], {}
    for r in range(3):
        for c in range(3):
            ctx = ('A%d' % r, 'B%d' % c)
            cells = {(al, bo) for al in rows for bo in cols if al[c] == bo[r]}
            contexts.append(ctx)
            sup[ctx] = frozenset(cells)
    return contexts, sup

def xor232_support(T):
    """(2,3,2) XOR table: T[i][j] target for a_i xor b_j."""
    contexts, sup = [], {}
    for i in range(3):
        for j in range(3):
            ctx = ('a%d' % i, 'b%d' % j)
            contexts.append(ctx)
            sup[ctx] = frozenset((a, a ^ T[i][j]) for a in (0, 1))
    return contexts, sup

def product_support(cx1, s1, cx2, s2):
    contexts, sup = [], {}
    for c1 in cx1:
        for c2 in cx2:
            ctx = c1 + c2
            contexts.append(ctx)
            sup[ctx] = frozenset(t1 + t2 for t1 in s1[c1] for t2 in s2[c2])
    return contexts, sup
