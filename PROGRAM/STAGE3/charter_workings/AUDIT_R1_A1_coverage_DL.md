# Verification A1: does the charter cover the definitional (D) and relocation (L) red-team lenses?

**Scope.** This is an independent, hostile, read-only audit carried out before the charter is frozen. No repository file was edited.

**Documents read in full:**
- `PROGRAM/STAGE3/STAGE3_CHARTER.md`, untracked on `grut2-stage3` in `/tmp/claude-0/mainwt`;
- `charter_workings/REDTEAM_D_definitional.md`: CT-D01 to CT-D16, A-1 to A-19, the harness additions and the priorities;
- `charter_workings/REDTEAM_L_relocation.md`: M0, the §A instruments, RT-1 to RT-23, and ambiguity notes 1–20;
- the D: and L: rows of the v1 Red-team ledger (Tables L1 and L2), together with every v1 clause those rows cite (`CHARTER_V1_WITH_LEDGER.md`);
- G2-11 in `OWNER_RULINGS.md`.

**Method.**
- Each verdict judges the charter's literal text.
- "v1" means `CHARTER_V1_WITH_LEDGER.md`.
- Every construction named in this report is an abstract gaming pattern labelled **CHARTER TEST**. None is a candidate law.

**The §24.1 presumption.**
- §24.1 extends the CHARTER TEST presumption to "every pattern in the working record's red-team reports and red-team ledger". That shifts the burden onto the card, but the presumption contains no decision procedure.
- Several L patterns state a fix but no classification: RT-3, RT-11, RT-13, RT-16 and RT-23. For these the presumption has nothing to apply.
- I therefore score an item PASS only when an operative clause blocks it. Items held only by the presumption are marked as such.

**Verdict key:**
- **PASS**: an operative clause blocks the pattern; the decisive words are quoted.
- **WEAKENED**: the charter catches the pattern less strictly than the report's fix or v1 did.
- **UNCAUGHT**: no clause blocks it.

---

## 1. Coverage table

### 1a. Report D: gaming patterns

| ID | Verdict | Charter clause | Note |
|---|---|---|---|
| CT-D01 Circular extractor | PASS | PC-6; §5.6; S3; CT-60 | Blocked by "No component evaluates, estimates or recomputes (from Ξ or otherwise) a record law P_a, any functional of Γ_Π, ε, d_op, P★, a chart coordinate, a battery verdict or a charter scoring function", by the substitution test, and by "Violation: … CARD-DEFINITIONAL". **Residue:** enforcement detects calls, not a re-implementation of a record functional from Ξ. Fix 25 (MINOR). |
| CT-D02 Pipeline identity gated by preconditions | PASS | §1.1 Dom_gate; DEF-12; Q4; NR-3; NR-4; CT-61 | Blocked by "ℛ holds at every Ξ ∈ Dom_gate(ι) … whether or not Ξ ∈ Sol"; Q4 "(a ⊥, undefined or non-persistent image never counts)"; NR-3 "'Lacks X' counts only for Π". **Residues:** (i) Q4's second sentence dropped D's wording (fix 5, MAJOR); (ii) the *relative* form is uncaught. In that form ℛ★ holds on Dom_gate ∩ R for a cheap Ξ-level predicate R ⊇ Sol, and 𝒦 only puts Ξ in R (fix 2, BLOCKER). |
| CT-D03 Off-slice extension | PASS | §2.5 realized coupling; Q5; §22 | Blocked by the hull 𝓗 := FB ∩ (cl U × cl R) of realized values; "if U is a single point, ℛ★ is NONJOINT"; "Not qualifying: … a disjunction of single-axis restrictions". **Residue:** a cross-instance sibling, the instance-indexed pin pair, is uncaught (fix 12, MAJOR). |
| CT-D04 Tier-swap jointness | WEAKENED | Q5; DEF-14; §2.5 c_J | **Gate holds:** "it survives evaluating ε at one fixed frozen class for all compared points (variation of T_Π alone, or of the tier at which ε is evaluated, never establishes jointness — DEF-14)". **Credit does not.** The credited c_J (§2.5(a)) is formed in the full hull, whose r contains "ε … evaluated at each frozen tier and at T_Π". v1's construction rule "Rectangles are formed within fixed-T fibers" was dropped. So c_J can count tier-swap codimension, and one codimension is worth N_cred·p★ = 480 bits. Fix 4 (MAJOR). |
| CT-D05 Conditional definitional identity | PASS | DEF-15; Q2(c); §2.5 ("reductions of log-volume by inequalities" never credited) | Blocked by "ℛ is assessed as P: NONJOINT if P is single-axis, uncredited if P is an open (inequality) condition"; Q2(c) "the burden of rebuttal is the card's". A joint *open* P gives c_J = 0 automatically. **Residue:** v1's "or of mathematics" was dropped from DEF-15 (fix 17, MINOR). |
| CT-D06 Unpublished identity of the card's own quotient | PASS | DEF-13; Q3(d),(e); §13.1; §15.5 | Blocked by "everything that follows by valid mathematics, published or not, from the definitions of ε and d_op at any admissible class … and from the card's component definitions, with any constants". **Residue:** §15.5 lost v1's "with 𝒮 closed under mathematics and under DEF-1 to DEF-17" (folded into fix 7). |
| CT-D07 Lossy canonical reduction | PASS | §1.4 (i)–(iii); 𝕃_T^adm; Q8; §19.3 | Blocked by "(ii) maximality … (iii) faithfulness … Without (i)–(iii), ε_R is undefined for the card and every ε-relation fails Q8". **Residues:** the card's "declared law class" can exclude families on which ε^{T_Π} is then used (Q3 witnesses, B-SRB); the kit checks only (ii)–(iii) and only on HB-1 to HB-9; the scale of s is set by the card. Fix 14 (MAJOR). |
| CT-D08 Response absorbed into the interface class | PASS | §1.3 T_Π; PC-6; NR-10(l); §1.6; §19.3 | Blocked by "Every t ∈ T_Π is computed **without evaluating any protocol, any protocol's action on Ξ, or any solution's response.**" **Residues:** (i) "if T_Π contains one", read by content, is a hidden kill for every T_Π ⊇ E₂± (fix 13, MAJOR); (ii) v1's PC-6 ban on reading protocol identity was dropped, and NR-10(a) covers only 𝒦, Emb and Obs (fix 19, MINOR). |
| CT-D09 ε produced by the readout | WEAKENED | PC-7(b),(c); §15.3; DIF-5(e); §5.5 | PC-7(b),(c) and the B-REC routing are present. D's consequence, "Failure voids every relation that uses ε^{T_Π}", was not adopted: (a) DIF-5(e) is a Stage-4 gate, run on the picked card only; (b) §5.5's GENERATED test, which awards G's log₂5 term at Stage 3, omits DIF-5; (c) KU-6 fires only "while those environments are claimed as realizable". DIF-5(e)'s "every exogenous B-REC/HB family" also sweeps in HB-8 (regime "X / 0"), which §15.3 leaves out. PC-7(b)'s factorization is non-unique (fix 15). Fix 6 (MAJOR). |
| CT-D10 Mode selection inside the persistence tolerance | PASS | §1.3 persistent core; PC-7(d); NR-11 | Blocked by "Records are read from the **persistent core**" and by PC-7(d), which recomputes every credited quantity "with the records of relata in ∪_a (Π_a Δ Π_ref) ∪ ∂ removed … Otherwise the verdict is MODE SELECTION". **Residues:** there is no §24.1 row; "within r_lock" is undefined for bit-valued quantities (fix 22, MINOR). |
| CT-D11 Tautology when standard models run through the card's pipeline | PASS | Q3(c); Q3(d); STD-9; CT-69 | Blocked by the transplant ("runs the **card's own components** on them … fraction ≥ 1/Q_min → CARD-STANDARD"); by Q3(d) ("never satisfies Q3 by itself"); and by STD-9 (RH-LOC; "|E_Π|, |∂|, block counts"). **Residue:** a type in which the transplant draws cannot be expressed, and ⊥ draws counted in the denominator. Fix 11 (MAJOR). |
| CT-D12(a) Generic baseline identity with an exotic witness | PASS | Q3(b); RH-AN; STD-14 | Blocked by "ℛ★ fails on an open neighbourhood of each witness … holds on an open dense subset … STANDARD-GENERIC". |
| CT-D12(b) Starved or silent B-SRB | WEAKENED | BP-5; §15.5; STD-3 | **Caught:** the constants'-data branch ("every datum used to fix a constant that enters the prediction") and silence ("is not silence: J_SRB is then the witness hull"). **Regressed:** the merged fix (S:RT-S-09, M:RT-01). v1's BP-5(iii) "connected correlators up to order m★★ … calibration run disjoint from the lock records" and (v) Θ_std became "every statistic of P_{a₀} **up to the order the prediction uses**". A route-(i) prediction that uses no P_{a₀} statistic leaves B-SRB without the reference 4-point function. STD-3 denies credit only for correlators "among the BP-5 inputs". This reopens the BRI1 Kubo/FDT precedent that G2-11 names. Fix 1 (BLOCKER). |
| CT-D13(a) Coordinate stretching | WEAKENED (minor) | §3.3; MC-4 | Meets D's fix: "frozen chart coordinates in frozen units … Reparametrizing o⃗ is prohibited". v1's hostile "minimum over {the frozen coordinate, log\|·\| of it}" was dropped. Fix 20 (MINOR). |
| CT-D13(b) Observables linked by DEF identities | WEAKENED | MC-4; MC-9; §15.5 | Neither D's independence test nor v1's DEF closure of 𝒮 in B-SRB survives. J_SRB is a "hull" of witness points. When a nonlinear DEF identity links two lock observables, the hull leaves the identity's graph and b_meas is inflated (the joint cell count does not help). Fix 7 (MAJOR). |
| CT-D13(c) Sub-grid or marginal prediction | PASS | DEF-13; LT-1(ii) | Blocked by "protocols, record channels **and** grid times all disjoint … must not be derivable from DEF-1 to DEF-17 ∪ 𝒮 alone". |
| CT-D13(d) Decorative interface input | PASS | MC-2 sensitivity | Blocked by "must widen the predicted region J_K by a factor ≥ Q_min in cell count. Otherwise the lock is a pin: DEFINITIONAL". |
| CT-D13(e) Platform cut chosen by response | PASS | MC-2 platform interface | Blocked by "No functional of the record laws of any protocol in A … Selecting the cut by maximizing a record functional is prohibited". |
| CT-D14 Dropping non-standard realizations | PASS | §2.5 realized image; §2.3 𝒜_T | Blocked by "Non-standard realizations are **never removed**" and by the generated T_Π "counts as a class that could have been supplied by hand". **Residue:** the converse pattern, *adding* one non-standard realization so that c_J(b) is disabled, is uncaught (fix 10, MAJOR). |
| CT-D15 Dimension certified at a singular point | PASS | §2.5 dimension certificates | Blocked by "**A rank at a chosen point certifies only dim ≥ that rank.**" |
| CT-D16 Structural credit counted twice | PASS | §3.1; §4.3(d) | The secondary relation "earns no credit", and "any credit from the secondary relation" is never counted. This is stronger than D's fix. |
| D:harness (seven rejection tests; priorities 1–6) | PASS | §19.3 rejection tests | All seven tests are present. They run in the kit, after the freeze and before Card 1 (D asked for "before the freeze"). Priority 4 is regressed by BP-5 (fix 1). |

### 1b. Report D: ambiguities

| ID | Verdict | Charter clause | Note |
|---|---|---|---|
| A-1 NR-1 scope | PASS | NR-1 | Resolved by "scope 𝒦, 𝒞, 𝒳, priors and Emb — components are governed by PC-6 and PC-7". The same conflict recurs in NR-10(f) "no input names … a readout class" (fix 28, MINOR). |
| A-2 "Content implying ℛ★" versus Q1 | PASS | §5.1 "Supplied" | Resolved by "A law that merely *implies* ℛ★ is what Q1 requires; that is not supplying it." The definition of "Supplied" lists fewer inputs than the §5.2 inventory (fix 29, MINOR). |
| A-3 E-B twin clause vacuous or over-broad | WEAKENED | NR-10(l); §15.6 | The twin is now run through X_h/X_T. But v1's "ℛ★ need not separate it" was dropped. §15.6 keeps "A relation satisfied by the twin of every family is record-only and earns no reciprocity credit". The twin has the same Γ, so under CV-1 the over-broad reading D warned about becomes available. Fix 18 (MINOR). |
| A-4 ε among Q5's coordinates | PASS (gate only) | §3.1 preamble; Q5; DEF-14 | Resolved by "it is never a coordinate of its own". On the credit side see CT-D04 and fix 4. |
| A-5 Range of 𝒟 | PASS | §2.3 𝒟 | "T ∈ 𝕃_T^adm ∪ {T_Π}, Γ any family of per-protocol laws". |
| A-6 𝔐_F; "applicable" | PASS | Q3(a); BP-6 | "At least two SFP frameworks applicable … fewer → Q3 fails"; "A framework applies at x unless the card proves one of its hypotheses fails". |
| A-7 How I_SRB is built; what \|·\| means | PASS | §15.5; MC-4 | "never an outer bound … Auditor derivations may only shrink it"; cell counts within W. DEF closure: fix 7. |
| A-8 Hostile enlargement cuts both ways | PASS | BP-7 | "It never enlarges FB or dim_lb". |
| A-9 Unbounded chart family | PASS | §1.5 chart | "Cards neither add nor remove coordinates … up to N_ch [A]". |
| A-10 ℓ_dec smaller than one token | PASS | NR-6; App A | "ℓ_dec := max(½·log₂\|𝒜_X(ι)\|, c_dec)", with c_dec = 60. This is now far below the G credit it guards (L:RT-2; fix 9). |
| A-11 NR-10(c) has no test | PASS | NR-10(c); NR-3; §1.1 | "with the NR-3 carrier W-pipe"; "Dom_gate^X drops the conditions that X itself must meet". |
| A-12 B-REC "through the card's interface" | PASS (semantics) | §15.3; DIF-5(e) | "passed through the card's static record maps … at the frozen tiers and at T_Π". Where the consequence sits: fix 6. |
| A-13 §4.4 code unspecified | PASS (moot) | §4.3–§4.4 | The two-part code was removed. Its removal (and NULL-M's) is not listed in Appendix D (fix 8). |
| A-14 α and t₁ undefined | PASS | App A templates; §1.7 | "α = 1 standard deviation, under a₀, of the driven S variable (never of a record); t₁ := H/4". |
| A-15 Time-indexed versus global Π tests | PASS | §1.3 | "**all** hold". |
| A-16 NR-7 and NR-16 have no statistic | PASS | NR-7; NR-16 | p_dec fraction; "one-sided binomial". NR-7's scope over components is a literal universal kill (fix 16). |
| A-17 Derivability from 𝒮 only semi-decidable | PASS | Q3(e); §13.4 | "decided constructively". |
| A-18 Im* versus "all of Sol" | PASS | §2.5; Q1 | "Im(ι) is the **full** image of Sol". |
| A-19 FC-2 ablation scope | PASS | §4.3(c) | "distinctions reproduced under 𝒦_∅ or 𝒦_𝒮 on Dom_pre". |

### 1c. Report L: patterns, shared instruments and ambiguity notes

| ID | Verdict | Charter clause | Note |
|---|---|---|---|
| L:M0 Coverage rows | PASS | App E | Items 1–9 and additions 1–4 are mapped. Rows do not name the exercising CT, as L asked. FZ-2's record file is absent (fix 30). |
| L:§A NR-D (decoder test) | PASS | NR-6 | Full inventory, uniform decoders, no 𝒦 solver, NOT-FOUND grading. Decoder budget: fix 9. |
| L:§A NR-S (symmetrization) | PASS | NR-5 generalization | "a G-invariant input must still yield some persistent X … an X that appears only on non-invariant inputs and moves equivariantly with them was supplied". |
| L:§A JN | WEAKENED | NR-17 | Transcribed faithfully, but literally vacuous for the pattern it targets. See RT-5. |
| L:§A P-rules (i), (ii), (iv) | PASS | IP-5 passing window; IP-2 D_KL; IP-6 ΔF_tgt; IP-10 | |
| L:§A P-rule (iii) | WEAKENED | IP-6 closure | L priced any structure "from which [an item] is L₀-definable within c_dec bits". The charter, like v1, catches only "a defined symbol whose interpretation satisfies an item's frozen axiom checklist". Fix 26 (MINOR). |
| L:§A FB | PASS | §2.3 FB | "Freedom reduction is measured inside FB, never against the product". |
| RT-1 Priced supply passes as generation | PASS | §5.1; §5.6; FR5 | "Supplying PS-1 to PS-4 at any price fails the corresponding generation gate"; "FR5 and RULES 1 … govern unprotected inputs only". |
| RT-2 Π encoded in an input asymmetry | WEAKENED | NR-5; NR-6; NR-7; §5.2; §4.3(b) | The operational tests are present. But ℓ_dec = max(½·log₂\|𝒜_Π\|, 60 bits) was set when generation earned nothing (v1 FC-3). The charter now pays up to 48 × 16 bits for a GENERATED Π, and NR-6 fires only on ≥ p_dec of AI-3. CHARTER TEST *decoder just above c_dec*: a 61–700-bit decoder that reads Π from 𝒞 fires nothing, while G pays for Π. Fix 9 (MAJOR). |
| RT-3 Ontology too small to fail | WEAKENED | §1.3 nontrivial; IP-14; B-DIF(x) | The size test is present. **Lost** (from v1 and L): "the law's selection removes at least b_Π bits beyond the IP-14 price of the ontology choice"; b_Π was also lowered from 8 to 6, which Appendix D does not list. **Hidden kill:** 𝒜_Π is post-SPS ("the smaller set governs", §2.3). So any Π that a standard selector finds fails the size test at S4. That contradicts ST-6 (which expects S5 CARD-STANDARD) and the App-A feasibility note. Fix 3 (MAJOR). |
| RT-4 Π defined as an extremizer of a response functional | PASS | PC-6; DEF-17(a); NR-13 | "the stationarity, fixed-point or extremality conditions of any rule the card uses to define Π, [h], T_Π or the carrier, and all their consequences". |
| RT-5 ℛ is a separable conjunct | **UNCAUGHT** (held only by the presumption) | NR-17; OR-2; OR-5 | NR-17: "if 𝒦₂ alone implies ℛ★ with Π, T_Π and Γ_Π treated as free variables". RT-5's conjunct is "written in Ξ-variables". With the pipeline outputs free, a Ξ-level conjunct never *implies* ℛ★, so JN fires only on target-level conjuncts, which NR-2 already catches. No §24.1 row covers RT-5. The other reading ("free" = whatever the pipeline returns once 𝒦₁ is dropped) has no non-vacuity guard, so under CV-1 it can relocate honest cards. The rule also omits Z_Π and [h], and lets the card pad 𝒦₂ above the price bound. Fix 2 (BLOCKER). |
| RT-6 Carrier taken from the chosen representation | PASS | NR-10(c),(d),(h),(i),(j) | "the card names the 𝒦-internal property … not L₀-equivalent, within c_dec bits, to 'the readout is a function of the instantaneous state'". **Residue:** NR-10(e) and (l) apply only "on any instance that can express" or "where the auditor can express". This is an inexpressible-type escape. Fix 11 (MAJOR). |
| RT-7 Protocol-indexed moves; a class so large that ε ≡ 0 | PASS | §1.6; §21.2; Q8; DIF-5(b); CT-14 | "a move indexed by protocol is mode selection"; behavioural GY-11/GY-12 test. v1's list of absorbed families was dropped, and the projection is "declared" by the card (fix 21, MINOR). |
| RT-8 T_Π equals a built-in symmetry or calibration | PASS | NR-10(k); §1.4 | "SUPPLIED if it equals, or is L₀-definable within c_dec bits from, a symmetry group, invariance requirement or calibration map"; "imports no R1 theorem". |
| RT-9 Gibbs/FDT through a chain of premises | PASS | PS-5; NR-12(b),(c) | Operational PS-5; "whether supplied, hidden or generated by 𝒦 … STANDARD-IMPLIED". |
| RT-10 Baseline under-imposed | PASS | §13.2–§13.4; STD-1 to STD-15; §13.8 | Covers nonlinear FDRs, NESS forms, fluctuation theorems, TURs (RH-LDB), Kramers–Kronig, the second law and the D5 reverse-direction relations. The floor is open and "retroactive until banking". |
| RT-11 Reduction on degenerate or unrealized sets | PASS | §2.5 nontrivial reduction; Q9 | "nonempty relative interior in FB … meets {ε > r_lock}, and meets the region where the card's Π is realized". |
| RT-12 Tailored repertoire | PASS | §1.7; Ch-2; Q9 | "a function of the generated Π … No repertoire is selected after any score". |
| RT-13 Tuned windows; unbounded error terms | PASS | §1.3 horizon and scale window; App A; MC-3 | The thresholds are charter constants; "Otherwise the lock is UNFALSIFIABLE". |
| RT-14 Battery verdicts encoded in the translation layer | PASS | §15.1 Emb; §4.3(c); IP-6; IP-10; DC-10; SEL-H | Part (f) was declined in v1 with a reason (D_sel ≤ 10 bits; SC1 is separate). |
| RT-15 Decision level per item; undecidable references | PASS | DC-10; DC-5 | "one level for all items. UNDECIDED = FAIL"; "priced as that object". |
| RT-16 Identity measure defined from Γ | PASS | PC-6; DEF-17(b),(c) | "Persistence and identity measures … are functionals of Ξ-level structure only". |
| RT-17 Scope switched or mis-declared | PASS | §14; Q10; RS-4; RS-5 | Scope Q: invariance plus the Π′-replacement test. Scope G: "violation of ℛ when Π or T_Π varies with the linear part of Γ held fixed". |
| RT-18 Loose, post-hoc, infeasible or retrodicted lock | PASS | §3.1; IP-11; MC-7; MC-8; §15.5 | One credited ℛ★; the secondary earns nothing; "published before card freeze (that is calibration)". |
| RT-19 Sectors already linked, or leakage | PASS | XS-2 SI-1 to SI-5; XS-6 | |
| RT-20 Pass resting on unproved premises | PASS | NR-15; PV-3; SM-9 | "A premise not proved at card freeze counts as SUPPLIED". |
| RT-21 Budget multiplication | PASS | BU-9; IP-9; BU-3; BU-4 | VAR-1 covers a resubmission in another gauge. |
| RT-22 Killed idea renamed | PASS | §21.2 behavioural equivalence | |
| RT-23 Coordinates, witnesses or distance chosen per card | PASS | §1.3 [h]; §1.4; C8 | "no per-card normalization or alternative distance". **Residues:** the scale of s_T (fix 14) and PC-7(b) (fix 15). |
| L:C1 "Not independently imposed" is open-ended | PASS | §13.4; Q3(e) | A closed list was declined as less hostile. |
| L:C2 "Nontrivial freedom reduction" | PASS | §2.5 | |
| L:C3 Units of "positive compression" | PASS | §4.2–§4.4 | |
| L:C4 "Measurable" | PASS | MC-7; App A N_max | |
| L:C5 Persistence timescales; earned time | PASS | §1.3; FR7; VB-9 | |
| L:C6 Grading of "generated" | PASS | NR-6; §5.5 | "NOT FOUND within the hostile window". |
| L:C7 Baseline needed before Ξ exists | PASS | §1.5; IP-14 | "𝒜_Π on the instance's relata V". |
| L:C8 Freedom on the 𝒜_T lattice | PASS | §2.3; §2.4 | \|𝒯 ∪ {⊥}\| = 5. |
| L:C9 Where KMS and Onsager apply | PASS | §13.2; STD-3 NESS forms; §13.5 | |
| L:C10 Quotient-irreducible relative to which T | PASS | §14 SCOPE-Q; XS-10 | |
| L:C11 Selectivity wording | PASS | §15.1 grades; §4.3(c) | |
| L:C12 "Genuinely distinct"; "GRUT fit"; "definitional" | PASS | BU-4; XS-6; DEF-1 to DEF-17 | |
| L:C13 A kill condition must be able to fire | PASS | KP-2; KP-3 | |
| L:C14 Who picks the comparators | PASS | OR-4; SFP-8 | |
| L:C15 Undecidability of consistency-only cards | PASS | DC-5; DC-8; DC-10 | |
| L:C16 Originality versus non-independence | WEAKENED | OR-2; NR-17 | Rests entirely on JN; see RT-5 and fix 2. |
| L:C17 Price of Ξ's type | PASS | IP-1; IP-14 | |
| L:C18 ε under an approximate Π | PASS | §1.3 core; PC-7(d); MC-3 | |
| L:C19 Derived versus laboratory carrier | PASS | MC-6 | "certifies **the carrier the card derives**". |
| L:C20 Charter constants | PASS | CV-6; App A | |

**Tally (91 rows):**

| Verdict | Count | Items |
|---|---|---|
| PASS | 79 | — |
| WEAKENED | 11 | CT-D04, CT-D09, CT-D12(b), CT-D13(a), CT-D13(b); A-3; L:§A JN; L:§A P-rule (iii); RT-2; RT-3; L:C16 |
| UNCAUGHT | 1 | RT-5 (held only by the §24.1 presumption) |

**New loopholes in the clauses I was asked to scan:**
- PC-6: fix 25.
- PC-7(b): fix 15.
- PC-7(a) together with NR-7: fix 16.
- §1.3 T_Π: fix 13.
- §1.4 s_T: fix 14.
- §2.5:
  - c_J(b): fix 10;
  - fixed-T fibers: fix 4;
  - c_ι: fix 27;
  - instance-indexed pin pair: fix 12.
- Q2: fix 24.
- Q4: fix 5.
- Q5: fixes 12 and 23.
- NR-3: fix 31.
- NR-4 and NR-17: fix 2.
- NR-6: fix 9.
- NR-10(e),(l): fix 11.
- NR-10(f): fix 28.
- DEF-12: fix 2.
- DEF-15: fix 17.

---

## 2. Fixes, by severity

Each fix states its clause, its severity and the replacement or insertion wording. Every new pattern is labelled CHARTER TEST.

### BLOCKER

**Fix 1. BP-5: restore the full standard reference package (CT-D12(b), merged with S:RT-S-09 and M:RT-01). BLOCKER.**

- **Problem.** "Every statistic of P_{a₀} up to the order the prediction uses" lets a prediction that consumes no correlators starve B-SRB of the reference 4-point function. That reopens the BRI1 Kubo/FDT route the owner excluded.
- **Fix.** In §2.1 BP-5, replace the parenthesis after "the **standard reference package**" with:

> "measured on the lock platform (on the instance, for in-silico fibers) in a calibration run whose records are disjoint from the lock records, **whatever the prediction uses**: every connected correlator of P_{a₀} up to order m★★ = 5 at every grid time of r★★; the independently calibrated linear-response functions of the driven and recorded variables; and every regime parameter a standard modeller calibrates (e.g. temperature, spectral densities, conserved-charge values). **Θ_std:** every further parameter a standard theory would use to predict o⃗ that can be measured without the lock records, declared in C13; the auditor may add to it."

- **Consequential edits:**
  - add "Θ_std" to C13;
  - change the Appendix-A scope-G window to "the observable's range over B-HB at Θ_std";
  - add an Appendix-D row recording the change.

**Fix 2. NR-17 (joint necessity) and NR-4: make JN catch a conjunct written in Ξ-variables, and the relative pipeline identity (RT-5, L:C16, L:§A JN, the CT-D02 residue). BLOCKER.**

Replace NR-17 with:

> "**NR-17 Joint necessity (JN).** For any L₀ split 𝒦 ≡ 𝒦₁ ∧ 𝒦₂ offered by the author or a reviewer in which 𝒦₂ does not imply 𝒦₁ on Dom_pre — any Ξ-level predicate R ⊇ Sol may be offered as 𝒦₂, since 𝒦 ≡ 𝒦 ∧ R — let Price_min(𝒦₂) be the L_stmt of the shortest L₀ statement equivalent to 𝒦₂ on Dom_pre exhibited by any party. If Price_min(𝒦₂) ≤ Price(ℛ★ stated directly) + c_dec and either
> (a) 𝒦₂ alone implies ℛ★ with Π, Z_Π, [h], T_Π and Γ_Π treated as free variables; or
> (b) on every lock-fiber instance, Dom_gate(ι) ∩ Sol(𝒦₂) is nonempty and ℛ★ holds within r_lock on the defined pipeline image of a reference-measure fraction ≥ 1 − 1/Q_min of it — that is, 𝒦₂ forces ℛ★ through the components, in whatever vocabulary it is written —
> then ℛ★ is **imposed, not forced**: RELOCATED on the target relation. Novelty at the assembled-law level does not override this."

Add to NR-4:

> "ℛ★ appears at Ξ if Ξ's defined pipeline image satisfies ℛ★ within r_lock; the p_dec-fraction rule applies to ℛ★ as to every other X."

Add a §24.1 row:

> "CT-77 (CHARTER TEST) | A cheap conjunct, or a cheap Ξ-level predicate R ⊇ Sol written in Ξ-variables, forces ℛ★ through the components, while the rest of 𝒦 only makes the chain defined | NR-17(b), NR-4 | RELOCATED (target relation)".

### MAJOR

**Fix 3. §1.3, nontrivial size test (RT-3). MAJOR.**

Replace "log₂|𝒜_Π(ι)| ≥ b_Π [A] on the lock fibers" with:

> "log₂|𝒜_Π^pre(ι)| ≥ b_Π [A] on the lock fibers, where 𝒜_Π^pre(ι) is 𝒜_Π(ι | H) of §2.3 *before* the standard selectors are applied to the realized dynamics of Sol; and the law's selection removes at least b_Π bits beyond the IP-14 price of the ontology choice. The standard-selector reduction acts only on G (§4.3(b))."

Then:
- record b_Π 8 → 6 in Appendix D, or restore 8 and re-run ST-10;
- re-confirm ST-6.

**Fix 4. §2.5: compute the coupling within fixed-T fibers (CT-D04, A-4). MAJOR.**

Insert after the definition of the product hull:

> "**Fixed-T fibers (DEF-14).** 𝓗 contains a cross pair (u₁, r₂) only if u₁ and u₂ carry the same T_Π, and ε and every T-invariant functional in ℛ★ are evaluated at that common class on both points. c_J, κ_J, c_ι and κ_ι are computed fiberwise, and the minimum over the fixed-T fibers that contain realized points is taken."

**Fix 5. Q4, second sentence (CT-D02). MAJOR.**

- **Problem.** "shows ℛ★ depends on 𝒦's clauses, not on the type, components, representation or prior" is either a universal kill (every ℛ★ depends on X_Π) or vacuous.
- **Fix.** Replace the sentence with:

> "The responsibility map (NR-4) shows that ℛ★ does not appear under 𝒦_∅ and fails, on some lock-fiber instance, when some clause of 𝒦 is deleted. Dependence on the type, components, representation or prior in addition to the clauses is allowed only where DEF-12, NR-9 and NR-17 do not fire."

**Fix 6. DIF-5(e), §15.3 and §5.5: the exogenous-zero test must bind at Stage 3 (CT-D09, A-12). MAJOR.**

In §15.3, replace "For the exogenous controls (C2-G, C2-NG, C2-F′, HB-5 with calibrated filters) the required value at T_Π is exactly 0 (DIF-5(e))." with:

> "For the exogenous controls C2-G, C2-NG, C2-F′, HB-3, HB-4 and HB-5 with calibrated filters, the required value at T_Π is exactly 0, and HB-8 (E2) never returns R1-PASS. These checks run at S4 on every card, whether or not it claims the environments realizable. If either fails, T_Π is not GENERATED (§5.5) and every relation that uses ε^{T_Π} fails Q8."

Also:
- **§5.5:** "Carrier, [h] and T_Π GENERATED iff NR-3, NR-4, NR-10(a)–(l) **and DIF-5(a)–(e)** are clean and T_Π ∈ 𝕃_T^adm."
- **DIF-5(e):** replace "every exogenous B-REC/HB family" with "every exogenous control listed in §15.3 … gives ε^{T_Π} = 0, and HB-8 never returns R1-PASS".

**Fix 7. §15.5 and MC-9: lock observables linked by DEF identities (CT-D13(b); the A-7 and CT-D06 residues). MAJOR.**

Append to §15.5's first bullet:

> "𝒮 is closed under valid mathematics and under DEF-1 to DEF-17. J_SRB is intersected with the set on which every DEF-1 to DEF-17 identity among the lock observables holds, and 'hull' means the hull within that set."

Append to MC-9:

> "Lock observables are independent only if none is implied by the others under 𝒮 ∪ DEF-1 to DEF-17. A dependent observable is removed before MC-4 is computed; it may still serve as a kill condition."

**Fix 8. Appendix D is not a complete diff from v1 (FZ-2, owner review). MAJOR.**

The charter states that "Appendix D lists the builder's choices that differ from v1". It does not. Add rows for at least the following, all inside the D/L lenses:

| v1 | Charter |
|---|---|
| BP-5(iii) correlators to m★★ on disjoint data; BP-5(v) Θ_std | "up to the order the prediction uses" |
| c_J rectangles "within fixed-T fibers" | dropped |
| Size test "beyond the IP-14 ontology price"; b_Π = 8 | dropped; b_Π = 6 |
| n_min = 6 (truncation semantics) | n_min = 8 with 8 ≤ \|V\| ≤ 16 |
| §4.4 NULL-ΠT/NULL-M two-part code | replaced by c_J(b); Price(M) undefined |
| MC-4 minimum over the log coordinate | dropped |
| §15.5 "𝒮 closed under mathematics and DEF-1 to DEF-17" and its scheme list | dropped |
| §15.6 "ℛ★ need not separate it" | dropped |
| DEF-15 "or of mathematics" | dropped |
| PC-6 ban on reading protocol identity | dropped |
| §21.2 list of families the GY classes absorb | dropped |
| D's "voids every relation that uses ε^{T_Π}" | not adopted |

Also noticed, outside the D/L lenses:

| v1 | Charter |
|---|---|
| OR-5 banking "only if S6 still passes when recomputed with NULL-M and c_J" | condition dropped |
| IP-6 ΔF_tgt's "credit of 𝒦 with only v" term | dropped |
| IP-5 "every expression tried counts toward n_drafts" | dropped |
| DC-4 resource and overrun clause for levels n+1 and 2n | dropped |

**Fix 9. NR-6 and §4.3(b): the decoder budget is far below the credit it guards (RT-2, A-10). MAJOR.**

The CHARTER TEST here is a *decoder just above c_dec*. Append to §4.3(b):

> "For each X ∈ {Π; [h] and T_Π; carrier}, the G term summed over I_𝒦 is capped at L_dec(X), the L₀ length of the shortest decoder (NR-6 rules, no length limit) exhibited within the hostile window that recovers X on every instance of I_𝒦. The X term of g(ι) is 0 on any credit instance on which an exhibited decoder of length ≤ ℓ_dec recovers X."

**Fix 10. §2.5 c_J(b): one non-standard realization disables the standard-class check, and Price(M) is undefined (new; the converse of CT-D14). MAJOR.**

The CHARTER TEST here is a *non-standard poison pill*. Replace "(b) for every standard model class M realizing Im (constants fitted, Π and T chosen by hand) with Price(M) ≤ Price(𝒦)" with:

> "(b) for every standard model class M realizing Im ∩ FB — the standard part of Im; non-standard realizations are scored by their own kill conditions and never disable this clause — with constants fitted, Π, [h] and T fixed by hand or by a priced rule, and Price(M) ≤ Price(𝒦), where Price(M) := the IP-4 price of the framework choice + L_stmt(M) + the IP-5 price of M's fitted constants at p + the price of the rule that fixes Π, [h] and T (the cheapest RB or SPS selector that returns them, else log₂|𝒜_Π/Aut| + log₂ 5 per instance)".

**Fix 11. Q3(c), NR-10(e) and NR-10(l): the inexpressible-type escape (new; CT-D11 and RT-6 residues). MAJOR.**

The CHARTER TEST here is an *inexpressible-type escape*. Append to Q3(c):

> "If a transplant draw cannot be expressed in the declared type, the card's frozen, priced standard-model embedding E_std (declared in C12) is used. Draws on which any component returns ⊥ or the carrier is not PASS are excluded from the denominator. If no E_std is declared, or fewer than half the draws are scorable, Q3(c) returns CARD-STANDARD."

Add to NR-10:

> "(m) If the declared type cannot express the configuration of (e) or the product-latent twin of (l) for some realized record family, the exclusion is carried by the type: the carrier is SUPPLIED (CARD-NONGENERATIVE)."

**Fix 12. Q5: the instance-indexed pin pair (new; a cross-instance sibling of CT-D03 and ST-11). MAJOR.**

The CHARTER TEST here is an *instance-indexed pin pair*. Add a Q5 bullet:

> "– The coupling is not carried by the instance inputs alone. If, for some L₀ split 𝒦 ≡ 𝒦₁ ∧ 𝒦₂ offered by the author or a reviewer, 𝒦₁ fixes the realized interface value of every instance of 𝓘 (with Γ_Π free) and 𝒦₂ fixes the realized response slice of every instance of 𝓘 (with Π, Z_Π, [h] and T_Π free), then the coupling is a composition of single-axis determinations through 𝒞, and ℛ★ is NONJOINT."

**Fix 13. §1.3 T_Π: "if T_Π contains one" is a hidden kill (new; CT-D08 residue). MAJOR.**

Read by content, every T_Π ⊇ E₂± (mandatory for SCOPE-Q) contains translations that coincide with a protocol's mean shift. Replace "if T_Π contains one" with:

> "if X_T's L₀ definition of any element or generator of T_Π refers to a protocol, a protocol's action on Ξ, a solution's response or a record law (a provenance test, checked by call-graph inspection and the PC-6 substitution test). A map that merely coincides with some protocol's effect (e.g. a translation in E₂±) does not count; its consequences are governed by DEF-1 to DEF-17 and §14."

**Fix 14. §1.4 s_T: law-class coverage and scale (new; CT-D07 and RT-23 residues). MAJOR.**

The CHARTER TEST here is a *card-scaled reduction*. Append to §1.4:

> "The declared law class contains every family on which charter code evaluates ε^{T_Π}: the image of Sol, B-REC, every B-HB family and composition within the frozen ranges, the Q3 witness and transplant draws, and the B-SRB scheme outputs. The kit checks (i)–(iii) on B-REC and all of B-HB. (iv) Normalization: s commutes with the frozen centering and whitening of T_lin on the record space; otherwise any scale constant in s is a priced constant under IP-5 with its passing window. A failure of (i)–(iv) on any family on which ε^{T_Π} is used makes ε_R undefined for the card (Q8)."

**Fix 15. PC-7(b): the factorization Obs = g∘Obs′ is non-unique (new; CT-D09 and RT-23 residues). MAJOR.**

- **Problem.** Since Obs = g∘(g⁻¹∘Obs) for every bijection g, "a relation that depends on g" is literally every ε-relation at a non-universal class: a universal kill under CV-1. Read the other way, the clause is vacuous.
- **Fix.** Replace PC-7(b) with:

> "(b) Static maps are calibrated out. Obs′ is the card's Obs with its **declared static tail** removed: every map on record space, applied after Obs's last read of Ξ, that depends on neither protocol nor state. The card declares the tail at freeze; an undeclared static tail found by the auditor → RELOCATED (NR-0). ε and the chart are computed on Obs′ (as in R1 §1); the auditor does not re-factor Obs. A relation stated through the static tail is CARD-DEFINITIONAL."

**Fix 16. NR-7 applied to components is a universal kill (new; PC-7(a) with NR-7; A-16). MAJOR.**

- **Problem.** PC-7(a) applies NR-7 to components. Scrambling X_Π always moves Π ("X tracks the component"), so every card is RELOCATED.
- **Fix.** Replace NR-7's first sentence with:

> "Replace each priced input datum (𝒞 constants and parameter values, tables, priors, θ_dict, Emb's numeric content, coarse-graining scales and thresholds), and each numeric constant or table inside a §1.2 component, by an independent draw of its type from the reference measure. The components' L₀ structure is not scrambled, and the extractor of X is never scrambled when X is tested."

### MINOR

| # | Clause | Problem | Fix (wording) |
|---|---|---|---|
| 17 | DEF-15 (CT-D05) | v1's "or of mathematics" was dropped | "…P ⇒ ℛ is a consequence of DEF-1 to DEF-14, of R1's theorems, or of valid mathematics (DEF-11, DEF-13)…" |
| 18 | §15.6 (A-3) | v1's guard against the over-broad twin reading was dropped | Append: "ℛ★ need not separate the twin. 'Satisfied by the twin' means satisfied by the twin's record family paired with the interface the twin's own pipeline returns." |
| 19 | PC-6 and NR-10(a) (CT-D08) | v1's ban on reading protocol identity was dropped; NR-10(a) covers only 𝒦, Emb and Obs | Add to PC-6: "No component reads protocol identity beyond the protocol's action on S." Change NR-10(a) to "no clause of 𝒦, Emb **or any §1.2 component**". |
| 20 | MC-4 (CT-D13(a)) | v1's hostile minimum over the log coordinate was dropped | Restore: "b_meas is the minimum over {the frozen coordinate, log\|·\| of it where it has one sign on J_SRB ∪ J_K}". |
| 21 | §21.2 (RT-7) | The absorbed-family list was dropped; the projection is card-declared | Restore "(unrestricted bimeasurable bijections; protocol-dependent linear readouts; a latent-dimension-only constraint)". Replace "on the declared finite projection" with "on the frozen chart's finite projection (template grid, A_{r★★})". |
| 22 | PC-7(d); Q4 (CT-D10) | "within r_lock" is undefined for bit-valued quantities | PC-7(d): "…each lock-observable prediction stays within r_lock and c_J, κ_J, c_ι, G and every gate verdict are unchanged". Q4: "…violates ℛ★ by more than r_lock in some lock observable". |
| 23 | Q5 (new) | The chart's interface statistics include "T-tier verdicts", which conflicts with the DEF-14 parenthetical | "…differ in Π, in the carrier class, or in a declared interface statistic **that is not a function of T_Π alone** (T-tier verdicts excluded)…" |
| 24 | Q2(a) (new) | Test domains are unclear and "realized fibers" is undefined | "DEF-12 is tested on Dom_gate, DEF-15 on Im, DEF-17(c) on FB, the others on 𝒟; 'realized fibers' means FB(u) for u ∈ U." |
| 25 | PC-6 (CT-D01; new) | Calls are detected but recomputation is not. s_T's "output" is ambiguous (s(P_a) changes under the substitution test). X_h reads Obs's definition while Obs reads [h]. | Add: "**Record-factorization test:** if an auditor exhibits an L₀ map F of length ≤ c_dec with a component's output = F(Γ_Π) on Dom_gate, the component recomputes a functional of Γ_Π." Add: "s_T's output is the map s, built from T_Π alone; s is applied to record laws only by charter code, and the substitution test compares s, not s(P_a)." Add: "X_h reads Obs only with its [h]-argument unbound; selecting [h] by any criterion evaluated through Obs is DEF-17(a)." |
| 26 | IP-6 closure (L P-rule (iii)) | The definability clause was dropped | "…or any structure from which such an item is L₀-definable within c_dec bits, is that item." |
| 27 | §2.5 c_ι (new) | "u_ι" is undefined when Sol realizes several interface values on ι | "c_ι := the minimum over realized u ∈ U_ι of …" |
| 28 | NR-10(f) (A-1 recurrence) | Every X_h or X_T "names" a readout class or group | "no input **other than a §1.2 component's construction** names a record-space group action or a readout class; a component whose returned class or group is constant on Dom_gate, or decodable within c_dec bits from its definition alone, supplies it (PS-3/PS-4)." |
| 29 | §5.1 "Supplied" (A-2) | The definition is narrower than the §5.2 inventory | "'Supplied' means present, declared, in any input of the §5.2 inventory, or in a clause NR-2 flags as target-level." |
| 30 | FZ-2 and §24.1 | `charter_workings/FREEZE_VERIFICATION.md`, which FZ-2 cites, does not exist. CT-D10, RT-3, RT-5, RT-16 and RT-23 have no §24.1 rows, and the blanket presumption is undefined for patterns with no stated classification. | Add CT rows (clause and outcome) for those IDs and for fixes 9–16. State that FZ-2 is not satisfied until the record exists and lists every report pattern with its blocking clause. |
| 31 | NR-3 (new) | "or with VI_norm > δ_Π" has no reference partition | "…or with VI_norm > δ_Π from every Π realized on Sol of the same instance". |

---

## 3. Summary

1. **Coverage.** Of 91 D/L items, 79 PASS, 11 are WEAKENED, and 1 is UNCAUGHT (L:RT-5, a separable conjunct written in Ξ-variables). RT-5 is held only by the §24.1 presumption, because NR-17's "Π, T_Π and Γ_Π treated as free variables" never fires on a Ξ-level conjunct.
2. **Blockers.**
   - Fix 1: BP-5's "up to the order the prediction uses" regresses v1 and S:RT-S-09/M:RT-01. It starves B-SRB of the reference correlators and reopens the BRI1 FDT route.
   - Fix 2: rewrite NR-17 (JN) and NR-4 so a cheap conjunct, or a cheap Ξ-level predicate, that forces ℛ★ through the components is RELOCATED.
3. **Distillation losses not listed in Appendix D:**
   - c_J no longer formed within fixed-T fibers;
   - the size test's "beyond the ontology price" and b_Π 8 → 6;
   - DIF-5(e) no longer binds at Stage 3;
   - the DEF closure in B-SRB;
   - "ℛ★ need not separate" the twin;
   - DEF-15 "or of mathematics";
   - MC-4's log minimum;
   - PC-6's ban on reading protocol identity.

   Appendix D is therefore not the complete diff it claims to be.
4. **New major loopholes in the scanned clauses:**
   - a decoder just above c_dec while G pays up to 768 bits for Π;
   - the non-standard poison pill that disables c_J(b), with Price(M) undefined;
   - the inexpressible-type escape from Q3(c) and NR-10(e)/(l);
   - the instance-indexed pin pair under Q5;
   - card-scaled or under-covered s_T.

   Four literal hidden kills under CV-1:
   - §1.3 "if T_Π contains one";
   - the non-unique factorization in PC-7(b);
   - NR-7 applied to components;
   - Q4's "not on the components".
5. **Recommendation.** Do not freeze until fixes 1 and 2 are applied, fixes 3–16 are applied or recorded as owner-reviewed Appendix-D choices, and `FREEZE_VERIFICATION.md` exists. The §1.3 size test currently contradicts self-test ST-6 and the Appendix-A feasibility note, so FZ-2's on-paper self-test confirmation cannot stand as written.
