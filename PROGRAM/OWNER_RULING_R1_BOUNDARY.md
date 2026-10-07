# OWNER RULING — R1 BOUNDARY (G2-08) · 2026-10-07

Recorded verbatim. Committed **before** the WO-002 result was read or interpreted, as the
ruling requires. Log entry: `PROGRAM/OWNER_RULINGS.md` → G2-08.

---

> I read the WO-002 work order line by line, and it already implements what ChatGPT and I worked out:
>
> * The odd channel is exactly right. The formula for A_abc subtracts, from each third cumulant, precisely the part a per-time monotone map can produce — it matches the Stein-identity derivation term for term, including the repeated-index entries. Its built-in "marginal-only control" (which must return zero) is exactly the test that proves this. So a nonzero A_abc is the genuine multi-time, copula-level signal.
> * The even channel is valid at leading order. It uses ordinary (Pearson) correlation, and ChatGPT was right that the exact theorem needs normal-score correlation. But for BRI1's force at leading order the two agree: the marginal distortion needed to explain the force's skewness is of order 1/N_B, and its effect on correlation is second order in that, so the difference is O(1/N_B²), below the order being computed.
> * The null case is already guarded. The work order says a leading-order null is reported as LEADING-ORDER NULL, not "absorbed."
>
> What our discussion adds is interpretation, not computation: what happens after a null, the declared top of R1, and the two-tier T. That only needs to be fixed before anyone acts on the result. Since you're happy to give it to him now, it can go in as a non-blocking commit; otherwise hand it over the moment the run finishes, before he reviews WO-002.
>
> FOR CLAUDE CODE — non-blocking; does not change the WO-002 computation
> Commit the following as `PROGRAM/OWNER_RULING_R1_BOUNDARY.md` (dated), and update `STATE.md` to close "owner decision pending: freeze T." Do this before reviewing or interpreting the WO-002 result.
>
> 1. R1 logic: operational reciprocity requires both a common-carrier certificate and failure of T-separability. Verdicts: carrier PASS + different classes → R1-PASS; carrier PASS + same class → R1-NULL; carrier UNRESOLVED + different → NO RECIPROCITY VERDICT; carrier FAIL + different → MODE SELECTION (not reciprocity); carrier FAIL or UNRESOLVED + same → R1-NULL.
> 2. BRI1 common-carrier certificate (record explicitly): same bath degrees of freedom, same bath Hamiltonian class, same equilibrium initial ensemble; protocols change only the forcing.
> 3. Two-tier T (owner freeze):
>    * Tier 1 — calibrated-readout reciprocity: T = GL(k) on the observed record, common carrier (arbitrary latent dimension; no protocol-dependent mode selection). BRI1: R1-PASS (Theorem C + certificate). Banked regardless of WO-002.
>    * Tier 2 — readout-robust reciprocity: T = T_mono, coordinatewise strictly monotone maps; residual group = coordinate reflections only (no permutations across time coordinates). This is the declared top of R1; no larger class will be considered.
> 4. Stopping rule: if BRI1's protocols lie in one copula reflection orbit at the T_mono level, the reciprocity spine ends as a portable observable, and Tier 1 is banked as a calibrated-readout result. No rescue class.
> 5. Post-null step (preregistered): a LEADING-ORDER NULL from WO-002 triggers an exact finite-N_B test of the copula's radial asymmetry (normal scores) before any verdict.
> 6. Finite-witness asymmetry: for T_mono, an escape on one finite grid is a process-level escape; a null on one grid is a null for that projection only, unless the projection was declared the terminal scope in advance.
> 7. Two notes for the WO-002 review:
>    * The even channel uses Pearson correlation; at leading order in 1/N_B this equals the normal-score correlation change (difference O(N_B⁻²)). Any exact copula test must use normal scores.
>    * Reflections can't absorb a small Δρ_ab unless ρ_ab is itself O(1/N_B); check that the base correlations on the frozen grid aren't near zero.
> 8. Stage 3 limits (for the record): at most three 𝒦 cards; the success criterion is freedom reduction relative to baseline spaces frozen before any card, plus positive compression, plus a measurable relation. Cross-sector means parameter transfer.
> 9. Repository: `grut2` is not merged into `main` until the R1 terminal.
>
> Short version: let the run finish undisturbed; this ruling just has to land before anyone reads the result as a verdict.

---

## Implementation notes (Claude Code)

**Item 2 — BRI1 common-carrier certificate, recorded.** From the BRI1 record at
`92dc6bb`, files `BRI1_PF4Q.md` §1 and `BRI1_ANALYTIC_ESCAPE_THEOREM.md`:
- **Same bath degrees of freedom.** N_B clamped oscillators (x_j, p_j), for every
  protocol.
- **Same bath Hamiltonian class.** H₀ = p²/2 + x²/2 + x⁴/4 per oscillator, with the
  coupling −ε·q(t)·x_j.
- **Same equilibrium initial ensemble.** The Gibbs law ∝ e^(−H₀), protocol-independent.
- **Only the forcing changes.** Protocols differ only in the prescribed system path q:
  P0 has q ≡ 0, and P1 and P2 are the frozen smooth ramps.
- **One readout map.** The record is the force F = N_B^(−1/2)·Σ_j x_j(t) on the same grid
  for all protocols, so h is common.

**Status: carrier PASS** (by construction of the model).

**Item 3 / RULES rule 8.**
- Tier 1 (BRI1: R1-PASS under T = GL(k) plus common carrier) is banked by this ruling.
- Under rule 8, adopted the same day, the `SCOREBOARD.md` entry is added only once the
  `CHECKS.md` line of the commit carrying the common-carrier version of Theorem C shows
  an external check with no open issue. This is flagged to the owner; it is not a
  departure from the ruling's substance.

**Item 7, second note.** The base correlations ρ_ab on τ = (π, 3π/2, 2π) are reported in
the WO-002 REPORT and checked against zero at review.

**Items 1, 3–6** are mirrored in `PROGRAM/RESULTS/R1/R1_T_LADDER.md` §0, and **item 8** in
`STATE.md` (Stage 3 definition).
