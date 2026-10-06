# F0 — OWNER RULING 02 (program level)
**Date:** 2026-10-06. **Scope:** acceptance of the consolidation and the G0 repair;
confirmation of the pre-publication governance set; formal selection and refinement of
Frontier A. Issued after the owner independently verified both remote branches and the
consolidation artifact.

## 1. Acceptances

- **F0 REQUIREMENTS CONSOLIDATION 01 — ACCEPTED.**
  `0a9a941c0951ffeb8f1cccafa12892057a62c884` is now the **governing program-level
  requirements map**. R1–R15 are live; **none are discharged** — an important status
  statement in itself.
- **G0 repair — ACCEPTED** at `a959e7d8962b592b1d9cfac0f54feebde1c5443c`. The repaired
  K4 witness establishes the intended no-go cleanly under both declared and ordinary
  p>0 support semantics. The G0 terminal remains **`F0-G0-SUPPORT-COUPLING`**, strictly
  interpreted as the preregistered C1 supplied-support constraint, with **NO
  possibility→support law derived**.

## 2. Governance set — G-1 through G-5 all BINDING

G-2 and G-4 are explicitly confirmed by this ruling; G-3 is ruled binding; G-1 and G-5
were ruling decisions already.

- **G-2 (confirmed, binding).** The canonical PHYS-02 bank boundary is
  **`1a1edd53ec82b1f6c9231edbcb907d020f69172c`** — not `f7ee861`. The commit messages
  settle this: `1a1edd5` declares itself the bank seal ("no further PHYS-02 edits
  without a numbered repair"); `f7ee861d5b5f0187e04178f461b61b505f37c0e3` merely records
  `1a1edd5` as the banked tip. There are not scientifically two PHYS-02 finals:
  `1a1edd5` = canonical scientific bank boundary; `f7ee861` = post-bank bookkeeping
  descendant / audit-only metadata. **Any future manifest must point to `1a1edd5`, with
  `f7ee861` explicitly classified as noncanonical bookkeeping.** Publication/governance
  cleanup, not a scientific repair. **Do not rewrite Git history.**
- **G-4 (confirmed, binding).** At `6e9b5d6` the record stated the F0-A n=3 family
  count was "exactly 20" and "enumerated" when that result was not supported by the
  then-current implementation. FR1 (`986fbfcbd1e2d8f23a3b97686fce5f68e91bee15`)
  correctly established **19** under the frozen convention with the empty family
  allowed, or **18** with an added nonempty-family condition, and explicitly withdrew
  20. Prescribed supersession wording (to appear in the publication-facing supersession
  layer that solves G-1; `6e9b5d6` is **not** rewritten):
  > The historical `6e9b5d6` "exactly 20, enumerated" claim is withdrawn; it resulted
  > from importing the full-Boolean-lattice/Dedekind convention and was not supported
  > by the then-current frozen-convention enumerator. The governing correction is
  > FR1/`986fbfc` and its descendants: 19/18 under the stated convention.
- **G-3 (binding).** The Abramsky–Brandenburger ID error was found independently by the
  owner before the program audit; the G0 repair correctly fixed its local copy. The
  sealed older artifact (`F0_PHYS_BASELINE_AUDIT_01.md:19,59`) is not to be silently
  edited; its incorrect citation and the PRA/PRR attribution need a **numbered
  correction/supersession before publication**.

## 3. Scientific ruling — program phase change

The consolidation's diagnosis is accepted. The record now holds a progressively
narrower chain: (C, Γ) → physicality unresolved → CT/task language useful but
insufficient to fix generalized compatibility → compatibility complex partly
subsidiary-supplied → compatibility/event structure does not determine weights →
supplied support can constrain weights → **the support itself is not generated**.

- **FRONTIER A — SUPPORT DETERMINATION** is formally selected: *what determines which
  local events are possible/impossible?* — before *what determines the positive weights
  of the possible events?* The future campaign must decide which of G0's three objects
  (declared possibility set; derived p>0 support; zero-probability-but-not-forbidden
  events) is the target physical object.
- **Phase change.** Up through G0, most useful work was decomposition and no-go
  mapping. Frontier A is to be judged much more harshly: it must **attempt an actual
  generative principle or prove that such a principle cannot be obtained from the
  surviving primitives**. Another long chain whose only result is "known framework X
  needs input Y" is not permitted — the consolidation has already done that job.
- Program status: **F0 PROBLEM MAP — MATURE ENOUGH TO ATTACK A LAW**, but **GENERATIVE
  LAW — STILL NOT FOUND**. The first place a genuinely inventive GRUT construction is
  permitted is support determination.

## 4. Frontier A refinement — PASS WITH THREE CORRECTIONS (charter input, not charter)

The support-spectrum idea is **ACCEPTED IN REFINED FORM**; the primary object is the
**admissible support family** ("support spectrum" is CONSTRUCTED program terminology,
not standard, and is so labeled). The three corrections, binding on the charter input:

1. **Target object indexed by a physical realization, not a bare scenario.**
   𝔖_T(R) = { Supp(p_s) : s ∈ States_T(R) } for a declared physical/task/measurement
   realization R of the scenario in theory T; envelope P_T(R) = ⋃_{S∈𝔖_T(R)} S =
   events possible in at least one admissible state; S_s = the actual state's p>0
   support; P_T(R) \ S_s = events structurally possible in the realization but
   zero-weight in that state. The individual support is state-level; the family and
   envelope are law/subsidiary-theory level. A scenario-level spectrum
   𝔖_T(Σ) = ⋃_{R∈Real_T(Σ)} 𝔖_T(R) exists only secondarily, as a comparator object.
2. **The "bipartite ≥3-setting quantum strong contextuality" positive control is
   REMOVED.** Per the owner's literature check, the cleaner (and harder-to-fake)
   dividing line is: Hardy_(2,2,2) ALLOW · PR_(2,2,2) FORBID · GHZ_(n≥3) ALLOW, with a
   KS/Peres–Mermin strong-contextuality example as an additional positive control. The
   excluding rule cannot be "forbid strong contextuality" (GHZ/KS must survive).
   Exact source scopes are graded in `F0_FRONTIER_A_CHARTER_INPUT_01.md`.
   *Post-ruling verification note:* the independent primary-text verification run
   (same date) **upheld the removal** of the ≥3-settings control (settings are not the
   resource) but **contradicted the blanket premise** "no bipartite quantum-realizable
   behaviour is strongly contextual": the proven absences are (2,2,2) and
   qubit-on-one-side bipartite (Brassard–Méthot–Tapp 2005), while bipartite quantum
   strong contextuality exists at local dimension ≥ 3 (Heywood–Redhead 1983; BMT 2005
   optimality 3×3; Cabello 2023). The charter input records the verified boundary, a
   correspondingly restated stretch gate, and an optional bipartite dimension-≥3
   positive control (A-BQ) — **flagged for owner decision, not adopted unilaterally**
   (`F0_FRONTIER_A_CHARTER_INPUT_01.md` §4, §7 row 1b).
3. **Local Orthogonality reclassified**: an event-orthogonality/composition comparator
   *adjacent to* Frontier A — fundamentally a probability inequality, not a pure
   support law — so it belongs in the comparator audit, not as a support-only null
   theory. (Single-copy PR passes LO; two copies violate it.)

Additional binding structure: the admissible-support family's closure properties under
state mixing (support of a proper mixture = union of supports) and under product
realizations are recorded as exact hostile controls before any amplitude talk. The
reconnaissance computation is staged (enumerate and classify possibilistic
no-signalling supports first; quantum-realizability of residual patterns is a separate,
later question).

## 5. What this ruling does NOT do

The Frontier A **charter is not written** and the campaign is **not opened** by this
ruling. F0-B remains prohibited. The charter, when written, builds on
`F0_FRONTIER_A_CHARTER_INPUT_01.md` and is subject to R1–R15 and the kill conditions
recorded there.
