# RECORD INTEGRATION 01 — campaign note

**Branch:** `record-integration-01` (from `main` @ `7baf2f1`). **Date:** 2026-10-05.

**Governing rule.** Migration and reproducibility may be verified. The frozen scientific status of imported work may not be changed. Any verification that reveals a contradiction stops and is recorded for owner review.

**Inventory authority.** `TESTINGGRUT_ARCHIVE_INDEX_01.md`, imported byte-exact from `ryangrvr/TestingGRUT` branch `archive-index` at `0b904240a4b1c1836a81a186f59ac97acab6b9db` (`record/testinggrut/TESTINGGRUT_ARCHIVE_INDEX_01.md`). All 27 index rows' pins were checked against `git ls-remote` of the frozen repository: **27/27 match**. TestingGRUT was treated as read-only throughout; nothing was pushed to it.

## What this campaign did

1. Imported each TestingGRUT campaign's additive delta byte-exact into `record/testinggrut/<campaign>/`, pinned per file by git blob id and sha256 in `record/RECORD_IMPORT_MANIFEST.json` (781 files, all re-verified by `record/tools/import_capsules.py verify`).
2. Wrote a `CAPSULE_README.md` per capsule: status (verbatim from the frozen record), role, source repository, branch, full 40-character pin, terminal, and classification.
3. Placed the governance trio under `governance/program_governance/` (active rules), created `registry/equivalence/EQUIVALENCE_REGISTRY.md` (cross-referencing the frozen EQ-01 / EQ-1 / SX-1 entries, never copying their verdict wording out of context) and `registry/open_questions/` (active forks and frontier-blocked items, each with source capsule and pin).
4. Left `theory/` untouched. BRI1 is referenced at its pin `27829f1fa8fd52353f596921da9630a9bf70397e`, not duplicated — its 56-file record is already imported byte-exact on branch `bri1-manuscript`.

## Deviations from the integration prompt (none scientific)

| # | Deviation | Why |
|---|---|---|
| D1 | **Tags not pushed.** The prompt's tag names (e.g. `bri1-verification-final`, `archive/scout-0`) are recorded as *labels* in each capsule README, marked "pending, not pushed". | TestingGRUT is frozen/read-only for this campaign, and the tags do not exist on the remote (`git ls-remote --tags` returned none). Creating them is a write to the frozen repository — owner action. |
| D2 | **`oldgrut` imported partially rather than skipped as superseded.** | IMPORT/REPRODUCIBILITY CHECK — DOES NOT MODIFY FROZEN SCIENTIFIC STATUS: comparing the pinned `oldgrut` tree (1087 files) to this repository's `main` showed 62 files *not* byte-identical here (37 absent, 25 variant). All 1087/1087 are byte-identical in `ryangrvr/GRUT-RAI` branch `v4` @ `058c40d4130c4c11c8b5fc7ebbe7620eb3a72ca8`, so nothing is lost; the 62-file delta is imported under `record/testinggrut/oldgrut/` and its classification is **flagged for owner review** (see that capsule's README). |
| D3 | **Named open questions located on the fat lineage, not the slim.** "Collisionality" and "IR carrier"/"infrared carrier" do not occur on the slim-lineage branches (scout-2 → … → conjecture-mode-1); they **are recorded verbatim on the fat lineage** (scout-0 / scout-1 / independent-verification-0, blob-identical in this repo's `main`): ledger item #17 / `rung3_single_pole` ("derived-pending") and the `rung9a_value` carrier identification ("LIVE and register-open"). The registry entries quote the recorded wording, note the nearest *distinct* slim-line items (T2-4; B4-CUC) to prevent false matches, and flag the referent for owner confirmation (`registry/open_questions/OQ-01`, `OQ-02`). | The frozen wording is authoritative; the registry cites recorded items rather than renaming anything. |

## Housekeeping (report only — nothing deleted)

- **Duplicate branch:** `claude/wizardly-hypatia-j48qk4` on this repository points at the same commit as `bri1-manuscript` (`92dc6bb` on the remote). It is the session's auto-created working branch and is redundant with `bri1-manuscript`. Reported for the owner to delete or keep; not deleted here.
- This campaign's branch `record-integration-01` is **not merged into `main`** — merge requires owner approval.
- F0 is not opened; no GGC0 ruling is modified.

## Contradictions and tensions found (recorded, not resolved)

All items below are recorded for owner review; no frozen status was changed.

1. **`oldgrut` supersession assumption partly false** (D2 above) — resolved factually via GRUT-RAI `v4`; classification decision left to owner.
2. **scout-2 vs scout-2-review status tension** — the frozen scout-2 `STATUS.md` terminal still reads **"SCOUT-2 SCIENTIFICALLY SATURATED AT CURRENT PREMISE ENVELOPE — INDEPENDENT REVIEW OWED"**, while scout-2-review's `SCOUT_2_REVIEW_HANDOFF.md` §Q8 declares **"HOSTILE REVIEW COMPLETED (independent code path + owner theorem / ledger review); RESIDUAL BOUNDARY CONFIRMED"** — and the review branch itself qualifies that completion ("Numerical reproductions are an independent code path, not an independent reviewer", `review/REVIEW_STATUS.md`; Q7 still lists an independent human / second-model review as owed). Both wordings are quoted verbatim in their own capsules. This is lineage (the review branch supersedes by *being later*, never by editing the frozen scout-2 files), not an error — recorded so nobody reads the scout-2 capsule alone.
3. **Named-open-question referents** (D3 above) — the recorded fat-line items are cited; confirmation that they are the prompt's referents is left to owner.

No sha256 mismatch, no blob mismatch, and no pin mismatch was found anywhere (781/781 imported files verified; 287/287 frozen manifest sha256 claims verified; the Conjecture-Mode analyzer transfer-check regenerated its committed summary byte-identically from imported inputs).
