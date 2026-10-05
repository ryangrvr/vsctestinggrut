#!/usr/bin/env python3
"""F0-A kinematic validator — validates DEFINITIONS ONLY (F0_A_KINEMATIC_FORMULATION_01.md).

This is a KINEMATIC VALIDATOR, not a physical-law implementation:
  * it classifies NO context transition as allowed or forbidden;
  * it implements NO R_Gamma, A_Gamma, Cl_Gamma, S, or U;
  * it checks only structural well-formedness declared in the formulation.

Pure Python stdlib. Run: python3 f0_kinematic_validator.py   (prints PASS/FAIL per test).
"""
from itertools import combinations, product
from fractions import Fraction as Fr

# ---------------------------------------------------------------- data structures

class KinematicObject:
    """K = (X, {O_x}, C, E, Gamma) per F0_A_KINEMATIC_FORMULATION_01.md.

    C : frozenset of frozensets (downward-closed family of nonempty subsets of X).
    E(C) = product of outcome alphabets (projection restriction maps, §5.1).
    Gamma = {C: {global_section: Fraction}} (§6.1).
    """
    def __init__(self, X, alphabets, contexts, gamma):
        self.X = frozenset(X)
        self.O = {x: tuple(sorted(alphabets[x])) for x in X}
        self.C = frozenset(frozenset(c) for c in contexts)
        self.gamma = {frozenset(c): {tuple(s): Fr(v) for s, v in g.items()}
                      for c, g in gamma.items()}

    def sections(self, ctx):
        out = tuple(self.O[x] for x in sorted(ctx))
        return sorted(product(*out)) if out else [()]

    def marginal(self, ctx, sub):
        """p_ctx restricted to sub (§6.1 condition 3, right side)."""
        keep = tuple(i for i, x in enumerate(sorted(ctx)) if x in sub)
        m = {}
        for s, v in self.gamma[ctx].items():
            t = tuple(s[i] for i in keep)
            m[t] = m.get(t, Fr(0)) + v
        return m

# ---------------------------------------------------------------- suite instances (§9)

def suite_k0_path():
    """K0 — acyclic control: path/tree-like contexts {ab, bc, cd}."""
    X = {"a", "b", "c", "d"}
    ctx = [frozenset(s) for s in ["a", "b", "c", "d", "ab", "bc", "cd"]]
    # binary alphabets everywhere; singleton contexts deterministic.
    alph = {x: [0, 1] for x in X}
    g = {}
    for x in X:
        g[frozenset([x])] = {(0,): Fr(1)}
    for pair in ["ab", "bc", "cd"]:
        g[frozenset(pair)] = {(0, 0): Fr(1, 2), (1, 1): Fr(1, 2)}
    # singleton marginals are determined by the pair data, but Γ must include them
    # with the SAME values (overlap compatibility is a condition, not automatic):
    for pair in ["ab", "bc", "cd"]:
        for x in pair:
            g[frozenset([x])] = {(0,): Fr(1, 2), (1,): Fr(1, 2)}
    return KinematicObject(X, alph, ctx, g)

def suite_k1_bell():
    """K1 — Bell four-cycle: labels a,b,c,d; maximal contexts ab, bc, cd, da."""
    X = ["a", "b", "c", "d"]
    ctx = [frozenset(s) for s in ["a", "b", "c", "d", "ab", "bc", "cd", "da"]]
    alph = {x: [0, 1] for x in X}
    g = {}
    for x in X:
        g[frozenset([x])] = {(0,): Fr(1, 2), (1,): Fr(1, 2)}
    # correlated pairs — the singleton marginals must match (compatibility is
    # checkable, not asserted by law; this instance satisfies it)
    for pair in ["ab", "bc", "cd", "da"]:
        g[frozenset(pair)] = {(0, 0): Fr(1, 2), (1, 1): Fr(1, 2)}
    return KinematicObject(X, alph, ctx, g)

def suite_k2_triangle():
    """K2 — Specker triangle: three pairwise contexts, NO triple context.
    Influence data: uniformly ANTI-correlated pairs (0,1)/(1,0) on each pair.
    Singleton marginals are uniform, so overlap compatibility holds, but NO global
    distribution on {a,b,c} reproduces all three pair marginals (a,b,c cannot be
    pairwise unequal simultaneously). Verified EXACTLY by test_global_extension
    (R1 repair: the previous correlated data was globally extendable and NOT a
    contextuality calibration)."""
    X = ["a", "b", "c"]
    ctx = [frozenset(s) for s in ["a", "b", "c", "ab", "bc", "ac"]]
    alph = {x: [0, 1] for x in X}
    g = {}
    for x in X:
        g[frozenset([x])] = {(0,): Fr(1, 2), (1,): Fr(1, 2)}
    for pair in ["ab", "bc", "ac"]:
        g[frozenset(pair)] = {(0, 1): Fr(1, 2), (1, 0): Fr(1, 2)}
    return KinematicObject(X, alph, ctx, g)

def suite_k3_complete():
    """K3 — complete context: everything jointly accessible (one maximal context)."""
    X = ["a", "b", "c"]
    ctx = [frozenset(s) for r in (1, 2, 3) for s in combinations(X, r)]
    alph = {x: [0, 1] for x in X}
    g = {}
    for x in X:
        g[frozenset([x])] = {(0,): Fr(1, 2), (1,): Fr(1, 2)}
    for pair in [("a", "b"), ("b", "c"), ("a", "c")]:
        g[frozenset(pair)] = {(0, 0): Fr(1, 2), (1, 1): Fr(1, 2)}
    g[frozenset(X)] = {(0, 0, 0): Fr(1, 2), (1, 1, 1): Fr(1, 2)}
    return KinematicObject(X, alph, ctx, g)

# ---------------------------------------------------------------- helpers

def maximal_contexts(C):
    return [m for m in C if not any(m < m2 for m2 in C)]

def overlaps(C, ctx):
    return [ctx & c for c in C if c != ctx and (ctx & c)]

def relabel(obj, perm, outperm=None):
    """Representation equivalence moves 1–2 (§7): relabel interventions/outcomes.
    perm: bijection on X. outperm: dict x -> permutation of O_x (as dict old->new).
    R4 repair: the outcome-permutation path is now correct and separately tested."""
    X2 = {perm[x] for x in obj.X}
    if outperm is None:
        O2 = {perm[x]: sorted(obj.O[x]) for x in obj.X}
    else:
        O2 = {perm[x]: sorted({outperm[x][o] for o in obj.O[x]}) for x in obj.X}
    C2 = [frozenset(perm[x] for x in c) for c in obj.C]
    g2 = {}
    for c, dist in obj.gamma.items():
        c2 = frozenset(perm[x] for x in c)
        order_old = sorted(c)          # coordinate order in the source context
        order_new = sorted(c2)         # coordinate order in the target context
        d = {}
        for s, v in dist.items():
            vals = {order_old[i]: (outperm[order_old[i]][s[i]] if outperm else s[i])
                    for i in range(len(c))}
            s2 = tuple(vals[x] for x in order_old)  # coordinate order unchanged; keys relabeled via c2
            d[s2] = d.get(s2, Fr(0)) + v
        g2[c2] = d
    return KinematicObject(X2, O2, C2, g2)

def down_closure_ok(C):
    """§4.1 with the §4.2 convention: contexts are nonempty; downward closure is
    checked for subcontexts of size >= 1 (the empty set is excluded by convention)."""
    for c in C:
        if not c:
            return False
        for x in c:
            if len(c) > 1 and frozenset(c - {x}) not in C:
                return False
    return True

# ---------------------------------------------------------------- tests

RESULTS = []

def test(name, fn):
    try:
        ok = fn()
        RESULTS.append((name, "PASS" if ok else "FAIL"))
    except Exception as e:  # noqa: BLE001 — validator must report, not crash
        RESULTS.append((name, f"ERROR ({e})"))

def _gamma_ok(obj):
    for c in obj.C:
        if c not in obj.gamma:
            return False
        if sum(obj.gamma[c].values()) != 1:
            return False
        if any(v < 0 for v in obj.gamma[c].values()):
            return False
    return True

def _compat_ok(obj):
    for c in obj.C:
        for sub in obj.C:
            if sub < c and not obj.marginal(c, sub).items() <= obj.gamma[sub].items():
                return False
    return True

def test_downward_closure():
    for s in (suite_k0_path(), suite_k1_bell(), suite_k2_triangle(), suite_k3_complete()):
        if not down_closure_ok(s.C):
            return False
        if any(not c for c in s.C):
            return False
    return True

def test_maximal_contexts():
    k0 = suite_k0_path(); k2 = suite_k2_triangle(); k3 = suite_k3_complete()
    m0 = sorted(sorted(m) for m in maximal_contexts(k0.C))
    m2 = sorted(sorted(m) for m in maximal_contexts(k2.C))
    m3 = sorted(sorted(m) for m in maximal_contexts(k3.C))
    return (m0 == [["a", "b"], ["b", "c"], ["c", "d"]] and
            m2 == [["a", "b"], ["a", "c"], ["b", "c"]] and
            m3 == [["a", "b", "c"]])

def test_overlaps():
    k2 = suite_k2_triangle()
    ov = {frozenset(o) for o in overlaps(k2.C, frozenset("ab"))}
    return ov == {frozenset(["a"]), frozenset(["b"])}

def test_presheaf_functoriality():
    k3 = suite_k3_complete()
    full = frozenset(k3.X)
    ab, a = frozenset(["a", "b"]), frozenset(["a"])
    # restriction through ab equals direct restriction (§5.1: r_{ab,a}∘r_{full,ab} = r_{full,a});
    # functoriality is checked on the EVENT presheaf (sections + projections), §5.1.
    s_full = set(k3.sections(full))
    s_ab = {tuple(s[i] for i, x in enumerate(sorted(full)) if x in ab) for s in s_full}
    s_a_via_ab = {tuple(s[i] for i, x in enumerate(sorted(ab)) if x in a) for s in s_ab}
    s_a_direct = {tuple(s[i] for i, x in enumerate(sorted(full)) if x in a) for s in s_full}
    return s_a_via_ab == s_a_direct

def test_gamma_wellformed():
    for s in (suite_k0_path(), suite_k1_bell(), suite_k2_triangle(), suite_k3_complete()):
        if not _gamma_ok(s):
            return False
    return True

def test_overlap_compatibility():
    for s in (suite_k0_path(), suite_k1_bell(), suite_k2_triangle(), suite_k3_complete()):
        if not _compat_ok(s):
            return False
    return True

# ------------------------------------------------- exact global-extension machinery (R1)

def k2_global_extends(obj):
    """Exact rational feasibility check: does a global distribution on the union of
    all contexts reproduce every pair marginal? Returns True/False."""
    full = frozenset(obj.X)
    targets = {c: obj.gamma[c] for c in obj.C if len(c) == 2}
    sections = obj.sections(full)
    n = len(sections)
    idx = {s: i for i, s in enumerate(sections)}
    rows = [([Fr(1)] * n, Fr(1))]
    order_full = sorted(full)
    for ctx, target in targets.items():
        keep = tuple(i for i, x in enumerate(order_full) if x in ctx)
        for t in sorted(target):
            row = [Fr(0)] * n
            for s in sections:
                if tuple(s[i] for i in keep) == t:
                    row[idx[s]] = Fr(1)
            rows.append((row, target[t]))
    # exact Gaussian elimination (Fraction arithmetic)
    mat = [list(r[0]) + [r[1]] for r in rows]
    pivots, r = [], 0
    for c in range(n):
        piv = next((rr for rr in range(r, len(mat)) if mat[rr][c] != 0), None)
        if piv is None:
            continue
        mat[r], mat[piv] = mat[piv], mat[r]
        pv = mat[r][c]
        mat[r] = [x / pv for x in mat[r]]
        for rr in range(len(mat)):
            if rr != r and mat[rr][c] != 0:
                f = mat[rr][c]
                mat[rr] = [a - f * b for a, b in zip(mat[rr], mat[r])]
        pivots.append(c)
        r += 1
    for row in mat[r:]:
        if all(x == 0 for x in row[:-1]) and row[-1] != 0:
            return False
    part = [Fr(0)] * n
    for i, c in enumerate(pivots):
        part[c] = mat[i][-1]
    free = [c for c in range(n) if c not in pivots]
    if not free:
        return all(x >= 0 for x in part)
    # one-parameter null space here (n=8, rank=7): intersect q(t) >= 0 exactly.
    v = [Fr(0)] * n
    for f in free:
        v[f] = Fr(1)
    for i, c in enumerate(pivots):
        v[c] = -mat[i][f]
    t_lo = t_hi = None
    for i in range(n):
        a_i, b_i = v[i], part[i]
        if a_i == 0:
            if b_i < 0:
                return False
        elif a_i > 0:
            lo = -b_i / a_i
            t_lo = lo if t_lo is None else max(t_lo, lo)
        else:
            hi = -b_i / a_i
            t_hi = hi if t_hi is None else min(t_hi, hi)
    if t_lo is not None and t_hi is not None and t_lo > t_hi:
        return False
    return True

def test_global_extension():
    """R1 repair: EXACT global-extension checker. Known contextuality CALIBRATION
    only — no F0 novelty claim. K2 (uniform anti-correlated triangle):
    overlap-compatible but NO global distribution on {a,b,c} reproduces all three
    pair marginals. K3: the declared triple context's distribution extends all pairs.
    Nonextendability is verified exactly, NOT inferred from absence of the triple
    context in C."""
    k2 = suite_k2_triangle()
    k2_ext = k2_global_extends(k2)
    k3 = suite_k3_complete()
    gfull = k3.gamma[frozenset(k3.X)]
    targets = {c: k3.gamma[c] for c in k3.C if len(c) == 2}
    order = sorted(k3.X)
    ok = True
    for ctx, target in targets.items():
        keep = tuple(i for i, x in enumerate(order) if x in ctx)
        m = {}
        for s, v in gfull.items():
            t = tuple(s[i] for i in keep)
            m[t] = m.get(t, Fr(0)) + v
        if m != target:
            ok = False
    return (k2_ext is False) and ok

def test_relabel_invariance():
    k1 = suite_k1_bell()
    perm = {"a": "d", "b": "a", "c": "b", "d": "c"}
    k1r = relabel(k1, perm)
    return (down_closure_ok(k1r.C) and
            sorted(sorted(m) for m in maximal_contexts(k1r.C)) ==
            sorted(sorted(perm[x] for x in m) for m in maximal_contexts(k1.C)) and
            _gamma_ok(k1r) and _compat_ok(k1r))

def test_outcome_relabel_invariance():
    """R4 repair: explicit test for the outcome-label permutation move (§7 move 2).
    Previously only the intervention permutation was exercised."""
    k1 = suite_k1_bell()
    outperm = {x: {0: 1, 1: 0} for x in k1.X}  # flip every outcome alphabet
    k1r = relabel(k1, {x: x for x in k1.X}, outperm)
    ok_struct = (sorted(sorted(m) for m in maximal_contexts(k1r.C)) ==
                 sorted(sorted(m) for m in maximal_contexts(k1.C)))
    # Γ must correspond exactly: p'_k1(b,x)(s) == p_k1(x)(outperm^{-1} s)
    ok_gamma = True
    for c in k1.C:
        d1, d2 = k1.gamma[c], k1r.gamma[c]
        for s, v in d1.items():
            s2 = tuple(outperm[x][s[i]] for i, x in enumerate(sorted(c)))
            if d2.get(s2) != v:
                ok_gamma = False
        if sum(d2.values()) != 1:
            ok_gamma = False
    return ok_struct and ok_gamma and _gamma_ok(k1r) and _compat_ok(k1r)

def test_hypergraph_roundtrip():
    for s in (suite_k0_path(), suite_k1_bell(), suite_k2_triangle(), suite_k3_complete()):
        M = maximal_contexts(s.C)                       # family -> antichain
        down = set()
        for m in M:
            for r in range(1, len(m) + 1):
                down |= {frozenset(c) for c in combinations(sorted(m), r)}
        if down != set(s.C):                            # ↓M == C  (§4.5)
            return False
        if set(maximal_contexts(frozenset(down))) != set(M):  # Max(↓M) = M (antichain)
            return False
    return True

def test_gluing():
    """§8 (R2 repair): the three-level distinction.
    (1) TWO compatible marginals on overlapping contexts ALWAYS admit a joint
        extension — verified exactly here via the standard construction
        p(a,b,c) = p_AB(a,b) p_BC(b,c) / p_B(b) (positive overlap mass;
        zero-mass handled the standard zero way).
    (2) An ENTIRE family may fail simultaneous extension on cyclic scenarios —
        verified exactly by test_global_extension on K2.
    (3) Physical accessibility of the union NEVER follows from either mathematical
        fact: the union is in C only if declared (here it is not)."""
    k2 = suite_k2_triangle()
    c1, c2 = frozenset("ab"), frozenset("bc")
    overlap = c1 & c2  # {b}
    agree = k2.marginal(c1, overlap) == k2.marginal(c2, overlap)
    glued = c1 | c2
    not_accessible = glued not in k2.C
    has_extension_declared = glued in k2.gamma  # K2: deliberately not declared
    # (1) explicit two-context extension construction, exact rational arithmetic:
    pB = k2.marginal(c1, overlap)  # == marginal of c2 on overlap
    ext = {}
    order1, order2 = sorted(c1), sorted(c2)  # ('a','b'), ('b','c')
    for (b_key, p_b) in pB.items():
        b_val = b_key[0]  # keys are 1-tuples over the single overlap variable
        if p_b == 0:
            continue  # zero-overlap mass contributes zero
        cond1 = {(s[order1.index('a')], v / p_b) for s, v in k2.gamma[c1].items() if s[order1.index('b')] == b_val}
        # normalize conditionals exactly
        tot = sum(v for _, v in cond1)
        cond1 = {(s, v / tot) for s, v in cond1}
        cond2 = {(s[order2.index('c')], v / p_b) for s, v in k2.gamma[c2].items() if s[order2.index('b')] == b_val}
        tot2 = sum(v for _, v in cond2)
        cond2 = {(s, v / tot2) for s, v in cond2}
        for s1, v1 in cond1:
            for s2, v2 in cond2:
                a_val, c_val = s1, s2
                ext[(a_val, b_val, c_val)] = ext.get((a_val, b_val, c_val), Fr(0)) + p_b * (v1 * v2)
    ext_exists = (sum(ext.values()) == 1 and all(v >= 0 for v in ext.values()))
    # verify the constructed extension reproduces both pair marginals exactly
    ext_ok = ext_exists
    if ext_ok:
        for ctx in (c1, c2):
            order_full = sorted(glued)
            keep = tuple(i for i, x in enumerate(order_full) if x in ctx)
            m = {}
            for s, v in ext.items():
                m[tuple(s[i] for i in keep)] = m.get(tuple(s[i] for i in keep), Fr(0)) + v
            if m != k2.gamma[ctx]:
                ext_ok = False
    # K3: declared triple context, extension declared and compatible
    k3 = suite_k3_complete()
    k3_ext_ok = frozenset(k3.X) in k3.C and _compat_ok(k3)
    return agree and not_accessible and (not has_extension_declared) and ext_ok and k3_ext_ok

def test_suites_k0_k3():
    """K0 path, K1 Bell four-cycle, K2 triangle, K3 complete: all four instantiate and
    pass structural checks (the per-check work is done by the tests above)."""
    suites = [suite_k0_path(), suite_k1_bell(), suite_k2_triangle(), suite_k3_complete()]
    for s in suites:
        if not (down_closure_ok(s.C) and _gamma_ok(s)):
            return False
    # K1 covers exactly the four-cycle maximal structure; K2 has no triple context.
    k1, k2 = suite_k1_bell(), suite_k2_triangle()
    return (sorted(sorted(m) for m in maximal_contexts(k1.C)) ==
            [["a", "b"], ["a", "d"], ["b", "c"], ["c", "d"]] and
            frozenset(["a", "b", "c"]) not in k2.C)

# ------------------------------------------------------------ negative controls (R4)

def test_negative_malformed_downward_closure():
    """Hostile: a family MISSING a required subcontext must FAIL the check."""
    bad = frozenset({frozenset("ab"), frozenset("b")})  # 'a' missing
    return not down_closure_ok(bad)

def test_negative_nonnormalized_gamma():
    k1 = suite_k1_bell()
    bad = KinematicObject(k1.X, k1.O, k1.C, k1.gamma)
    c = next(iter(bad.C))
    bad.gamma = dict(bad.gamma)
    bad.gamma[c] = dict(bad.gamma[c])
    bad.gamma[c][next(iter(bad.gamma[c]))] = Fr(3, 4)  # sums to 1.25
    return not _gamma_ok(bad)

def test_negative_probability():
    k1 = suite_k1_bell()
    bad = KinematicObject(k1.X, k1.O, k1.C, k1.gamma)
    c = next(iter(bad.C))
    bad.gamma = dict(bad.gamma)
    bad.gamma[c] = dict(bad.gamma[c])
    bad.gamma[c][next(iter(bad.gamma[c]))] = Fr(-1, 4)
    return not _gamma_ok(bad)

def test_negative_overlap_incompatible():
    """Hostile: singleton marginals that contradict the pair data must FAIL."""
    k1 = suite_k1_bell()
    bad = KinematicObject(k1.X, k1.O, k1.C, k1.gamma)
    bad.gamma = dict(bad.gamma)
    bad.gamma[frozenset("a")] = {(1,): Fr(1)}  # pair data says uniform
    return not _compat_ok(bad)

def test_negative_k2_global():
    """Hostile/calibration: repaired contextual K2 must FAIL global extendability
    while PASSING local (overlap) compatibility."""
    k2 = suite_k2_triangle()
    return _compat_ok(k2) and not k2_global_extends(k2)

if __name__ == "__main__":
    print("== POSITIVE CONTROLS (well-formed objects must pass) ==")
    test("test_downward_closure        (§4.1–4.2)", test_downward_closure)
    test("test_maximal_contexts        (§4.6)", test_maximal_contexts)
    test("test_overlaps                (§4.3, §4.6)", test_overlaps)
    test("test_presheaf_functoriality  (§5.1)", test_presheaf_functoriality)
    test("test_gamma_wellformed        (§6.1 conds 1–2)", test_gamma_wellformed)
    test("test_overlap_compatibility   (§6.1 cond 3)", test_overlap_compatibility)
    test("test_relabel_invariance      (§7 move 1)", test_relabel_invariance)
    test("test_outcome_relabel        (§7 move 2, R4)", test_outcome_relabel_invariance)
    test("test_hypergraph_roundtrip    (§4.4–4.5)", test_hypergraph_roundtrip)
    test("test_gluing                  (§8, R2: pair extension exists; family may fail)", test_gluing)
    test("test_global_extension        (R1: K2 no global dist; K3 has one)", test_global_extension)
    test("test_suites_k0_k3            (K0/K1/K2/K3)", test_suites_k0_k3)
    pos = list(RESULTS)
    RESULTS.clear()
    print("\n== NEGATIVE CONTROLS (malformed objects must be REJECTED) ==")
    test("neg: malformed downward closure FAILS", test_negative_malformed_downward_closure)
    test("neg: non-normalized Gamma FAILS", test_negative_nonnormalized_gamma)
    test("neg: negative probability FAILS", test_negative_probability)
    test("neg: overlap-incompatible Gamma FAILS", test_negative_overlap_incompatible)
    test("neg/cal: contextual K2 passes local, FAILS global", test_negative_k2_global)
    neg = list(RESULTS)
    np_pos = sum(1 for _, r in pos if r == "PASS")
    np_neg = sum(1 for _, r in neg if r == "PASS")
    print(f"\nVALIDATOR (positive): {np_pos}/{len(pos)} PASS")
    for name, r in pos:
        print(f"  [{r:6s}] {name}")
    print(f"\nVALIDATOR (negative controls): {np_neg}/{len(neg)} PASS (all must reject)")
    for name, r in neg:
        print(f"  [{r:6s}] {name}")
    print("\nNOTE (R1/R2 repairs, kinematic data, no law): K2 (uniform anti-correlated "
          "triangle) is overlap-compatible while NO global distribution reproduces "
          "its pair marginals — verified exactly, not inferred from absence of the "
          "triple context. Two-context gluing ALWAYS admits an extension; the "
          "obstruction belongs to whole-family (cyclic) extension. Physical access "
          "of the union follows from neither fact.")
