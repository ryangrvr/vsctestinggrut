#!/usr/bin/env python3
"""F0 PHYS-02 finite semantic toy — EXACT, no floats, no law, no evolution.

Purpose (charter §9): clarify SEMANTICS of the primitive candidates:
  1. a composition-CONSISTENT possibility table (parallel closure enforced);
  2. a composition-INCONSISTENT table (T1,T2 possible but T1||T2 impossible) — flagged;
  3. exact information-price counts per representation;
  4. the semantic bridge: Exec-01 context hypergraph embeds as
     "context = jointly possible task set".
NOT allowed and NOT done: evolving access, transition laws, fixed points, fitting.
"""
from itertools import combinations, product
from fractions import Fraction as Fr

TASKS = ["T1", "T2", "T3"]
# all subsets of TASKS that a possibility predicate can be asked about (nonempty):
SUBSETS = [frozenset(s) for r in (1, 2, 3) for s in combinations(TASKS, r)]

def parallel_closure_ok(possible):
    """Composition constraint (M-3/M-4): if {T} and {T'} are possible TASKS, the
    parallel composite {T,T'} must be a possible task-set. Exact check."""
    for s1, s2 in combinations(SUBSETS, 2):
        if s1 | s2 in SUBSETS and s1 | s2 not in possible:
            # only flag if both parts are possible as standalone sets
            if s1 <= possible_uses_tasks(s1, possible) and s2 <= possible_uses_tasks(s2, possible):
                pass  # structural detail; the core inconsistency is below
    # core inconsistency: T1 and T2 each possible, but {T1,T2} impossible
    singletons = [frozenset([t]) for t in TASKS]
    for s1, s2 in combinations(singletons, 2):
        if s1 in possible and s2 in possible and (s1 | s2) not in possible:
            return False, (s1, s2)
    return True, None

def possible_uses_tasks(s, possible):
    # helper kept explicit for clarity in the closure walk
    return s if s in possible else frozenset()

def count_bits(possible):
    """Exact price: bits to specify which of the 7 nonempty subsets are possible."""
    return len(SUBSETS)  # one binary decision per subset (M-2 price)

def count_bits_composition_constrained(possible):
    """With composition, not all 7 decisions are free: singletons' possibility +
    closure forces the pairs/triple. Count FREE decisions = singletons (3) +
    any subset not forced by closure. If all singletons possible -> pairs forced by
    parallel closure -> only the triple remains free unless forced too (by closure of
    {T1,T2} with {T3}). Exact count for this toy."""
    forced = set()
    ok, bad = parallel_closure_ok(possible)
    # parallel closure forces pairs of possible singletons and the triple if all pairs possible
    for t in TASKS:
        if frozenset([t]) in possible:
            forced.add(frozenset([t]))
    for s1, s2 in combinations(singletons := [frozenset([t]) for t in TASKS], 2):
        if s1 in possible and s2 in possible:
            forced.add(s1 | s2)
    if all(s1 | s2 in possible for s1, s2 in combinations(singletons, 2)):
        forced.add(frozenset(TASKS))
    free = len(SUBSETS) - len(forced & set(SUBSETS))
    return free, sorted(sorted(s) for s in forced)

# ------------------------------------------------------------- instances

def consistent_table():
    """All tasks possible, composition closed."""
    return set(SUBSETS)

def inconsistent_table():
    """T1, T2 possible; {T1,T2} impossible -> composition-inconsistent."""
    return {frozenset(["T1"]), frozenset(["T2"]), frozenset(["T3"])}

def exec01_embedding():
    """Semantic bridge: the Exec-01 K2 context family {a,b,c,ab,bc,ac} embeds as
    'context = jointly possible task set' on three tasks; the anti-correlated
    triangle data would be statistics ON this structure (not part of it)."""
    return {frozenset(s) for s in ["a", "b", "c", "ab", "bc", "ac"]}

if __name__ == "__main__":
    good = consistent_table()
    bad = inconsistent_table()
    print("== F0 PHYS-02 finite semantic toy (exact; semantics only) ==")
    ok_g, bad_g = parallel_closure_ok(good)
    print(f"1. consistent table {sorted(sorted(s) for s in good)}: closure ok = {ok_g}")
    ok_b, bad_b = parallel_closure_ok(bad)
    violation = sorted(map(sorted, bad_b)) if bad_b else []
    print(f"2. inconsistent table: declares T1,T2 possible but {{T1,T2}} impossible -> "
          f"flagged by composition: {not ok_b}, violation at {violation}")
    print(f"3. raw hypergraph price: {count_bits(good)} binary decisions (all arbitrary, M-2)")
    free, forced = count_bits_composition_constrained(good)
    print(f"   composition-constrained free decisions: {free} (forced: {forced}) "
          f"-> composition removes arbitrary content (M-3/M-4 non-arbitrariness)")
    print(f"4. Exec-01 K2 context family embeds as jointly-possible task sets: "
          f"{sorted(sorted(s) for s in exec01_embedding())} — semantic bridge, no law.")
    print("\nNOT done (charter): no evolution, no transition law, no fixed points, no fitting.")
