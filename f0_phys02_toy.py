#!/usr/bin/env python3
"""F0 PHYS-02 interface toy (REPAIRED per owner ruling R2-R5) — EXACT, no law.

Repairs:
  * CT-PARALLEL composition modeled explicitly: task-sets carry SUBSTRATE
    requirements; a parallel composite is DEFINED only where substrate conditions
    hold. Closure enforced ONLY where composition is DEFINED (R4 control 3).
  * FULL general-subset closure: possible A + possible B + DEFINED composite A||B
    => composite possible — over all subsets, not just singleton pairs (R3/R4).
  * CONTEXT-COMPATIBLE (F0 joint realizability) kept SEPARATE from CT-PARALLEL
    (R2); not identified.
  * K2 interface control: under the naive "context = possible parallel task-set"
    mapping with composite substrates defined, K2 (three pairs, no triple)
    CONTRADICTS full CT closure -> the direct embedding FAILS (R3), recorded.
  * Separate information-price accounting for DISTINCT objects (R5).
NOT done: evolving access, transition laws, fixed points, fitting.
"""
from itertools import combinations
from fractions import Fraction as Fr

TASKS = ["T1", "T2", "T3"]
SUBSETS = [frozenset(s) for r in (1, 2, 3) for s in combinations(TASKS, r)]

# ------------------------------------------------------------------ CT model (R2)
# Each task-set S requires a composite substrate for the parallel task "perform all
# tasks in S". CT parallel composition is DEFINED only when the substrate conditions
# are met. SUBSTRATE COMPATIBILITY IS AN EXPLICIT MODEL INPUT (substrate_ok), NOT
# silently set-union — union is one possible substrate model, not an identification.

def ct_parallel_defined(s1, s2, substrate_ok):
    """CT parallel composite of task-sets s1, s2 is DEFINED iff the composite
    substrate conditions are satisfied (explicit substrate model, R4-3)."""
    if not s1 or not s2:
        return False
    return substrate_ok(s1 | s2)

def full_ct_closure(possible, substrate_ok):
    """R3/R4 FULL closure over ALL subsets: possible A + possible B + DEFINED
    composite A||B => composite possible. Returns (ok, violations)."""
    violations = []
    for s1 in SUBSETS:
        if s1 not in possible:
            continue
        for s2 in SUBSETS:
            if s2 not in possible:
                continue
            comp = frozenset(s1 | s2)
            if comp == frozenset(s1) or comp == frozenset(s2):
                continue  # trivial (subset), no new composite task
            if not ct_parallel_defined(s1, s2, substrate_ok):
                continue  # composition undefined here -> NO closure conclusion (R4-3)
            if comp not in possible:
                violations.append((frozenset(s1), frozenset(s2), comp))
    return (not violations), violations

# ------------------------------------------------------------- controls (R4)

def control_positive_pair():
    """R4-1: singleton possible + singleton possible -> DEFINED pair composite possible."""
    possible = {frozenset(["T1"]), frozenset(["T2"]), frozenset(["T1", "T2"])}
    ok, v = full_ct_closure(possible, substrate_ok=lambda s: len(s) <= 2)
    return ok and v == []

def control_positive_triple():
    """R4-2: pair composite possible + compatible singleton -> defined triple possible."""
    possible = {frozenset(s) for s in [("T1",), ("T2",), ("T3",), ("T1", "T2"),
                                        ("T2", "T3"), ("T1", "T3"),
                                        ("T1", "T2", "T3")]}
    ok, v = full_ct_closure(possible, substrate_ok=lambda s: True)
    return ok and v == []

def control_substrate_undefined():
    """R4-3: incompatible substrate: parallel composition NOT DEFINED -> no closure
    conclusion permitted (instance is legal even though naively it 'looks' violating)."""
    possible = set(SUBSETS) - {frozenset(TASKS)}
    ok, v = full_ct_closure(possible, substrate_ok=lambda s: len(s) <= 2)
    return ok and v == []

def control_negative_missing_pair():
    """Negative: T1,T2 possible with a DEFINED pair composite substrate but the pair
    composite task declared impossible -> closure violation MUST be flagged."""
    possible = {frozenset(["T1"]), frozenset(["T2"]), frozenset(["T1", "T3"])}
    # T1,T2 possible, pair substrate {T1,T2} defined (len<=2 ok), but pair composite
    # NOT in possible -> at least one closure violation expected.
    ok, v = full_ct_closure(possible, substrate_ok=lambda s: len(s) <= 2)
    return (not ok) and len(v) >= 1

# --------------------------------------------------- K2 interface control (R3)

def k2_interface_control():
    """R3 DECISIVE CONTROL: K2/Specker triangle — three singleton contexts, three
    pair contexts, NO triple context. Under the naive PHYS-02 mapping 'context =
    possible parallel task-set' with composite substrates defined (as they must be:
    K2's pair contexts presuppose pair composite tasks), full CT closure FORCES the
    triple: {T1,T2} possible + {T3} possible + defined composite => {T1,T2,T3}
    possible. K2 has no triple => CONTRADICTION => direct embedding FAILS.
    Recorded, not weakened (R3)."""
    possible = {frozenset(s) for s in [("T1",), ("T2",), ("T3",),
                                        ("T1", "T2"), ("T2", "T3"), ("T1", "T3")]}
    pairs = {frozenset(["T1", "T2"]), frozenset(["T2", "T3"]), frozenset(["T1", "T3"])}
    triple = frozenset(TASKS)
    shape_ok = pairs <= possible and triple not in possible
    ok, v = full_ct_closure(possible, substrate_ok=lambda s: True)
    triple_forced = any(comp == triple for _, _, comp in v)
    return {
        "k2_shape_ok": shape_ok,
        "full_ct_closure_violated": not ok,
        "triple_forced_by_ct": triple_forced,
        "violations": [(sorted(a), sorted(b), sorted(c)) for a, b, c in v],
        "verdict": ("DIRECT EMBEDDING FAILS: under CT-PARALLEL with defined composite "
                    "substrates, K2's pair contexts force the triple context; K2 has "
                    "none. CONTEXT-COMPATIBLE != CT-PARALLEL possibility."),
        "escape_routes_examined": [
            "declare triple substrate undefined: unavailable — K2's pair substrates are defined and coexist on the same underlying scenario",
            "weaken composition: FORBIDDEN (would modify CT to save the reduction)",
            "restrict to independent substrates: yields at most a restricted one-way implication, not the general reduction (R2 analysis)"
        ],
    }

# --------------------------------------------------------- price accounting (R5)

def prices_n3():
    """R5: SEPARATE accounting for DISTINCT objects; withdrawn claims:
    'arbitrary n=3 context structure = 7 independent bits' (an arbitrary Boolean
    table is NOT the F0-A object) and 'composition reduces the all-possible instance
    to 0 free decisions' (composition constrains COMPOSITES conditionally; it does
    not force singleton tasks to be possible)."""
    # exact enumeration of downward-closed families (simplicial complexes) on 3 labeled vertices
    count = 0
    for mask in range(128):
        fam = {SUBSETS[i] for i in range(7) if mask >> i & 1}
        if all(all(frozenset(s - {x}) in fam for x in s) for s in fam):
            count += 1
    return {
        "arbitrary_boolean_table": "one Boolean per queried subset, no downward-closure assumption: 7 free bits per instance (2^7 = 128 tables); this is NOT the F0-A object",
        "f0a_context_complex": (f"downward-closed families (simplicial complexes) on 3 "
                                 f"labeled vertices: exactly {count} (exact enumeration) "
                                 f"=> log2({count}) bits, NOT 7; subset decisions are "
                                 f"COUPLED by downward closure (a present pair forces its "
                                 f"singleton subcontexts)"),
        "ct_task_possibility": ("possibility values on a declared task algebra with "
                                 "serial/parallel closure; composition constrains "
                                 "COMPOSITE possibility CONDITIONALLY — it does NOT "
                                 "force primitive singleton tasks to be possible "
                                 "(3 singleton decisions remain genuinely free); the "
                                 "previous '0 free decisions' claim is WITHDRAWN"),
        "comparison_note": ("the three objects are DISTINCT; their prices are not "
                            "inter-comparable as previously stated (R5)")
    }

if __name__ == "__main__":
    print("== F0 PHYS-02 interface toy (repaired; exact; semantics only) ==")
    print(f"R4-1 pair-from-singletons control:             {control_positive_pair()}")
    print(f"R4-2 triple-from-pair+singleton control:      {control_positive_triple()}")
    print(f"R4-3 undefined-substrate control (no closure): {control_substrate_undefined()}")
    print(f"R4-neg missing-pair flagged:                   {control_negative_missing_pair()}")
    k2 = k2_interface_control()
    print("\nR3 K2 interface control:")
    for k, val in k2.items():
        print(f"  {k}: {val}")
    print("\nR5 price accounting (separate objects):")
    for k, val in prices_n3().items():
        print(f"  {k}: {val}")
    print("\nNOT done (firewall): no transition law, no fixed points, no fitting.")
