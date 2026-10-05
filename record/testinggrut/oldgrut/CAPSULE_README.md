# Capsule: oldgrut (partial import — unique content only; classification flagged for owner review)

| Field | Value |
|---|---|
| Source repository | `ryangrvr/TestingGRUT` (frozen historical record; read-only) |
| Branch | `oldgrut` |
| Pin (authoritative) | `ceeecd9419049e43bd404523078bfdcaea05786c` (head commit dated 2026-09-14) |
| Proposed tag | `archive/oldgrut` (label — pending, not pushed; tags do not exist on the remote) |
| Recorded state (verbatim; **not a terminal**) | "This is a freeze, not a burial." (`GRUT_PROGRAM_FREEZE.md`; the head commit postdates it) |
| Classification | ARCHIVED SCIENTIFIC RESULT (imported delta) — **flagged for owner review** |

## What is imported, and why only part

IMPORT/REPRODUCIBILITY CHECK — DOES NOT MODIFY FROZEN SCIENTIFIC STATUS. The pinned tree (1087 files) was compared by git blob id against this repository's `main` at `7baf2f1`:

| Slice | Count | Handling |
|---|---|---|
| Byte-identical in `main`, same path | 1025 | referenced, not copied |
| Present in `main` at the same path, **different content** | 25 | **imported byte-exact** under this capsule |
| Absent from `main` (by path and by blob) | 37 | **imported byte-exact** under this capsule |

The 62 imported files (paths and hashes in `record/RECORD_IMPORT_MANIFEST.json`) include the branch's late adjudication work of 2026-09-14 that exists nowhere else in this repository: the R′ adjudication (filed **"R'_UNRESOLVED (demonstrated)"**), the A3-4 contract differential (**"OBJECTS_NOT_COMPARABLE"**), the P1A/P1B edge adjudications and ratification packages, the U1 observable map, U2 covariant kernel, U3 IR selector, the WALL-A reduction, the static-patch discharge gate, the gauge-invariant Tier-3 target spec, the RAI capability-test certifications, and the tier-provenance baseline.

## Containment in the canonical repository (verified)

IMPORT/REPRODUCIBILITY CHECK — DOES NOT MODIFY FROZEN SCIENTIFIC STATUS: all **1087/1087** files of the pinned `oldgrut` tree are byte-identical (git blob match) in `ryangrvr/GRUT-RAI`, branch `v4`, at `058c40d4130c4c11c8b5fc7ebbe7620eb3a72ca8`; that branch carries **4 additional files** beyond the pin (its own later state, out of this campaign's scope). Nothing in `oldgrut` is lost: it is fully preserved in the canonical repository and, for the 62-file delta, now also here.

## Flag for owner review

The integration prompt's working assumption was that `oldgrut` is superseded by the record this repository carries. The measurement above shows that is **only partly true**: 62 files were not in this repository until this import, and this repository's `main` descends from GRUT-RAI `master-w25bu9`, not from `v4`. What the owner should decide: whether the `oldgrut`/`v4` line's adjudication work (R′, A3-4, P1A/P1B, U1–U3, WALL-A, Tier-3) has any standing in the consolidated program, or remains archived as a closed historical line. **No scientific status is assigned or changed here.**
