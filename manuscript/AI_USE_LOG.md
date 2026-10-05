# AI-use log — BRI1 manuscript build

This log is the provenance record behind the two disclosure placeholders in the manuscript:

- Methods/Supplement (S6): `[AI-USE DISCLOSURE — research: proof development, code, numerical verification]`
- Acknowledgments: `[AI-USE DISCLOSURE — manuscript preparation]`

The disclosure texts themselves are deliberately not drafted; the author writes them from this log once the target journal's policy has been checked against its official page.

**Policy.** An AI system is a tool, not an author. No AI system is listed as an author of the manuscript. In Git metadata, no commit from the repair commit (`7d806e1`) onward carries an AI `Co-Authored-By` trailer; the session's Git identity is a separate matter, recorded under "Git metadata" below.

**AI system.** Claude (Anthropic), operated through Claude Code in a cloud session. The exact model version is recorded in the session metadata, not in this repository. Session: https://claude.ai/code/session_013LcLgdYXEg8W8jjixp56xM

## What the AI did

| Date | Activity | Output | Human verification status |
| --- | --- | --- | --- |
| 2026-10-05 | Located the proof/verification record (`ryangrvr/TestingGRUT@27829f1`) and imported it byte-exact; wrote the import ledger and verifier | `backreaction_identifiability_0/`, `RECORD_IMPORT.json`, `tools/record_import.py` | import verified mechanically (git blob ids); not reviewed by a human |
| 2026-10-05 | Wrote the build system: value generation, placeholder rendering, pandoc/xelatex conversion, build checks | `tools/*.py`, `Makefile`, `BUILD_MANIFEST.json`, `build/BUILD_REPORT.*` | owner review of commit `ca0f4d5` (2026-10-05) graded the provenance engineering; repair pass in commit 2 |
| 2026-10-05 | Fresh symbolic recomputation of the small-time series of c(t) through t^14 | `tools/gen_constants.py`, `data/constants.json` | agrees exactly with the record's symbolic log; not reviewed by a human |
| 2026-10-05 | Fresh numerical small-time check (S2) | `tools/check_t7.py`, `data/t7_check.json` | per the owner's review of `ca0f4d5` (review not archived in this repository) |
| 2026-10-05 | Generated figures and tables from the authoritative numerical output | `tools/gen_figures.py`, `tools/gen_tables.py`, `figures/`, `data/tables/` | owner's review of commit `ca0f4d5` covered the artefacts present at that commit only |
| 2026-10-05 | Drafted all manuscript prose: main text sections 1–7 and supplements S1–S6, including the human-readable exposition of the proofs in S1 | `src/*.md` | **pending**: the author's line-by-line proof review of S1 has not yet taken place |
| 2026-10-05 (repair pass) | Extracted the record's archived convergence-ladder results from its logs for S5 (no recomputation) | `tools/extract_frozen_convergence.py`, `data/frozen_convergence.json` | not reviewed by a human |
| 2026-10-05 (repair pass) | Ran a convergence ladder before the owner's scope rule arrived; archived only, labelled MANUSCRIPT REPRODUCIBILITY CHECK — NOT PART OF FROZEN SCIENTIFIC EVIDENCE, used by no claim | `tools/convergence_ladder.py`, `data/reproducibility/convergence_ladder.json` | owner ruled it out of scope for the manuscript |
| 2026-10-05 (repair pass) | Second numerical implementation for S6, framed as a reproducibility cross-check | `tools/second_path.py`, `data/second_path.json` | not reviewed by a human |
| 2026-10-05 (repair pass) | Redesigned Fig. 3 as normalised residuals; added the S5 convergence and S6 cross-check tables | `tools/gen_figures.py`, `data/tables/s5_convergence.md`, `data/tables/s6_second.md` | not reviewed by a human |
| 2026-10-05 (repair pass) | Architecture and semantic build firewalls with negative regression tests | `tools/firewalls.py`, `tools/test_firewalls.py`, `tools/check.py` (C10, C11) | not reviewed by a human |
| 2026-10-05 (repair pass) | Updated the trace map and findings for the repaired architecture | `tools/trace_items.json`, `BUILD_MANIFEST.json` | not reviewed by a human |
| 2026-10-05 (fix pass) | Applied the confirmed findings of the final adversarial conformance review (statement scopes, S3/S5/S6 wording, firewall hardening, this log) | `src/`, `tools/` | the findings themselves came from AI reviewers; not reviewed by a human |
| 2026-10-05 (repair pass) | Re-ran the record script behind the authoritative JSON and compared outputs | `tools/repro_record.py`, `data/repro_record.json` | not reviewed by a human |

## What the human author did

- Developed the underlying research program and the proof record (the record's own provenance applies).
- Fixed the manuscript blueprint (v1.1), the build prompt, the vocabulary firewall and the citation rules.
- Reviewed commit `ca0f4d5` and issued the conformance findings that the repair pass addresses, and the scope rule the fix pass enforces.
- Retains every scientific and editorial decision, including the final disclosure wording, the citation sweep, and whether to squash the branch history before publication.

## What no one has done yet

- External human peer review of the theorem.
- The literature sweep (all non-record citations are visible placeholders).
- A check of the target journal's AI policy against its official page.

## Git metadata

Both manuscript commits so far (`ca0f4d5`, `7d806e1`) record the AI session as Git author and committer; that identity is tool provenance set by the session, not manuscript authorship. Commit `ca0f4d5` additionally carries a `Co-Authored-By` trailer naming the AI system; from `7d806e1` onward no commit carries such a trailer, and a `Claude-Session` link is kept as tool provenance. Whether to re-author or squash the working history into a clean provenance-preserving commit before publication is the author's decision.
