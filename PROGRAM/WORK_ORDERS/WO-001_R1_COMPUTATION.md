# WO-001 — R1 computational package (for VS Code)

**Status: OPEN** · Issued 2026-10-06 by Claude Code · Stage 2.

**Definitions.** The definition of ε_R is owned by Claude Code and will be issued as
`PROGRAM/RESULTS/R1/R1_DEFINITION.md`. Until it exists, use the **provisional spec**
below. If the final definition differs, results get re-run, not re-interpreted.

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
  - Report results for **two** declared choices of d_op, plus the sensitivity between
    them. Suggested pair: sliced Wasserstein-1 on the k-dimensional path vector, and a
    standardized-cumulant distance.
  - Computable lower bound (use it as the primary witness): any positive affine map
    leaves per-time standardized cumulants of order ≥ 3 unchanged, and a negative map
    only flips the odd ones. So the spread across protocols of per-time |standardized
    skewness| lower-bounds the distance to E₂±. This is BRI1's own witness.

## Tasks

- **C1 — BRI1 reproduction under ε_R.**
  - Use BRI1's frozen finite Duffing bath (the record and code on `bri1-manuscript`).
  - Compute the skewness-witness lower bound on ε_R along an N_B ladder and show the
    ∝ 1/N_B scaling.
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
