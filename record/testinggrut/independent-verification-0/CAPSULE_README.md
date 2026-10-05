# Capsule: independent-verification-0

| Field | Value |
|---|---|
| Source repository | `ryangrvr/TestingGRUT` (frozen historical record; read-only) |
| Branch | `grut-independent-verification-0` |
| Pin (authoritative) | `bd287a88dc08ae54173a6c73368db0e250cc1c7f` |
| Proposed tag | `archive/grut-independent-verification-0` (label — pending, not pushed; tags do not exist on the remote) |
| Recorded state (verbatim; **not a terminal**) | PAUSED FOR OWNER PROGRAM-LEVEL DISCUSSION." (`verification_0/VER0_STATUS.md`) |
| Parent | `scout-0` (this capsule holds only the files this campaign added over it) |
| Files imported (byte-exact) | 48 — paths, git blob ids and sha256 in `record/RECORD_IMPORT_MANIFEST.json` |
| Classification | REPRODUCIBILITY SUPPORT **and** ACTIVE OPEN QUESTION |

**Classification basis (recorded wording):** REPRODUCIBILITY SUPPORT from VER0_CHARTER.md's own purpose line, "verification / reproduction, not exploration", and the ledger's reproduction/comparison/owner-ruling structure. ACTIVE OPEN QUESTION because the recorded state is a pause, not a terminal ("PAUSED FOR OWNER PROGRAM-LEVEL DISCUSSION."), with "Criterion 2 is not met" and items V0-5/V0-6 "OUTSTANDING — PRIMARY-TEXT ACCESS DEPENDENT" (VER0_STATUS.md).

## What this campaign is (from its own documents)

- The branch was "created from the frozen scientific parent scout-0 @ ab2da47407bb670d94e2a52c87599fa13fd8ab99 (unmodified)" with "Purpose (verification / reproduction, not exploration)" (verification_0/VER0_CHARTER.md), to discharge the SCOUT-0 criterion-2 reproduction debts (VER0-A) and independently reconstruct the BRI1-X1 theorem from a sealed statement-only target (VER0-B).
- git diff ab2da47..origin/grut-independent-verification-0 confirms the capsule is exactly 48 added files, all under verification_0/ (charter, ledger, status, 5 target specs, 5 reproduction/comparison doc pairs plus a second-reader report, and 22 code/log files); no file of scout-0 was modified or deleted.
- Five items were accepted by owner ruling at grade VER-I1 (orchestrator-exposed), each reproduction performed by a "context-isolated sub-agent" with an audited file-access report: V0-1-C (P-17, correction CL-1), V0-2-C (P-15 chain, CR-1..3), V0-3-C with subgrade V0-3-T3-F ("the single-v_b theorem refuted as stated"), V0-4-C (EDA-01 second read: "Headline NO-FIX confirmed (22 / 22)", "6 / 22 rows discordant at the CON boundary"), and VER0-B-A with "S-1 banked: X1 ∉ E₂± for every N_B ≥ 1 on a common small-time interval (internally reproduced, not externally reviewed)".
- VER0_STATUS.md records "SCOUT-0: PROVISIONALLY SATURATED — OWED CHECKS ONLY. **Criterion 2 is not met.**", with "Items 4 and 6 are **OUTSTANDING — PRIMARY-TEXT ACCESS DEPENDENT**. Every item is at most VER-I1." (VER0_CHARTER.md: "VER-I1 is the **maximum grade the present automated workflow can earn**" and is "not independent external review").
- The final owner ruling in verification_0/VER0_LEDGER.md (boundary ae56ed0) reads "**STOP:** no governance branch, no V0-5 / V0-6, no BRI0 change, no new campaign. The owner will discuss program-level questions" — consistent with the index recorded state; no branch document contradicts "PAUSED FOR OWNER PROGRAM-LEVEL DISCUSSION."

## Key recorded statements

- `verification_0/VER0_CHARTER.md`: “Purpose (verification / reproduction, not exploration) ... Nothing here modifies `scout-0` ... No PR, no merge.”
- `verification_0/VER0_STATUS.md`: “SCOUT-0: PROVISIONALLY SATURATED — OWED CHECKS ONLY. **Criterion 2 is not met.** ... Items 4 and 6 are **OUTSTANDING — PRIMARY-TEXT ACCESS DEPENDENT**. Every item is at most VER-I1.”
- `verification_0/VER0_LEDGER.md`: “**STOP:** no governance branch, no V0-5 / V0-6, no BRI0 change, no new campaign. The owner will discuss program-level questions”
- `verification_0/VER0_CHARTER.md`: “VER-I1 is the **maximum grade the present automated workflow can earn**. It is **not** "independent external review" and **not** "independent scientific replication by another researcher".”
- `verification_0/VER0_LEDGER.md`: “**Owner ruling, V0-3.** Accepted: overall **V0-3-C**, plus subgrade **V0-3-T3-F** (the single-v_b theorem refuted as stated). Edge-data-set replacement banked.”

---

Imported files are **never edited**. Verification: `python3 record/tools/import_capsules.py` (IMPORT/REPRODUCIBILITY CHECK — DOES NOT MODIFY FROZEN SCIENTIFIC STATUS).
