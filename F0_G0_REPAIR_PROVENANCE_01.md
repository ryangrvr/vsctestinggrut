# F0 G0 — REPAIR PROVENANCE 01
**Date:** 2026-10-06 · **Branch:** `ggc0-f0-g0-repair-0`, from the banked campaign tip
`c5bfcb911ee1761442c15a6d548af336759ad5ab` (`ggc0-f0-g0-possibility-statistics-identifiability-0`,
untouched). **Status:** numbered repair only, per `F0_G0_OWNER_RULING_01.md`.
**Terminal unchanged: `F0-G0-SUPPORT-COUPLING` (strictly the preregistered C1 class).
No new science beyond the repaired witness; no F0-B; frozen charters untouched.**

## Numbered repairs

| # | What changed | Where |
|---|---|---|
| R1 | K4 witness repaired: primary pair is now Γ_U (uniform pairs, p=1/4) vs Γ_T (tilted, 3/8·1/8·1/8·3/8), strictly positive, identical full support under **both** the declared and the derived (p>0) reading, machine-checked — the solver now verifies every witness against the constraint rows (0/24 violations each) instead of printing assertions. The pre-repair correlated/anti-correlated pair is retained, **relabeled**: its derived supports are disjoint on every pair context (16/24 sections each, machine-checked), so it witnesses that declared support does not pin derived support — not same-support/different-weights. Semantics declared at the K4 site; owner's single-context remark recorded (the basic statement needs no cycle). | `f0_g0_solver.py` (K4 block), `F0_G0_IDENTIFIABILITY_01.md` §3, `F0_G0_RESULT.md` §3, `F0_G0_LEDGER.md` row G9 |
| R2 | Terminal definition reworded to the narrower earned statement — "Given supplied support information, support zeros constrain Γ; bare compatibility does not identify Γ" (RESULT adds the uniqueness parenthetical between the clauses) — with the explicit qualification **NO POSSIBILITY→SUPPORT LAW WAS DERIVED** and the standing prose descriptor **C1 supplied-support constraint**. | `F0_G0_RESULT.md` §1, `F0_G0_STATUS.json` |
| R3 | Abramsky–Brandenburger arXiv ID corrected **1006.0484 → 1102.0264** (1006.0484 is an unrelated galactic-dynamics paper; verified externally during the audit). | `F0_G0_BASELINE_AUDIT_01.md` §1 |
| R4 | Five stale charter section references corrected: `F0_G0_IDENTIFIABILITY_01.md` §4 header §11→§7 and §7 header §12→§8; `F0_G0_RESULT.md` §8 header §12→§8; `F0_G0_LEDGER.md` G10 §9→§6; `F0_G0_BASELINE_AUDIT_01.md` §7 header §9→§6. | those files |
| R5 | "physical possibility"/"physically possible" replaced by declared-possibility wording per Future-Law Requirement 11 (the F0-PHYS gate is OPEN; no physicality assumption is priced in G0). | `F0_G0_RESULT.md` §5/§8, `F0_G0_IDENTIFIABILITY_01.md` §5/§7, `F0_G0_STATUS.json` (central_question, grut_room, possibility_vs_zero_probability) |
| R6 | `F0_G0_STATUS.json` synchronized: repair records, qualification, prose descriptor, repaired no-go-control block (machine_checked: true), branch provenance. | `F0_G0_STATUS.json` |

## Reported, NOT edited here (outside this repair's authority)

- **Sealed exec01 artifact carries the same wrong arXiv ID:** `F0_PHYS_BASELINE_AUDIT_01.md:19,59`
  cite Abramsky–Brandenburger as arXiv:1006.0484. That record is banked under the
  exec01/PHYS-02 seals; fixing it requires its own numbered repair.
- **Frozen G0 charter wording:** `F0_G0_CHARTER.md` §§1–2 themselves say "physical possibility";
  the charter is frozen and is not edited. Its lineage header (lines 3–5) also omits the
  I0 repair/seal commits (`b80c9be`, `2573fa1`) that `F0_G0_STATUS.json` records correctly.
- **Additive-repair governance hazard (program-wide):** withdrawn I0 claims remain in
  live-looking files without in-file supersession banners; two divergent "final" PHYS-02
  status JSONs exist across branches (`1a1edd5` vs `f7ee861`). Owner ruling: architectural
  fix required before publication; listed in the consolidation artifact.

## Verification

`python3 f0_g0_solver.py` re-runs the full ladder unchanged (dims 3/5/6/8; correlated
support dim 1; anti-correlated UNIQUE) and now machine-verifies all four K4 models
(0/24 constraint violations each; derived supports 24/24, 24/24, 16/24, 16/24).
