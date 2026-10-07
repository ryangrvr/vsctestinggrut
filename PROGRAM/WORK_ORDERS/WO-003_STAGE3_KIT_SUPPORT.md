# WO-003 — Stage-3 kit: computational support for the pending external checks

**Status: OPEN** (issued by Claude Code at handoff, 2026-10-07; owner direction: hand off to VS Code).
**Assignee:** VS Code. **Output:** `PROGRAM/RESULTS/WO-003/`. **Governs:** `PROGRAM/HANDOFF_VSCODE.md` §4.

These are reproductions that **support** the owner's/ChatGPT's external check. They are not themselves an
external check: `CHECKS.md` status is set only by the owner or a checker. Do not modify `PROGRAM/STAGE3/kit/`
or the charter; if you find a defect, report it (with a reproduction) and STOP that item.

## Tasks
1. **Smoke run.** `cd PROGRAM/STAGE3/kit && python3 test_l0_code.py && python3 test_kit.py && python3 sel222.py`
   (SEL takes ~3 min). Record outputs in `RESULTS/WO-003/smoke.md`. Expected: 10 ok, 11 ok, `matches_frozen: true`.
2. **Price coder vs Appendix B.** Write an *independent* implementation (do not import `l0_code.py`) of charter
   §4.1 L_stmt, ℓ(n) (Elias-δ of n+1), literal pricing at p ∈ {6, 10, 16}, and the Appendix B alphabet. Compare
   with `l0_code.py` on ≥ 50 expressions (all token groups, nat/rat/real literals, repeated variables,
   quantifier nesting) and on every worked number in §4 and Appendix A/B. Also compare `compression_verdict`
   and `coupling_credit` against §4.3–§4.4 and §2.5 on boundary cases (ΔL0 = 10 exactly; p=16 margin 0; family
   cap binding). Report every mismatch with the charter clause it violates → `RESULTS/WO-003/price_coder_check.md`.
3. **HB controls.** Cross-check `kit/hb_controls.py` against `R1/c2_controls.py` (C2-G, C2-NG exact zeros; the
   static-tail witness). Add at least one k ≥ 2 affine-entry instance with random rational G_a (fixed seed) and
   confirm the exact identity. → `RESULTS/WO-003/hb_check.md`.
4. **NR-4 fix.** Independently reproduce: (a) the owner's toy (constant law-free image satisfying ℛ★ while K
   varies with coupling) → pre-fix `git show 608d72f~1:PROGRAM/STAGE3/kit/nr4_ablation.py` gives
   NOT-RELOCATED, fixed gives RELOCATED; (b) VOID case gives no 0/0 fractions and 'VOID' responsibility;
   (c) try ≥ 3 further abstract fixtures (no physics) that might make the fixed harness return a
   card-favourable verdict. → `RESULTS/WO-003/nr4_check.md`.

## Done when
All four reports are pushed, this file's status is `DONE — PENDING REVIEW`, and `STATE.md` lists them.
Every judgment in the reports is marked `DRAFT — pending Claude Code review`.
