# Red-team of the Stage-3 Charter v0: measurability, decidability and stopping

**Source.** I read the full v0 text (1792 lines) at `/tmp/claude-0/-home-user-vsctestinggrut/1a09ed24-aca1-5a3e-824d-0bafde87a0b5/scratchpad/rt_def/charter_v0.md`. I checked it against G2-11, STATE, RULES, R1_SYNTHESIS §12, D5_COMPARATOR_AUDIT §6, F0_SD0_RESULT, F0_REQUIREMENTS_CONSOLIDATION_01, GRAVEYARD and SCOREBOARD. Nothing was edited.

**Every pattern below is a CHARTER TEST.** Each is an abstract gaming pattern against the rules. None is a physical proposal, and none names or sketches a candidate 𝒦. I suggest adding them to §24.1 as CT-60 to CT-109.

## Fix before freeze: highest severity

| Rank | Pattern | Why it matters |
|---|---|---|
| 1 | RT-01, RT-02: I_SRB is wide by starvation or by intractability | MC-4 and b_meas can be met without beating standard physics |
| 2 | RT-04, RT-47: LOCK-INCONCLUSIVE has no consequence and no stage has a clock | The route can avoid ever reaching a terminal |
| 3 | RT-15: MC-5 voids only changes made "after unsealing" | The lock can drift between card freeze and unsealing |
| 4 | RT-20: "lock resolution" is undefined | Both directions favour a small value: regime escape and easy Q3 |
| 5 | RT-21: CR-n repairs may loosen rules while drafts exist | Thresholds can be set after drafts are seen |
| 6 | RT-24, RT-25: the B-CF collapse test is exact equality and DC-8 is syntactic | This is the SD0 arc-consistency boundary again |
| 7 | RT-30: dim_ub can be certified by "rank at an explicit point" | The certificate is unsound and gives spurious codimension |
| 8 | RT-38, RT-39: constant tiling across cards; VAR-6 is over-broad | Budget evasion, or owner discretion on every distinctness call |
| 9 | RT-42, RT-43, RT-46: the staircase test needs a failure motive; no batch clock; Stage-6 slot reuse | Staircases and stalls that the stopping rule does not forbid |
| 10 | Appendix A: q = 3 finite alphabet versus T_lin = GL(k) | ε_R is not computable as written |

---

## A. Measurability: locks that cannot be falsified or tested

### RT-01 · CHARTER TEST · Starving the baseline of FDT inputs
- **Pattern.** The card's prediction deliberately uses none of the platform's reference (undriven) correlators. It uses only coarse interface-side statistics, and its content comes from priced law constants. B-SRB gets "exactly" the card's inputs, so it cannot run the Kubo/FDT route, which needs those correlators, and I_SRB comes out wide. On the real platform the correlators are cheap to measure and would pin O. This is the BRI1 Tier-1 lesson, and D5 reverse-direction relation (i).
- **Slips through.** BP-5: "The baseline receives exactly the data that the card's prediction consumes." §15.5: "**Input:** exactly what the card's prediction consumes".
- **Fix.** "BP-5 Same or more inputs. The baseline receives the union of three sets:
  - (i) every datum the card's prediction consumes;
  - (ii) every quantity measurable on the lock platform under a₀, in a calibration run independent of the lock records: reference laws, and connected correlators up to order m★★ on the frozen grid;
  - (iii) all MC-6 certification data.

  The card's prediction may use the same union. I_SRB is computed from it."

### RT-02 · CHARTER TEST · I_SRB wide by default
- **Pattern.** The card picks an observable or regime where standard computations are intractable. I_SRB is then wide because the auditor failed to constrain it, not because standard freedom was shown. MC-4 and b_meas pass because the comparison is intractable.
- **Slips through.** §15.5: "the auditor computes I_SRB(o) from STD-1 to STD-12…". MC-4: "|I_SRB|/|I_K| ≥ Q_min."
- **Fix.** "|I_SRB(o)| is credited only as a certified inner width. That width is the diameter of the set of O-values realized by verified, regime-matched standard witnesses (B-HB members, plus card-added witnesses verified independently) that are consistent with every BP-5 input. Auditor derivations may only shrink it. If no two such witnesses differ by more than |I_K|, MC-4 fails." This mirrors how dim_lb is certified.

### RT-03 · CHARTER TEST · Safe interval with no live rival (noise-floor lock)
- **Pattern.** I_K is narrow relative to the window, but it sits where standard environments on that platform class already concentrate, for example near ε = 0, where the R1 calibration environments sit at O(1/N_B). Confirmation is then near-certain. Power is computed against a hypothetical point of I_SRB, not against a standard model consistent with the platform.
- **Slips through.** MC-5: "**LOCK-CONFIRMED** if dist ≤ 2σ_tot, σ_tot ≤ |I_K|/4, and MC-4 holds." MC-4: "The effect size against the nearest certified standard witness is reported." MC-7: "power ≥ 0.9 against the nearest point of I_SRB at distance ≥ |I_K|."
- **Fix.**
  - "MC-4(b) Live rival. At least one verified standard witness, consistent with every BP-5 input, predicts O outside I_K by at least 3σ_pre. MC-7 power is computed against the nearest such rival."
  - "MC-4(c) Risk. For scope Q, I_K ∩ [0, 3σ_pre] = ∅."
  - "The effect size is a gate (≥ 3σ_pre), not only a report."

### RT-04 · CHARTER TEST · Inflating σ to shield the lock
- **Pattern.** The card preregisters large systematics, or the realized σ_tot grows. The 3σ_tot falsification line is never crossed, confirmation fails the σ_tot ≤ |I_K|/4 test, and the result is INCONCLUSIVE indefinitely. Nothing says what INCONCLUSIVE does to the route.
- **Slips through.** MC-5: "**LOCK-FALSIFIED** if dist(O_meas, I_K) > 3σ_tot… **LOCK-INCONCLUSIVE** otherwise." Also: "σ_tot includes the preregistered systematics".
- **Fix.**
  - "σ_pre is frozen in C13 and satisfies σ_pre ≤ |I_K|/4."
  - "Falsification uses max(σ_pre, σ_stat)."
  - "Realized systematics above 1.25·σ_pre make the result LOCK-VOID, which counts as FALSIFIED."
  - "LOCK-INCONCLUSIVE on the primary platform, and on the alternate if one is used, is a G5-LOCK FAIL for T-3(b)."

### RT-05 · CHARTER TEST · Self-reported feasibility
- **Pattern.** The card computes N_req from an asymptotic variance that ignores heavy tails and autocorrelation, and counts correlated samples as "independent records". S7 then passes on paper only.
- **Slips through.** MC-7: "N_req ≤ N_max = 10⁹ independent records in total per lock observable…"
- **Fix.** "The Evaluator computes N_req by simulating the frozen estimator on two cases: the card's in-silico realization at the lock fiber, and the live rival (RT-03). Sample sizes are effective sample sizes from a frozen integrated-autocorrelation estimator. The larger of the card's value and the Evaluator's value governs."

### RT-06 · CHARTER TEST · Witness-gap lock (scope Q)
- **Pattern.** ℛ★ fixes ε_R, but MC-7 forces measurement through a lower-bound witness w ≤ ε. The card's I_K for w is one-sided, [0, ε_pred], or it claims tightness without proof. Any w below the prediction confirms, so this is really a sign or bound test.
- **Slips through.** MC-1: "…or through a witness with a frozen constant." MC-7: "Estimation uses per-witness forms".
- **Fix.** "A witness lock is admissible only if ℛ★ fixes the witness value on the lock fiber. Either ℛ★ is stated in the frozen witness, or w = ε is proved at DERIVED grade on the fiber (for example, the two-protocol symmetric case of Theorem F). An I_K with an endpoint at a DEF-2 bound is a sign test and inadmissible under MC-4."

### RT-07 · CHARTER TEST · Knife-edge lock fiber
- **Pattern.** Forcing and c ≥ 1 hold only on measure-zero instances, such as an exact symmetry or an exact coincidence of parameters. A real platform never realizes them, so the lock tests a relation that is not forced at the realized point.
- **Slips through.** §1.5: "I_𝒦… has at most 3 structurally distinct instances… declared at freeze". LT-1: "ℛ★ is evaluated on a physically realized environment".
- **Fix.** "Lock-fiber robustness. Q1, Q6 and Q9 hold on a neighbourhood of each lock-fiber instance of relative size at least max(2^(−p★), the platform's certified parameter uncertainty), checked as in DIF-6. I_K propagates that uncertainty. A lock without this robustness is VOID at S7."

### RT-08 · CHARTER TEST · Self-sealing escape through the verdict table
- **Pattern.** ℛ★ is shaped so that every configuration that would violate it is one where carrier certification fails, or where the verdict is MODE SELECTION or NO RECIPROCITY VERDICT. Violations are then read as INCONCLUSIVE.
- **Slips through.** MC-6: "Failure gives NO RECIPROCITY VERDICT, which counts as LOCK-INCONCLUSIVE."
- **Fix.** "MC-6 certification is completed and frozen by hash, by an agent blind to O, before O is unsealed. It cannot be revised using lock data. If RS-6 predicted a certifiable carrier on the lock platform, then a failed certification, MODE SELECTION or NO RECIPROCITY VERDICT counts as LOCK-FALSIFIED."

### RT-09 · CHARTER TEST · A platform class that cannot be certified
- **Pattern.** The card passes S7 by naming a platform class for which no existing apparatus can pass the 10-item checklist. The card can be ADMISSIBLE, but the lock can never be run.
- **Slips through.** "Listing a class does not claim that any relation can be tested there." SC3: "An admissible and **feasible** LT-1 instantiation".
- **Fix.** "SC3 requires a named, existing platform with published operating parameters. The Intake auditor pre-assesses each MC-6 item on it as satisfiable. Otherwise the card is CARD-UNMEASURABLE at S7."

### RT-10 · CHARTER TEST · A token independent input
- **Pattern.** MC-2 is met by one interface-side input that the prediction barely depends on. The rest is self-prediction from Γ.
- **Slips through.** MC-2: "At least one input to the prediction is an interface-side measurement made independently of the record laws used for O."
- **Fix.** "Input relevance. Replacing every independent interface-side input by its full admissible range must widen I_K by a factor of at least Q_min. Otherwise the lock is DEFINITIONAL (CT-34)."

### RT-11 · CHARTER TEST · Postdiction from an archive the author knows
- **Pattern.** LOCK-H draws from a pool of one or two archived datasets that pass MC-6. The author already knows them, so the Selector has no real choice.
- **Slips through.** MC-8: "**LOCK-H:** existing datasets chosen after freeze by the Selector".
- **Fix.**
  - "LOCK-H requires an eligible pool of at least 5 datasets [P]."
  - "Datasets that appear in the author's C1 'seen' declaration, or that the card cites, are ineligible."
  - "The Selector draws at random with a committed seed. Otherwise only LOCK-E is allowed."

### RT-12 · CHARTER TEST · Holdout scope that is too narrow, or holdouts replaced
- **Pattern.** Four variants:
  - The declared scope is so narrow that no max(2, n) realized system classes exist inside it.
  - Holdouts are replaced by the card's own preregistered experiment.
  - Holdouts are evaluated on modelled rather than measured data.
  - The holdout tolerance is a "declared error" the card sets.
- **Slips through.** G5-HOLD: "Each is a physically realized system class inside the declared scope that the card does not reference." Also: "A preregistered prospective experiment may replace a holdout." KU-12: "beyond the declared error".
- **Fix.**
  - "If the auditor cannot find the required number of classes inside the scope, G5-HOLD FAILS."
  - "C13 lists at least 2·max(2, n_obs) candidate classes."
  - "Holdouts use measured data only."
  - "A replacement experiment is designed or approved by the hostile auditor, and at most one is allowed."
  - "The holdout tolerance is σ_pre plus the width of I_K. A separate 'declared error' is not allowed."

### RT-13 · CHARTER TEST · Persistence by horizon choice
- **Pattern.** H is tied to the *shortest* internal timescale. A Π that is only an unrelaxed imprint of initial data, or of a slow mode, persists over H trivially. Horizon doubling only multiplies H by 2.
- **Slips through.** §1.3: "H ≥ max(…, 10·τ_int), where τ_int is the card's declared shortest internal timescale".
- **Fix.** "H ≥ max(window, 10·τ_int, 3·τ_slow). The Evaluator computes both τ_int and τ_slow from the law at the truncation; τ_slow is the slowest relaxation time, for example the inverse spectral gap. If τ_slow is not computable, Π must be shown invariant under the realized stationary dynamics; otherwise DIF-2 fails."

### RT-14 · CHARTER TEST · Kill conditions with no risk
- **Pattern.** The card's own kill conditions are decided on public battery items the author has already checked. Or they are "named experimental outcomes" for experiments that will never be scheduled.
- **Slips through.** KP-1: "…or is a named experimental outcome." KP-2: "Each is reachable: some 𝒮-admissible outcome triggers it."
- **Fix.** "KP-2′ Risk. Each card-specific kill is decided on post-batch seeds, on sealed holdouts, or by the C13 lock. Kills decided on public items are consistency checks and do not count toward KP-4."

---

## B. Moving lock targets

### RT-15 · CHARTER TEST · Lock drift before unsealing
- **Pattern.** After Stage-4 results are known and before unsealing, the estimator, tier, protocol subset or platform is changed. MC-5 voids only changes made after unsealing, and G5-LOCK preregisters the design a second time.
- **Slips through.** MC-5: "If any threshold, observable, tier, protocol set, grid, estimator or exclusion rule changes after unsealing…" G5-LOCK: "The LT-1 design is preregistered."
- **Fix.**
  - In MC-5, replace "after unsealing" with "after card freeze".
  - G5-LOCK: "The preregistration is a byte-identical copy of C13. The only allowed differences are fields that C13 explicitly deferred to a frozen deterministic rule, such as a device chosen by the Selector. Any other difference is a BU-3 modification."

### RT-16 · CHARTER TEST · Hedging across two relations and several observables
- **Pattern.** The card registers ℛ★, a secondary relation and several observables, then reports whichever confirms. The charter does not say whether a falsified secondary relation kills the card, or whether a confirmed secondary relation earns PREDICTIVE.
- **Slips through.** §3.1: "A secondary relation is scored separately…". MC-9: "Thresholds are Bonferroni-adjusted across lock observables." MC-10.
- **Fix.**
  - "At most 3 lock observables per card."
  - "LOCK-CONFIRMED requires every observable of ℛ★ to be CONFIRMED."
  - "LOCK-FALSIFIED on any observable of any registered relation fires KU-12."
  - "PREDICTIVE is conferred on ℛ★ only."

### RT-17 · CHARTER TEST · Using the alternate platform as a second draw
- **Slips through.** MC-6: "One preregistered alternate platform is allowed. There is no third."
- **Fix.** "The alternate is used only if the primary fails MC-6 before any lock datum is unsealed. Once the primary's lock data are unsealed, its verdict is final."

### RT-18 · CHARTER TEST · Carving the domain after the seeds are drawn
- **Pattern.** The 10% AI-3 allowance is spent on excluding exactly the instances where ℛ★ fails, after the seeds are visible.
- **Slips through.** DIF-7: "The domain contains AI-1, AI-2 and at least θ_gen = 0.9 of AI-3."
- **Fix.** "The domain is a decidable predicate frozen in C16 at card freeze and never edited. The 0.9 is a coverage test of that predicate on the AI-3 draws. IP-13 prices the predicate."

### RT-19 · CHARTER TEST · An unfrozen transfer plan
- **Pattern.** The sector pair or the transfer observable is chosen after Stage-5 data are seen.
- **Slips through.** BU-3's list of modifications omits the transfer plan. C20: "the transfer plan, declared only".
- **Fix.** Add to BU-3: "the transfer plan: the sector pair, the transfer observable, the partition of θ into θ_K, θ_dict, θ_std and θ_cal, and the SI witnesses."

---

## C. Thresholds set after the fact

### RT-20 · CHARTER TEST · Undefined lock resolution
- **Pattern.** The card chooses a tiny lock resolution. That lets it prove a regime hypothesis such as RH-KMS fails, which removes the FDT/KMS baseline. It also lets Q3 witnesses violate ℛ "by more than the lock resolution" trivially.
- **Slips through.** BP-4: "…unless the card proves it fails by more than the lock resolution." Q3: "…must violate ℛ by more than the lock resolution." RH-KMS: "within lock resolution".
- **Fix.** Add to Appendix A:
  - "r_lock(o) := max(2σ_pre(o), 2^(−p★)·|window(o)|), frozen in C13."
  - "A regime hypothesis fails only if a deviation of at least 3·r_lock is certified on the lock platform."
  - "Q3 witnesses must violate ℛ★ by at least 3·r_lock."

### RT-21 · CHARTER TEST · Charter repair informed by drafts
- **Pattern.** Drafts exist from the charter freeze onward; IP-12 counts them. When a draft narrowly fails, a loosening CR-n is issued before Card 1 is frozen.
- **Slips through.** §19.2: "**Before Card 1 is frozen:** numbered repairs CR-n, by owner ruling only."
- **Fix.** "After the charter freeze, every repair tightens only. A loosening requires a fresh charter freeze, with a certification that no draft has been logged since the previous freeze."

### RT-22 · CHARTER TEST · The card declares its own constant ranges
- **Slips through.** IP-5: "The range is declared at freeze."
- **Fix.** "The range is the widest of three: the default range, the card's declared range, and the largest natural range an auditor exhibits."

### RT-23 · CHARTER TEST · Flooding the owner with disputes
- **Pattern.** The author raises many interpretive disputes. Owner rulings on interpretation are not "repairs", so the tighten-only rule does not bind them.
- **Slips through.** CV-1: "…resolved against the card until the owner rules."
- **Fix.** "After Card 1, an owner ruling on a dispute chooses between the two submitted computations. It is recorded as an interpretation CI-n and applied uniformly to every card, null and self-test. It is void if it changes any ST-1 to ST-5 verdict."

---

## D. Decidability and the SD0 arc-consistency boundary

### RT-24 · CHARTER TEST · A consistency selector that just misses the collapse test
- **Pattern.** Selectivity comes from bounded-width propagation of a different level or kind than the B-CF members: k = 4 to 6, (j,k)-consistency, an LP/AIP relaxation, or a B-CF member with one item flipped by an extra clause. Boolean combinations of two members also escape. Exact vector equality is evaded in every case.
- **Slips through.** §15.2: "If a card's SEL vector equals that of a B-CF member, or its FORBID set equals the set that k-consistency refutes for some k ≤ 3".
- **Fix.**
  - "B-CF* = {(j,k)-consistency for j ≤ k ≤ 6; SLAC; BLP; AIP; BLP+AIP; Sherali–Adams levels ≤ 3; ASP}, plus every conjunction or disjunction of two members."
  - "Collapse holds if either (a) the card's SEL vector is within Hamming distance 1 of a B-CF* vector on the mandatory and graded items, or (b) the responsibility map shows that the card's FORBID verdicts are bounded-width refutations of width ≤ 6."
  - "The differing item in (a) is treated as IP-10 structure."

### RT-25 · CHARTER TEST · A consistency card in disguise
- **Pattern.** The clauses are not syntactically consistency conditions. On every embedding, though, Sol equals the fixpoint set of a local propagation.
- **Slips through.** DC-8: "Cards built only from consistency conditions are flagged at intake."
- **Fix.** "DC-8 is semantic. The harness flags a card if, on every B-SEL embedding and on an AI-3 sample, supp(Sol) equals the survivor set of some B-CF* member up to Emb."

### RT-26 · CHARTER TEST · A token weight rule
- **Pattern.** The card escapes DC-8's UNMEASURABLE verdict by adding weights that are a fixed function of the support pattern, such as uniform or maximum-entropy on the support. Its ε values are then conventions.
- **Slips through.** DC-8: "That weight rule is then the actual law, priced and judged as such."
- **Fix.** "Weights that are a fixed function of the support are a convention. ε-relations under them are scored as support relations, with ε credit 0. ε credit requires a W-pipe showing that the weights change under clause ablation while the support stays fixed."

### RT-27 · CHARTER TEST · A semi-decision procedure with a depth tuned to the battery
- **Pattern.** FORBID and ALLOW are both found by r.e. certificate search. The search is "terminated" by an enumeration bound set just above the longest certificate in the battery, and a timeout defaults to ALLOW.
- **Slips through.** DC-1: "…a termination argument: a proof, or a finite bound on an enumeration."
- **Fix.**
  - "An enumeration bound is a law constant priced under IP-5. Its timeout branch is declared and scored."
  - "A verdict that flips at half the bound or at twice the bound is BATTERY-TUNED."
  - "The Selector draws at least one SEL holdout whose shortest known certificate is longer than twice the battery maximum."

### RT-28 · CHARTER TEST · A truncation level used as a size threshold (GY-4 in disguise)
- **Pattern.** FORBID verdicts hold only because the frozen truncation level excludes larger realizations. The level is placed between the anchors' sizes and the sizes the FORBID items would need.
- **Slips through.** DC-4: "That level is part of the law, is priced, and is what gets scored." IP-9 and SEL-11 cover branches and clauses, not a global constant.
- **Fix.** "Every FORBID must hold at truncation levels n, n+1 and 2n. A verdict that flips within that range is a size discriminator: a GY-4 return. The truncation level counts as VB-10."

### RT-29 · CHARTER TEST · An infeasible next truncation level
- **Pattern.** The truncation level is set where the next level cannot be computed, so the Ch-4 check never runs.
- **Slips through.** Ch-4: "…or fails at the next truncation level."
- **Fix.** "The card declares resources for level n+1 (and 2n for FORBIDs). If the check does not finish within κ times those resources, the relation is a truncation artifact and earns zero."

### RT-30 · CHARTER TEST · An unsound dimension certificate
- **Pattern.** dim_ub is "certified" by the rank at a point the card chooses where the rank drops. The rank of a parametrization at one point is a lower bound on dimension, not an upper bound, so this certifies a spurious codimension.
- **Slips through.** §2.5: "dim_ub is certified by a proof, or by an exact rank computation at an explicit point."
- **Fix.** "dim_ub is certified in one of two ways:
  - by a proof; or
  - by c explicit equations, verified by exact symbolic identity to vanish on all of Im*(ι) in the window, whose Jacobian has rank c everywhere on Im* in the window (or has generic rank c with a certified lower-dimensional singular locus).

  Rank at a single point never certifies dim_ub."

### RT-31 · CHARTER TEST · Keeping exactness as an option
- **Pattern.** The card claims an exact characterization. If the proof is missing, it falls back to the OUTER label instead of failing.
- **Slips through.** DC-5: "Without one the card is CARD-UNDECIDABLE, or labelled OUTER."
- **Fix.** "OUTER or INNER status is declared in C4 at freeze. A claim of exactness without a proof is CARD-UNDECIDABLE and is never relabelled."

### RT-32 · CHARTER TEST · Unbounded declared resources
- **Pattern.** The card declares very large resources. The Evaluator cannot run them, and there is no status for that case, so evaluation stalls.
- **Slips through.** DC-2: "The card declares time and memory per item. The evaluator allows κ = 10 times that."
- **Fix.** "Appendix A sets absolute ceilings R_item and R_card [P]. Declared resources above them make the card CARD-UNDECIDABLE at S2. The Evaluator runs each item for min(κ·declared, R_item); an overrun is UNSCORABLE. There is no 'pending compute' status."

### RT-33 · CHARTER TEST · An intractable baseline
- **Pattern.** The card chooses a type where "persistent under some m ∈ 𝔐_std" cannot be computed. It also declares that 𝒞 "fixes no dynamics", which gives it the full baseline of 2^|V| − 2 partitions.
- **Slips through.** §2.3: "{Π persistent and A-stable under some m ∈ 𝔐_std(ι | H)}", "If 𝒞 fixes no dynamics…", and "Under CV-2 the smaller construction is used."
- **Fix.** "The Intake auditor decides whether 𝒞 fixes dynamics. Any baseline quantity that cannot be computed by a terminating frozen procedure within the work-order budget contributes ΔF = 0 on its axis."

---

## E. Cross-sector claims that are really one sector, or a re-fit

### RT-34 · CHARTER TEST · A transfer that uses no information from A
- **Pattern.** The frozen θ_K already predicts sector B, so sector A's data add nothing. TG > 0 is the Stage-5 lock counted again as CROSS-SECTOR.
- **Slips through.** XS-7: "TG := F_p(𝒜_B^base) − F_p(𝓡_{𝒦,B}(θ̂_A)) ≥ p★."
- **Fix.** "Also require TG_A := F_p(𝓡_{𝒦,B}(priors)) − F_p(𝓡_{𝒦,B}(θ̂_A)) ≥ p★. At least one parameter is fixed on D_A, and the responsibility map shows that this parameter sets the B prediction."

### RT-35 · CHARTER TEST · Mathematics as sector A
- **Pattern.** θ is fixed by matching B-SEL verdicts, which are public development items rather than data, and then "transferred" to a physical sector.
- **Slips through.** XS-1: "Q: correlation and contextuality (the B-SEL type)". SI-1: "The datasets are disjoint and frozen by hash".
- **Fix.** "Sector data are empirical measurements on physical systems. Battery items, classifications and theorems are card design, priced under §4, and never θ̂_A."

### RT-36 · CHARTER TEST · θ_K both frozen and fitted
- **Pattern.** Law constants are left free "to be fixed in sector A", which avoids the IP-5 tuning price at Stage 3.
- **Slips through.** XS-5: "1. Fix θ_K and θ_dict on D_A alone…". This contradicts BU-3, under which constants are frozen.
- **Fix.** "θ_K is frozen at card freeze. Only θ_dict, whose count and ranges are declared in C20, is fitted on D_A. Each fitted parameter is priced under IP-11 and subtracted from TG."

### RT-37 · CHARTER TEST · Shopping for regime labels
- **Pattern.** One physical regime is labelled "quantum" for A and "thermodynamic" for B by vocabulary alone.
- **Slips through.** XS-3: "A and B must lie in different regimes among quantum, thermodynamic and gravitational."
- **Fix.** "Regime membership is operational:
  - 'quantum' means the target observable changes by at least 3σ between F_σ and its classical limit;
  - 'thermodynamic' means an RH-TH observable whose large-N limit is essential;
  - 'gravitational' means F_σ contains gravitational coupling.

  F_A and F_B are different SFP entries."

---

## F. Budget evasion with near-duplicate cards

### RT-38 · CHARTER TEST · Tiling a constant across cards
- **Pattern.** Three cards share the mechanism that generates Π and ℛ★ but differ in peripheral modules and in ℛ★'s constants. Their I_K values tile I_SRB. Under BU-7 the owner can step through them after Stage-5 failures, which amounts to fitting the constant by sequential locking. BU-4(c) is met by a single point in Z Δ Z.
- **Slips through.** BU-4(c). BU-7: "If the picked card fails Stage 4 or 5, the owner may take another frozen ADMISSIBLE card, unmodified." MC-9 Bonferroni applies only within a card.
- **Fix.**
  - "BU-4(e) Mechanism distinctness. The clause sets that carry ℛ★ and Π in the NR-4 responsibility maps must not be equivalent under VAR-1 or VAR-2."
  - "BU-7′. An unsealed lock dataset never serves another card. Cards with a shared lock observable on a shared platform class are a VARIANT pair. Confirmation thresholds are Bonferroni-adjusted across every card locked in the route."

### RT-39 · CHARTER TEST · VAR-6 is too broad
- **Pattern.** "Any composition" of single-clause patches connects every pair of laws. Read literally, every second and third card is a VARIANT, so each call becomes an owner dispute. Read narrowly, it lets the RT-38 hedges through.
- **Slips through.** VAR-6: "any composition of VAR-1 to VAR-5."
- **Fix.** "VAR-6: a composition whose total edit is at most max(3·b_patch, 25% of K_i's clauses), or one that preserves the clauses carrying ℛ★ and Π (BU-4(e))."

### RT-40 · CHARTER TEST · Drafting from a template
- **Pattern.** The author logs one "draft" that is a template, then searches its instances in code against the public items. τ_sel counts a single draft.
- **Slips through.** IP-12: "n_drafts counts every 𝒦 draft in any form".
- **Fix.** "n_drafts counts every law instance written or evaluated on any item, including instances generated by a program. A template counts as the size of its instance space. The search code and its logs are disclosed in C1."

### RT-41 · CHARTER TEST · Using intake as an oracle
- **Pattern.** A probe card is frozen first to learn how the auditor rules on NR-1, NR-2, S1 and S2. Cards 2 and 3 are then designed around those rulings.
- **Slips through.** §19.4: "Static intake audits may run card by card." Intake results "are not gate scores", so the information-hygiene rule does not cover them.
- **Fix.** "Intake runs at batch close for all cards together. No intake result is visible to any author before the batch closes."

---

## G. Stopping, and staircase moves the stopping rule does not forbid

### RT-42 · CHARTER TEST · A staircase that starts before any failure
- **Pattern.** Foundations work is described as "designing the next card" before anything has been scored. It never meets condition (i), so the staircase test does not catch it.
- **Slips through.** §20: "…a forbidden staircase move if both hold: (i) it is motivated by a card failure… **and** (ii)…"
- **Fix.** "A forbidden staircase move is any work item that delivers an ingredient for a present or future 𝒦 card and is not a frozen card, the §19.3 work order, a gate result or a terminal record. Motivation is irrelevant."

### RT-43 · CHARTER TEST · The batch never closes
- **Pattern.** One or two cards are frozen and the final count is never declared. Nothing is scored and the route never terminates.
- **Slips through.** BU-6: "…until every card is frozen, or until the route declares its final count."
- **Fix.** "The batch closes automatically D_batch days [P] after the harness is validated. Slots not used by then are forfeit. The owner declares the final count."

### RT-44 · CHARTER TEST · The harness work order as a staircase
- **Pattern.** The work order grows into foundations work, such as a theory of standard persistence for 𝒜_Π, I_SRB tooling, or d_op for generated T. The phrase "implements frozen text" shields it.
- **Slips through.** §19.3: "…not a prerequisite campaign: it implements frozen text and nothing else."
- **Fix.** "The work order is time-boxed (T_harness [P]). The §19.3 validation list is its complete deliverable. Anything it cannot compute within the box takes its hostile default (RT-33), set by CR before Card 1. An overrun leads to a CR or to STAGE3-OWNER-HALT, never to an extension."

### RT-45 · CHARTER TEST · Conditional verdicts turn pending items into prerequisites
- **Pattern.** A verdict proceeds "conditional on" M5, A-BL or F and reaches LOCK-CONFIRMED. Banking is then blocked, so a campaign on that item becomes the only way to bank.
- **Slips through.** §20: "…labelled 'conditional on ⟨item⟩' and proceeds." PV-3: "…banking is blocked."
- **Fix.** "Every credited claim or gate verdict that depends on a pending or evidence-grade item is scored now under the hostile reading of that item. Q1 needs DERIVED grade without the item. The verdict never proceeds conditionally."

### RT-46 · CHARTER TEST · Stage 6 has no end, and slots can be reused there
- **Pattern.** Stage 6 has no gates. T-3(c) implies that unused slots can buy a modified 𝒦 after Stage-4 and Stage-5 scores are visible, which contradicts batch freeze.
- **Slips through.** T-3(c): "Stage 6 requires modifying 𝒦 and no unused slot remains." §15.12 is "(pointer only)".
- **Fix.**
  - "Declaring the final count forfeits the remaining slots."
  - "Any need to modify 𝒦 at Stage 6 gives STAGE3-ROUTE-TERMINATED."
  - "Stage 6 opens only under a Stage-6 charter frozen alone, with its own gates and clock. Failing a Stage-6 gate terminates the route."

### RT-47 · CHARTER TEST · Terminals stuck in limbo
- **Pattern.** Three ways to stall:
  - S9 stops partway, as SD0's audit did at 1 of 5.
  - LOCK-E waits on an experiment indefinitely.
  - A void holdout is reselected after an unfavourable look.
- **Slips through.** OR-6: "The audit must be complete… before the owner's pick." MC-8 (LOCK-E). CT-55: "Evaluation void; holdouts reselected".
- **Fix.**
  - "If S9 is not complete within T_audit [P], the card is CARD-RESTATED."
  - "If LOCK-E data are not unsealed within T_lock [P] of G5-LOCK, G5-LOCK FAILS."
  - "A void caused by the author side is a FAIL. A void caused by the auditor side allows one reselection, with the voided result disclosed."
  - "The T-2 terminals are exhaustive. There is no OPEN terminal."

### RT-48 · CHARTER TEST · Laundering the terminal
- **Pattern.** The card makes one mandatory item unscorable, so S2 is the first failing screen. The GRAVEYARD line then reads "not refuted" instead of RELOCATED or STANDARD, and the idea survives for a later route.
- **Slips through.** T-1: "The first failing screen in §18.2 names the terminal." DC-6: "…'UNSCORABLE AT FROZEN BATTERY', not 'refuted'."
- **Fix.** "The GRAVEYARD line lists every failed screen from S0 to S8, since all are run. Every line counts as a killed idea for the GY return test, in this route and in any later one."

### RT-49 · CHARTER TEST · Library banking that seeds a new route
- **Pattern.** Cards are built to leave bankable sub-results behind. Examples are a generated T_Π with its reduction s_T, which is in effect a new R1 tier and distance, or carrier lemmas. These then seed a "new" route under T-5.
- **Slips through.** T-5: "banking DERIVED sub-results as a library". §1.4: "This is a use of R1, not a modification of it (OD-6)."
- **Fix.**
  - "Library banking excludes interface classes, distances, s_T, carrier constructions, and any result whose stated use is a law ingredient."
  - "A generated T_Π is card-internal and never enters the R1 ladder."
  - "A new route inherits this route's GRAVEYARD and FR standings and cannot cite library items as discharging any FR."

### RT-50 · CHARTER TEST · Tooling repair as a free option
- **Pattern.** The card freezes an ambiguous statement. After scores are visible, the code is "realigned" to a different faithful reading. Harness fixes made in a card's favour after batch close raise the same issue.
- **Slips through.** BU-3: "The only exception is a tooling repair that realigns code to the frozen statement." DC-9. §19.3: "A harness defect is fixed in the harness…"
- **Fix.**
  - "Where the statement is ambiguous, the frozen reference implementation is normative."
  - "A tooling repair may only fix a crash or a failure to terminate, and must reproduce all prior outputs byte for byte."
  - "A harness fix after batch close is rerun on every card, null and self-test. A verdict that changes in a card's favour needs the Recomputer's confirmation and an external check."

---

## H. Ambiguous or uncomputable clauses

| Clause | Problem | Resolution |
|---|---|---|
| BP-4, Q3, RH-KMS: "lock resolution" | Never defined | RT-20 formula in Appendix A |
| MC-5: LOCK-INCONCLUSIVE | No consequence for the route under T-3 | RT-04: counts as a G5 FAIL |
| Appendix A: q = 3 finite alphabet, together with T_lin = GL(k) with translations and the whitened-cumulant window | GL(k) cannot act on a 3-letter alphabet; no binning rule is given | Say whether ε is computed on continuous or discretized records. If discretized, freeze the binning (tertiles of P_{a₀} from an independent calibration run) and the group acting on it |
| Appendix A: "starting after t₁"; "α = 1 null-protocol standard deviation" | t₁ undefined; the coordinate whose standard deviation is meant is unnamed | Freeze t₁ (for example H/4) and the reference coordinate |
| §1.4, DC-3, Q1: ε_R = inf over P★ of max d_op | Not exactly computable (non-convex inf over P★ and O(k)). Interval tests can never certify an equality, so Q1's "exact computation" route is unavailable for ε-equalities | ε-relations are decided by theorem, or stated against the frozen enclosure [witness lower bound, upper bound from a frozen optimizer], with fixed semantics: holds if the enclosure lies inside the priced band |
| MC-7: "independent records" | Undefined | Effective sample size (RT-05) |
| §1.5: "whichever admissible chart minimizes the credited bits" | Minimum over an unbounded set | "Among charts exhibited by the card or the auditor before S6" |
| §2.3: "under some m ∈ 𝔐_std"; "the smaller construction" | Existential over all standard models; "smaller than what" is unclear | RT-33 |
| NR-4: "X appears under 𝒦_∅" | Quantifier unspecified. Read as "some Ξ", every card is RELOCATED, since Sol ⊆ 𝒳 | "On at least p_dec of the reference measure on 𝒳, and on every lock-fiber instance" |
| NR-5: "persist as λ → 0" | A limit claim, which DC-4 says earns nothing | Evaluate at λ = 0 (if in domain), 2^(−p★) and 2^(−2p★) |
| NR-6: ℓ_dec = ½·F_X | For small instances this is below one 6-bit token; unclear whether RB/SPS templates are capped by it | Templates are uncapped; ℓ_dec := max(½·F_X, 24 bits) |
| XS-7: n_B and F_p | Undefined | Define both, or drop n_B |
| LT-1 route 2: "a protocol subset disjoint from the one used to evaluate O" | Every A ∈ 𝔄 must contain a₀, so disjointness is impossible, or a₀ sharing is allowed silently | Allow a₀ on both sides, with records from independent runs |
| §15.9(b) and Q1: reciprocity holdouts are standard-model environments | Unclear what Q1 tests on them, since they are not solutions of 𝒦; G5-HOLD does not say whether data are measured or modelled | Specify the test object; measured data only (RT-12) |
| FC-1: b_struct(ℛ) = Σ ΔF(ι) | Includes the Π, T and support terms, which are not specific to ℛ. This contradicts FC-3 (D_diff = 0) and Q5 | b_struct(ℛ) := the reduction on joint coordinates of 𝒜^base versus 𝒜^base ∩ Z(ℛ) |
| BU-6: "the route declares its final count" | Who declares is not said | The owner (RT-43) |
| DIF-6: "the card's declared ε_C" | Meaning undefined | Define it, or delete it |
| KP-4: "without new theory" | Undefined | "Using only the frozen harness and the card's reference implementation" |
| I_𝒦, Ch-5: "structurally distinct… mutually independent data" | No test is given | Define distinctness by non-isomorphic 𝒞 and disjoint seeds, decided by the auditor |
| VAR-1: "the whole battery universe"; a translation search up to 32 bits | Universe undefined; who runs a 2^32 search, with what resources, is unspecified | Fix the universe as battery, AI-1 to AI-3 and lock fibers; card bears the burden of proof, auditor search capped by R_item |
| MC-6: R1's 10-item checklist | Has POST-RESULT SEED status (PV-5) and is not quoted in the charter | Quote it verbatim into the charter and freeze it |
| RH-WC, RH-MF, RH-TH: "weak", "macroscopic" | No thresholds, so regime status cannot be decided | Frozen numeric thresholds per regime hypothesis |
| §13.4: closure of 𝒮 "by published standard theorems" | Open-ended, so Q3 status is never final | Freeze the closure at S9 completion; later derivations go through PV-3 recompute |
| CV-1, §4.7: "until the owner rules" | Owner discretion after Card 1 has no bound | RT-23 |

**New [P] constants this would need in Appendix A:** r_lock, σ_pre, D_batch, T_harness, T_audit, T_lock, R_item, R_card, the LOCK-H pool size, the record binning rule, and t₁.