# Capsule: program-governance-1

| Field | Value |
|---|---|
| Source repository | `ryangrvr/TestingGRUT` (frozen historical record; read-only) |
| Branch | `grut-program-governance-1` |
| Pin (authoritative) | `5baa8afd83b8a2dbce31b8f3c4bd484417afbc11` |
| Proposed tag | `archive/grut-program-governance-1` (label — pending, not pushed; tags do not exist on the remote) |
| Terminal status (verbatim) | **"FROZEN BY OWNER RULING."** |
| Parent | `selector-screen-1` (this capsule holds only the files this campaign added over it) |
| Files imported (byte-exact) | 3 — paths, git blob ids and sha256 in `record/RECORD_IMPORT_MANIFEST.json` |
| Classification | ACTIVE GOVERNANCE |

**Classification basis (recorded wording):** The three files are headed "program law" and "FROZEN BY OWNER RULING" (PROGRAM_CAMPAIGN_GATE_01.md, PROGRAM_GOVERNANCE_OWNER_RULING_01.md), and the execution branch's import manifest assigns each the role "ACTIVE GOVERNANCE REFERENCE: rules a future campaign may cite" (CONJECTURE_MODE_IMPORT_MANIFEST_01.md lines 79–81).

**Role.** The three files of this capsule are imported under `governance/program_governance/` (the active-rules area) and are referenced from here rather than duplicated; see `governance/GOVERNANCE_README.md`.

## What this campaign is (from its own documents)

- The branch holds the program's governance set in three program_governance/ files; the owner ruling on `grut-program-governance-1 @ 2236e93` records "Governance accepted. The governance state at `2236e93` is accepted as scientifically correct" and the result "FROZEN BY OWNER RULING." (program_governance/PROGRAM_GOVERNANCE_OWNER_RULING_01.md).
- PROGRAM_CAMPAIGN_GATE_01.md is "program law, FROZEN BY OWNER RULING" and governs "the opening of every new scientific campaign in the GRUT program" through two doors — Door D (derivation/selector, requirements D-1 to D-4) and Door C (conjecture) — with "A proposal that fits neither door is refused: NO CAMPAIGN."
- CONJECTURE_MODE_CHARTER_01.md is "ACCEPTED IN SUBSTANCE" with editorial repairs ER-1 to ER-3 applied, carries Annex A (refiled historical cards) and Annex B (Card #1 rerun requirements), and at this freeze states "CARD #1 IS NOT EXECUTABLE" with every numerical kill boundary "an OWNER-LOCK slot, left empty on purpose."
- The ruling states "Program law creates no physics and modifies no frozen scientific result," makes the Prior-Exposure Disclosure permanent (Charter §4D), and creates the immutable snapshot `grut-program-governance-1-frozen`, from which "The execution branch `grut-conjecture-mode-1` descends."
- On the execution branch, CONJECTURE_MODE_IMPORT_MANIFEST_01.md assigns all three program_governance/ files the role "ACTIVE GOVERNANCE REFERENCE" ("rules a future campaign may cite").

## Key recorded statements

- `program_governance/PROGRAM_GOVERNANCE_OWNER_RULING_01.md`: “**Result:** **FROZEN BY OWNER RULING.**”
- `program_governance/PROGRAM_GOVERNANCE_OWNER_RULING_01.md`: “6. **Program law creates no physics and modifies no frozen scientific result.**”
- `program_governance/PROGRAM_CAMPAIGN_GATE_01.md`: “A proposed campaign must enter through exactly one of two legal doors. A proposal that fits neither door is refused: **NO CAMPAIGN**.”
- `program_governance/CONJECTURE_MODE_CHARTER_01.md`: “**Execution status:** **CARD #1 IS NOT EXECUTABLE.**”
- `program_governance/CONJECTURE_MODE_CHARTER_01.md`: “> **A postulate may be unearned. It may never be hidden.**”
- `CONJECTURE_MODE_IMPORT_MANIFEST_01.md (on grut-conjecture-mode-1)`: “| `program_governance/PROGRAM_GOVERNANCE_OWNER_RULING_01.md` | ACTIVE GOVERNANCE REFERENCE | `9f5c893c0311dfcba9978887f2dd0dd1fd96d9c539789dd1947d0cb1c4bcba13` |”

---

Imported files are **never edited**. Verification: `python3 record/tools/import_capsules.py` (IMPORT/REPRODUCIBILITY CHECK — DOES NOT MODIFY FROZEN SCIENTIFIC STATUS).
