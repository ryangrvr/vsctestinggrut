# WO-001 C1 REDO — REPORT (numbers only; generated from c1_redo_results.json)

**Status:** C1 redone from finite-N_B dynamics. Everything below is computed; nothing
about the N_B scaling is inserted analytically. The RETRACTED first run
(`c1_witness.json`, git history at `b5e7dde`) is kept labelled.

## Setup

- Frozen Duffing bath, V3-R2 machinery (`v3_r2_authoritative.py`, byte-identical to the
  B1 record). Coupling **ε = N_B^(−1/2)** enters the dynamics; κ₂, κ₃, γ₁ = κ₃/κ₂^(3/2)
  of the force are measured from the evolved ensemble.
- Grid: nx=240, dt=0.0005 (reference run); nx=120 cross-check.
- Times: t* = 0.5, 0.25, 0.75, 1.0; N_B ladder: 4, 8, 16, 32, 64, 128.

## Results at t* = 0.5 (protocol P1)

| N_B | γ₁ | N_B·γ₁ | √N_B·γ₁ |
|-----|-----|--------|---------|
| 4   | −5.338286e−06 | −2.135314e−05 | −1.067657e−05 |
| 8   | −2.669143e−06 | −2.135314e−05 | −7.549477e−06 |
| 16  | −1.334572e−06 | −2.135314e−05 | −5.338286e−06 |
| 32  | −6.672858e−07 | −2.135314e−05 | −3.774738e−06 |
| 64  | −3.336429e−07 | −2.135314e−05 | −2.669143e−06 |
| 128 | −1.668214e−07 | −2.135314e−05 | −1.887369e−06 |

**Scaling exponent (global fit): 1.000000; local exponents all 1.0.**
**N_B·γ₁ relative spread: 1.7e−10.**

## The other times

| t* | N_B·γ₁ | rel spread | exponent |
|-----|--------|-----------|----------|
| 0.25 | −1.898867e−07 | 1.8e−08 | 1.000000 |
| 0.75 | −3.066966e−04 | 7.1e−09 | 1.000000 |
| 1.00 | −1.856763e−03 | 1.4e−07 | 1.000000 |

## Cross-check (nx=120)

N_B·γ₁ at t*=0.5: identical to 1e−14; exponent 1.0000000000027.

## Exact controls

- **Odd-in-ε control** (κ₃(+ε) vs κ₃(−ε), N_B=4 and 16): sums ≈ −5.6e−17 / −7.8e−17
  (machine zero); ratios −0.99999999998 / −0.99999999997. ✓
- **Gibbs moment identity**: residual 6.661e−16. ✓

## Verdict (computed, not asserted)

- **N_B·γ₁ is constant across the ladder** (rel spread ≤ 1.4e−07 at all four times).
- **√N_B·γ₁ is not constant** (varies by ×5.7 across the ladder).
- Both columns were allowed to fail; only the N_B column passes.
- **This matches BRI1's theorem statement** (γ₁ = O(1/N_B)) and **contradicts the
  RETRACTED run** (which reported the 1/√N_B constant by construction).

## RETRACTED (first run, kept per instructions)

The first run (`c1_witness.json`, code at git `b5e7dde`) inserted the scaling
analytically: its "N_B·γ₁" and "√N_B·γ₁" were computed from analytic κ₃ scaling, not from
dynamics, and its reported "1/√N_B" result was a construction artifact. **RETRACTED.**
The K-tensor transfer check inside it (K vs archived pf4q_results.json, rel ~1e−15)
remains valid and is unaffected.
