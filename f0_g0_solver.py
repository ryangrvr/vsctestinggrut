#!/usr/bin/env python3
"""F0-G0 exact finite solver — identifiability of Gamma from static possibility structure.

EXACT rational arithmetic (Fraction), exact linear algebra. No Monte Carlo, no floats.

Computes, for each static input level and each finite scenario:
  Adm_Gamma(input) = { probability-valued empirical models compatible with the structure }
via exact Gaussian elimination on normalization + no-disturbance (overlap compatibility)
constraints, with support zeros imposed as equalities. Reports: dimension of the solution
affine space (rank deficiency), number of free parameters, and explicit distinct models
when non-unique.

Scenarios: G0-K0 complete classical, G0-K1 path/acyclic, G0-K2 Specker triangle,
G0-K3 Bell four-cycle (binary). Input levels: G0-A (C only -> no event data: trivially
unidentifiable, argued not computed), G0-B (C+E), G0-C (C+E+full support), G0-D (adds
declared event relations where justified).
"""
from itertools import combinations, product
from fractions import Fraction as Fr

def solve_rank(A, b, n):
    """Exact RREF of augmented [A|b]. Returns (rank, solution_description).
    Columns: n variables. Consistency + free-variable count = n - rank."""
    M = [row[:] + [bb] for row, bb in zip(A, b)]
    pivots = []
    r = 0
    for c in range(n):
        pr = next((rr for rr in range(r, len(M)) if M[rr][c] != 0), None)
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for rr in range(len(M)):
            if rr != r and M[rr][c] != 0:
                f = M[rr][c]
                M[rr] = [a - f * x for a, x in zip(M[rr], M[r])]
        pivots.append(c)
        r += 1
    # consistency
    for row in M[r:]:
        if all(x == 0 for x in row[:n]) and row[n] != 0:
            return None  # inconsistent: empty admissible set
    return (r, n - r, M, pivots)  # rank, free dims

def build_constraints(scenario, support=None, extra=None):
    """Build normalization + no-disturbance (+ support zeros) constraints.
    Variables: one probability p_C(s) per context C and section s in E(C).
    Returns (A, b, var_list)."""
    contexts = scenario["contexts"]
    sections = {c: scenario["sections"](c) for c in contexts}
    var_list = []
    idx = {}
    for c in contexts:
        for s in sections[c]:
            idx[(c, s)] = len(var_list)
            var_list.append((c, s))
    n = len(var_list)
    A, b = [], []
    # normalization per context
    for c in contexts:
        row = [Fr(0)] * n
        for s in sections[c]:
            row[idx[(c, s)]] = Fr(1)
        A.append(row); b.append(Fr(1))
    # no-disturbance: for C' proper subset of C (overlap), marginal of p_C on C' == p_C'
    for c in contexts:
        order_c = sorted(c)
        for c2 in contexts:
            if c2 >= c or not (c2 < c):
                continue
            if not c2:
                continue
            # marginal of p_C onto c2 must equal p_c2 sectionwise
            keep = tuple(i for i, x in enumerate(order_c) if x in c2)
            order_c2 = sorted(c2)
            for t in product(*[scenario["alph"][x] for x in order_c2]):
                row = [Fr(0)] * n
                # LHS: sum of p_C sections restricting to t
                for s in sections[c]:
                    if tuple(s[i] for i in keep) == t:
                        row[idx[(c, s)]] += Fr(1)
                # RHS: -p_c2(t)
                if (c2, t) in idx:
                    row[idx[(c2, t)]] -= Fr(1)
                A.append(row); b.append(Fr(0))
    # support zeros: p_C(s) = 0 for s not in support
    if support is not None:
        for c in contexts:
            for s in sections[c]:
                if s not in support.get(c, set()):
                    row = [Fr(0)] * n
                    row[idx[(c, s)]] = Fr(1)
                    A.append(row); b.append(Fr(0))
    if extra:
        for row, val in extra:
            r2 = [Fr(0)] * n
            for (c, s), co in row.items():
                r2[idx[(c, s)]] = co
            A.append(r2); b.append(Fr(val))
    return A, b, var_list, n

def analyze(name, scenario, support=None, extra=None):
    A, b, var_list, n = build_constraints(scenario, support, extra)
    res = solve_rank(A, b, n)
    if res is None:
        return {"name": name, "status": "EMPTY admissible set (inconsistent constraints)", "n_vars": n}
    rank, free, M, pivots = res
    return {"name": name, "n_vars": n, "rank": rank, "free_dims": free,
            "classification": ("UNIQUE (singleton)" if free == 0 else
                               f"POLYTOPE with {free} free parameters (affine dim {free})")}

def sections_binary(alph, ctx):
    return sorted(product(*[alph[x] for x in sorted(ctx)]))

def make_scenario(name, X, ctx_list, alph=None):
    alph = alph or {x: [0, 1] for x in X}
    contexts = [frozenset(c) for c in ctx_list]
    return {"name": name, "X": X, "alph": alph, "contexts": contexts,
            "sections": lambda c: sections_binary(alph, c)}

# ---------------- scenarios ----------------
def sc_K0_complete():
    return make_scenario("G0-K0 complete classical", ["a", "b"], [["a"], ["b"], ["a", "b"]])

def sc_K1_path():
    return make_scenario("G0-K1 path/acyclic", ["a", "b", "c"], [["a"], ["b"], ["c"], ["a", "b"], ["b", "c"]])

def sc_K2_triangle():
    return make_scenario("G0-K2 Specker triangle", ["a", "b", "c"],
                         [["a"], ["b"], ["c"], ["a", "b"], ["b", "c"], ["a", "c"]])

def sc_K3_bell():
    return make_scenario("G0-K3 Bell four-cycle", ["a", "b", "c", "d"],
                         [["a"], ["b"], ["c"], ["d"], ["a", "b"], ["b", "c"], ["c", "d"], ["a", "d"]])

# ---------------- support generators ----------------
def full_support(scenario):
    return {c: set(scenario["sections"](c)) for c in scenario["contexts"]}

def k2_deterministic_style_support(scenario):
    """Restricted support example: each pair context only allows correlated sections,
    singletons allow both. (Possibilistic support only, no weights.)"""
    supp = {}
    for c in scenario["contexts"]:
        if len(c) == 2:
            supp[c] = {s for s in scenario["sections"](c) if s[0] == s[1]}
        else:
            supp[c] = set(scenario["sections"](c))
    return supp

def k2_anti_support(scenario):
    """Restricted support: pair contexts allow only anti-correlated sections."""
    supp = {}
    for c in scenario["contexts"]:
        if len(c) == 2:
            supp[c] = {s for s in scenario["sections"](c) if s[0] != s[1]}
        else:
            supp[c] = set(scenario["sections"](c))
    return supp

# ---------------- run ----------------
if __name__ == "__main__":
    print("== F0-G0 exact identifiability analysis (rational, no floats) ==")
    print("\n-- G0-B level: C + E (normalization + no-disturbance only) --")
    for sc in (sc_K0_complete(), sc_K1_path(), sc_K2_triangle(), sc_K3_bell()):
        r = analyze(sc["name"], sc)
        print(f"  {r['name']}: vars={r['n_vars']} rank={r['rank']} -> {r['classification']}")
    print("\n-- G0-C level: C + E + FULL support (support adds nothing beyond E) --")
    for sc in (sc_K0_complete(), sc_K2_triangle()):
        r = analyze(sc["name"], sc, support=full_support(sc))
        print(f"  {r['name']}: vars={r['n_vars']} rank={r['rank']} -> {r['classification']}")
    print("\n-- G0-C/D level: C + E + RESTRICTED support --")
    r = analyze("G0-K2 triangle, correlated-pair support", sc_K2_triangle(), support=k2_deterministic_style_support(sc_K2_triangle()))
    if 'status' in r:
        print(f"  {r['name']}: {r['status']}")
    else:
        print(f"  {r['name']}: rank={r['rank']} free={r['free_dims']} {r['classification']}")
    r = analyze("G0-K2 triangle, anti-correlated support", sc_K2_triangle(), support=k2_anti_support(sc_K2_triangle()))
    if 'status' in r:
        print(f"  {r['name']}: {r['status']}")
    else:
        print(f"  {r['name']}: rank={r['rank']} free={r['free_dims']} {r['classification']}")
    print("\n-- G0-K4 hostile identifiability control (REPAIRED, R1): machine-checked witnesses --")
    # Semantics declaration (owner ruling 2026-10-06): G0's "support" is a DECLARED
    # possibility input (zeros imposed off the set; p>0 on the set permitted, not
    # enforced). The DERIVED support of a model is its p>0 sections (the standard
    # empirical-model meaning). The primary K4 witness pair below is strictly positive,
    # so its declared and derived supports coincide (full) under BOTH readings.
    sc = sc_K3_bell()

    def full_bell_model(pair_probs):
        """A complete model over ALL contexts of the Bell four-cycle: singletons
        uniform (1/2, 1/2); every pair context carries pair_probs (a dict over
        the four sections in sorted-variable order)."""
        m = {}
        for c in sc["contexts"]:
            if len(c) == 1:
                m[c] = {(0,): Fr(1, 2), (1,): Fr(1, 2)}
            else:
                m[c] = dict(pair_probs)
        return m

    def check_model(scenario, model, label):
        """Exact verification: normalization + no-disturbance residuals, negativity
        count, and the DERIVED (p>0) support. Returns (admissible, full_derived)."""
        A, b, var_list, n = build_constraints(scenario)
        p = [model[c][s] for (c, s) in var_list]
        viol = sum(1 for row, bb in zip(A, b)
                   if sum(r * x for r, x in zip(row, p)) != bb)
        neg = sum(1 for x in p if x < 0)
        total = len(var_list)
        pos = sum(1 for x in p if x > 0)
        full_derived = (pos == total)
        print(f"  {label}: constraint violations={viol}/{len(A)}, negative entries={neg}, "
              f"derived (p>0) support = {pos}/{total} sections"
              f" ({'FULL' if full_derived else 'NOT full'})")
        return (viol == 0 and neg == 0), full_derived

    # PRIMARY witness pair (interior): strictly positive everywhere, so declared-full
    # and derived-full support agree; both no-disturbing; m_u != m_t.
    m_u = full_bell_model({(0,0): Fr(1,4), (0,1): Fr(1,4), (1,0): Fr(1,4), (1,1): Fr(1,4)})
    m_t = full_bell_model({(0,0): Fr(3,8), (0,1): Fr(1,8), (1,0): Fr(1,8), (1,1): Fr(3,8)})
    ok_u, full_u = check_model(sc, m_u, "witness U (uniform pairs)")
    ok_t, full_t = check_model(sc, m_t, "witness T (tilted pairs 3/8,1/8,1/8,3/8)")
    assert ok_u and ok_t and full_u and full_t and m_u != m_t
    print("  => identical X, alphabets, C; identical FULL support under BOTH the declared")
    print("     and the derived (p>0) reading; both admissible; U != T.")
    print("  => C + E + full support does NOT identify Gamma.")
    print("  Remark (owner ruling): the basic statement needs no cycle — a single context")
    print("  with >=2 outcomes already admits many full-support distributions;")
    print("  the cyclic exhibit shows the freedom persists under the full no-disturbance")
    print("  coupling of a contextual cover.")

    # SECONDARY exhibit (relabeled, R1): the original correlated/anti-correlated pair.
    # Both admissible under DECLARED-full support, but their DERIVED supports are
    # disjoint on every pair context — so this pair shows something different: the
    # declared possibility set does not even pin the derived support.
    m_corr = full_bell_model({(0,0): Fr(1,2), (0,1): Fr(0), (1,0): Fr(0), (1,1): Fr(1,2)})
    m_anti = full_bell_model({(0,0): Fr(0), (0,1): Fr(1,2), (1,0): Fr(1,2), (1,1): Fr(0)})
    ok_c, full_c = check_model(sc, m_corr, "exhibit C (correlated pairs)")
    ok_a, full_a = check_model(sc, m_anti, "exhibit A (anti-correlated pairs)")
    assert ok_c and ok_a and not full_c and not full_a
    print("  => exhibits C and A: admissible under declared-full support, DERIVED supports")
    print("     disjoint on every pair context — declared support does not pin derived support.")

    print("\nNote: 'no local/noncontextual subset' analysis: local polytope is a strict subset")
    print("of the no-disturbance set; its separate computation is standard (CHSH facet) and")
    print("not needed for the identifiability question.")
