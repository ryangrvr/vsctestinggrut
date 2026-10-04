# GGC0 NAMING CONVENTION 01
## Frozen 2026-10-04 — canonical vocabulary for residual accounting

**Purpose.** The record has drifted between near-synonyms ("residual",
"remnant", "dependent residue", "supplied input", "grout") that are *not*
synonyms, and the drift has already caused misreadings (e.g., treating a
residual item as though the record had concluded it is solution data — it has
not; that is what the proposed GGC0 classification exists to test). This
document fixes the vocabulary. All GGC0 documents, registers and charters use
these terms and no others. Existing record documents are not rewritten; where
they use older words, the mapping in §3 applies.

**Status.** Frozen convention. Amendment requires a dated dated-correction
document (`GGC0_NAMING_CORRECTION_NN.md`), never silent edits.

---

## 1. Canonical terms

| Term | Definition | Use |
|---|---|---|
| **SUPPLIED INPUT** | A structure the record explicitly prices as an input rather than a derived result. The canonical inventory is Ledger A (A-1 … A-16) in `GRUT_WORKING_THEORY_SYNTHESIS_01.md` §1, consolidated into nine layers in its §5.1. | Inventory-level noun. Never used for a *classification verdict*. |
| **RESIDUAL ITEM** | A supplied input that remains supplied *after* all campaigns run to date. Synonym in practice for supplied input at the current boundary; "residual" emphasizes that derivation attempts have already been made and failed or blocked. | The unit classified by the GGC0 classification charter. |
| **LAW-LIKE / SOLUTION-LIKE / MIXED** | The three bins of the proposed classification criterion (`GGC0_LAW_SOLUTION_CLASSIFICATION_CHARTER_01.md`, PROPOSED — awaiting owner approval). | Verdict nouns only. May not be used until the criterion is approved, and then only with the recorded Q1/Q2/Q3 answers and an adversarial counterargument. |
| **UNCLASSIFIED** | The mandated state of every residual item between now and owner approval of the criterion. | The only legal bin-value in the register today. |
| **ADMISSION CONTRACT** | The recorded conditions under which a residual item would change status: what artifact, derivation, or reproduction would move it (e.g., BRI1 moves from UNREPRODUCED-IN-REPO to load-bearing upon import of its frozen source artifacts). | Register column. |
| **PRICED COST** | The recorded consequence of an item being supplied: which derivations run only conditionally downstream of it. Sourced from Ledger C / Ledger D of the synthesis. | Register column. |

## 2. Deprecated terms (never introduce in new documents)

| Deprecated | Reason | Replacement |
|---|---|---|
| "remnant" | Ambiguous between residual item and left-over derived content. | RESIDUAL ITEM |
| "dependent residue" | Suggests a classification (solution-like) not yet earned. | RESIDUAL ITEM, with bin stated separately |
| "grout" | Rhetorical; appears in informal discussion only. | SUPPLIED INPUT |
| "residual datum" (singular, unqualified) | Invites treating the whole ledger as one object. | Cite the specific item ID (A-n) |

## 3. Mapping for reading older documents

Older record documents use "supplied", "supplied primitive", "residual
input", "remaining input", and "irreducible input" interchangeably. All of
them map to SUPPLIED INPUT / RESIDUAL ITEM as defined above. None of them,
without an explicit owner ruling, may be read as having assigned a
LAW-LIKE/SOLUTION-LIKE verdict.

## 4. Binding rule

Any GGC0 document that states or implies a LAW-LIKE / SOLUTION-LIKE verdict
without (i) an approved criterion, (ii) recorded Q1/Q2/Q3 answers, and (iii)
a recorded adversarial counterargument, is invalid and must be marked as such
on discovery.
