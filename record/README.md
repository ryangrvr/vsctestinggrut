# record/ — the consolidated frozen record

**Created by the Record Integration campaign (branch `record-integration-01`), 2026-10-05.**

**Governing rule.** Files under `record/testinggrut/` (and the governance files under `governance/`) are **byte-exact imports from the frozen historical record and are never edited**. Migration and reproducibility may be verified; the frozen scientific status of imported work may not be changed. Any verification that reveals a contradiction stops and is recorded for owner review.

## Layout

| Path | Content |
|---|---|
| `record/testinggrut/<campaign>/` | one capsule per TestingGRUT campaign: the campaign's own files (its additive delta over its parent branch), byte-exact, plus a `CAPSULE_README.md` carrying status, role, source, pin and terminal |
| `record/testinggrut/TESTINGGRUT_ARCHIVE_INDEX_01.md` | the frozen branch inventory (imported from TestingGRUT branch `archive-index`), the authority for pins and verbatim statuses |
| `record/RECORD_IMPORT_MANIFEST.json` | per-file provenance: source branch, pinned 40-character commit SHA, git blob id and sha256 over the blob bytes |
| `record/tools/` | the import and verification tooling (`import_capsules.py verify` re-hashes every imported file) |
| `governance/` | the active program rules (byte-exact; referenced from capsules, never duplicated) |
| `registry/equivalence/` | the program-wide equivalence / rediscovery registry (cross-references frozen entries) |
| `registry/open_questions/` | active forks and frontier-blocked items, each with its source capsule and pin |
| `theory/` | untouched by this campaign |

## Capsule structure

Every campaign is **purely additive** over its parent branch (verified: no file modified or removed by any campaign relative to its parent), so a capsule holds exactly the files its campaign created, at their original paths. Three capsules are reference-only (`scout-0`, `bri1`, and most of `oldgrut`): their content is already byte-identical elsewhere in this repository or on `bri1-manuscript`, and the capsule README records where.

Campaign lineage at import time:

```
slim line: scout-2 → scout-2-review(ed) → bridge-1 → qft-scout-1 → gravity-scout-1
           → residual-synthesis-1 → selector-screen-1 → { program-governance-1 → conjecture-mode-1
                                                        ; reflexive-autonomy-0 → directed-autonomy-0 }
fat line:  scout-0 → { scout-1 ; independent-verification-0 ; bri1 }
separate:  oldgrut (= GRUT-RAI v4 snapshot; see its capsule README)
```

## Verification

`python3 record/tools/import_capsules.py` re-verifies every imported file's sha256 against the manifest (and, when the frozen source clone is present, the source blob ids at the pins). All reproducibility checks performed during the import are labelled **IMPORT/REPRODUCIBILITY CHECK — DOES NOT MODIFY FROZEN SCIENTIFIC STATUS** in the capsule READMEs.
