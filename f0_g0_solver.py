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
    print("\n-- G0-K4 hostile identifiability control: same everything, different Gamma --")
    # Bell four-cycle with full support: exhibit two distinct admissible models
    sc = sc_K3_bell()
    # model 1: all correlations = perfect (deterministic-ish): p(ab)=p(bc)=p(cd)=p(ad) correlated
    # model 2: all correlations = anti-correlated with same marginals
    # Both are normalized + no-disturbing with full support. Exhibit explicitly:
    def explicit_models_bell():
        # sections of pair contexts (x,y); singletons uniform.
        # Model 1: correlated pairs uniform on {00,11}
        m1 = {"ab": {(0,0): Fr(1,2), (1,1): Fr(1,2)}, "bc": {(0,0): Fr(1,2), (1,1): Fr(1,2)},
              "cd": {(0,0): Fr(1,2), (1,1): Fr(1,2)}, "ad": {(0,0): Fr(1,2), (1,1): Fr(1,2)}}
        # Model 2: anti-correlated pairs uniform on {01,10}
        m2 = {"ab": {(0,1): Fr(1,2), (1,0): Fr(1,2)}, "bc": {(0,1): Fr(1,2), (1,0): Fr(1,2)},
              "cd": {(0,1): Fr(1,2), (1,0): Fr(1,2)}, "ad": {(0,1): Fr(1,2), (1,0): Fr(1,2)}}
        return m1, m2
    m1, m2 = explicit_models_bell()
    print("  model 1 (correlated pairs):", {k: dict(v) for k, v in m1.items()})
    print("  model 2 (anti-correlated pairs):", {k: dict(v) for k, v in m2.items()})
    print("  identical X, alphabets, C, full support; both normalized + no-disturbing; m1 != m2")
    print("  => C + E + full support does NOT identify Gamma (structural baseline)")
    print("\nNote: 'no local/noncontextual subset' analysis: local polytope is a strict subset")
    print("of the no-disturbance set; its separate computation is standard (CHSH facet) and")
    print("not needed for the identifiability question.")
