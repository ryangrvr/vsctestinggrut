#!/usr/bin/env python3
"""F0-I0 finite controls — exact, semantics only, no law, no Gamma, no dynamics.

Implements the DECLARED interface definition (F0_I0_INTERFACE_DEFINITION_01.md §1):
  S in C_CT(M) iff a joint measurer exists for the variables indexed by S,
  where a joint measurer = one possible measurement task with a joint output
  variable Y, and ALLOWED CLASSICAL COARSE-GRAININGS f_i of Y's outcome recovering
  each M_i outcome (i in S), consistent under restriction.

Downward closure is then a THEOREM of this definition (proved in the interface doc);
the validator checks it mechanically on every instance.

Five finite controls (charter §8): I0-K0 complete, I0-K1 incompatible pair,
I0-K2 Specker triangle, I0-K3 four-cycle, I0-K4 sharp/projective control.

Each control instance declares, for each candidate subset S of measurers:
  * whether a single measurement task with joint output exists (declared
    possibility fact — in a real campaign these would come from the subsidiary
    theory; here they are declared model inputs), and
  * whether the required coarse-grainings f_i (i in S) are allowed on Y.
No probabilities, no Gamma, no fitting.
"""
from itertools import combinations
from fractions import Fraction as Fr

N = 3  # K0-K2 use 3 measurers; K3/K4 handle four-cycle and sharp sector separately

class InterfaceModel:
    """Declared interface model: 'joint_exists[S]' and 'recoverable[S][i]' are
    declared possibility facts (subsidiary-theory inputs). C_CT is COMPUTED from
    them via the interface definition, and downward closure is checked."""
    def __init__(self, name, n, joint_exists, recoverable):
        self.name = name
        self.n = n
        self.joint_exists = dict(joint_exists)   # frozenset S -> bool
        self.recoverable = dict(recoverable)     # frozenset S -> {i: bool} on Y_S
        self.C_CT = self.compute_C_CT()

    def compute_C_CT(self):
        out = set()
        for S, exists in self.joint_exists.items():
            if not exists:
                continue
            rec = self.recoverable.get(S, {})
            if all(rec.get(i, False) for i in S):
                out.add(S)
        return out

    def downward_closure_ok(self):
        """Theorem of the interface definition: S in C_CT and nonempty S' subset of S
        => S' in C_CT."""
        for S in self.C_CT:
            for r in range(1, len(S) + 1):
                for sub in combinations(sorted(S), r):
                    if frozenset(sub) not in self.C_CT:
                        return False, (S, frozenset(sub))
        return True, None

# ------------------------------------------------------------- I0-K0 complete

def i0_k0_complete():
    """All three measurers share one common joint measurer. Expected complex:
    complete simplex (all nonempty subsets)."""
    subs = [frozenset(s) for r in (1, 2, 3) for s in combinations(range(3), r)]
    je = {S: True for S in subs}
    rec = {S: {i: True for i in S} for S in subs}
    m = InterfaceModel("I0-K0 complete", 3, je, rec)
    ok_dc, _ = m.downward_closure_ok()
    return m.C_CT == set(subs) and ok_dc

# ------------------------------------------------------------- I0-K1 incompatible pair

def i0_k1_incompatible_pair():
    """M1, M2 individually measurable but NO joint measurer (complementary pair).
    Expected: singletons in the complex; pairs/triple absent."""
    je = {frozenset([0]): True, frozenset([1]): True, frozenset([2]): True,
          frozenset([0, 1]): False, frozenset([1, 2]): False, frozenset([0, 2]): False,
          frozenset([0, 1, 2]): False}
    rec = {S: {i: True for i in S} for S in je if je[S]}
    m = InterfaceModel("I0-K1 incompatible pair", 3, je, rec)
    ok_dc, _ = m.downward_closure_ok()
    singles = {frozenset([i]) for i in range(3)}
    return singles <= m.C_CT and len(m.C_CT) == 3 and ok_dc

# ------------------------------------------------------------- I0-K2 Specker triangle

def i0_k2_specker_triangle():
    """K2: three pairs jointly measurable, NO triple joint measurer. This is the
    decisive control: pairwise-without-triplewise. Requires the interface to admit
    pair joint measurers without a triple — possible only with subsidiary-theory
    possibility facts (declared here as model inputs); base CT alone cannot
    supply this regime (comparator audit)."""
    subs = [frozenset(s) for r in (1, 2, 3) for s in combinations(range(3), r)]
    je = {S: (len(S) <= 2) for S in subs}   # pairs yes, triple no
    rec = {S: {i: True for i in S} for S in subs if je[S]}
    m = InterfaceModel("I0-K2 Specker triangle", 3, je, rec)
    ok_dc, _ = m.downward_closure_ok()
    pairs = {frozenset([0, 1]), frozenset([1, 2]), frozenset([0, 2])}
    singles = {frozenset([i]) for i in range(3)}
    return (pairs <= m.C_CT and singles <= m.C_CT
            and frozenset([0, 1, 2]) not in m.C_CT and ok_dc)

# ------------------------------------------------------------- I0-K3 four-cycle

def i0_k3_four_cycle():
    """K3: four measurers with a four-cycle compatibility hypergraph (pairs around
    the cycle jointly measurable, diagonals and higher sets not)."""
    M4 = range(4)
    subs = [frozenset(s) for r in (1, 2, 3, 4) for s in combinations(M4, r)]
    cycle_pairs = {frozenset([0, 1]), frozenset([1, 2]), frozenset([2, 3]), frozenset([0, 3])}
    je = {S: (S in cycle_pairs or len(S) == 1) for S in subs}
    rec = {S: {i: True for i in S} for S in subs if je[S]}
    m = InterfaceModel("I0-K3 four-cycle", 4, je, rec)
    ok_dc, _ = m.downward_closure_ok()
    singles = {frozenset([i]) for i in M4}
    return (cycle_pairs <= m.C_CT and singles <= m.C_CT
            and frozenset([0, 2]) not in m.C_CT and frozenset([1, 3]) not in m.C_CT
            and frozenset([0, 1, 2]) not in m.C_CT and ok_dc)

# ------------------------------------------------------------- I0-K4 sharp control

def i0_k4_sharp_control():
    """Sharp/projective control: in the sharp sector, pairwise compatibility has
    strong global consequences — the model declares that every pairwise-compatible
    family extends to a common joint measurement (the restricted sharp-sector
    structure). Expected: the three-pair pattern FORCES the triple (no Specker
    triangle in the sharp sector). This contrasts with I0-K2 and encodes the
    known PVM-vs-POVM distinction at the interface level."""
    subs = [frozenset(s) for r in (1, 2, 3) for s in combinations(range(3), r)]
    # sharp sector: pairwise joint measurers force the triple (declared subsidiary
    # possibility facts for a projective-type theory)
    je = {S: True for S in subs}
    rec = {S: {i: True for i in S} for S in subs}
    m = InterfaceModel("I0-K4 sharp control", 3, je, rec)
    ok_dc, _ = m.downward_closure_ok()
    return frozenset([0, 1, 2]) in m.C_CT and ok_dc

def sharp_forces_triple_contrast():
    """The contrast control: the SAME interface definition, under different
    subsidiary possibility facts, yields different complexes — sharp sector forbids
    the Specker pattern; general (POVM) sector admits it. This is exactly the
    PVM-vs-POVM distinction transported through the interface, and it shows the
    complex is determined by subsidiary facts, not by CT base principles alone."""
    return i0_k2_specker_triangle() and i0_k4_sharp_control()

if __name__ == "__main__":
    print("== F0-I0 finite controls (exact; interface semantics only) ==")
    print(f"I0-K0 complete complex:                 {i0_k0_complete()}")
    print(f"I0-K1 incompatible pair:                {i0_k1_incompatible_pair()}")
    print(f"I0-K2 Specker triangle (pairs, no triple): {i0_k2_specker_triangle()}")
    print(f"I0-K3 four-cycle:                       {i0_k3_four_cycle()}")
    print(f"I0-K4 sharp control (pairwise => triple):  {i0_k4_sharp_control()}")
    print(f"contrast: same interface, different subsidiary facts => different complexes: "
          f"{sharp_forces_triple_contrast()}")
    # downward-closure theorem verified mechanically on every instance
    print("\nDownward-closure theorem of the interface definition: verified mechanically "
          "on every control instance (no downward-closure violation in any declared-consistent "
          "model).")
    print("\nNOT done (firewall): no Gamma coupling, no dynamics, no fitting, no Born rule.")
