# F0 G0 LEDGER
**Rule (inherited):** one status per load-bearing element; nothing strengthened silently.

| # | element | status | reason / artifact |
|---|---------|--------|-------------------|
| G1 | Scenarios K0/K1/K2/K3 (reused from Exec-01, historical artifacts unmodified) | `CONSTRUCTED` (re-instantiated) | `f0_g0_solver.py` |
| G2 | Constraint builder: normalization + no-disturbance + support zeros | `CONSTRUCTED`, exact rational | solver `build_constraints` |
| G3 | Exact rank/affine-dimension computation | `CONSTRUCTED` + verified | solver `solve_rank` (exact RREF over Fractions) |
| G4 | G0-A level (C only) | `DERIVED` (structural): no event data → no weights definable at all; identifiability question is degenerate | ladder doc |
| G5 | G0-B results: K0 dim 3, K1 dim 5, K2 dim 6, K3 dim 8 (affine dims, exact) | `DERIVED` | solver output; ladder doc §G0-B |
| G6 | G0-C full-support level: identical dims (support ⊇ E(C) adds zero constraints) | `DERIVED` | solver; support ≠ weights confirmed at full support |
| G7 | G0-C restricted-support: correlated-pair support on K2 → affine dim 1 | `DERIVED` | support DOES remove freedom (C1-class behavior at restricted support) |
| G8 | G0-C restricted-support: anti-correlated support on K2 → **UNIQUE** (the K2 empirical model forced) | `DERIVED` | support can even force uniqueness in special cases (C4 locally) |
| G9 | G0-K4 hostile no-go (witness repaired [R1]): Γ_U ≠ Γ_T (uniform vs tilted pairs), strictly positive, identical full support under BOTH the declared and the derived (p>0) reading, both normalized+no-disturbing, machine-checked | `DERIVED` | **C + E + full support does NOT identify Γ**; the pre-repair correlated/anti-correlated pair is relabeled a secondary exhibit — its derived supports are disjoint, so it witnesses only that declared support does not pin derived support |
| G10 | Possibility ⇒ zero probability | `POSTULATED` as a convention at the support level (support zeros imposed as constraints); the converse (p=0 ⇒ impossible) NOT assumed | charter §6 [R4]; result §possibility |
| G11 | Symmetry | `UNRESOLVED` (tested conceptually: uniform Γ follows only after a state-invariance postulate, which is priced, not assumed) | result §symmetry |
| G12 | G0-E comparator analysis (Gleason, GPT, CT-probability) | `REPRESENTATIONAL` baseline | baseline audit |
| G13 | Coupling classification | `DERIVED`: **C1 — SUPPORT ONLY** in general; special supports reach C4 locally | result |
| G14 | Terminal | resolved in `F0_G0_RESULT.md` | |

## Supplied / postulated inputs

- Scenarios and outcome alphabets: declared data (Exec-01 objects re-instantiated).
- Support sets in G0-C/D restricted cases: declared inputs (the possibilistic layer) —
  the campaign *computes their effect* on identifiability rather than deriving them.
- Normalization + no-disturbance constraints: the empirical-model consistency definition
  (Exec-01, standard sheaf machinery — `REPRESENTATIONAL` of known mathematics).
- Nothing hidden; no probabilities imported from quantum theory (quantum appears only as
  G0-E comparator, not as data).
