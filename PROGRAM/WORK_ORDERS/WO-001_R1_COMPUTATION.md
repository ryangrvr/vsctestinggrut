# WO-001 — R1 computational package (for VS Code)

**Status: OPEN** · Issued 2026-10-06 by Claude Code · Stage 2.
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
