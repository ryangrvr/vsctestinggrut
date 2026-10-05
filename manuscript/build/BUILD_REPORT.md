# Build report

**Result: PASS**

## Failures

- none

## Record import

56 files verified byte-exact.

## Vocabulary firewall

Banned: GRUT, ontology, quotient, X1, P0, P1, V1, V2, V3, owner, ruling, charter, tier, gate

Added by this build: BRI, BRI0, BRI1, PF4Q, SCOUT, Candidate

Exceptions: none

Violations: 0

## Numeric-literal check

Allowlist:
- t_star = 0.5 (prompt allowlist)
- beta = 1 (prompt allowlist)
- protocol definition (prompt allowlist)
- integer N_B values 4, 8, 16, 32, 64, 128
- single-digit structural integers (exponents, orders, combinatorial factors)
- section, table, figure, lemma and equation numbers
- bibliographic entries inside the references block

Violations: 0

## Trace

66 marked statements; 66 trace items; quote failures: 0

## Architecture firewall (C10)

Supplement titles enforced: # S1. Theorem and notation sheet; # S2. Small-time consistency check; # S3. Class hierarchy and mechanism map; # S4. Reservoir-limit proof; # S5. Numerical methods and convergence; # S6. Second numerical code path and reproducibility

Displayed ladder enforced: $\mathcal{H} \subset \mathcal{E}_1 \subsetneq \mathcal{E}_2^{\pm} \subsetneq \mathcal{E}_{\mathrm{univ}}$

Violations: 0

## Semantic firewalls (C11)

Quantifier chain enforced verbatim and in order:
- There exists $\delta \in (0, 1]$
- for each fixed $t \in (0, \delta)$
- there is a finite integer $N_0(t)$
- for every bath size $N_B \geq N_0(t)$
- admit no common representation in the class $\mathcal{E}_2^{\pm}$
- The numbers $\delta$ and $N_0(t)$ are existential
- $N_0(t)$ is not claimed to be uniform in $t$

Also enforced: no numerical delta or N_0; no uniform threshold; t_star never inside (0, delta); reservoir limit never the harmonic class; effective-harmonic only as a cited, unclaimed connection. Negative unit tests: tools/test_firewalls.py.

Violations: 0

## Findings (record, blueprint, notation)

- **F1 BLUEPRINT.** Blueprint v1.1 is not present in either repository. Commit ca0f4d5 inferred S4/S6 contents and mis-assigned the supplements. After the owner's conformance review of ca0f4d5, the supplement architecture follows the frozen structure stated in that review: S1 theorem and notation; S2 small-time check; S3 proved class hierarchy and mechanism non-escapes; S4 reservoir-limit proof; S5 numerical methods and convergence; S6 second numerical code path and reproducibility. These titles and their order are enforced by make check (C10). Blueprint 'patch items' not restated in the prompt or the review remain unverifiable.
- **F2 RECORD-VS-PROMPT.** All four load-bearing formulas named in the prompt match the record: parent Hamiltonian (CAND §1, V1-1); E2± with G_t[q] != 0 and prefix consistency (B0 §R BRI-O2/O3, §R2 BRI-O9); c(t) = -Var(x0^2) t^7/(28 pi^3) + O(t^8), K = 3c (THM T1/T2, preflight log); C0(ta,tb) = <x0(ta)x0(tb)>_Gibbs (THM T4). The theorem quantifiers match THM §T4-R and the synthesis §2. No disagreement found.
- **F3 NOTATION.** The record uses C_k (Taylor coefficients of c), C_R, C(t*) and b_k (y1 coefficients), which collide with the covariance C0(ta,tb) fixed by the prompt and with the initial momentum b. The manuscript writes c_k, Lambda, Theta(t) and eta_k. Values and statements are unchanged.
- **F4 RECORD-INTERNAL.** BRI1_PUBLICATION_FIGURE_REPORT_03.md §9 states 'Relative drift (t=1.0, N_B 4->128): 1.748e-10'. The authoritative JSON gives 1.37e-7 for that quantity (the synthesis §4 agrees with the JSON). The manuscript prints the JSON-derived value.
- **F5 RECORD-INTERNAL.** The record names v3_r2_authoritative.py as the sole authoritative script, but the committed v3_r2_results.json has the output schema of extract_data.py (single reference resolution, no resolution ladder, no fit residuals). Re-running extract_data.py in this build environment reproduced the JSON: identical schema, 208 significant values within 3.7e-9 relative, round-off-level entries within 3e-17 absolute (not bitwise; different numpy build).
- **F6 RECORD-GAP.** No generator for the record's committed figure is in the record, so there was no existing figure generator to reuse. Figs. 1–3 are produced by manuscript/tools/gen_figures.py; Figs. 2 and 3 draw only on the authoritative JSON, and Fig. 1 is a data-free schematic drawn from the protocol definitions.
- **F7 RECORD-GAP.** Superseded by F10: the resolution ladder is reported in S5 from the record's archived logs (extracted by tools/extract_frozen_convergence.py), and the finest cell, absent from the archives, is reported as not archived.
- **F8 REFERENCES.** Only four references carry full bibliographic details in the record (Immer et al. 2023; Makri 1999; Makri 2024; Carcaterra & Akay 2016). Verification depth in the record: Immer primary-source extracts (no page numbers recorded); the other three search-level only. Kiefer et al. (arXiv:2505.15665) and Zweig et al. (arXiv:2505.15987) lack full details and remain CITATION NEEDED placeholders.
- **F9 CONSISTENCY-NOTE.** Non-evidentiary consistency note: the fixed-t limit K(t)/m2^{3/2} of N_B*gamma1 (first-order expansion, Lemma 3), with K(t) from this build's fresh small-time code, differs from the record's finite-N_B numerics by 1.3e-7 relative at t_star = 0.5 and 2.0e-8 at t = 0.25 — within the small-time code's own run-to-run spread. Reported as consistency, not as verification of the frozen output.
- **F10 RECORD-GAP.** The record's archived ladder logs are incomplete: authoritative.log holds 7 of 9 cells (gamma_1 to 7 significant figures; nx=480 dt=5e-4 logged without output, nx=480 dt=2.5e-4 absent) and v3_r2.log holds 8 of 9 (5 significant figures; nx=480 dt=2.5e-4 logged without output). S5 reports exactly the archived cells and marks the finest cell as not archived; nothing was recomputed for the manuscript.
- **F11 GOVERNANCE.** Commit ca0f4d5 carries an AI Co-Authored-By trailer. From the repair commit onward no AI co-author trailer is used; a Claude-Session link is kept as tool provenance. AI_USE_LOG.md records AI use. Squashing the working history before publication is left to the author.
- **F12 SCOPE.** Per the owner's scope rule for the repair pass (repair the manuscript from the frozen evidence; do not re-open numerical verification), a convergence ladder computed during this pass is archived only, under data/reproducibility/ with the label MANUSCRIPT REPRODUCIBILITY CHECK — NOT PART OF FROZEN SCIENTIFIC EVIDENCE, and is used by no theorem, disposition, fitted result, table, figure or claim. The second implementation is a manuscript-stage cross-check; it agrees with the frozen data (max relative difference 1.4e-7 in gamma_1, signs equal) and changes nothing.

## Citation placeholders

- [CITATION NEEDED: Caldeira–Leggett-type linear-response universality]
- [CITATION NEEDED: Mori–Zwanzig projection-operator formalism]
- [CITATION NEEDED: classical fluctuation–dissipation theorem]
- [CITATION NEEDED: generalized Langevin equation from a harmonic bath with linear coupling (Zwanzig; Caldeira–Leggett)]
- [CITATION NEEDED: generalized Langevin equations with non-Gaussian orthogonal forces, Kiefer et al., arXiv:2505.15665 — full bibliographic details to be verified]
- [CITATION NEEDED: identifiability of interventional stochastic differential equations, Zweig et al., arXiv:2505.15987 — full bibliographic details to be verified]
- [CITATION NEEDED: location-scale / conditional-transformation regression literature]
- [CITATION NEEDED: multivariate Lindeberg–Feller central limit theorem, standard probability text]

## S2 small-time check (computed by this build)

| t | ratio | method B | series |
|---|---|---|---|
| 0.1 | 0.972776 | 0.972776 | 0.972776 |
| 0.2 | 0.939232 | 0.939232 | 0.939232 |
| 0.25 | 0.920306 | 0.920306 | 0.920306 |
| 0.5 | 0.808518 | 0.808517 | 0.808500 |

## PDF

Manuscript pages: 29; S1 sheet pages: 9

