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
    """K2 — Specker triangle: three pairwise contexts, NO triple context."""
    X = ["a", "b", "c"]
    ctx = [frozenset(s) for s in ["a", "b", "c", "ab", "bc", "ac"]]
    alph = {x: [0, 1] for x in X}
    g = {}
    for x in X:
        g[frozenset([x])] = {(0,): Fr(1, 2), (1,): Fr(1, 2)}
    # pairwise-even marginals (each pair agrees on shared labels)
    for pair in ["ab", "bc", "ac"]:
        g[frozenset(pair)] = {(0, 0): Fr(1, 2), (1, 1): Fr(1, 2)}
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
    """Representation equivalence moves 1–2 (§7): relabel interventions/outcomes."""
    X2 = {perm[x] for x in obj.X}
    O2 = {perm[x]: sorted(obj.O[x]) if outperm is None else sorted(outperm[x]) for x in obj.X}
    C2 = [frozenset(perm[x] for x in c) for c in obj.C]
    g2 = {}
    for c, dist in obj.gamma.items():
        c2 = frozenset(perm[x] for x in c)
        d = {}
        order = sorted(c2)
        for s, v in dist.items():
            order_old = sorted(c)
            s2 = tuple((outperm[perm[order_old[i]]][s[i]] if outperm else s[i])
                       for i in range(len(c)))
            d[tuple(s2[order.index(x)] if False else s2[i] for i in range(len(c)))] = v
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
    # K2 (triangle) data IS overlap-compatible while NO global section exists at this C —
    # the validator records this as kinematic data only; no law, no transition verdict.
    return True

def test_relabel_invariance():
    k1 = suite_k1_bell()
    perm = {"a": "d", "b": "a", "c": "b", "d": "c"}
    k1r = relabel(k1, perm)
    return (down_closure_ok(k1r.C) and
            sorted(sorted(m) for m in maximal_contexts(k1r.C)) ==
            sorted(sorted(perm[x] for x in m) for m in maximal_contexts(k1.C)) and
            _gamma_ok(k1r) and _compat_ok(k1r))

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
    """§8.1: gluing is an operation on DESCRIPTIONS. We check agreement-on-overlap
    and REPORT whether an extension over the glued union is declared in the data.
    Adding a context is a declared act, never inferred (§8.2)."""
    k2 = suite_k2_triangle()
    c1, c2 = frozenset("ab"), frozenset("bc")
    overlap = c1 & c2
    agree = k2.marginal(c1, overlap) == k2.marginal(c2, overlap)
    glued = c1 | c2
    # structural verdict: the union is NOT in C unless declared (§8.2); here it is not.
    not_accessible = glued not in k2.C
    # extension data: is a distribution over the union declared? (K2: deliberately not)
    has_extension = glued in k2.gamma
    # For K3 the union IS declared — extension exists and must be compatible.
    k3 = suite_k3_complete()
    full = frozenset(k3.X)
    k3_ext_ok = full in k3.C and _compat_ok(k3)
    return agree and not_accessible and (not has_extension) and k3_ext_ok

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

if __name__ == "__main__":
    test("test_downward_closure        (§4.1–4.2)", test_downward_closure)
    test("test_maximal_contexts        (§4.6)", test_maximal_contexts)
    test("test_overlaps                (§4.3, §4.6)", test_overlaps)
    test("test_presheaf_functoriality  (§5.1)", test_presheaf_functoriality)
    test("test_gamma_wellformed        (§6.1 conds 1–2)", test_gamma_wellformed)
    test("test_overlap_compatibility   (§6.1 cond 3)", test_overlap_compatibility)
    test("test_relabel_invariance      (§7 moves 1–2)", test_relabel_invariance)
    test("test_hypergraph_roundtrip    (§4.4–4.5)", test_hypergraph_roundtrip)
    test("test_gluing                  (§8.1–8.2)", test_gluing)
    test("test_suites_k0_k3            (K0/K1/K2/K3)", test_suites_k0_k3)
    n_pass = sum(1 for _, r in RESULTS if r == "PASS")
    print(f"\nVALIDATOR: {n_pass}/{len(RESULTS)} PASS")
    for name, r in RESULTS:
        print(f"  [{r:6s}] {name}")
    # structural-observation note (kinematic data, no verdict):
    k2 = suite_k2_triangle()
    print("\nNOTE (kinematic observation, NOT a law): K2 triangle data is "
          "overlap-compatible while the glued union {a,b,c} is not a declared context; "
          "extension existence is reported as data (§8.1), never as permission (§8.2).")
