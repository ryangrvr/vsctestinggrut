# Stage-3 evaluation kit (charter §19.3)

**Authority:** owner ruling G2-12 item 3: the kit was authorized after the CR-1 re-freeze
(`0b414e6`), with T_kit = one session and priority (a)–(d). Unfinished items take
hostile defaults set by a charter repair, and there is no extension. Those defaults are
**CR-3** in charter Appendix H. CR-2 is reserved for the loophole queue,
`charter_workings/CR2_QUEUE.md`.

**What this is not:** this is not Card 1 and not a 𝒦 candidate. Nothing here states,
drafts, scores or optimizes a law. Test fixtures are abstract pipelines over clause tokens
and carry no physics.

**Status:** built in one session by Claude Code.

**External check (owner ruling G2-13):**
- The SEL values were reproduced independently with non-SD0 code.
- The kit tests pass.
- An NR-4 harness defect was found in the pre-fix harness and fixed (see below).
- **Still pending external check:** the price coder against Appendix B, the HB controls, and the G2-13 NR-4 fix together with its post-review hardening.

Charter §19.3 requires the kit's outputs to be checked externally before the first draft is logged. Every card cites the kit SHA.

## Contents

| File | Item | What it does |
|---|---|---|
| `l0_code.py` | (a) | The Appendix B alphabet (64 tokens, 6 bits each), Elias-δ ℓ(n), literal pricing at p, L_stmt, and a prenex-NNF normalizer. Price items IP-4, IP-5 (CR-1 exact values), IP-6, IP-12 and IP-13; the §4.3–§4.4 verdicts; and the §2.5 coupling credit b_J with the family cap. |
| `nr4_ablation.py` | (b) | NR-4 harness. Runs auditor-built variants K, K_∅, K_𝒮 and single-clause deletions. ρ_abl = 2^(−p★)·abs(W) per lock observable. The decoupled-corner set (G2-12 item 5) is computed once under K and shared by every variant and the responsibility map (G2-13 item 1); the excluded fraction is reported. Includes the lock-fiber clause. |
| `hb_controls.py` | (c), partial | Exact zeros of ε^{T_lin} for affine-entry records (HB-3 and HB-4 form). The static-map control on HB-4: a protocol-dependent static tail gives an exact nonzero γ₁² witness, and removing the known tail (PC-7(b)) restores the exact zero. |
| `sel222.py` | (d), SEL only | Reproduces the §2.4 values with the SD0 enumeration code (`f0_sd0_recon_222.py`, exact rational LP). Writes `results/sel222.json`. |
| `test_l0_code.py`, `test_kit.py` | (a)–(c) | Validation tests. Run `python3 test_l0_code.py` and `python3 test_kit.py`. |

## Validation list (§19.3) — status at the end of the kit session

| Item | Status |
|---|---|
| SEL 2961 / 1721 / 1232 / 8, the 240 gap, 2721 | **Reproduced** (`results/sel222.json`) |
| PR-forcing | **Reproduced as:** the strongly contextual exact-support-realizable set equals the 8 PR boxes. If the lemma means more than this, the remainder falls under CR-3 KD-1. |
| Price coder on Appendix B | **Built and tested** (`test_l0_code.py`, 10 tests) |
| NR-4 ablation harness | **Built and tested** (`test_kit.py`, abstract fixtures). The owner checked the pre-fix harness externally and found the per-variant exclusion defect. It is fixed (G2-13), with regression tests that fail on the pre-fix code. The fix is **pending external check**. |
| Exact zeros on HB-3, HB-4 under T_lin | **Shown** on exact rational affine-entry instances. They are not yet wired to the R1 numerical families or to a card's T_Π. |
| Static map on HB-4 | **Witness part shown.** The DIF-5(e) wiring is not built (KD-4). |
| ε ≡ 0 on single-protocol families; zeros on HB-1, and on HB-5 with calibrated filters; HB-9 MODE SELECTION; the sign of BRI1 Tier-1 on HB-2; STD-1 on every HB family | Not built: **KD-1** |
| B-CF vectors | Not built: **KD-2** |
| ST-6 to ST-9 computed | Not built: **KD-3** |
| Every other rejection test in §19.3 | Not built: **KD-4** |
| Decoder battery (RB, SPS); transplant, W-pipe and substitution harnesses; regime surrogates; VB checklists; ε witness enclosures | Not built: **KD-5** |

## Readings taken by the NR-4 harness (accepted, G2-13 item 2)

The ablated variants are constructed by the auditor, never by the card author (G2-13 item 2). A card-built variant could be written to fail or to return nothing, and so dodge the test (the pattern of CR-2 item Q-4).

1. **Undefined images.** A point where the pipeline image is undefined is not an appearance of ℛ★. It stays in the denominator, since the charter's fraction is of Dom_gate.
2. **Decoupled-corner test (as fixed by G2-13 item 1).**
   - A point is a decoupled corner if its image under the **full law K** and the K-image of the decoupled Ξ (every S–E coupling set to zero) agree within ρ_abl on every lock observable.
   - If either K-image is undefined, the point is not excluded, for any variant. This is reading 1 applied to K's images under G2-13 item 1; see the open question in `charter_workings/FREEZE_VERIFICATION.md` §13.
   - The set is computed once and removed identically for K, K_∅, K_𝒮, every single-clause deletion and the responsibility map.
   - The superseded per-variant reading let a coupling-insensitive ablation empty its own denominator. That variant then scored 0, giving a false NOT-RELOCATED or a false responsibility.
3. **All points excluded.** If every point is excluded, the verdict is VOID, and ℛ★ is not GENERATED (hostile default).
   - The harness never reports a fraction of 0 over an empty domain. In the VOID case, every run's fraction is undefined (`None`), and every responsibility entry is `'VOID'`, never True or False.
   - Because the set is shared, no variant can reach an empty denominator unless K does.
4. **Internal copies (PC-6).** Internal copies of law clauses inside components must already have been removed from the supplied variants. The harness cannot detect them.

**Builder notes (not part of the accepted readings; for owner confirmation; CV-1 governs meanwhile):**
- **Empty lock fibers.** A lock-fiber instance with no non-excluded weight is skipped in the every-instance clause and in the per-fiber responsibility report. That covers a fiber whose points are all excluded, and one whose remaining weight is zero. The first case was already the checked kit's behaviour. Skipping zero-weight fibers was added after review, because a 0/0 fiber had been scored as 0.
- **Responsibility map.**
  - `responsibility[c]` is True if and only if ℛ★'s overall fraction under K − c is below 1/Q_min. This is NR-4's sentence "ℛ★ appears under an ablated law if it does so on a reference-measure fraction ≥ 1/Q_min of Dom_gate".
  - `responsibility_lock_fiber[c]` lists the lock-fiber instances on which that fraction is below 1/Q_min. It is reported so that the auditor can read Q4's "fails, on some lock-fiber instance, when some clause of 𝒦 is deleted".

## Validation output

`python3 test_l0_code.py`: 10 ok. `python3 test_kit.py`: 11 ok, including the two G2-13 regression tests and the VOID and per-fiber tests added after review. `python3 sel222.py`: see
`results/sel222.json`, where `matches_frozen` is true.
