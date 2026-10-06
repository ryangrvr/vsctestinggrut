# WO-002 — BRI1 against per-time nonlinear interfaces: multi-time leading-order channels (for VS Code)

**Status: OPEN** · Issued 2026-10-06 by Claude Code · Stage 2 · Priority: after WO-001 C3.

**Why.** `PROGRAM/RESULTS/R1/R1_T_LADDER.md`:
- BRI1's escape survives every linear interface class (Theorem C).
- It is absorbed at a single time by per-time nonlinear (monotone) interfaces, T_mono
  (Prop. D1).
- Whether it escapes T_mono across several times is OPEN. At leading order in 1/N_B the
  answer is decided by two numbers per index set (Prop. D4). This WO computes them. It
  is a computation, not a theorem: the D4 formulas are formal, and their proof is
  Claude Code's.

**Preregistered reading (fixed before any number is computed).**
- **Odd channel.** On the frozen grid τ = (π, 3π/2, 2π), BRI1 escapes T_mono at leading
  order if, for P1 or P2, some A_abc with (a, b, c) not all equal is nonzero beyond its
  quadrature spread by a factor ≥ 10².
- **Even channel.** Likewise if some Δρ_ab (a ≠ b) is nonzero beyond its spread by a
  factor ≥ 10².
- **No escape.** If every A and Δρ is consistent with 0, the leading order does not
  decide, and the result is reported as LEADING-ORDER NULL. It is **not** reported as
  "absorbed".
- **Grade.** The archived K values are graded "strong numerical evidence — NOT
  CERTIFIED". Anything derived from them inherits that grade.

## Inputs

- **Code.** `R1/pf4q_core.py`, which is byte-identical to the BRI1 record: protocols
  P1/P2, Method A (variational + Gauss–Hermite) and Method B (nonlinear at small ε,
  trapezoid).
- **Archived K tensor.** `R1/pf4q_results_archived.json`: 10 components each for P1 and
  P2. Use the columns K_A06, K_A08, K_B08 and K_B12; their spread is the quadrature
  error. GH192 is a cross-check only.
- **Model.** H₀ = p²/2 + x²/2 + x⁴/4; Gibbs ρ ∝ e^{−H₀}; m₂ = E x₀².

## Tasks

**T1 — Free quantities (P0).**
- Compute m₂ and ρ_ab = E[x₀(t_a)x₀(t_b)]/m₂ for a, b ∈ τ.
- Use Method A and Method B quadratures, and report both plus the spread.
- **Exact check (can fail):** ρ_aa = 1, and E x₀(t)² = m₂ at every t in τ, by
  stationarity.

**T2 — Odd channel.**
- With K̃ = K/m₂^(3/2), compute

  A_abc = K̃_abc − (1/3)·[K̃_aaa·ρ_ab·ρ_ac + K̃_bbb·ρ_ba·ρ_bc + K̃_ccc·ρ_ca·ρ_cb]

  for all 10 components, for P1 and P2, from each archived column.
- **Exact checks (both can fail):**
  - A_aaa = 0 to rounding.
  - **Marginal-only control.** Draw a random correlation matrix ρ and random c_m. Build
    K̃_abc = 2·[c_a·ρ_ab·ρ_ac + c_b·ρ_ba·ρ_bc + c_c·ρ_ca·ρ_cb]; note this gives
    K̃_mmm = 6c_m. Your A code must return 0 to rounding for every component.

**T3 — Even channel (new computation).**
- Compute the second-order covariance coefficient C2, where
  Cov X^ε = Cov x₀ + ε²·C2 + O(ε⁴):

  C2_ab = Cov(y₁(t_a), y₁(t_b)) + ½·[Cov(x₀(t_a), y₂(t_b)) + Cov(y₂(t_a), x₀(t_b))].

- **Method A (extend the variational system).** Solve
  ÿ₂ + (1 + 3x₀²)·y₂ = −6·x₀·y₁², with y₂(0) = ẏ₂(0) = 0.
- **Method B.** Compute C2 ≈ (Cov X^ε − Cov X⁰)/ε² for at least two values of ε, and
  check ε² convergence.
- Then compute Δρ_ab = [C2_ab − ½·ρ_ab·(C2_aa + C2_bb)]/m₂ for P1 and P2.
- **Exact checks (can fail):**
  - The first-order term Cov(x₀, y₁) = 0 to rounding (parity).
  - Method A and Method B agree within their spreads.
  - **Harmonic control.** Drop the x⁴ term from H₀ and the x³ term from the dynamics.
    Then C2 ≡ 0 and K ≡ 0 to rounding.

## Output

- **Location:** `PROGRAM/RESULTS/WO-002/`.
- **Contents:** code, JSON, and one `REPORT.md` with numbers only:
  - every A_abc and Δρ_ab with its spread, per protocol;
  - the pass/fail of every exact check;
  - the preregistered reading applied mechanically (ESCAPE-ODD / ESCAPE-EVEN /
    LEADING-ORDER NULL, per protocol).
- **No theorem statements.** If one gets written anyway, mark it
  `DRAFT — pending Claude Code review`.
- When done, set this file's status to `DONE — PENDING REVIEW`, update `STATE.md`, and
  push.
