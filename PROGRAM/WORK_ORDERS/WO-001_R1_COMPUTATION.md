# WO-001 — R1 computational package (for VS Code)

**Status: IN PROGRESS — executed by Claude Code from 2026-10-07 (VS Code paused).** C1 redo ACCEPTED (Review 2). C2 done, with the Amendment A process fixes (`RESULTS/WO-001/C2_REPORT.md`). C3 next. External checks: `PROGRAM/CHECKS.md`. · Issued 2026-10-06 by Claude Code · Stage 2.
**Reopened after review (2026-10-06):** C1 = REVIEWED — REVISE. The witness scaling was
inserted analytically and contradicts BRI1. See `PROGRAM/REVIEW.md`. C2–C4 are not run.

**Definitions.** The definition is now issued: `PROGRAM/RESULTS/R1/R1_DEFINITION.md`
(v1). It fixes **d_op = W₃ between per-time-standardized multi-time laws**. Where it
differs from the provisional spec below, it governs.

## Provisional spec

- **Process law P_a.** The joint law of the environment force path
  (F(t₁), …, F(t_k)) on a fixed time grid, under intervention protocol a (a prescribed
  system path q_a). Estimate it from samples. It is the multi-time joint law, never a
  single-time marginal.
- **Class T = E₂± (from BRI1).** Pathwise maps t_a: ξ ↦ M_a + G_a·ξ, where:
  - M_a(t) is deterministic;
  - G_a(t) ∈ ℝ∖{0} is deterministic;
  - Law ξ = P★ is shared across all protocols.

  Source: `backreaction_identifiability_0/BRI0_CHARTER.md` §5 on branch
  `bri1-manuscript` @ `92dc6bb`. E₂ is defined there with G > 0; E₂± allows
  G ∈ ℝ∖{0} (same file, line 9).
- **ε_R^(T) = inf over (P★, {t_a}) of max_a d_op(P_a, (t_a)#P★).**
  - **Superseded (erratum, Claude Code).** The earlier suggested distance pair
    (sliced W₁, cumulant distance) and the claim that skewness spread "lower-bounds the
    distance" were written before any d_op was fixed. The claim is false for TV, W₁
    and W₂ (R1_DEFINITION Prop. 3).
  - **Use instead:** d_op = W₃∘std (sensitivity check: W₄∘std).
  - **Witness and bound (R1_DEFINITION Prop. 2a, 2b):**
    - ε_R ≥ max | |γ_a| − |γ_b| | / (2·L_ab), with L_ab = m_a² + m_a·m_b + m_b² and
      m = ‖standardized force‖₃;
    - ε_R ≥ max | Δ|ρ| | / 4 for cross-time correlations.
  - Report the **skewness witness** |Δ|γ|| itself, plus the data-computed bound.

## Tasks

- **C1 — BRI1 reproduction under ε_R.**
  - Use BRI1's frozen finite Duffing bath (the record and code on `bri1-manuscript`).
  - **Redo from dynamics (owner instruction).** For each N_B in {4, …, 128}, integrate
    the bath with coupling **ε = N_B^(−1/2)**. Compute κ₂, κ₃ and γ₁ of the force
    directly from the ensemble. Report **N_B·γ₁ and √N_B·γ₁ side by side.**
  - **Nothing about the N_B scaling may be inserted analytically.** Any check must be
    able to fail.
  - Reuse the V3-R2 machinery
    (`publication_verification/v3_r2/v3_r2_authoritative.py`) for the single-time
    case.
  - Expected per BRI1: N_B·γ₁ is approximately constant, with small finite-N
    corrections. Report whatever is found.
  - Keep the first run, labelled RETRACTED (the scaling was imposed analytically),
    in the result file. Don't delete it.
  - Where quantities are comparable, the outputs must reproduce BRI1's frozen archived
    numbers. This is reproduction, not new science. Do **not** restate BRI1's theorem;
    its quantifiers belong to the record.
- **C2 — exogenous controls (must give ε_R = 0).**
  - (i) Colored Gaussian (Ornstein–Uhlenbeck) noise.
  - (ii) A non-Gaussian non-Markovian noise.
  - In both, the protocol dependence enters only through M_a and G_a (that is,
    through T).
  - **Exact control:** for one case, build the protocol dependence analytically inside
    T. The optimizer must return 0 to machine precision when given the exact law, and
    a value consistent with 0 at finite sample size.
- **C3 — nonlinear-interface controls (must give ε_R > 0).**
  - F_q = h_q(ξ), where h_q is non-affine and depends on the protocol.
  - Show that ε_R grows with the nonlinearity strength, and is 0 at strength 0.
- **C4 — finite-data identifiability simulations.**
  - Report bias and variance of the ε_R estimator against sample size and against the
    number of protocols.
  - Report detection curves: the smallest ε_R distinguishable from 0 at fixed
    error rates.

## Output

- Location: `PROGRAM/RESULTS/WO-001/`.
- Committed code, machine-readable JSON, and tables generated from the JSON.
- One short `REPORT.md` with numbers only, plus the exact controls' pass/fail.
- **No proofs, theorem statements, or comparator verdicts.** If one gets written
  anyway, mark it `DRAFT — pending Claude Code review`.
- When done, set this file's status to `DONE — PENDING REVIEW` and push.

## Amendment A (Claude Code, 2026-10-06, after Review 2)

**C2 cleanup (required before C2 can be ACCEPTED).**
- Commit `PROGRAM/RESULTS/WO-001/c2_controls_results.json` and a `C2_REPORT.md`
  (numbers only).
- Make the docstring and the run agree on the noise-floor sample size (2×10⁶ vs
  2×20,000).
- Replace "false positive" for C2-F with: "correct nonzero value under E₂±. E₂± is not
  closed under calibrated linear filters, and C2-F is one orbit of path-level linear
  interfaces (ε_R = 0 under T_lin)."
- Update this file's status line and `STATE.md`.

**C3 conditions.** The classes are defined in `PROGRAM/RESULTS/R1/R1_T_LADDER.md`.
- **Two classes, reported separately.**
  - **E₂±** (primary; this WO's class).
  - **T_lin on the observed grid** (secondary). Its witness is the Mardia witness, ladder
    Prop. B2: ε_R^lin ≥ |Δ√β₁|/(2Λ).
  - Do not report T_mono: it absorbs every per-time h_q by construction (Prop. D1).
- **Report for each case:**
  - the exact single-time d_q from the sorted coupling;
  - the two-protocol bracket ½d ≤ ε_R ≤ d;
  - the witness lower bounds.
- **Mandatory symmetry test (can fail; it tests Theorem C's mechanism).** Use a driver ξ
  whose sample is exactly symmetric: stack ξ and −ξ.
  - **(i) Odd interface,** h_q(ξ) = tanh(α_q ξ)/α_q. Every odd-moment witness (skewness,
    Mardia) must be 0 to rounding at every α_q. Report d_q anyway: it may be > 0 through
    even-order shape.
  - **(ii) Even-part interface,** h_q(ξ) = ξ + α_q(ξ² − 1). The skewness and Mardia
    witnesses must be > 0, grow with α_q, and equal 0 at α_q = 0.
- The class definitions are now issued, so they are not DRAFT. Any interpretive sentence
  beyond numbers is DRAFT.

**Next after C3:** C4, then `WO-002_BRI1_MULTITIME_TMONO.md`.
