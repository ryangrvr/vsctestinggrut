#!/usr/bin/env python3
"""F0-SD0 Stage-1 reconnaissance (charter 909eaf8, Owner Ruling 05 C4 Stage 1(i)).

Exact enumeration of the (2,2,2) Bell scenario at the support level.

Objects: Alice measurements a0,a1; Bob b0,b1; contexts the four pairs (x,y);
binary outcomes. A support table S assigns each context a nonempty subset of
{0,1}^2. Constraints and classifications:

  POSSIBILISTIC NO-SIGNALLING (pNS): for each party, the set of locally possible
  outcomes of a measurement is the same in both contexts containing it.

  GLOBAL SECTIONS: g in {0,1}^4 (values for a0,a1,b0,b1) consistent with S iff
  g's restriction to every context lies in that context's support.
    - strongly contextual: no consistent global section;
    - possibilistically LOCAL (noncontextual): every possible section of every
      context extends to a consistent global section;
    - logically contextual: consistent globals exist but some possible section
      does not extend.

  PROBABILISTIC EXACT-SUPPORT REALIZABILITY: S is the exact (p>0) support of a
  probabilistic no-disturbance model iff the polytope P_S (normalization per
  context + no-disturbance equalities + p=0 off S + p>=0) contains, for every
  cell c in S, a point with p_c > 0. By the mixing-union lemma (F0 charter-input
  section 3, proved), a uniform mixture of the per-cell witnesses then has
  support exactly S. Each check is an exact rational LP (Fraction simplex,
  Bland's rule).

All arithmetic exact (fractions / integers). No floats anywhere.
"""
from fractions import Fraction as Fr
from itertools import product, combinations

XS = [0, 1]            # Alice measurement index
YS = [0, 1]            # Bob measurement index
CELLS = [(x, y, o1, o2) for x in XS for y in YS for o1 in (0, 1) for o2 in (0, 1)]
CIDX = {c: i for i, c in enumerate(CELLS)}
CTX = [(x, y) for x in XS for y in YS]

# ---------------- exact rational simplex (maximize c.x st Ax=b, x>=0) ----------
def simplex_max(A, b, c):
    """Return (status, value) with status 'OPT'/'INFEASIBLE'/'UNBOUNDED'.
    Two-phase simplex, Bland's rule, exact Fractions. Small problems only."""
    m, n = len(A), len(c)
    # phase 1: add artificials
    T = [row[:] + [Fr(0)] * m + [b[i]] for i, row in enumerate(A)]
    for i in range(m):
        if T[i][-1] < 0:
            T[i] = [-v for v in T[i]]
        T[i][n + i] = Fr(1)
    basis = list(range(n, n + m))
    cost1 = [Fr(0)] * n + [Fr(1)] * m

    def pivot(T, basis, col, row):
        pv = T[row][col]
        T[row] = [v / pv for v in T[row]]
        for r in range(len(T)):
            if r != row and T[r][col] != 0:
                f = T[r][col]
                T[r] = [a - f * d for a, d in zip(T[r], T[row])]
        basis[row] = col

    def solve(T, basis, cost):
        while True:
            # reduced costs (maximize): z_j - c_j with cost of basis
            red = []
            for j in range(len(T[0]) - 1):
                zj = sum(cost[basis[i]] * T[i][j] for i in range(len(T)))
                red.append(zj - cost[j])
            # Bland: entering = smallest j with red<0 (for maximize of -cost1 we minimize)
            enter = next((j for j, r in enumerate(red) if r < 0), None)
            if enter is None:
                return True
            ratios = [(T[i][-1] / T[i][enter], i) for i in range(len(T)) if T[i][enter] > 0]
            if not ratios:
                return False  # unbounded
            _, row = min(ratios, key=lambda t: (t[0], basis[t[1]]))
            pivot(T, basis, enter, row)

    # phase 1: minimize sum of artificials == maximize -sum
    neg1 = [Fr(0)] * n + [Fr(-1)] * m
    solve(T, basis, neg1)
    p1val = sum(Fr(1) * T[i][-1] for i in range(m) if basis[i] >= n)
    if any(basis[i] >= n and T[i][-1] != 0 for i in range(m)):
        return ('INFEASIBLE', None)
    # drive artificials out of basis where possible; then drop artificial columns
    for i in range(m):
        if basis[i] >= n:
            col = next((j for j in range(n) if T[i][j] != 0), None)
            if col is not None:
                pivot(T, basis, col, i)
    keep_rows = [i for i in range(m) if basis[i] < n]
    T = [[T[i][j] for j in range(n)] + [T[i][-1]] for i in keep_rows]
    basis = [basis[i] for i in keep_rows]
    # phase 2: maximize c
    cost2 = list(c)
    ok = solve(T, basis, cost2)
    if not ok:
        return ('UNBOUNDED', None)
    val = sum(cost2[basis[i]] * T[i][-1] for i in range(len(T)))
    return ('OPT', val)


def build_eqs(support_cells):
    """Equality system over the support cells only (off-support fixed to 0)."""
    cols = sorted(support_cells, key=lambda c: CIDX[c])
    ci = {c: i for i, c in enumerate(cols)}
    A, b = [], []
    # normalization per context
    for (x, y) in CTX:
        row = [Fr(0)] * len(cols)
        for c in cols:
            if c[0] == x and c[1] == y:
                row[ci[c]] = Fr(1)
        A.append(row); b.append(Fr(1))
    # no-disturbance: Alice's marginal of (x,o1) equal across y=0,1
    for x in XS:
        for o1 in (0, 1):
            row = [Fr(0)] * len(cols)
            for c in cols:
                if c[0] == x and c[2] == o1:
                    row[ci[c]] += Fr(1) if c[1] == 0 else Fr(-1)
            A.append(row); b.append(Fr(0))
    for y in YS:
        for o2 in (0, 1):
            row = [Fr(0)] * len(cols)
            for c in cols:
                if c[1] == y and c[3] == o2:
                    row[ci[c]] += Fr(1) if c[0] == 0 else Fr(-1)
            A.append(row); b.append(Fr(0))
    return cols, A, b


def exact_support_realizable(S):
    """S: dict ctx -> frozenset of (o1,o2). Exact-support realizability check."""
    cells = {(x, y, o1, o2) for (x, y) in CTX for (o1, o2) in S[(x, y)]}
    cols, A, b = build_eqs(cells)
    for c in cols:
        obj = [Fr(1) if cc == c else Fr(0) for cc in cols]
        status, val = simplex_max(A, b, obj)
        if status == 'INFEASIBLE':
            return False
        if val == 0:
            return False
    return True


# ---------------- enumeration ----------------
def proj1(sec_set): return frozenset(s[0] for s in sec_set)
def proj2(sec_set): return frozenset(s[1] for s in sec_set)

NONEMPTY = [frozenset(s) for r in range(1, 5) for s in combinations(product((0, 1), repeat=2), r)]

def pns_tables():
    out = []
    for s00 in NONEMPTY:
        for s01 in NONEMPTY:
            if proj1(s00) != proj1(s01):
                continue
            for s10 in NONEMPTY:
                if proj2(s00) != proj2(s10):
                    continue
                for s11 in NONEMPTY:
                    if proj1(s10) != proj1(s11) or proj2(s01) != proj2(s11):
                        continue
                    out.append({(0, 0): s00, (0, 1): s01, (1, 0): s10, (1, 1): s11})
    return out


def classify(S):
    globals_ok = []
    for g in product((0, 1), repeat=4):  # (a0,a1,b0,b1)
        if all((g[x], g[2 + y]) in S[(x, y)] for (x, y) in CTX):
            globals_ok.append(g)
    if not globals_ok:
        return 'strong', globals_ok
    for (x, y) in CTX:
        for s in S[(x, y)]:
            if not any(g[x] == s[0] and g[2 + y] == s[1] for g in globals_ok):
                return 'logical', globals_ok
    return 'local', globals_ok


# anchors
def pr_boxes():
    """The 8 PR boxes: a xor b = x.y xor (alpha.x xor beta.y xor gamma)."""
    boxes = []
    for alpha in (0, 1):
        for beta in (0, 1):
            for gamma in (0, 1):
                S = {}
                for (x, y) in CTX:
                    target = (x * y) ^ (alpha * x) ^ (beta * y) ^ gamma
                    S[(x, y)] = frozenset((o1, o2) for o1 in (0, 1) for o2 in (0, 1)
                                          if (o1 ^ o2) == target)
                boxes.append(S)
    return boxes


def hardy_canonical():
    """Canonical Hardy support (possibilistic form, Mansfield-Fritz):
    (0,0) possible in (a0,b0); (0,0) impossible in (a0,b1) and (a1,b0);
    (1,1) impossible in (a1,b1); realized by the standard Hardy supports."""
    return {(0, 0): frozenset({(0, 0), (0, 1), (1, 0), (1, 1)}) - frozenset(),
            }  # placeholder; detection is pattern-based below


SYMS = []
def all_symmetries():
    """Generate table transforms: swap Alice measurements, swap Bob measurements,
    swap parties, flip any outcome labels per measurement (2^4)."""
    ops = []
    for swap_a in (False, True):
        for swap_b in (False, True):
            for swap_p in (False, True):
                for fa0 in (0, 1):
                    for fa1 in (0, 1):
                        for fb0 in (0, 1):
                            for fb1 in (0, 1):
                                ops.append((swap_a, swap_b, swap_p, (fa0, fa1), (fb0, fb1)))
    return ops

def transform(S, op):
    swap_a, swap_b, swap_p, fa, fb = op
    T = {}
    for (x, y) in CTX:
        xs = 1 - x if swap_a else x
        ys = 1 - y if swap_b else y
        src = S[(ys, xs)] if swap_p else S[(xs, ys)]
        cells = set()
        for (o1, o2) in src:
            if swap_p:
                o1, o2 = o2, o1
            cells.add((o1 ^ fa[x], o2 ^ fb[y]))
        T[(x, y)] = frozenset(cells)
    return T

def has_hardy(S):
    """Hardy configuration (plain, (2,2,2)): up to symmetry,
    (0,0) in S_{00}; (0,0) not in S_{01}; (0,0) not in S_{10}; (1,1) not in S_{11}."""
    for op in SYMS:
        T = transform(S, op)
        if ((0, 0) in T[(0, 0)] and (0, 0) not in T[(0, 1)]
                and (0, 0) not in T[(1, 0)] and (1, 1) not in T[(1, 1)]):
            return True
    return False


def main():
    global SYMS
    SYMS = all_symmetries()
    tables = pns_tables()
    print(f"possibilistic no-signalling support tables (nonempty contexts): {len(tables)}")

    classes = {'local': [], 'logical': [], 'strong': []}
    for S in tables:
        k, _ = classify(S)
        classes[k].append(S)
    for k in ('local', 'logical', 'strong'):
        print(f"  {k}: {len(classes[k])}")

    # realizability (exact-support) per class
    real = {k: [] for k in classes}
    for k in ('local', 'logical', 'strong'):
        for S in classes[k]:
            if exact_support_realizable(S):
                real[k].append(S)
        print(f"  {k} AND probabilistically exact-support realizable: {len(real[k])}")

    # Lal reproduction: strongly contextual & realizable == the 8 PR boxes
    prs = pr_boxes()
    def key(S): return tuple(sorted((ctx, tuple(sorted(S[ctx]))) for ctx in CTX))
    sr = {key(S) for S in real['strong']}
    pk = {key(S) for S in prs}
    print(f"  PR boxes constructed: {len(pk)}; strongly-contextual realizable set equals PR set: {sr == pk}")

    # Mansfield-Fritz check: every realizable possibilistically-nonlocal table
    # (logical or strong) contains a plain Hardy configuration
    nonlocal_real = real['logical'] + real['strong']
    hardy_ok = sum(1 for S in nonlocal_real if has_hardy(S))
    print(f"  realizable possibilistically-nonlocal tables: {len(nonlocal_real)}; "
          f"containing a Hardy configuration: {hardy_ok} "
          f"(completeness reproduced: {hardy_ok == len(nonlocal_real)})")

    # possibilistic-but-not-realizable gap
    gap = {k: len(classes[k]) - len(real[k]) for k in classes}
    print(f"  pNS tables NOT exact-support realizable: "
          f"local {gap['local']}, logical {gap['logical']}, strong {gap['strong']}")

if __name__ == '__main__':
    main()
