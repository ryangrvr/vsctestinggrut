# Capsule: conjecture-mode-1

| Field | Value |
|---|---|
| Source repository | `ryangrvr/TestingGRUT` (frozen historical record; read-only) |
| Branch | `grut-conjecture-mode-1` |
| Pin (authoritative) | `6c58155a5e3e74a8533281defbf7e5ff0b6833dc` |
| Proposed tag | `conjecture-mode-01-final` (label — pending, not pushed; tags do not exist on the remote) |
| Terminal status (verbatim) | **"CARD-01-v1R2 — COMPUTATIONALLY UNRESOLVED AT AVAILABLE MINIMIZATION METHOD"** |
| Parent | `program-governance-1` (this capsule holds only the files this campaign added over it) |
| Files imported (byte-exact) | 286 — paths, git blob ids and sha256 in `record/RECORD_IMPORT_MANIFEST.json` |
| Classification | ARCHIVED SCIENTIFIC RESULT **and** ACTIVE OPEN QUESTION **and** ACTIVE THEORY CONSTRAINT / EQUIVALENCE **and** REPRODUCIBILITY SUPPORT |

**Classification basis (recorded wording):** The import manifest labels the card record files "ARCHIVED SCIENTIFIC RECORD" and the code/configs/logs "REPRODUCIBILITY SUPPORT" (CONJECTURE_MODE_IMPORT_MANIFEST_01.md; Addendum A adds 232 raw files). The terminal is an unresolved computation, left open on recorded wording: "COMPUTATIONALLY UNRESOLVED AT AVAILABLE MINIMIZATION METHOD" and "Any further work needs a new owner ruling" (open question). EQ-01 is a standing constraint: "banked here permanently. A mathematically equivalent model may not return as a new card under different notation," verdict "C1-EQUIVALENT (narrow), per governance Annex A" (conjecture_mode/EQUIVALENCE_REGISTRY.md).

**Role.** Archived downstream empirical campaign — non-load-bearing for generative theory. Governance available for future empirical prediction campaigns (see `governance/`). Card #1: POSTULATED; COMPUTATIONALLY UNRESOLVED.

## What this campaign is (from its own documents)

- Earned (CONJECTURE_MODE_FINAL_SYNTHESIS_01.md §1): Conjecture Mode governance (two legal doors, owner-locked thresholds, prior-exposure disclosure, network preflight, nested-null result states, C-F1–C-F10); "Card #1 (horizon relaxor) was implemented and brought into contact with official DESI DR2 products"; "Provenance was verified" (all consumed likelihood data pinned and SHA-256 hashed); "The first apparent mechanical result was invalidated by convergence auditing" (v1's mechanical EXPLANATORY-SURVIVES failed the frozen 0.2 start-spread diagnostic and "was never accepted"); "The local-optimizer terminal was reached honestly" (v1 → v1R → v1R2, each frozen before execution, "no v1R3"); and "EQ-01 equivalence banked (narrow scope)."
- Not earned (§2): "No accepted empirical verdict for Card #1" (not EXPLANATORY-SURVIVES, EXPLANATORY-KILLED or MODEL-KILLED by any accepted run); "No GRUT prediction, and no validation" (a DR2 comparison is "retrospective by construction"); "No evidence that Card #1 is GRUT's generative law" (its response form is "POSTULATED HEURISTIC TOY LAW — NOT DERIVED FROM THE GRUT EFFECTIVE STRESS TENSOR"); "Cards #2–#4 remain historical and unrepaired"; "The supernova extensions, the ε > 0 control and the MCMC posterior were never run."
- Card #1 final status line (§3): "**Card #1** | **POSTULATED; COMPUTATIONALLY UNRESOLVED** (`CARD-01-v1R2 — COMPUTATIONALLY UNRESOLVED AT AVAILABLE MINIMIZATION METHOD`, commit `a8dbf3f`)"; further optimizer campaigns: "None (no v1R3). Any further work needs a new owner ruling, e.g. a fundamentally different, independent likelihood / minimization implementation."
- Orientation-only numbers, exactly as stated under the header "Orientation only — not a verdict, and not an S5 evaluation. These are the reproduced v1R2 core minima": χ²_Λ ≈ 10976.08; χ²_CPL ≈ 10963.81; χ²_Card ≈ 10972.72 (free-ε fit, ε ≈ −0.084); I_Card ≈ 3.36; I_CPL ≈ 12.28; F ≈ 0.27.
- The v1R2 terminal mechanism (CARD_01_V1R2_RESULT.md): ΛCDM, CPL and free-ε were reproduced under the frozen lower-minimum criterion, but "fixed ε = −0.08 was not reproduced" — "only 1 start within 0.2 of L = 10972.769. The closest independent route is 0.287 above it" — so "no Stage B" was run and "no S5 state is assigned."

## Key recorded statements

- `conjecture_mode/cards/CARD_01_V1R2_RESULT.md`: “## **TERMINAL: CARD-01-v1R2 — COMPUTATIONALLY UNRESOLVED AT AVAILABLE MINIMIZATION METHOD**”
- `CONJECTURE_MODE_FINAL_SYNTHESIS_01.md`: “**No accepted empirical verdict for Card #1.** v1, v1R and v1R2 are all unresolved. Card #1 is not EXPLANATORY-SURVIVES, EXPLANATORY-KILLED or MODEL-KILLED by any accepted run.”
- `CONJECTURE_MODE_FINAL_SYNTHESIS_01.md`: “**Orientation only — not a verdict, and not an S5 evaluation.** These are the reproduced v1R2 core minima.”
- `CONJECTURE_MODE_FINAL_SYNTHESIS_01.md`: “| χ²_Λ | ≈ 10976.08 | / | χ²_CPL | ≈ 10963.81 | / | χ²_Card | ≈ 10972.72 (free-ε fit, ε ≈ −0.084) | / | I_Card | ≈ 3.36 | / | I_CPL | ≈ 12.28 | / | F | ≈ 0.27 |”
- `conjecture_mode/EQUIVALENCE_REGISTRY.md`: “| **EQ-01** | Card #3 (linear geometric target) | In flat homogeneous FRW with pressureless matter and a `w = −1` vacuum, at the declared background level, targets linear in `ρ_m`, `ρ_v`, `H²` and `Ḣ` collapse to the same linear-response family after coefficient redefinition. | radiation; curvature; perturbations; different interaction laws; nonlinear target functions | **C1-EQUIVALENT (narrow)**, per governance Annex A |”
- `conjecture_mode/EQUIVALENCE_REGISTRY.md`: “Under C-F3, every proven collapse or reparameterization is banked here permanently. A mathematically equivalent model may not return as a new card under different notation.”

---

Imported files are **never edited**. Verification: `python3 record/tools/import_capsules.py` (IMPORT/REPRODUCIBILITY CHECK — DOES NOT MODIFY FROZEN SCIENTIFIC STATUS).
