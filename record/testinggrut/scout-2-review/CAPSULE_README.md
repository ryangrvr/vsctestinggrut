# Capsule: scout-2-review

| Field | Value |
|---|---|
| Source repository | `ryangrvr/TestingGRUT` (frozen historical record; read-only) |
| Branch | `scout-2-review` |
| Pin (authoritative) | `1f08ae156a346f6089ae3b3aab2be80b9ee4ef8f` |
| Proposed tag | `archive/scout-2-review` (label — pending, not pushed; tags do not exist on the remote) |
| Recorded state (verbatim; **not a terminal**) | SCOUT-2 REVIEW STATUS (live; `scout-2-review`)" (`review/REVIEW_STATUS.md`) |
| Parent | `scout-2` (this capsule holds only the files this campaign added over it) |
| Files imported (byte-exact) | 32 — paths, git blob ids and sha256 in `record/RECORD_IMPORT_MANIFEST.json` |
| Classification | ACTIVE GOVERNANCE **and** REPRODUCIBILITY SUPPORT |

**Classification basis (recorded wording):** review/REVIEW_STATUS.md is headed "(live; scout-2-review)"; SCOUT_2_REVIEW_HANDOFF.md Q9 says the branch "may receive later review additions" and that the scout-2-reviewed snapshot decision "is brought to the owner" / "Creation is left to the owner" (open governance decision). The branch's review/nr_*.py, ir06_check.py scripts and logs are the independent-code-path reproductions ("fresh implementations; different numerical routines; fresh random frames", review/README.md), i.e. reproducibility support for the frozen record.

## What this campaign is (from its own documents)

- scout-2-review is the post-freeze hostile audit of SCOUT-2, "built on the frozen SCOUT-2 head af0042f"; "The frozen record (scout-2) is unchanged" and "New material lives only under review/" (SCOUT_2_REVIEW_HANDOFF.md header; review/README.md).
- Its review layers are the owner's theorem review (IR-01…IR-04), the owner's ledger audit (IR-06, IR-07), and numerical reproductions that are "an independent code path, not an independent reviewer (same agent; no shared code; different routines; fresh frames / seeds)", which produced IR-05 (SCOUT_2_REVIEW_HANDOFF.md header).
- Findings IR-01…IR-07 yielded proposed errata E-01…E-08 in review/ERRATA_PROPOSED.md (frozen files untouched); review/REVIEW_STATUS.md records "none affects the residual boundary" and, under open findings, "none threatening C5 → D_dyn ⊕ [Σ ⊗ H_corr]_coupled ⊕ A_res".
- "Only the S2-ΣH H1 conflict case as originally characterized" was not reproduced (IR-05: it was "coarse-compatible"); the intended incompatibility result was "re-established on a separate code path with certified-incompatible pairs, 3/3", and every other targeted load-bearing conclusion reproduced (SCOUT_2_REVIEW_HANDOFF.md §Q4; review/REVIEW_STATUS.md §2).
- Q7 lists what "remains genuinely unreviewed": "an independent human or second-model reviewer for the numerics", "further decomposition of A_res" (UNREVIEWED in review/REVIEW_STATUS.md §3), re-fetching primary sources ("arXiv / APS blocked"), "the full Stoica theorem and the full-commutant epoch question (not adjudicated)", and out-of-envelope questions; Q9 records "No scout-2-reviewed branch has been created. That decision is brought to the owner" with "Creation is left to the owner".

## Key recorded statements

- `review/REVIEW_STATUS.md`: “# SCOUT-2 REVIEW STATUS (live; `scout-2-review`)”
- `SCOUT_2_REVIEW_HANDOFF.md`: “**SCOUT-2 SCIENTIFICALLY SATURATED AT CURRENT PREMISE ENVELOPE — HOSTILE REVIEW COMPLETED (independent code path + owner theorem / ledger review); RESIDUAL BOUNDARY CONFIRMED.**”
- `review/REVIEW_STATUS.md`: “**Numerical reproductions are an *independent code path, not an independent reviewer*.**”
- `SCOUT_2_REVIEW_HANDOFF.md`: “**Only the S2-ΣH H1 conflict case as originally characterized** (IR-05). The intended incompatibility result was **re-established on a separate code path** with certified-incompatible pairs, 3/3.”
- `review/REVIEW_STATUS.md`: “| IR-01 … IR-07 | recorded; errata E-01 … E-08 proposed; none affects the residual boundary |
| open | none threatening `C5 → D_dyn ⊕ [Σ ⊗ H_corr]_coupled ⊕ A_res` |”
- `SCOUT_2_REVIEW_HANDOFF.md`: “**No `scout-2-reviewed` branch has been created.** That decision is brought to the owner (Q9).”

---

Imported files are **never edited**. Verification: `python3 record/tools/import_capsules.py` (IMPORT/REPRODUCIBILITY CHECK — DOES NOT MODIFY FROZEN SCIENTIFIC STATUS).
