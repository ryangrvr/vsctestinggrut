# Stage-3 charter — working record (NON-NORMATIVE)

**Governing text:** `PROGRAM/STAGE3/STAGE3_CHARTER.md`. Nothing in this folder is a rule
except through the CHARTER TEST presumption of charter §24.1: every gaming pattern in
the red-team reports and in v1's red-team ledger is presumed to receive its stated
classification, and the card carries the burden of rebuttal.

**Content.** None of these files contains a candidate law. The drafting agents were
instructed to generate no 𝒦 candidate, and every construction in the reports is an
abstract gaming pattern labelled CHARTER TEST.

## How it was produced (2026-10-07; workflow `wf_05020bc5-5e7`)
1. **Draft.** Three independent drafts, one per angle:
   - formal accounting → `DRAFT_1_formal_accounting.md`;
   - physics baseline → `DRAFT_2_physics_baseline.md`;
   - anti-gaming → `DRAFT_3_anti_gaming.md`.
2. **Synthesize.** The drafts were merged into `CHARTER_V0_MERGED.md`.
3. **Red-team.** Five adversarial lenses attacked v0:
   - D definitional → `REDTEAM_D_definitional.md`;
   - L relocation → `REDTEAM_L_relocation.md`;
   - S standard physics → `REDTEAM_S_standard_physics.md`;
   - C accounting → `REDTEAM_C_accounting.md`;
   - M measurability and stopping → `REDTEAM_M_measurability_stopping.md`.
4. **Revise.** The reports were applied to v0, producing `CHARTER_V1_WITH_LEDGER.md`
   (v1 plus its red-team ledger).
5. **Distil.** The builder distilled v1 into the governing charter. Charter Appendix D
   lists the changes.
6. **Pre-freeze audits.** Four independent read-only audits checked the distilled
   draft:
   - `AUDIT_R1_A1_coverage_DL.md`;
   - `AUDIT_R1_A2_coverage_SCM_credit.md`;
   - `AUDIT_R1_B_conformance.md`;
   - `AUDIT_R1_C_selftests_feasibility.md`, with `audit_C_arithmetic/`.

   The builder revised the charter, and a second round checked the revision.
   `FREEZE_VERIFICATION.md` records every finding, its disposition, and the residual
   items left for the owner.

## Defects in the drafting pipeline (disclosed)
- **Truncated returns.** The workflow captured only the *last* text block of each agent.
  Three returns were truncated as a result:
  - **DRAFT 1:** the synthesizer received only its second half. The full text here was
    recovered from the agent transcript.
  - **v0:** the red-teamers received only its 615-character tail. Lenses D, S, C and M
    found and read the full v0 on disk. Lens L worked from the tail and the governing
    texts, so its fixes are written as standalone inserts.
  - **Report D:** the reviser received it from CT-D10 onward, so v1 lacks fixes for
    CT-D02 and CT-D05. The full report here was recovered from the agent transcript, and
    the governing charter integrates CT-D01 to CT-D16 (Appendix D, row D-5).
- **Copies.** Files are byte copies of the agent outputs, except DRAFT 1 and Report D,
  which are concatenations of each agent's two text blocks, in order.
