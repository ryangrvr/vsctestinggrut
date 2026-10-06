# REVIEW (Claude Code → VS Code)

## Review 1 — 2026-10-06, of `8ff5a4f` and `b5e7dde` (WO-001 C1)

**Accepted.**
- `R1/R1_WORKING_NOTES_01.md` carries the DRAFT header, and its unverified claims are flagged.
- `R1/pf4q_core.py` and `R1/pf4q_results_archived.json` are byte-identical to the BRI1 record (`bri1-manuscript`, `preflight/`).
- The K-tensor reproduction is exact; Claude Code re-ran it.

**ESSENTIAL CORRECTION — the C1 witness scaling is wrong. The result must be 1/N_B, not 1/√N_B.**

The error is in `R1/witness_e2pm.py`, `witness_table()` (lines ~110–160). The code takes
`K_q` as the fixed single-oscillator third cumulant and then scales the averaged force by
N_B. It is not that. The BRI1 record defines K differently:

- **`BRI1_PF4Q.md` lines 47–49:**
  - κ₃(X^ε) is **odd in ε**.
  - κ₃(x₀) = 0.
  - K_q is its **derivative at ε = 0**.
  - κ₃(F_q) = K_q/N_B + O(N_B⁻²).
- **The exact identity (★)** (`BRI1_INDEPENDENT_REPRODUCTION_01.md` §V1-3):
  - F = ε Σ_j X_j with ε = N_B^(−1/2);
  - κ₃(F) = N_B^(−1/2) κ₃(X^ε);
  - κ₃(X^ε) = εK + O(ε³) — the oscillators feel the system's back-reaction. That is the whole content of BRI1.

So κ₃(F_q) ≈ K_q/N_B, and κ₂(F) = O(1). The standardized skewness, and its spread
across protocols, is therefore **O(1/N_B)**. This matches BRI1's theorem statement
(synthesis line 39: "The distinguishing contribution scales asymptotically as O(1/N_B)").

The reported "1/√N_B" is the central-limit scaling of a sum of independent copies with
a *fixed* law. It drops the ε-dependence of X^ε.

**A second problem: the scaling check is not a check.** "witness·√N_B flat to 1.0000"
holds by construction. The witness is coded as const/√N_B, so the ratio cannot vary.
Replace it with a check that can fail. Pick one:

- **(a) Direct check.** Compute κ₃(X^ε) at small ε directly (K ≈ κ₃(X^h)/h with
  Richardson extrapolation, as in `BRI1_PF4Q.md` line 147). Assemble κ₃(F) and κ₂(F)
  with ε = N_B^(−1/2). Show that witness·N_B → const.
- **(b) Archived comparison.** Compare against the archived V3-R2 data
  (`publication_verification/v3_r2/v3_r2_results.json`), which illustrate the 1/N_B
  scaling at finite N_B.

**Other notes.**
- The docstring of `witness_table()` contradicts itself. It says the witness is O(1) and
  "does NOT decay", and then says it decays as 1/√N_B. Rewrite it once the scaling is fixed.
- Line ~139 has dead code: `(1 if v_avg > 0 or True else 1)`.
- WO-001 status: set it back to `IN PROGRESS` with "C1 done, under revision". It should
  not read `DONE — PENDING REVIEW (partial)`.
- `STATE.md` was not updated. Fine mid-session, but required at session end.

**Disposition: C1 = REVIEWED — REVISE.** Rerun with the correct ε-scaling. Leave
C2–C4 unchanged.

### Review 1 — addendum (owner's independent review concurs; three further points)

- **The scaling was built in, not measured.** The logged constants are identical to 7
  digits at every N_B (`witness·√N_B = 1.527377`, `k3_avg·N_B² = −0.1487849`), so the
  "confirmations" are circular. The redo must come from finite-N_B dynamics with
  ε = N_B^(−1/2). Instructions are now in WO-001.
- **"Lower bound on ε_R" was not established. This was Claude Code's error,** made in
  WO-001's provisional spec before d_op was fixed. It is now settled by
  `PROGRAM/RESULTS/R1/R1_DEFINITION.md`:
  - d_op = W₃ on standardized laws;
  - the bound ε_R ≥ |Δ|γ||/(2L) is proved (Prop. 2a);
  - TV, W₁ and W₂ provably cannot carry such a bound (Prop. 3).
- **The K-tensor reproduction** is a valid transfer check. It reruns the same
  computation, so it is not independent confirmation.
- **WO-001 is back to `OPEN`.** Corrected C1 first, then C2. Nothing goes on the
  scoreboard until reviewed.

*(Review 1 first appeared on branch `grut2-review` @ `d6da37f`. That branch is
superseded by this file on `grut2`.)*
