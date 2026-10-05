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

58 marked statements; 58 trace items; quote failures: 0

## Findings (record, blueprint, notation)

- **F1 BLUEPRINT-MISSING.** Blueprint v1.1 is not present in ryangrvr/vsctestinggrut or in any branch of ryangrvr/TestingGRUT. The binding constraints quoted in the build prompt were applied; section-level placement that only the full blueprint can settle is marked BLUEPRINT-UNVERIFIED (S4 contents: competitor-class proofs; S6 contents: methods, verification history, provenance). No record-vs-blueprint disagreement can be assessed until the blueprint is supplied.
- **F2 RECORD-VS-PROMPT.** All four load-bearing formulas named in the prompt match the record: parent Hamiltonian (CAND §1, V1-1); E2± with G_t[q] != 0 and prefix consistency (B0 §R BRI-O2/O3, §R2 BRI-O9); c(t) = -Var(x0^2) t^7/(28 pi^3) + O(t^8), K = 3c (THM T1/T2, preflight log); C0(ta,tb) = <x0(ta)x0(tb)>_Gibbs (THM T4). The theorem quantifiers match THM §T4-R and the synthesis §2. No disagreement found.
- **F3 NOTATION.** The record uses C_k (Taylor coefficients of c), C_R, C(t*) and b_k (y1 coefficients), which collide with the covariance C0(ta,tb) fixed by the prompt and with the initial momentum b. The manuscript writes c_k, Lambda, Theta(t) and eta_k. Values and statements are unchanged.
- **F4 RECORD-INTERNAL.** BRI1_PUBLICATION_FIGURE_REPORT_03.md §9 states 'Relative drift (t=1.0, N_B 4->128): 1.748e-10'. The authoritative JSON gives 1.37e-7 for that quantity (the synthesis §4 agrees with the JSON). The manuscript prints the JSON-derived value.
- **F5 RECORD-INTERNAL.** The record names v3_r2_authoritative.py as the sole authoritative script, but the committed v3_r2_results.json has the output schema of extract_data.py (single reference resolution, no resolution ladder, no fit residuals). Re-running extract_data.py in this build environment reproduced the JSON: identical schema, 208 significant values within 3.7e-9 relative, round-off-level entries within 3e-17 absolute (not bitwise; different numpy build).
- **F6 RECORD-GAP.** No generator for the record's v3_r2_figures.png is committed in the record, so there was no existing figure generator to reuse. Figures 1-3 are produced by manuscript/tools/gen_figures.py directly from the authoritative JSON (and, for the Fig. 3 overlay, this build's independent small-time computation).
- **F7 RECORD-GAP.** The resolution ladder (nx 120/240/480, dt 1e-3/5e-4/2.5e-4) is described in the record but is not in machine-readable output; the manuscript states this and prints no ladder numbers.
- **F8 REFERENCES.** Only four references carry full bibliographic details in the record (Immer et al. 2023; Makri 1999; Makri 2024; Carcaterra & Akay 2016). Verification depth in the record: Immer primary-source extracts (no page numbers recorded); the other three search-level only. Kiefer et al. (arXiv:2505.15665) and Zweig et al. (arXiv:2505.15987) lack full details and remain CITATION NEEDED placeholders.
- **F9 INDEPENDENT-CHECK.** The leading-order prediction N_B*gamma1 -> K(t)/m2^{3/2}, computed with this build's fresh small-time code, agrees with the record's finite-N_B numerics to 1.3e-7 relative at t_star = 0.5 and 2.0e-8 at t = 0.25.

## Citation placeholders

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

Manuscript pages: 23; S1 sheet pages: 9

