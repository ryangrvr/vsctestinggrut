# Red-team of Stage-3 Charter v0. Lens: compression and pricing loopholes

**What I reviewed.** The task text contained only the Appendix E tail, so I reviewed the full v0 at `/tmp/claude-0/-home-user-vsctestinggrut/1a09ed24-aca1-5a3e-824d-0bafde87a0b5/scratchpad/rt_def/charter_v0.md` (1792 lines), against G2-11, RULES, STATE and the SD0 compactness precedent.

**Constraint kept.** Every item below is an abstract **CHARTER TEST** gaming pattern. None of them is a physical proposal or a candidate 𝒦. Nothing was edited or committed.

## 0. Structural finding to settle first: the credit scale pushes cards toward gaming

This is a rough paper estimate, not a theorem.
- **What an honest relation can earn under v0.** A relation with coupling codimension 1, on the ≤ 3 credit instances, earns at most 3·p★ = 30 bits of continuous credit. The Π and T terms add up to about 55 bits more, and D_sel adds ≤ 10 bits.
- **What a card costs.** Every component (X_Π, X_Z, X_h, X_T, Obs, Emb, the 𝒳 declaration) is priced at 6 bits per token (PC-2, §4.1). A realistic Price is therefore a few hundred bits.
- **The consequence.** SC2 requires ρ ≥ 2, so Credited must be several hundred bits. That is only reachable by:
  - inflating c through the chart or through rigidity (RT-01, RT-05);
  - multiplying lock observables (RT-07);
  - counting the same bits twice (RT-02, RT-04).
- **The risk.** As written, the thresholds reward exactly the loopholes below, and may be unreachable for an honest card.
- **Proposed fix.** Add self-test ST-6 (§E). Then choose one of two options: (a) let credit scale over N ≥ 16 Selector-drawn instances with independent data, each worth p★·c_J; or (b) recalibrate ρ. Either way, close the loopholes first.

---

## A. Credit side: bits counted that the intent does not allow

### RT-01 CHARTER TEST: rigidity credited as if it were the relation
- **Pattern.** A law whose realized set is rigid on the Γ axis (a few points in a rich chart), paired with an ℛ★ that is only weakly joint. The full freedom reduction of the card is then credited to ℛ★.
- **Slips through.**
  - FC-1: "b_struct(ℛ) = Σ over ι ∈ I_𝒦 of ΔF(ι)".
  - §2.5: "ΔF(ι) = p·c(ι) + min(16, ΔF_Π) + min(log₂5, ΔF_T) + ΔF_supp".
  - ΔF is a property of the card's image, not of ℛ. Q5 only gates.
- **Fix.** Replace the b_struct line with:
  > For X ⊆ 𝒜(ι|H), Rect(X) := (π_I X × π_Γ X) ∩ 𝒜(ι|H), with π_I onto (Π,[h],T) and π_Γ onto Γ. Let Z_ℛ(ι) := Z(ℛ) ∩ 𝒜(ι|H).
  > - **Coupling codimension:** c_J(ℛ,ι) := dim_lb Rect(Z_ℛ(ι)) − dim_ub Z_ℛ(ι).
  > - **Coupling bits:** κ_J(ℛ,ι) := log₂|Rect(Z_ℛ(ι))/~| − log₂|Z_ℛ(ι)/~|.
  > - **b_struct(ℛ) := Σ_{ι∈I_𝒦} [p★·c_J(ℛ,ι) + κ_J(ℛ,ι)]**, computed after 𝒮.
  > - ΔF(ι) is reported for SC1 only and never enters Credited.

### RT-02 CHARTER TEST: the same bits counted under two relations
- **Pattern.** The card declares ℛ★ and a secondary ℛ₂. Both inherit b_struct = Σ ΔF(ι), and Credited adds them together.
- **Slips through.**
  - "Credited(𝒦) := Σ_ℛ b(ℛ) + D_sel".
  - "never credited to ℛ★ (no cross-subsidy)" forbids transfer between relations, but does not forbid duplication.
- **Fix.**
  > Credited(𝒦) := b(ℛ★) + b_inc(ℛ₂) + D_sel, where b_inc(ℛ₂) := max(0, b(ℛ★ ∧ ℛ₂) − b(ℛ★)).

### RT-03 CHARTER TEST: conjunctive padding
- **Pattern.** ℛ★ = (a restriction on one axis that is non-standard and non-definitional) ∧ (a coupling term that is definitional or standard-implied). The certificates are passed through the padding:
  - Q3 witnesses violate the padding, not the coupling;
  - Q2 is violated through the padding;
  - Q6's codimension comes from the padding;
  - Q5 holds because one rectangle witness exists.
- **Slips through.**
  - Q3: "a witness m*_F … must violate ℛ".
  - Q2: "some tuple in 𝒟(ι) violates ℛ".
  - Q5's single rectangle witness.
  - CT-27 catches only exact rectangles.
- **Fix.** Restate the certificates on the coupling part:
  > - **Q2:** some tuple in Rect_𝒟(Z(ℛ)) \ Z(ℛ) exists.
  > - **Q3:** Obs(m*_F) ∈ Rect(Z_ℛ(ι)) \ Z(ℛ), violated by more than the lock resolution. A witness that violates a single-axis consequence of ℛ does not count.
  > - **Q6:** c_J ≥ 1 or κ_J ≥ log₂ Q_min at every lock fiber.
  > - **Q5:** c_J ≥ 1 or κ_J > 0. One rectangle witness is necessary, not sufficient.
  >
  > Add CT-60 (padding) → CARD-NONJOINT or CARD-STANDARD.

### RT-04 CHARTER TEST: differentiation credited despite FC-3
- **Pattern.** A law that does nothing but generate a unique persistent Π and T on 3 instances collects 3·(16 + 2.32) ≈ 55 bits. The discrete ΔF is also summed per axis, so it credits restrictions on single axes and gives zero for pure coupling, which is the reverse of the intent.
- **Slips through.**
  - "ΔF_disc = … on the Π, T and support axes, subject to the caps".
  - This contradicts FC-3: "D_diff = 0. Persistence and differentiation are gates".
  - ΔF_supp is also uncapped. Choosing a large scenario as a credit instance inflates it without limit.
- **Fix.**
  > Delete min(16, ΔF_Π), min(log₂5, ΔF_T) and ΔF_supp from every credited quantity. They are reported under SC1 and the G4 gates only. Selectivity is credited only through FC-2.

### RT-05 CHARTER TEST: chart inflation
- **Pattern.** The card declares a chart with many coordinates (for example all cumulant coordinates up to order m, over the grid, for every protocol). Then dim_lb 𝒜^base is large, a rigid image has dim_ub = 0, and c is in the tens per instance. The card also takes credit at r★★, which has more coordinates.
- **Slips through.**
  - "The card declares it and the auditor may add coordinates. Credit is computed on whichever admissible chart minimizes the credited bits."
  - "admissible" is undefined.
  - Adding coordinates usually *raises* c, so the min does not stop inflation.
- **Fix.**
  > The chart φ is frozen by the charter for each scope and resolution, and is generated by the harness before Card 1:
  > - Scope Q: every T-invariant witness coordinate of order ≤ m on the template grid.
  > - Scope G: the response functionals listed in Appendix A.
  >
  > Cards neither add nor remove coordinates. c_J ≤ the number of functionally independent scalar equations in ℛ★. Credit is the minimum of the values at r★ and r★★.

### RT-06 CHARTER TEST: credit from realizations outside the baseline
- **Pattern.** Most realizations of the law lie outside 𝒜^base, in regimes declared "outside 𝒮's established domain". Then Im* = Im ∩ 𝒜^base is tiny and ΔF is close to the full baseline. ℛ only needs to hold on Im*, so it can fail on the non-standard part.
- **Slips through.**
  - "𝓡_𝒦 := Im* := Im ∩ 𝒜^base".
  - Q1: "𝓡_𝒦(ι) ⊆ Z(ℛ)". This contradicts the very next line, "on all of Sol".
- **Fix.**
  > Replace Im* with Im in §2.5, §3.1 and §4.3. Q1 becomes: Im(ι) ⊆ Z(ℛ). Realizations outside 𝒜^base enlarge the denominator of every credit term and never shrink it.

### RT-07 CHARTER TEST: multiplying lock observables
- **Pattern.** One relation is split into many "independent" lock observables (protocol pairs, grid points, settings). Each one's marginal SRB interval is wide, even though a few shared standard parameters fix all of them jointly. Summing the marginal log-ratios overcounts. The N_max budget also grows with the number of observables.
- **Slips through.**
  - "b_meas(ℛ) = Σ over independent lock observables o of log₂(|I_SRB(o)| / …)".
  - MC-7: "N_max = 10⁹ … per lock observable".
- **Fix.**
  > b_meas(ℛ) := log₂(vol J_SRB / vol J_K), where:
  > - o⃗ is the vector of all of the card's lock observables;
  > - J_SRB := {o⃗(m) : m is one regime-matched standard model under the B-SRB inputs}, the joint image and never a product of marginals;
  > - J_K is the card's joint region, inflated by 2σ_tot in each coordinate.
  >
  > Cap: b_meas ≤ p★·Σ_fibers c_J. N_max and the 30 days are totals per card.

### RT-08 CHARTER TEST: a lock that uses only response data
- **Pattern.** The card uses LT-1's second route: it predicts O on protocol subset A₂ from response data on A₁, and adds one token interface input to satisfy MC-2. b_meas then credits extrapolation within Γ.
- **Slips through.**
  - "or from response-side data on a protocol subset disjoint from the one used to evaluate O".
  - MC-2: "At least one input to the prediction is an interface-side measurement".
- **Fix.**
  > Also cap b_meas at I_int := log₂(vol J_K^{∅I} / vol J_K). Here J_K^{∅I} is the card's own prediction recomputed with every interface-side input replaced by its full range over 𝒜_Π × 𝒜_T. The response-side route earns credit only through I_int.

### RT-09 CHARTER TEST: starving the SRB baseline
- **Pattern.** The card's prediction consumes as few inputs as possible, so the "same inputs" B-SRB is wide. Meanwhile the law's constants silently match published values for the platform, and LOCK-H draws on existing datasets.
- **Slips through.**
  - BP-5: "The baseline receives exactly the data that the card's prediction consumes".
  - B-SRB: "Input: exactly what the card's prediction consumes".
- **Fix.**
  > BP-5: the baseline receives every datum the card consumes **plus** the platform's standard calibration set Θ_std. Θ_std is every parameter standard theory would use for O that can be measured without the records used for O. It is declared in C13 and frozen before unsealing.
  >
  > A law constant whose implied value falls within the passing window of a published value specific to the platform, for any candidate LOCK-H dataset, is treated as a lock-side fit (IP-11).

### RT-10 CHARTER TEST: choosing the representation to inflate the interval ratio
- **Pattern.** The card reparametrizes O nonlinearly (an RM3 move) so that I_K is narrow where I_SRB is stretched. Scope-G observables have no frozen window, and I_SRB is read as the loose outer bound implied by the constraints.
- **Slips through.**
  - Appendix A windows cover only "[−4, 4] … [0, 2] for ε".
  - B-SRB never says whether I_SRB is an inner or an outer bound.
- **Fix.**
  > b_meas is computed in the observable's frozen parametrization, and is the minimum over {identity, log|·| when the observable has one sign on I_SRB}.
  >
  > I_SRB is the hull of values realized by certified regime-matched standard witnesses. It is never an outer bound from the constraints and never a window.
  >
  > The scope-G window is the observable's range over B-HB at Θ_std.

### RT-11 CHARTER TEST: two-part code computed on the card's own data
- **Pattern.** §4.4 compares description lengths on "the card's realized data", which the card itself generated. A rigid card has zero residual. NULL-ΠT, meanwhile, pays:
  - log₂|𝒜_Π| without the 16-bit cap;
  - the full cell count of the card's chart;
  - the cost of Γ arguably twice (once in Price(NULL-ΠT), once in the residual).
- **Slips through.**
  - §4.4: "plus the residual bits needed to describe the card's realized data".
  - "Price(NULL-ΠT) = log₂|𝒜_Π| + … + log₂(the number of φ-cells for Γ)".
- **Fix.**
  > §4.4 is reported only at Stage 3. It becomes a gate at Stage 5 on sealed LOCK-H or LOCK-E data:
  > - the card's residual is the distance from the measured o⃗ to J_K;
  > - the null's residual is the distance from o⃗ to J_SRB.
  >
  > Price(NULL-ΠT) := min(log₂|𝒜_Π/Aut|, the price of the cheapest SPS/RB selector that returns the null's Π) + log₂|𝒯∪{⊥}| + the framework index, on the frozen chart. Each cell count is used once.

---

## B. Price side: target vocabulary and background structure left unpriced

### RT-12 CHARTER TEST: vocabulary whose leverage is measured "alone"
- **Pattern.** A priced vocabulary item does its work only together with a short clause. With every non-vocabulary clause deleted, it restricts nothing, so ΔF_tgt(v) ≈ 0 and P_v is just the length of its definition.
- **Slips through.** "'Alone' means the card with every non-vocabulary clause removed."
- **Fix.**
  > ΔF_tgt(v) := max(the credit of 𝒦 with only v, Credited(𝒦) − Credited(𝒦[v ↦ v̄])), where v̄ is an uninterpreted symbol of the same signature with v's axioms deleted. SEL distinctions that change under this replacement are added.

### RT-13 CHARTER TEST: protected structure brought in through an imported component
- **Pattern.** The card imports a whole standard component that internally carries an S/E split, a Gibbs bath, Hilbert space or the Born rule. It pays about log₂|SFP menu| ≈ 6 bits. The component is referenced by name, so NR-1's unfolding and the VB-5/6/7 RELOCATED rule never see inside it.
- **Slips through.**
  - IP-8: "Priced at log₂|SFP menu| plus their constants".
  - NR-1 unfolds "definitions", and an import is not a definition.
- **Fix.**
  > An import is unfolded into L₀ before every firewall and pricing test. Its price is max(log₂|SFP| + its constants, L_stmt of the unfolding, Σ P_v over the VB items it uses).
  >
  > NR-1, NR-2, NR-12, IP-6 (including VB-5/6/7) and §5.6 apply to the unfolding. Import subtraction applies to b(ℛ) as well as to D_sel.

### RT-14 CHARTER TEST: base tokens that encode priced or protected structure
- **Pattern.** The card uses 6-bit base tokens instead of paying for vocabulary:
  - `law`, `kernel`, `E` and `cond-prob` applied to Ξ or to the relata give an unpriced measure (VB-13);
  - `⊗`, `parallel`, `pair` or `×` splitting V_Ξ give a factorization (VB-4) and effectively a pre-split partition (PS-1);
  - the 4 "Reserved" tokens could be assigned to macros.
- **Slips through.** The B.1 alphabet ("kernel cond-prob E ⊗ marginal do law support"; "sequential parallel contract wire"; "Reserved | — | 4").
- **Fix.**
  > These tokens are base only when every argument is an intervention, a record or a record law. Applied to Ξ, 𝒞, V_Ξ or a relatum, they are VB-13. Splitting V_Ξ or 𝒳 into blocks is VB-4, and NR-1 flags it as a PS-1 candidate. Reserved tokens are unavailable to cards.

### RT-15 CHARTER TEST: vocabulary re-derived in plain L₀
- **Pattern.** The card defines in ℚ arithmetic a function that satisfies the metric axioms, a positive semidefinite bilinear form, or a map from vectors to probabilities that is quadratic in its vector argument. No VB token appears, and CT-42 covers only "isomorphic L₀ tables", not definitions.
- **Slips through.** NR-1 is "(syntactic …)". IP-6 prices only named VB items.
- **Fix.**
  > The harness holds a finite axiom checklist for each VB item. Any defined symbol whose interpretation satisfies a checklist on any audit or battery instance *is* that item, priced at P_v. A match to VB-5, VB-6 or VB-7 triggers the selectivity RELOCATED rule. Every defined symbol carries a VB declaration, and an undeclared match found later → RELOCATED.

### RT-16 CHARTER TEST: target vocabulary carried in the battery data
- **Pattern.** Emb reads structure that comes with the battery for free:
  - SEL-7 cites `f0_sd0_k6_core.json`. I verified that this file stores explicit complex ray coordinates, which carry orthogonality and Hilbert-space structure.
  - The ordering of items in the file.
- **Slips through.**
  - "Emb is uniform and priced". Only Emb's statement is priced; the scenario data are not.
  - What Emb receives is never specified.
- **Fix.**
  > Emb receives only the abstract signature: ports, alphabets, the context hypergraph and the support. Labels are scrambled under RM1/RM2 by post-batch seeds. Rays, operator or vector representations, quantum witnesses, literature names and file order are withheld.
  >
  > Verdicts must agree across ≥ 2 seeds. Emb may add no relata, relations or weights beyond a uniform image of the incidence structure. Any reading beyond that is RELOCATED (NR-0).

### RT-17 CHARTER TEST: unpriced selection in the reference implementation
- **Pattern.** The code does more than the L₀ statement:
  - solver tie-breaking, ordering, initialization or tolerance picks particular elements of Sol;
  - it calls charter code (B-HB, the ε code, the 𝒮-checker) as subroutines.
- **Slips through.**
  - DC-9: "frozen with the card and run unchanged".
  - NR-0's "no files, no embedded data" does not mention harness functions.
- **Fix.**
  > The Recomputer derives Sol and every credited quantity from the L₀ statement independently. Code behaviour not fixed by L₀ is either priced as a clause (IP-2) or, if it selects within Sol, makes the result CARD-UNFORCED. Any call into charter code → RELOCATED.

### RT-18 CHARTER TEST: a range narrowed by the card makes constants cheap
- **Pattern.** The card declares a narrow range around the value it tuned, so log₂(range/window) is close to 0.
- **Slips through.** IP-5: "The range is declared at freeze."
- **Fix.**
  > The tuning price uses R := max(declared range, the charter default for the constant's type). A narrower declaration costs log₂(default/declared) under IP-13.

### RT-19 CHARTER TEST: constants that are "forced" or numerological
- **Pattern.** The card finds a short L₀ expression (a ratio, a root, a count) that lands inside the passing window. It is "forced", so it costs 0, and the search for it was not a "draft".
- **Slips through.** IP-5: "A value forced by other priced items costs 0."
- **Fix.**
  > A value costs 0 only if a DERIVED theorem from 𝒦's clauses fixes it, with no expression introduced for the purpose. Otherwise it costs max(L_stmt(expression), tuning price), and every expression tried counts toward n_drafts.

### RT-20 CHARTER TEST: dodging the decoder through instance size
- **Pattern.** The card declares small instances and a small AI-3 truncation. Then ℓ_dec = ½·F_X is smaller than the bit cost of the RB/SPS template index itself, so NR-6 can never fire.
- **Slips through.** "any uniform L₀ decoder of price ≤ ℓ_dec = ½·F_X". It is unclear whether RB and SPS are bound by ℓ_dec.
- **Fix.**
  > ℓ_dec := max(½·F_X, ℓ_floor = 24 bits [P]). The RB and SPS templates always run, whatever their price.

### RT-21 CHARTER TEST: search left out of the selection tax
- **Pattern.** The search is hidden in one of three ways:
  - a program enumerates and scores many laws inside a single "draft";
  - exploration happens before the charter freeze;
  - the card reuses archived proposals.
- **Slips through.** IP-12: "every 𝒦 draft … logged between the charter freeze and this card's freeze".
- **Fix.**
  > n_drafts counts every distinct 𝒦, or distinct assignment of constants, for which any score, verdict, price or chain output was computed or estimated by any agent or program since G2-11 (2026-10-07). Enumerations count their full size. Reusing an archived proposal adds log₂ of the archive's size.

### RT-22 CHARTER TEST: citing a small family to cut the selection price
- **Slips through.** IP-4: "The card may argue for a smaller family by citing the published family it actually chose from."
- **Fix.**
  > Delete that sentence. m := the largest family any auditor exhibits. The cited family is only a lower bound.

### RT-23 CHARTER TEST: spreading a per-item clause onto an item that earns nothing
- **Pattern.** A clause that flips one credited verdict also touches a report-only or audit item (SEL-14, 15 or 16), so it is no longer "confined to one".
- **Slips through.** IP-10: "whose effect is confined to one battery item or one instance".
- **Fix.**
  > The clause is confined if ablating it changes ≤ 2 *credited* verdicts or instances. Effects on report, audit and holdout items are ignored when counting. Such a clause costs max(L_stmt, the bits it flips), and those distinctions leave D_sel.

### RT-24 CHARTER TEST: ALLOW anchors credited, and D_sel filling the compression margin
- **Pattern.**
  - A law that allows everything reproduces the 6 ALLOW anchor classes and earns 6 bits.
  - Up to 10 bits of D_sel, earned on public items used during development, can supply all of ΔL ≥ p★ = 10.
- **Slips through.**
  - FC-2: "1 bit for each verified B-SEL verdict class … that the card reproduces".
  - §4.5's ΔL test, which includes D_sel.
- **Fix.**
  > A class earns its bit only if the card is correct **and** the closest B-CF member (by Hamming distance) is wrong. It earns nothing if the reference law that admits every no-signalling support gives the same verdict. SC2's ΔL ≥ p★ must hold with D_sel = 0. D_sel enters ρ only.

---

## C. Baseline side: making the null expensive

### RT-25 CHARTER TEST: a baseline inflated by declarations
- **Pattern.** The card inflates the baseline through its own declarations:
  - it declares a small relabelling group;
  - it declares a meaning for 𝒞 with no dynamics, so 𝒜_Π contains all 2^|V| − 2 partitions;
  - it chooses a large |V| on AI-1;
  - it chooses its own I_𝒦, including public battery embeddings;
  - it chooses the AI-3 truncation and the parametrization in which "uniform" is taken.
- **Slips through.**
  - "modulo the scenario's declared relabelling group".
  - "If 𝒞 fixes no dynamics…".
  - "I_𝒦 … declared at freeze".
  - "uniform on the declared finite truncation".
- **Fix.**
  > - The quotient is by Aut(𝒞_ι), computed by the harness.
  > - The branch with no dynamics applies only if the auditor confirms that the meaning declared under FR11 admits no standard dynamical reading.
  > - I_𝒦 = AI-1 plus 2 instances drawn by the Selector from AI-3 after the batch closes. AI-4 is never used for credit. Credit per instance is the minimum over I_𝒦, times |I_𝒦|.
  > - Reference measures are fixed per primitive type in the canonical parametrization (uniform on finite sets; log-uniform on the default range). The truncation includes every configuration of size ≤ n_min [P].

### RT-26 CHARTER TEST: a coarse reduction s_T
- **Pattern.** The card supplies an s_T that is T_Π-invariant but not separating, effectively quotienting by a larger group. This reshapes ε for ℛ★ and costs only L_stmt.
- **Slips through.** "proves that d_op^{T_Π}(P, T_Π·Q) … is invariant under T_Π acting on both arguments". Nothing requires the reduction to separate T_Π-orbits.
- **Fix.**
  > s_T must be a proved **maximal invariant**: d_op^{T_Π}(P, T_Π·Q) = 0 ⇔ P ∈ cl(T_Π·Q). The Recomputer checks this on the frozen chart.

### RT-27 CHARTER TEST: excluding instances cheaply
- **Slips through.** IP-13: "priced as a selection from the family of domains". The family is undefined.
- **Fix.**
  > IP-13 price := max(L_stmt(predicate), log₂ C(N, k)), where N is the size of the AI-3 batch and k is the number of AI-3 instances excluded.

### RT-28 CHARTER TEST: the card adds witnesses that inflate dim_lb
- **Pattern.** CV-2 forbids the evaluator from adding witnesses, but the card may add standard models that raise dim_lb. Those models need not be regime-matched or use the same inputs for this purpose.
- **Slips through.**
  - "dim_lb is certified by standard models (B-HB)…".
  - "Cards may add witnesses".
- **Fix.**
  > A dim_lb witness must (i) come from the HB families or their compositions within the frozen ranges, (ii) satisfy BP-3 at the hostile fiber, and (iii) receive the B-SRB inputs through the card's declared dictionary (see D2). Witnesses the card adds count only after the skeptic fails to refute (i)–(iii).

### RT-29 CHARTER TEST: the harness written by the future card author
- **Pattern.** The agent that later writes cards builds the pricing substrate:
  - the canonical VB encodings (B.2);
  - the HB-10 ensemble;
  - the chart;
  - the reference measures;
  - the decoders.
- **Slips through.**
  - §19.3, which does not name who executes the work order.
  - §23: "Author: the builder, Claude Code".
- **Fix.**
  > The §19.3 work order is executed by an agent context that authors no card. Its outputs are externally checked (not pending) before the first draft, and every card cites the harness SHA.

---

## D. Clauses that are ambiguous or cannot be computed as written

1. **The chart.** "Admissible chart" and the min over charts are undefined, and the min cannot be computed over an open family (RT-05).
2. **"Same inputs" across ontologies** (BP-5; §2.2(iii) "uses the card's inputs"). There is no dictionary 𝒞 → standard parameters.
   - Fix: a priced, declared dictionary θ_dict, used both for the b_struct baseline and at the lock.
3. **Undefined terms in the credit.**
   - "Independent lock observables" (FC-1).
   - "Structurally distinct instances with mutually independent data" (§1.5).
   - "An observable implied by the others": partial or statistical implication is not handled.
4. **Contradictions inside the charter.**
   - Q1: Im* versus "all of Sol" (RT-06).
   - FC-3 versus the ΔF_Π and ΔF_T terms (RT-04).
   - FC-4's "bits on 𝒜_ε" versus b_meas on scope-Q observables, which are ε-valued.
5. **IP-5 passing window.** "No credited verdict or prediction changes" gives a window of width 0 for any continuous prediction, so the price is infinite.
   - Fix: I_K moves by < ¼|I_K| and no verdict changes.
6. **IP-4 "largest natural family an auditor exhibits".** It is unbounded and "natural" is undefined. max(L_stmt, log m) can also exceed the MDL bound.
7. **NR-6 decoders.** Enumerating every L₀ decoder up to ½·F_X bits is infeasible for large F_X. It is also unclear whether RB and SPS are bound by ℓ_dec.
8. **§4.4 terms.** "Residual bits" and "realized data" are undefined, and the null's Γ term may be counted twice (RT-11).
9. **The SRB interval.**
   - I_SRB as an outer or inner bound is not specified.
   - "Interval" is meaningless for vector observables.
   - Scope-G windows are not frozen.
10. **𝒟(ι) as a space for ΔF_tgt and P_X.** It is infinite-dimensional, and no chart is specified for it.
11. **The AI-3 reference measure.** "Uniform" depends on the parametrization, and the card controls the truncation.
12. **NR-7 "independent draw of its type".** The distribution for function-valued components is unspecified.
13. **VAR-1.** It requires a search over 2^32 translations, and "the whole battery universe" is undefined.
14. **r★ versus r★★.** Every claim must hold at both, but the charter never says which value is credited.
15. **FR11 "meaning … priced".** There is no pricing rule for meaning, yet the meaning switches the construction of 𝒜_Π.
16. **"Clause normal form".** Distributive, Tseitin or Skolemized is not specified, nor how Skolem symbols are priced.
17. **"Reserved" tokens.** Who may assign them is not specified.
18. **MC-7.** Whether "30 days" and N_max apply per observable or per card is not specified.
19. **"p·c(ι)".** Cells per coordinate are window/2^(−p), not 2^p. For example the [−4,4] window adds 3 bits per coordinate.
20. **The ΔF_supp baseline.** It is unclear whether this is the 2721 no-signalling-realizable supports or the quantum-realizable ones, and the term is uncapped.
21. **MC-2 "interface-side measurement".** There is no operational boundary with response data. Certifying Π or T on a platform necessarily uses records.
22. **IP-3.** "Uniform quantification is not a table", but quantifying over a list supplied in the input is uniform in form and is a table in substance.
23. **What Emb receives from B-SEL items.** Is it the scenario signature or the file contents (RT-16)?

## E. Proposed additions

- **§24.1 rows.** Add CT-60 to CT-78 mirroring RT-01 to RT-29, each with the fixed clause it is caught by. The FZ-1 rule ("a pattern no rule catches is a charter defect") currently fails for RT-01 to RT-03, RT-06 to RT-08, RT-11 to RT-17 and RT-24.
- **ST-6 Credit feasibility** (paper only; no candidate).
  - Compute (a) the maximum Credited for a relation of coupling codimension c on the frozen chart at p★, and (b) a lower bound on the Price of the mandatory components in their shortest well-typed L₀ form.
  - If SC2 requires a c larger than the frozen chart provides, or requires lock-observable counts beyond the N_max and 30-day totals, the thresholds are inconsistent. Fix them before freeze (§0).
- **ST-7 Padding control.** Apply the fixed Q2, Q3, Q5 and Q6 to a known definitional relation (CT-21) conjoined with an arbitrary non-standard restriction on Γ alone. The required verdict is CARD-NONJOINT or CARD-DEFINITIONAL. Under v0 this construction passes, which is the defect.