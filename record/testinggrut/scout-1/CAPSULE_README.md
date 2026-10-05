# Capsule: scout-1

| Field | Value |
|---|---|
| Source repository | `ryangrvr/TestingGRUT` (frozen historical record; read-only) |
| Branch | `scout-1` |
| Pin (authoritative) | `a2987fed5880da62c874857faa0a93099d23f64d` |
| Proposed tag | `archive/scout-1` (label — pending, not pushed; tags do not exist on the remote) |
| Terminal status (verbatim) | **"FROZEN."** |
| Parent | `scout-0` (this capsule holds only the files this campaign added over it) |
| Files imported (byte-exact) | 98 — paths, git blob ids and sha256 in `record/RECORD_IMPORT_MANIFEST.json` |
| Classification | ARCHIVED SCIENTIFIC RESULT **and** ARCHIVED NEGATIVE / FAILED ROUTE **and** REPRODUCIBILITY SUPPORT |

**Classification basis (recorded wording):** "FROZEN" and "SCOUT-1 stops here" mark the record archived; §F "Major negative results / killed routes" plus "SCOUT-1 earned zero distinctive GRUT empirical predictions" ground the negative reading; §E's theorem-grade positive results (KRI/NIG/SFR labelled) and the CANONICAL-CANDIDATE TC-1 ground the scientific-result reading; §K "Owed checks" and the verdict's "INDEPENDENT REVIEW OWED" ground reproducibility support.

## What this campaign is (from its own documents)

- SCOUT-1, the "Quotient Selection Campaign", was "forked from the frozen SCOUT-0 head ab2da47" and began with "Can anything actually FIX a quotient value, rather than merely classify consequences of supplied values?", evolving into "Where does irreducible specification information enter a physical theory, and where does GRUT sit relative to that boundary?" (playground/SCOUT_1/SCOUT_1_HANDOFF.md §A).
- Its final product is a hierarchy C1–C5 explicitly labelled "candidate; not a universal theorem", with C5 (operational framework / composition / dimension) as the "current universal stopping point of the scout" and the note "In GRUT, C4 remains supplied" (handoff §B); the one CANONICAL-CANDIDATE result is TC-1 ("earned-layer non-selection under G") with "Owed: independent review" (handoff §C).
- The handoff's empirical status is "SCOUT-1 earned zero distinctive GRUT empirical predictions", and §I records GRUT as "a theory-construction / dependency framework over supplied C4/C5 and basin/state structure" — "a statement about the current record, not a proof about every imaginable future GRUT extension".
- Owed checks at freeze (handoff §K): independent reproduction of TC-1 (W1-C lemma + census); an independent hostile review of the final hierarchy / TC-4' lineage (D1 → W4 → W5 → D3); a full primary-text review of the D3 reconstruction proofs (headlines are PRIMARY-ABSTRACT-VERIFIED only); verification of SECONDARY-graded literature claims in LITERATURE_LEDGER.md (e.g. N_c ≈ 2.9; PrimEx width; Koecher–Vinberg / fermionic local tomography; alpha-vacua; Renou et al.; quaternionic composites); a second reader for the information-accounting classifications; and review of numerical probes carrying finite-size/noise qualifications (W2-ETH L ≤ 12; W3-NL small-epsilon exponents; W4 width/skewness inconclusive; W5 anisotropic drift; W2-QE grid norm drift).
- Queue items not run at freeze (playground/SCOUT_1/FRONTIER_QUEUE.md): W2-POS "PARKED ... literature-gated; not run"; "C17/C18 positivity bounds, C29 TKNN | not run (deferred at freeze)"; D2 and D4 "CLOSED by owner ruling, not opened"; "W6+ | not authorized".
- The capsule delta is confirmed in git: `git diff --name-only origin/scout-0 origin/scout-1` lists exactly 98 paths, all under playground/SCOUT_1/; corrections are tracked visibly ("There are banners on the affected files, ledger entries X-01…X-13, and AUDIT REPAIR 01/02", handoff header).

## Key recorded statements

- `playground/SCOUT_1/SCOUT_1_HANDOFF.md`: “**Status:** FROZEN.”
- `playground/SCOUT_1/SCOUT_1_HANDOFF.md`: “**SCOUT-1 SCIENTIFICALLY SATURATED AT CURRENT QUESTION / PREMISE ENVELOPE — INDEPENDENT REVIEW OWED.**”
- `playground/SCOUT_1/SCOUT_1_HANDOFF.md`: “**SCOUT-1 earned zero distinctive GRUT empirical predictions.**”
- `playground/SCOUT_1/SCOUT_1_HANDOFF.md`: “Nothing here carries canonical ACCEPTED status. Results judged promotion-worthy are labelled CANONICAL-CANDIDATE.”
- `playground/SCOUT_1/FRONTIER_QUEUE.md`: “**Status: SCOUT-1 is FROZEN** (owner ruling). No further scientific probes are authorized in this campaign. Every row is CLOSED / DONE / RETIRED / PARKED.”
- `playground/SCOUT_1/FRONTIER_QUEUE.md`: “| C17/C18 positivity bounds, C29 TKNN | not run (deferred at freeze) |”

---

Imported files are **never edited**. Verification: `python3 record/tools/import_capsules.py` (IMPORT/REPRODUCIBILITY CHECK — DOES NOT MODIFY FROZEN SCIENTIFIC STATUS).
