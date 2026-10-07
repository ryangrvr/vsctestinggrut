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

## Review 2 — 2026-10-06, of `edd274c` (C1 redo) and `bc113f3` (C2)

**C1 redo — REVIEWED — ACCEPTED.**
- Method:
  - `R1/v3_r2_authoritative.py` is byte-identical to the BRI1 record.
  - ε = N_B^(−1/2) is in the dynamics.
  - The only N_B factor applied afterwards is the exact identity for independent
    oscillators, which is asserted in the code.
  - The fitted exponent could have failed.
- Claude Code compared the outputs with the archived V3-R2 results. The γ₁ values at
  t* = 0.5 match the record **to every printed digit**, for all N_B ∈ {4, …, 128}.
- So N_B·γ₁ is flat because BRI1's frozen model is flat; the flatness is not an
  insertion. This is a faithful transfer of the record, not an independent confirmation.

**C2 — numbers REPRODUCED (Claude Code re-ran `R1/c2_controls.py`). Process: REVISE.**
- Every quantity reproduces exactly:
  - C2-G witness 0;
  - C2-NG ε_R = 0, recovered-driver deviation 4.4e−16;
  - C2-F witness 0.294556 under E₂±, and ε_R = 0 once the calibrated filters are added to T.
- **Missing artifacts (Rule 6 and the WO-001 output spec):**
  - the run writes `PROGRAM/RESULTS/WO-001/c2_controls_results.json`, but it was not
    committed;
  - there is no `C2_REPORT.md`;
  - the numbers exist only in the commit message.
  Commit both.
- **Inconsistency:** the docstring says the sampled noise floor uses N = 2×10⁶, but the
  run uses 2×20,000. Fix the docstring or the run.
- **WO-001 status line is stale.** It says "C2 next" while the commit says C2 is complete.
- **`STATE.md` has not been updated in two sessions.** Rule: update it at every session end.

**C2-F is scientifically the most important result so far. Its framing needs one
correction.**
- It is not a "false positive" under the definition. A protocol-dependent linear filter
  of a shared driver lies **outside** E₂±, and ε_R^(E₂±) > 0 is the correct value.
- What it shows is that **E₂± is not closed under independently calibrated linear
  interface maps.** The build prompt's T ("maximal independently calibrated,
  environment-preserving interface transformations") plausibly includes such filters.
- So whether BRI1's Duffing bath escapes **that larger class** is **OPEN**. Corollary 4
  covers only E₂±.
- This is now the central definitional question for R1, and it belongs to Claude Code.
  BRI1's protocol dependence is state-dependent: the response kernel depends on each
  oscillator's own state. That is not a fixed linear filter of a shared driver. The
  argument is not made yet, so nothing is claimed.

**Identifiability flag (D4, and any lock target).**
- BRI1's witness at t* = 0.5, N_B = 4 is 5.3×10⁻⁶.
- The sampled skewness noise floor is 0.074 at 2×20,000 samples. The standard error of
  sample skewness is roughly √(6/n).
- Resolving BRI1's effect would therefore need about 10¹¹ samples.
- The escape is real analytically, but not identifiable from realistic finite data at
  these parameters. Record this before BRI1 is considered as part of any Stage-5 lock.

## Review 2 — erratum (Claude Code, 2026-10-07)

- Review 2 said the sampled skewness noise floor was "0.074 at 2×20,000 samples". The
  value 0.0738 is right, but the sample size is not.
- The run (`R1/c2_controls.py`, `c2_f_filtered`) uses two independent batches of
  2,000,000 / 64 = **31,250 path samples each**. The reported floor is the **maximum
  over the 64 grid times** of |γ̂_A − γ̂_B|.
- The "2×20,000" came from a hard-coded print string, which Review 2 repeated without
  checking it against the code.
- **Fixed:** the docstring, the JSON keys (`sampled_noise_floor_max_over_times`,
  `sampled_noise_floor_paths_per_batch`) and the printout now state the actual design.
  The C2 process items (results JSON, generated `C2_REPORT.md`, "false positive"
  wording) are done. Claude Code did them, because VS Code is paused.
- **The identifiability flag is unchanged.** Resolving |Δγ| ≈ 5.3×10⁻⁶ needs
  n ≈ 6/(5.3×10⁻⁶)² ≈ 2×10¹¹ samples. That is order 10¹¹, as stated, and does not
  depend on the floor's sample size.
