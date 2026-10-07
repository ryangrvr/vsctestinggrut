# Red-team of Stage-3 Charter v0: definitional and tautological wins

## Input defect (fix first)

- The "CHARTER v0" in this task is only the 615-character traceability tail of the synthesizer's last message.
- The full v0 is the long assistant text block on line 89 of `/root/.claude/projects/-home-user-vsctestinggrut/1a09ed24-aca1-5a3e-824d-0bafde87a0b5/subagents/workflows/wf_05020bc5-5e7/agent-a6668d58e88f57631.jsonl`. It runs 1,792 lines, covering §§0–25 and Appendices A–E.
- I copied it verbatim to `/tmp/claude-0/-home-user-vsctestinggrut/1a09ed24-aca1-5a3e-824d-0bafde87a0b5/scratchpad/rt_def/charter_v0.md` and red-teamed that copy. Every quote below comes from it.
- The other red-team lanes probably received the same tail, so their results should be checked. The script should capture the longest assistant text block, not the last one.

## Why the patterns work (four root causes)

1. **Off-slice certificates.** Q2 tests against 𝒟. Q3 accepts witnesses whose interface is supplied by hand. Q5 accepts a rectangle anywhere in 𝒜. None of these points is a tuple the card actually produces. The card chooses how ℛ★ extends away from its realized set, so it can pass all three with a relation that says nothing on that set.
2. **Card components have no typing.** X_Π, X_Z, X_h, X_T, Obs and s_T may read objects downstream of them (Γ, ε). Partial pipelines count as W-pipes ("lacks X").
3. **Credit is not specific to ℛ.** ΔF, c and b_struct are totals for the whole law. Im* drops non-standard points. Two relations double count. b_meas depends on the coordinate chosen for the observable.
4. **The definitional and standard closures are fixed lists.** DEF-1 to DEF-11 freeze R1's constants. 𝒮 closes only under "published standard theorems". B-SRB receives only the data the card chooses to consume.

---

## Gaming patterns

All patterns are abstract. Each is labelled CHARTER TEST and none is a physical proposal. I propose adding them to §24.1 as CT-60 to CT-75.

### CT-D01 Circular extractor (CHARTER TEST)
**Pattern.**
- A component computes its output from objects downstream of it. Examples:
  - X_Π returns the cut at which a record-law functional, or ε on candidate cuts, is extremal or crosses a threshold.
  - X_T returns the subgroup of a frozen tier that aligns P_{a₀} with the other P_a.
  - X_h picks the readout representative by a record statistic.
- The reading can be direct, or indirect by simulating Obs under each protocol inside the component.
- ℛ★ is the extractor's defining condition, or its stationarity condition. It therefore holds wherever the extractor returns a value.

**Slips through.**
- PC-1 to PC-5 constrain uniformity, price, covariance, decidability and ablatability. They do not constrain what a component reads.
- Q2 asks only that "some tuple in 𝒟(ι) violates ℛ". 𝒟 treats Π, T and Γ as independent, so a violator always exists.
- NR-2 applies only to "𝒦 in clause normal form", not to components.
- NR-13 ("No objective, penalty or selection criterion is monotone in ℛ") misses a stationarity condition, which is not monotone in the objective.
- NR-1 ("lists every symbol and flags any that names or encodes a protected structure") either exempts components, in which case D01 passes, or flags every card, because X_h, X_T and Obs must name readouts and record maps (see A-1).

**Fix.** Add §1.2 **PC-6 Upstream-only reads**:
> Each component reads only objects upstream of it:
> - X_Π reads (Ξ, 𝒞);
> - X_Z reads (Ξ, Π);
> - Obs reads (Ξ, Π) and returns records;
> - X_h reads (Ξ, Π, Z_Π) and the definition of Obs as a map;
> - X_T reads (Ξ, Π, Z_Π, [h]) and the definition of Obs as a map;
> - s_T reads T_Π.
>
> No component other than Obs evaluates a protocol. No component evaluates, estimates or recomputes (from Ξ or otherwise) any of: a record law P_a, a functional of Γ_Π, ε, d_op, P★, a chart coordinate, a certificate, or a charter scoring function.
>
> The harness enforces this in two ways:
> - a call-graph inspection of the reference implementation;
> - a substitution test: replacing every per-protocol law produced by Obs with an independent draw of the same type, with Obs's definition unchanged, must leave the outputs of X_Π, X_Z, X_h, X_T and s_T unchanged.
>
> Violation: the affected structure is RELOCATED in the pipeline, and every relation whose responsibility map touches it is CARD-DEFINITIONAL.

### CT-D02 Pipeline identity gated by the preconditions (CHARTER TEST)
**Pattern.**
- ℛ★ holds at every Ξ of the type where the chain is defined and the gate preconditions hold: Π persistent and nontrivial, carrier PASS, T_Π admissible. This is a fact about the type plus the components.
- 𝒦's only role is to make the preconditions true.
- W-pipes come from points Ξ ∉ Sol where Π is non-persistent or undefined.
- The effect is that persistence, which FC-3 credits at zero ("D_diff = 0"), is laundered into lock credit.

**Slips through.**
- NR-3 accepts "some Ξ ∉ Sol … whose pipeline output **lacks** X".
- Q4 asks for "Some Ξ … ∉ Sol [that] has a pipeline image that violates ℛ", and a non-persistent image qualifies.
- NR-4's "X appears under 𝒦_∅" is undefined when X is a relation.
- FC-4 excludes only restrictions that hold "for every Ξ ∈ 𝒳 consistent with 𝒞", not every Ξ in the gate domain.

**Fix.** Add to §1.3:
> **Gate domain.** Dom_pre(ι) := {Ξ ∈ 𝒳 consistent with 𝒞_ι : every chain map is defined at r★ and r★★; Π is persistent, A-stable and nontrivial; the carrier is PASS; T_Π ∈ 𝕃_T^adm}.
>
> Dom_pre^X drops the conditions that X itself must meet.
>
> Extractors are total: outside their domain they return a declared ⊥.

Add **DEF-12 Pipeline identity:**
> ℛ holds at every Ξ ∈ Dom_pre(ι), on every in-domain instance, whether or not Ξ ∈ Sol.

FC-4 also applies on Dom_pre.

**Q4 (replacement):**
> Some Ξ ∈ Dom_pre(ι) ∖ Sol has a *defined* pipeline image that violates ℛ by more than the lock resolution. A ⊥, undefined or non-persistent image never counts.
>
> The responsibility map must show that deleting 𝒦's clauses removes ℛ. Dependence on the type, extractors, representation or prior in addition to the clauses is allowed only if DEF-12 does not fire.

**NR-3 (replacement):**
> - **For X = Π:** a W-pipe is some Ξ ∉ Sol with no persistent nontrivial Π, or with VI_norm > δ_Π.
> - **For every other X ∈ {Z_Π, [h], T_Π, Gibbs/FDT, ℛ★}:** a W-pipe is some Ξ ∈ Dom_pre^X(ι) ∖ Sol whose pipeline yields a defined and different X. That means one of:
>   - carrier FAIL (not UNRESOLVED and not ⊥);
>   - a different readout class or interface class;
>   - a Q4 violation of ℛ★.
> - "Lacks X" counts only when X = Π.

**NR-4 "appears":**
> - X ∈ {Π, Z_Π, [h], T_Π} appears under 𝒦′ ∈ {𝒦_∅, 𝒦_𝒮} if the pipeline on Sol_{𝒦′} returns X within tolerance on a reference-measure fraction ≥ p_dec of Dom_pre^X.
> - ℛ★ appears under 𝒦′ if it holds on Dom_pre under 𝒦′.

### CT-D03 Off-slice extension (CHARTER TEST)
**Pattern.**
- The law makes two separate single-axis restrictions on Sol:
  - it fixes the interface at u_K = (Π, [h], T_Π);
  - it pins a response coordinate, g(Γ) = g₀.
- ℛ★ is then written in one of two forms:
  - (u = u_K ∧ g = g₀) ∨ (u ≠ u_K ∧ C(u, Γ)), for any joint C;
  - g(Γ) = G(u), for any G that passes through G(u_K) = g₀.
- On the realized set, ℛ★ is just the pin. Its jointness lives only where the law never goes.

**Slips through.**
- Q5's rectangle needs "(u₁, Γ₁) and (u₂, Γ₂) [in] Z(ℛ); (u₁, Γ₂) and (u₂, Γ₁) [in] 𝒜(ι | H)". Here u₂ can be any unrealized baseline interface.
- Q2 finds its violator in 𝒟, off the realized slice.
- Q3 is met by a witness with u_K supplied by hand and g ≠ g₀.
- Q6 ("c ≥ 1 at every lock fiber") is met by the pin itself, because c is the law's codimension, not ℛ★'s.
- B-SRB treats u_K as "generated, treated as supplied", which leaves g free, so b_meas is large.
- MC-2 needs only that "at least one input to the prediction is an interface-side measurement", even if the prediction ignores that input.
- §22 lists "Restrictions on a single axis … presented as ℛ" as not credited, but its only enforcement is Q5, which passes.

**Fix.** Replace Q5 with a test on the realized projections:
> **Q5 Joint (realized coupling).**
> - The card declares a lock family 𝓘 at freeze. 𝓘 contains in-domain instances that share one chart, and includes AI-1, the lock fibers and the AI-3 draws in the domain.
> - **U** is the set of realized interface values: (Π, Z_Π, [h]_{T_Π}, T_Π, and the declared interface statistics) over 𝓡_𝒦 on 𝓘.
> - **R** is the set of realized response values: frozen chart coordinates of Γ that do not depend on u. ε_R and every T-invariant functional count as response-side.
> - The product hull is 𝓗 := 𝒜(𝓘|H) ∩ (cl U × cl R).
> - **b_J(ℛ) := F_p(𝓗) − F_p(𝓗 ∩ Z(ℛ))**, using the frozen §2.5 F_p with ε evaluated at each point's own T.
> - Q5 holds if and only if both:
>   - b_J(ℛ) > 0;
>   - the reduction is witnessed by u₁, u₂ ∈ U that differ in Π, in Z_Π, or in a declared interface statistic.
> - If U is a single point, the relation is NONJOINT.

**Q6:**
> b_J ≥ log₂ Q_min (discrete case), or codim_𝓗 Z(ℛ) ≥ 1 (continuous case), at every lock fiber; and b_meas ≥ log₂ Q_min.

**FC-1:**
> b_struct(ℛ) := b_J(ℛ). ΔF(ι) remains the law-level report and is never credited to a relation.

### CT-D04 Jointness manufactured by ε's dependence on T (CHARTER TEST)
**Pattern.**
- ℛ★ restricts only ε_R (or another T-invariant functional) at the realized tier, for example a window on ε. T_Π is constant on Sol.
- The rectangle witness is built by swapping tiers: (T_Π, Γ₁) and (T′, Γ₂) satisfy ℛ★, while (T_Π, Γ₂) violates it because ε[Γ₂, T_Π] ≠ ε[Γ₂, T′].
- The only "interface" dependence is the definitional T-argument of ε (DEF-1, DEF-4).

**Slips through.**
- Q5 places ε_R on the response side ("Z_Γ on the response side (Γ, ε_R)").
- But the rectangle witness is stated in (u, Γ) pairs, so the cross points recompute ε at the swapped tier. Read that way, the rectangle exists.

**Fix.** Add to Q5:
> - Variation of T_Π alone never establishes jointness.
> - Variation of the tier at which ε or a T-invariant is evaluated never establishes jointness either.
> - A relation whose interface dependence enters only through that tier is NONJOINT.

This is already built into the CT-D03 wording, which requires u₁ and u₂ to differ in Π, in Z_Π, or in a declared interface statistic.

### CT-D05 Conditional definitional identity, which turns an inequality into an equality (CHARTER TEST)
**Pattern.**
- On a class 𝒫 of record families, ε satisfies an exact identity with other chart coordinates: ε = κ·W for some T-invariant witness W, or an exact formula for a protocol pair. 𝒫 may be open (inequality-defined) or single-axis.
- 𝒦 forces Γ ∈ 𝒫, and ℛ★ is the identity.
- ℛ★ fails outside 𝒫. Its only physical content is Γ ∈ 𝒫.
- The lock observable o := ε − κW then has I_K = {0} ± σ. I_SRB is wide whenever the same inputs do not force 𝒫.

**Slips through.**
- Q2 requires only that ℛ be "none of DEF-1 to DEF-11".
- DEF-5 lists only "Witness bounds with frozen constants".
- DEF-11 requires truth on all of 𝒟.
- §2.5 ("reductions that only shrink a log-volume through inequalities are … never credited") is bypassed, because the relation earns its credit through b_meas.

**Fix.** Add **DEF-14 Conditional identities:**
> Any statement P ⇒ Q in which Q follows from DEF-1 to DEF-13 under hypothesis P.
>
> If such a P holds on the realized set and is either single-axis or open, every relation equivalent to Q on the realized set is assessed as P:
> - NONJOINT if P is single-axis;
> - uncredited if P is open (§2.5).

**Q2(c):**
> The auditor may exhibit such a P. Burden: the card.

### CT-D06 Unpublished identity of the card's own quotient (CHARTER TEST)
**Pattern.**
- ℛ★ is a theorem of pure mathematics about ε at the card's generated T_Π with its reduction s_T. It could be an exact formula, a bound with new constants, or a link to ε at a frozen tier.
- ℛ★ fails at tuples of 𝒟 with other T, so it is not a 𝒟-tautology.
- It is published nowhere and contained in no STD item.

**Slips through.**
- DEF-5 covers only "frozen constants".
- DEF-11 requires truth on all of 𝒟.
- §13.4: "𝒮 includes every relation derivable from STD-1 to STD-12 by **published** standard theorems".
- B-SRB "computes I_SRB(o) from STD-1 to STD-12 … using SFP-1 to SFP-6", with no instruction to push standard predictions through the card's ε code.
- Q3 is met by a witness with a frozen tier supplied by hand.

**Fix.** Add **DEF-13 Mathematics of ε:**
> Everything that follows by valid mathematics, published or not, from the definitions of ε and d_op at any admissible class (the frozen tiers, or T_Π with its s_T) and from the card's component definitions, with any constants. This explicitly includes:
> - repertoire monotonicity: A ⊆ A′ ⇒ ε(A) ≤ ε(A′);
> - ½·D_T ≤ ε ≤ D_T, where D_T := max_{a,b} d_op^T(P_a, T·P_b), wherever d_op^T is an orbit pseudo-metric;
> - the time-marginalization and coarse-graining facts wherever they hold;
> - exact two-protocol formulas;
> - witness bounds.

**Q2(a):**
> ℛ is not implied by DEF-1 to DEF-15. DEF-12 is tested on Dom_pre; the others on 𝒟.

**Q2(b), fiberwise:**
> For every realized u ∈ U, the definitional fiber 𝒟(ι | u) contains a response value that violates ℛ.

**§13.4 (replacement):**
> 𝒮 is closed under valid mathematical derivation, published or not, from STD-1 to STD-12, DEF-1 to DEF-15 and the card's component definitions.
>
> Non-implication is certified only constructively, by a Q3 witness. Without one, CV-1 applies.

### CT-D07 Lossy canonical reduction (CHARTER TEST)
**Pattern.**
- s_{T_Π} is invariant but not maximal. It discards everything except a chosen statistic.
- d_op^{T_Π} is invariant, as the charter asks, but it vanishes between different T_Π-orbits.
- ε^{T_Π} therefore becomes a discrepancy the card designed. DIF-5's nontriviality test becomes trivial.
- This feeds CT-D05 and CT-D06.

**Slips through.**
- §1.4 requires only that the card "proves that d_op^{T_Π}(P, T_Π·Q) := min_{k∈K} d_BL(s(P), k#s(Q)) is invariant under T_Π acting on both arguments".
- 𝕃_T^adm admits any "generated T_Π with a proved canonical reduction".

**Fix.** §1.4 (replacement):
> The card proves three properties on its declared law class:
> - **(i) Invariance:** s(t#P) ∈ K·s(P) for every t ∈ T_Π.
> - **(ii) Maximality:** s(P) ∈ K·s(Q) ⇒ P ∈ T_Π·Q.
> - **(iii) Faithfulness:** d_op^{T_Π}(P, T_Π·Q) = 0 if and only if P ∈ T_Π·Q. Hence ε^{T_Π} = 0 if and only if the family is T_Π-separable (**DEF-15**, the analogue of Theorem A).
>
> The harness checks (ii) and (iii) on B-REC and on HB-1 to HB-9, with seeds committed after the batch closes.
>
> A reduction that is invariant but not maximal leaves ε undefined for the card, and every ε-relation fails Q8.

### CT-D08 Response absorbed into the interface class (CHARTER TEST)
**Pattern.**
- X_T builds T_Π from the maps through which each protocol moves the record, computed from the protocol's action on Ξ.
- Y_a = t_a(h(Z)) with t_a ∈ T_Π then holds by construction, so carrier PASS is definitional.
- The E-B twin's readouts h_a = t_a∘h fall inside [h]_{T_Π}, so MODE SELECTION can never fire.
- ε^{T_Π} measures only what the card chose to leave out of T_Π.

**Slips through.**
- NR-10(f) requires readout redundancy only for [h] ("[h] is derived as the readout redundancy of the card's own observation map").
- T_Π is defined as "a group of record maps acting per protocol, generated from (Ξ, Π)".
- Carrier PASS holds "if and only if the card proves from 𝒦 that Y_a = t_a(h(Z_Π))".

**Fix.** Add **NR-10(h):**
> - Every t ∈ T_Π is a record-space map computed by X_T without evaluating any protocol, any protocol's action on Ξ, or any solution's response.
> - T_Π is one set for all protocols.
> - A map that encodes how a protocol moves the system or the environment is response, not interface.
> - If T_Π contains such a map, carrier PASS is definitional and every reciprocity relation is CARD-DEFINITIONAL.

### CT-D09 ε produced by the readout (CHARTER TEST)
**Pattern.** Obs either:
- ends in a fixed nonlinear map g on record space; or
- weights E-relata by a function of Π (distance to S, boundary membership, block size).

A pure mean response then gives ε^{T_lin} > 0 in general. R1 §7 notes that "an uncalibrated nonlinear detector fires Tier 1 on an exogenous environment". Alternatively ε becomes a function of Π through the weighting. ℛ★ is the resulting identity.

**Slips through.**
- NR-10(a) forbids only indexing "by protocol identity".
- Obs may take Π as an argument.
- B-REC says only that "each record is fed through the card's Γ_Π interface". It is unclear whether g and T_Π are applied, so the exogenous zero controls may never see g.
- DIF-5 asks only that some family have ε > 0 and some have ε = 0.

**Fix.** Add §1.2 **PC-7:**
> **(a) Static maps are calibrated out.** If Obs = g∘Obs′, with g a fixed map independent of protocol and state, then ε and the chart are computed on Obs′, as in R1 §1. A relation that depends on g is CARD-DEFINITIONAL.
>
> **(b) The readout is blind to the partition.** Obs reads only E(Π_ref) ∖ ∂, through one uniform map per relatum and one fixed symmetric aggregation declared at freeze. Weighting relata by any function of Π is a supplied readout structure (PS-3) unless 𝒦 generates it with a W-pipe.

Add **DIF-5(e) Exogenous-zero soundness:**
> - Each record is passed through the card's complete Obs chain, after the platform's calibrated maps are removed by their known maps.
> - HB-3, HB-4, HB-5 and C2-F′ must return ε^{T_Π} = 0 within certification tolerance. For SCOPE-Q, HB-1 must as well.
> - HB-8 never returns R1-PASS.
> - Failure voids every relation that uses ε^{T_Π}.

### CT-D10 Mode selection inside the persistence tolerance (CHARTER TEST)
**Pattern.**
- Obs pools whichever relata are currently in E (Π_a), or applies a state-dependent membership rule written as a single h.
- Protocols move up to η = 5% of relata across the cut, and ∂ holds up to 10%.
- Those relata enter and leave the readout with the protocol. The readout is formally "one h", but its support depends on the protocol.

**Slips through.**
- The tolerances "δ_Π / η / δ_∂ | 0.05 / 0.05 / 0.10".
- NR-10(a)'s rule against indexing "by protocol identity".

**Fix.** Add **PC-7(

c) Ablation:**
> Every credited quantity is recomputed with the contribution of ∪_a (Π_a Δ Π_ref) ∪ ∂ removed from the records. Each must stay within lock resolution. Otherwise the verdict is MODE SELECTION (NR-11).

### CT-D11 Tautology that appears when standard models run through the card's pipeline (CHARTER TEST)
**Pattern.**
- ℛ★ holds for generic standard models of the declared type when they are run through the card's own components.
- Abstract example: a relation between a size or boundary statistic of Π and a T-invariant record functional. It follows from Obs aggregating over E-relata plus a limit theorem for sums of weakly dependent terms.
- Q3 is met by a standard witness whose cut, readout or tier is supplied by hand. Such a witness violates ℛ★ trivially.

**Slips through.**
- §2.2 lets the baseline model "(iv) take Π, Z, [h] and T as supplied".
- Q3 asks only that "a witness m*_F ∈ 𝔐_F(ι | H) must violate ℛ".
- STD-9 "Applies under RH-MF" (mean-field), so a local or mixing type escapes it.
- B-SRB scores only the lock observable.

**Fix.** Q3, transplant bullet (replacement):
> **(a) Transplant.**
> - For each lock fiber, the Evaluator draws standard models of the declared type from NULL-ΠT under H. Parameters are generic: B-HB ranges under the charter reference measure, with seeds committed after the batch closes.
> - It runs the card's own components on them, using the card's realized Π wherever X_Π is undefined, followed by the charter ε code.
> - If ℛ★ holds within lock resolution on a reference-measure fraction f_std ≥ 1/Q_min of the draws, the card is CARD-STANDARD (implied by the pipeline).
>
> **(c) Hand-supplied interfaces.** A witness whose interface is supplied by hand is reported, but it never satisfies Q3 by itself.

**STD-9 (extended):**
> Applies under RH-MF or **RH-LOC** (E is a local or mixing system of n units read by a normalized aggregate).
> - It covers cumulant scaling with n and with the fraction of units that respond (dilution), and the Gaussian limits.
> - No credit for scaling of ε_R or of its witnesses with n, with block sizes, or with the boundary-to-bulk ratios of Π that these imply.

### CT-D12 Generic baseline identity with an exotic witness; a B-SRB that is starved or silent (CHARTER TEST)
**Pattern (a).**
- ℛ★ holds for every analytic, generic standard model in the regime. Examples are a leading-order identity across the templates a₊ and a₊₊ = 2α, or a symmetry identity.
- Q3 is met by a single standard witness that is fine-tuned, non-analytic or of measure zero.

**Pattern (b).**
- The card's prediction uses constants (θ_dict, platform calibration) that were fixed from platform data containing the reference correlators.
- B-SRB never sees those correlators, so it reports a wide I_SRB.
- Alternatively, B-SRB reports silence because no standard formula exists for the card's new quotient.

**Slips through.**
- Q3 accepts a single witness.
- BP-5: "The baseline receives exactly the data that the card's prediction consumes."
- B-SRB "computes I_SRB(o) from STD-1 to STD-12". How I_SRB is built is unspecified. Taking it as the hull of all 𝒮-admissible models favours the card.

**Fix.**

**Q3(b) Genericity:**
> A witness counts only if ℛ★ fails on an open parameter neighbourhood of it within its standard family.

**New regime hypothesis and standard constraint:**
> - **RH-AN:** record laws depend analytically on the template amplitude.
> - **STD-13 (under RH-AN):** the leading amplitude power in each T-irreducible channel is standard. So are the ratios across a₊, a₋ and a₊₊ that this power and symmetry fix.

**BP-5 (replacement):**
> The baseline receives:
> - every datum the prediction consumes;
> - every datum used to fix a constant that enters the prediction (θ_K, θ_dict, platform calibration);
> - always, the lock platform's reference law P_{a₀} and its correlators, up to the order the prediction uses.

**B-SRB procedure (replacement):**
> - I_SRB(o) is the **narrowest** interval obtained by any standard scheme valid under H(x), with that scheme's error bars. The schemes are SFP-1 to SFP-6, with 𝒮 closed under mathematics and DEF-1 to DEF-15.
> - It is computed by pushing the record families each scheme predicts through the charter's ε and witness code at T_Π.
> - "No standard formula exists for this quotient" is not silence.
> - I_SRB is never the hull of all 𝒮-admissible models.

### CT-D13 Definitional wins on the lock side (CHARTER TEST)
**Patterns.**
- **(a) Coordinate stretching.** The card reports o as φ(ε), for example log ε or 1/ε. The ratio |I_SRB|/|I_K| is not invariant under reparametrization, and with log ε, I_SRB is unbounded.
- **(b) Definitional observable splitting.** Several "independent" observables are linked by DEF identities. One example is ε on a pair together with ½·d_q on the same pair.
- **(c) Definitional prediction route.** O on the full grid or repertoire is predicted from sub-grid or marginal records of the same protocols, or from overlapping sub-repertoires, through DEF-13 bounds.
- **(d) Decorative interface input.** The prediction formally includes an interface measurement but does not depend on it, so the lock tests a pin.
- **(e) Platform cut selected by response.** The platform's Π or T_Π is identified by maximizing a record functional on calibration protocols. This does not "presuppose ℛ★", yet it couples the measured interface to the response.

**Slips through.**
- FC-1's b_meas formula.
- "An observable implied by the others under 𝒮 together with ℛ contributes 0", which omits DEF.
- MC-2: "A lock that predicts ε_R from the same Γ it is computed on is definitional." Sub-grid and marginal predictions are not addressed.
- MC-2: "At least one input … is an interface-side measurement."
- LT-1: "response-side data on a protocol subset disjoint", which says nothing about channels or times.
- MC-2: "A certification that presupposes ℛ★ is circular."

**Fix.** FC-1 b_meas (replacement):
> - Each o is a frozen chart coordinate, or a fixed affine function of frozen chart coordinates, in Appendix-A units and windows W(o).
> - b_meas = Σ_o log₂(|I_SRB(o) ∩ W(o)| / max(|I_K(o)|, 2σ_tot(o) at N_max)).
> - Reparametrizing o is prohibited.
> - Observables are independent only if none is implied by the others under 𝒮 ∪ DEF-1 to DEF-15 ∪ {ℛ★}, and their estimators share no records.

MC-2 (additions):
> - **Sensitivity.** There are two admissible values of the independently measured interface input whose predicted intervals I_K are disjoint. Otherwise the lock is a pin and SC3 fails.
> - **Response-side inputs** are allowed only from protocols, record channels and grid times all disjoint from O's. The map from those inputs to I_K must not be derivable from DEF-1 to DEF-15 ∪ 𝒮 alone.
> - **Platform interface.** The platform's Π and T_Π are obtained by the card's frozen X_Π and X_T applied to interface-side structural data only. No record-law functional of any protocol may be used.

### CT-D14 Credit earned by leaving the baseline (CHARTER TEST)
**Pattern.**
- Realized triples outside 𝒜^base (non-standard realizations, in regimes where 𝒮 is silent) are dropped from Im*.
- A law whose large realized set is mostly non-standard therefore gets a small Im* and a near-maximal ΔF and c, without reducing any freedom.
- If T_Π ∉ 𝒯, Im* is empty, which leaves ΔF undefined, makes Q1 vacuous and makes Q9 fail.

**Slips through.**
- "𝓡_𝒦 := Im* := Im ∩ 𝒜^base".
- "ΔF_disc = log₂|𝒜/~| − log₂|Im*/~|".
- "c(ι) := dim_lb 𝒜^base − dim_ub Im*".
- "A generated T_Π is added to 𝒯 for placement and ε computation only".

**Fix.** §2.5:
> - ΔF and c are computed on the **full** realized image: ΔF_disc := log₂|𝒜^base/~| − log₂|Im/~| and c(ι) := dim_lb 𝒜^base − dim_ub Im.
> - Non-standard realizations are reported and carry their kill conditions. They are never removed to shrink the realized set.
> - For membership in 𝒜^base, the generated T_Π counts as a class that can be supplied by hand.
> - Q1, Q5 and Q9 use Im.

### CT-D15 Dimension certified at a singular point (CHARTER TEST)
**Pattern.**
- The card certifies dim_ub by an exact Jacobian rank at an explicit point it chooses, where its parametrization of Sol is singular.
- A rank at one point is only a lower bound on the generic rank. It never bounds the dimension from above, so c is inflated.

**Slips through.** "dim_ub is certified by a proof, or by an exact rank computation at an explicit point."

**Fix.** Replacement:
> - dim_ub is the generic rank. It is certified by a proof, or by a proof that the parametrization is analytic on a connected domain together with the exact rank at points drawn with seeds committed after the batch closes (the maximum is taken).
> - A rank at a chosen point certifies only dim ≥ that rank.

### CT-D16 Structural credit counted twice (CHARTER TEST)
**Pattern.**
- The card declares a second relation with its own observable.
- FC-1 gives each relation b_struct = the same law-level total, Σ ΔF(ι).
- "Credited(𝒦) := Σ_ℛ b(ℛ) + D_sel" then adds them.

**Fix.**
> - Credited(𝒦) := b(ℛ★ ∧ ℛ₂) + D_sel, computed once, with b_J on Z(ℛ★) ∩ Z(ℛ₂) and b_meas over the union of independent observables.
> - Each relation is still scored separately for Q1 to Q12 and for its kill conditions.

---

## Ambiguous or uncomputable clauses

- **A-1. NR-1 scope.** It is unclear whether "every symbol" includes the components.
  - If it does, X_h, X_T and Obs necessarily name readouts and record maps, so every card is SUPPLIED and therefore NONGENERATIVE.
  - If it does not, the components are unpoliced (CT-D01).
  - *Fix:* NR-1 covers 𝒦, 𝒞, 𝒳, priors and Emb. The components are governed by PC-6 and PC-7.
- **A-2. §5.6 "ℛ★, or content implying ℛ★, supplied in any form → CARD-RELOCATED" conflicts with Q1.** Q1 requires 𝒦 to imply ℛ★, so every law that forces ℛ★ is "content implying" it.
  - *Fix:* "Supplied" means present in 𝒞, 𝒳, the components, priors or Emb, or in a clause that NR-2 flags as target-level.
- **A-3. B-NULL E-B twin: "ℛ★ or the derived carrier must exclude the twin."** The twin has the same Γ.
  - Any card with a derived carrier excludes the twin automatically, because the twin's readouts depend on the protocol. The clause is then vacuous.
  - Otherwise it rejects every ℛ(Π, [h], T, Γ).
  - *Fix:* Apply the card's X_h and X_T to the twin. It must return carrier FAIL or MODE SELECTION (this guards against CT-D08). ℛ★ need not separate it.
- **A-4. Q5's coordinates.** ε_R is listed on the response side, but the rectangle recomputes it at the cross points (CT-D04).
- **A-5. The range of 𝒟(ι).** Neither the range of T (𝒯 alone, 𝒯 ∪ {T_Π}, or all groups) nor "well-typed" is defined. DEF-11 and Q2 depend on both.
  - *Fix:* Π is any partition, [h] any class, T ∈ 𝕃_T^adm ∪ {T_Π}, and Γ any well-typed family.
- **A-6. 𝔐_F(ι | H), "applicable", and "A framework with no witness: ℛ is RESTATED by it" are undefined.** A framework that cannot express the type either forces RESTATED or is silently skipped.
  - *Fix:* 𝔐_F := the 𝔐_std models built in F. F is applicable if and only if it has a model of the declared type under H. Inapplicable frameworks are listed with reasons. At least two applicable frameworks are required.
- **A-7. How I_SRB is built (hull of models or narrowest scheme) and what |·| means.** |·| is undefined for points, unions, unbounded intervals, and the 0/0 case. *Fix:* CT-D12 and CT-D13.
- **A-8. CV-2 lets the evaluator add "larger hostile families", but this cuts both ways.** Enlarging 𝒜^base raises dim_lb and ΔF, and widens I_SRB. Both help the card.
  - *Fix:* Enlargement is allowed for Q3 transplant draws, for 𝒮 derivations and for the narrowest I_SRB. It is not allowed for 𝒜^base, ΔF or c.
- **A-9. "Credit is computed on whichever admissible chart minimizes the credited bits."** The chart family is unbounded, so the minimum cannot be computed.
  - *Fix:* Use a frozen chart family plus at most N_ch [P] auditor coordinates registered before evaluation.
- **A-10. NR-6's ℓ_dec = ½·F_X is smaller than one 6-bit token at the frozen sizes.** For Π at n = 8 it is about 4 bits; for T it is about 1.2 bits. The "any uniform L₀ decoder" clause is vacuous, and RB/SPS carry no price cap.
  - *Fix:* ℓ_dec := max(½F_X, 60 bits [P]). RB and SPS always run.
- **A-11. NR-10(c) "derived … not by definition" has no test.** X_Z is card-supplied, so every Z_Π is "by definition".
  - *Fix:* Use the NR-3 W-pipe in Dom_pre^carrier (carrier FAIL off Sol) plus PC-6. Drop "not by definition".
- **A-12. B-REC "fed through the card's Γ_Π interface".** It is unclear whether the card's static maps and T_Π apply, and at which tier the "required value" holds. *Fix:* DIF-5(e).
- **A-13. §4.4 "residual bits needed to describe the card's realized data".** No code is specified, either for the card or for NULL-ΠT.
  - *Fix:* A uniform code over chart cells at resolution 2^(−p★) on 𝓘: within Im for the card, and within 𝒜 for the null.
- **A-14. Appendix A: "α = 1 null-protocol standard deviation".** The variable is not named, and t₁ is undefined. If α is in record units, the templates are calibrated by the response, and amplitude-scaling relations become partly definitional.
  - *Fix:* α is 1 SD under a₀ of the driven S variable, never of a record. t₁ := [P]. The template-to-Ξ map is part of Emb: uniform, priced and frozen.
- **A-15. §1.3 lets the card choose between a time-indexed Π (tested against Π_ref) and a global Π (tested pairwise).** The two tests differ. *Fix:* Both must pass.
- **A-16. NR-7 "X tracks the scrambled component" and NR-16 "a systematic pattern" have no statistic.**
  - *Fix:* NR-7 uses agreement measured at p_dec. NR-16 is a preregistered binomial test comparing holdout and public failure rates at α.
- **A-17. "A derivation from 𝒮 … STANDARD-IMPLIED" is only semi-decidable.** *Fix:* The constructive-witness rule in §13.4 (CT-D06).
- **A-18. Q1 is inconsistent with itself.** It says "𝓡_𝒦(ι) ⊆ Z(ℛ)" with 𝓡_𝒦 = Im*, and also requires "all of Sol". Q5 and Q9 use Im* and ignore non-standard realized points. *Fix:* Use Im throughout (CT-D14).
- **A-19. FC-2 removes distinctions reproduced by "a vocabulary item or an import" but does not name ablation of the type, Emb or Obs.** FC-4 covers it only through "every Ξ ∈ 𝒳".
  - *Fix:* Remove every SEL distinction reproduced under 𝒦_∅ or 𝒦_𝒮 on Dom_pre.

## Additions to §19.3 harness validation

Build each of the following from HB models plus supplied structure, with no law involved. Each must be rejected with its predicted terminal before the freeze:

| Test | Construction (abstract) | Required terminal |
|---|---|---|
| CT-D01 | X_T reads Γ on HB-2 | CARD-DEFINITIONAL |
| CT-D03 | Disjunctive pin | NONJOINT |
| CT-D04 | Tier-swap rectangle | NONJOINT |
| CT-D07 | Invariant but non-maximal s_T | Q8 void |
| CT-D08 | Protocol-induced maps added to T on HB-1 | CARD-DEFINITIONAL |
| CT-D09 | Static g applied on HB-4 | DIF-5(e) fails |
| CT-D13(a) | log-reparametrized o | b_meas computed in frozen units |

## Priority

1. PC-6 (upstream-only reads).
2. Dom_pre and DEF-12.
3. The Q5/Q6 product-hull coupling b_J, which replaces b_struct.
4. The Q3 transplant test plus the B-SRB/BP-5 replacements.
5. A maximal and faithful s_T (DEF-15).
6. b_meas in frozen coordinates, plus the MC-2 sensitivity test.

The rest are tightening.