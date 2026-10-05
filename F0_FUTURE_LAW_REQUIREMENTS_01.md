# F0 — FUTURE LAW REQUIREMENTS 01 (requirements only; NO LAW)
**Status:** campaign artifact. Records what any future F0-B candidate
(`R_Gamma` / `A_Gamma` / `Cl_Gamma` / `S` / `U`) would have to satisfy, **as requirements
only**. Per the hard firewall: **no formula is proposed, no thresholds chosen, no searches
run, nothing optimized.** If a formula were proposed here it would be a campaign violation.

## Hard requirements (each traceable to a campaign artifact)

1. **Representation invariance.** Any law must be invariant under the declared
   representation-equivalence moves (Formulation §7) and only those. *Trace:*
   `test_relabel_invariance`; P2.
2. **Gluing compatibility without automatic access.** Agreements over overlaps must be
   usable as *data*; adding a glued context must be an explicit act of the law, never an
   automatic consequence of agreement. *Trace:* Formulation §8.2; `test_gluing`.
3. **No inaccessible-context data.** The law may not assume a probability law, response
   data, or hidden outcomes for a jointly inaccessible context (the EA-0 / charter
   kill-condition (a)). *Trace:* charter §8(a); `F0_CHARTER_02_REPAIRED.md`.
4. **Observer independence.** The law's output must not depend on which observer (or which
   equipment class) evaluates it — modal/counterfactual framing does not count (P4 shows
   the relocation pattern). *Trace:* physicality doc P4.
5. **No supplied subsystem split.** The law may not presuppose a tensor-factor or
   subsystem decomposition without declaring it as a supplied input and paying its price
   (charter §8(b); P5). *Trace:* physicality doc §8 table.
6. **Scope declaration for compatibility.** The law must state which compatibility notion
   it uses (menu / operational / co-instantiability / structural) and, for measurement
   scopes, sharp vs. unsharp explicitly (charter §3.1; P7). Sharpness must be loaded into
   the intervention definitions, not left to presentation (P7 consequence).
7. **Temporality must be earned.** Distinguishing simultaneous/sequential/commuting/
   jointly-measurable/jointly-realizable requires structure the program has not earned;
   any law must either declare the required structure as supplied or remain silent about
   temporal distinctions (P6). *Trace:* physicality doc §7.6.
8. **Constraint ≠ selection.** `R_Gamma`-type relations may veto; they may not be silently
   read as positive selection (charter §2 F0-C; kill-condition (d)).
9. **No outer→exact upgrade.** Quantum-status labels follow the charter §6 firewall.
10. **Information price accounting.** Every input the law consumes beyond `(C, Γ)` must be
    declared and priced (charter §2 F0-A information-price clause; Formulation §2 note).
11. **F0-PHYS precondition.** The law may not be constructed on a meaning of `C` that has
    not passed (or been ruled out by) the physicality gate; given this campaign's terminal
    (`F0-PHYS-OPEN`), any future law must declare which of the four meanings it builds on
    and pay the corresponding §8 price. *Trace:* physicality doc §10.
12. **Convention fixes.** The law must fix: empty-context convention (here: excluded,
    Formulation §4.2); canonical presentation (family-of-subsets, Formulation §4.1);
    non-distributional event scopes if used (Formulation §5.2).

## Deliberately NOT done

- No `R_Gamma(C,C') = …` — not proposed.
- No thresholds, cutoffs, tolerance constants.
- No search over access laws; no optimization against Bell/Specker/quantum/
  almost-quantum/PR data; no fixed-point iteration.
- No proposal of `Cl_Gamma` as a default (monotone growth + idempotence remain unearned,
  charter §2 F0-B).
- No claim about *how* access changes at all — out of campaign scope by authorization.

## Observation recorded for future use (kinematic, no verdict)

The K2 (triangle) validator instance demonstrates **kinematically** that a family can be
overlap-compatible with every declared context while no distribution over the glued union
is declared, and the union is not a context. What a future law does with that observation
is exactly what F0-B would have to decide — and is not decided here.
