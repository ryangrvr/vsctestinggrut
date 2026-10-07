# WO-002 — BRI1 against coordinatewise monotone interfaces (T_mono): copula class modulo reflections

**Status: IN PROGRESS — executed by Claude Code (VS Code paused).**
- **Freeze:** owner ruling **G2-07** (2026-10-07). It supersedes v1 of this file, issued
  2026-10-06; v1 is in git history.
- **Stage:** 2, R1 exit-gate item (ii).

**Theory.** `PROGRAM/RESULTS/R1/R1_T_LADDER.md` §9.
- **M1 (exact quotient).** ε_R^(T_mono) = 0 if and only if all protocols' copulas lie in
  one coordinate-reflection orbit.
- **M2 (symmetry certificate).** A radially symmetric C₀ and a radially asymmetric C₁
  give ε_R > 0.
- **M3 (Gaussian tangent structure).** rank J = k, and C(k+2, 3) − k surviving
  leading-order third-order directions. M3 is a diagnostic only.

**Scope.**
- **Interface class.** Coordinatewise strictly monotone maps, increasing or decreasing,
  on the frozen observed grid τ = (π, 3π/2, 2π).
- **Laws.** Margins are continuous and atomless, with interval supports. BRI1's force
  marginals have everywhere-positive densities.

## Computation (`PROGRAM/RESULTS/WO-002/wo002_copula_channels.py`)

**Odd sector.**
- A_abc: the normal-score third-order tensor projected off span{T^(m)}, for P1 and P2.
- At formal leading order it is computed from the archived K tensor and the free Gibbs
  autocorrelations ρ at τ; K is also recomputed and checked against the archive.
- There are 7 off-diagonal components per protocol (k = 3).

**Even sector.**
- Normal-score correlation change modulo reflections, Δρ_ab, from the second-order
  covariance response C2.
- C2 is a new computation: the variational y₂ (Method A) and an ε² Richardson
  extrapolation (Method B).

**N_B scaling.** N_B·(cumulant-level copula coordinate), for N_B ∈ {4, 8, 16, 32, 64,
128}, from the finite-N_B nonlinear flow.

**Exact controls (each can fail).**
- A_aaa = 0.
- Marginal-only synthetic control: A = 0.
- Parity: Cov(x₀, y₁) = 0.
- Stationarity: E x₀(t)² = m₂.
- Gibbs identity: m₂ + m₄ = 1.
- Harmonic bath: K = 0 and C2 = 0.
- K reproduces the archived PF4Q values.

**Independent cross-check.** A separate implementation, written without reading this
script, must agree within the quadrature spread.

## Preregistered outcomes (G2-07; fixed before the numbers were read)

1. **Some leading-order surviving component is nonzero** beyond 10² × its quadrature
   spread → **escape at leading order** (M2 for the odd sector, M1 for the even
   sector). Grade: numerical evidence, not certified.
2. **All leading-order components are zero** → compute the exact copula radial asymmetry
   from finite-N_B dynamics (normal scores) **before any verdict**. This is not a kill.
3. **The copulas lie exactly in one reflection orbit** → this reciprocity branch is
   **KILLED** (→ GRAVEYARD, after external check).

**Theorem grade for BRI1 (§9 M5).** OPEN: a Cramér-condition Edgeworth expansion,
uniform in ε, in normal-score coordinates. Outcome 1 stays evidence-grade until it is
proved.

## Output

`PROGRAM/RESULTS/WO-002/`:
- the script;
- `wo002_results.json`;
- the generated `REPORT.md`;
- the cross-check JSON.

Each pushed result gets a line in `PROGRAM/CHECKS.md`.
