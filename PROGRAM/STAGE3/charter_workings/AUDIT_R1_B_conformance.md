# Pre-freeze audit B: conformance, R1 integrity, cross-references, consistency, freezability, candidate check

**Audited:** `PROGRAM/STAGE3/STAGE3_CHARTER.md` (2353 lines, untracked) in worktree `/tmp/claude-0/mainwt`, branch `grut2-stage3` at `86bf5a0`.
**Against:** OWNER_RULINGS G2-11 (ruling block, additions 1–5, reconciliation note) and G2-10; STATE, RULES, NORTH_STAR, CHECKS; R1_SYNTHESIS §1 and §12; R1_T_LADDER §0–§2, §8–§10; D5 audit and identification; F0_REQUIREMENTS_CONSOLIDATION_01 (R1–R15); GRAVEYARD; and the working record `charter_workings/`.
**Mode:** read-only. No repository file was edited. No candidate law is proposed here.
**Line numbers** ("L###") refer to the current untracked charter file.

---

## Part 1. What passes

**Conformance to G2-11.** Each binding sentence has an implementing clause, and none is weakened outright:
- items 1–9 map to §§2–10;
- additions 1–4 map to §§11–14;
- the central task maps to §1.2 and §3.1;
- "derive modulo representation, no unique h" maps to §1.3, Q7, C17 and NR-10(h);
- "no presumed monotone tradeoff" maps to CV-5, Q11, NR-13, PS-6 and C18;
- "frozen ALONE" and "STOP before Card 1" map to the status header, FZ-1 to FZ-3, §18.1 step 0 and §25.

**𝒜_ε.** The charter treats 𝒜_ε as the image of 𝒜_Γ × 𝒜_T everywhere it appears: L91, L423–424, L793, L1322, L1432, L2049 and L2312. No bits are counted on it, and the charter nowhere treats it as an axis. The reconciliation note is honoured.

**Candidate check: PASS.** The charter contains no candidate law and no sketch, name or example of 𝒦.
- The only "examples" are of protected inputs (PS-5), of definitional classes (DEF-15), of regime facts (RH-DB), of abstract gaming patterns (CT-xx) and of known textbook objects (§24.2).
- The Appendix-A feasibility note counts tokens only.
- The working-record README makes the same statement for its own files.

**Syntactic cross-references.**
- Every numbered ID cited in the text lies inside a defined range: Q1–12, SC1–4, PC-1–8, NR-0–17, PS-1–6, DEF-1–17, STD-1–15, MC-1–11, BU-1–9 (with BU-7′), VAR-1–6, KU-1–13, KP-1–5, IP-1–14, CT-01–76, ST-1–11, DIF-1–10, SEL-0–16 and SEL-H, HB-1–12, RS-1–6, XS-1–10, SI-1–5, PV-1–6, SM-1–9, T-1–5, FR1–15, GY-1–12, CV-1–7, BP-1–7, OR-1–6, SFP-1–11, DC-1–10, FZ-1–3, C1–C20, AI-1–5, RM1–5, Ch-1–5, VB-1–21, RB1–6, P-1–4, S0–S9, G4-*/G5-*.
- Every § number resolves.
- Appendices A, B, D, E and G exist.
- GY-1..GY-12 match the 12 GRAVEYARD.md entries in order.
- FR1–FR15 match F0 R1–R15.
- Every cited source file and commit exists (`0a9a941`, `dbfd64b`, `86bf5a0`, `82d311e`, `cb81a3b`, `aacbc52`).
- The *wrong* targets are listed below.

**Numbers against Appendix A.** These agree with the text:
- N_cred = 48 = 1 + 47;
- p★ = 10;
- Q_min = 10 (3.32 bits);
- b_Π = 6;
- n_min = 8, giving 8 ≤ |V| ≤ 16;
- 2⁸ − 2 = 254 ≈ 7.99 bits;
- 2961 = 1721 + 1232 + 8, 1232 = 992 + 240, and 2721 = 1721 + 992 + 8;
- the 128-element (2,2,2) relabelling group;
- c_dec, ℓ_dec and p_dec; ℓ_tr and b_patch; κ, R_item and R_card;
- N_max, α = 0.0027 (3σ), power, σ_pre ≤ |J_K|/4 and 1.25·σ_pre;
- N_pool, the clocks, the HB ranges and θ_gen.

The feasibility arithmetic also checks: 640 bits of price; 48 × 19.32 ≈ 927; 48 × 13.32 ≈ 639; 48 × 23.32 ≈ 1119.

The B-REC numbers match their sources:
- the harmonic twin, 1.27×10⁻¹⁴;
- M-A and M-A′, 1.915×10⁻²;
- M-B, 7.98×10⁻³;
- the Prop. G rate with V* = 0.943578;
- the grid (π, 3π/2, 2π).

**KU-11 against §4.4.** These are consistent: KU-11 is exactly "not COMPRESSIVE".

**Evaluation order.** BU-6, §18.1 and §0.6 item 5 agree on sequential evaluation. The only literal "batch" left is IP-13 (finding 12). Appendix D row D-3 quotes v1's batch rule as history, and that is legitimate.

**Freezability (owner decisions).** No open owner decision point blocks the freeze.
- Appendix D, §19.2 and Appendix A make every rule a default that the owner may change in either direction before the first draft is logged.
- OD-12 (authorizing the kit) is correctly placed after review, not before the freeze.
- The undefined *numbers* that remain are listed below (findings 3, 12, 13, 14).

---

## Part 2. Findings

Severity: **BLOCKER** = must fix before freezing · **MAJOR** · **MINOR**.

### BLOCKER

**1. BLOCKER — The freeze act as written contradicts RULES 8, and its verification record does not exist.**
- **Locations:**
  - Status header L15–16: "The freeze commit carries a `pending` line in `PROGRAM/CHECKS.md` (RULES rule 8)."
  - FZ-1 L1903: "This charter is committed **alone**, with a `pending` CHECKS line."
  - §25 L2187: same wording.
  - FZ-2 L1905–1909: "At the freeze, the builder confirmed … The confirmation record is `charter_workings/FREEZE_VERIFICATION.md`."
  - §18.1 step 2 L1866–1867: "Card freeze: one commit … a CHECKS line."
- **Problem.**
  - RULES 8 and the CHECKS header both say a line is added *only after the push is verified on the remote*, and the line carries the SHA. A commit cannot contain its own CHECKS line, so the charter tells the builder to break RULES 8 while citing RULES 8. §23 has the correct rule.
  - `FREEZE_VERIFICATION.md` does not exist in `charter_workings/`, yet FZ-2 states in the past tense that it does.
  - The §24.1 presumption and FZ-2 depend on `charter_workings/`, which is untracked. "Committed alone" read literally would leave those references dangling at the freeze SHA.
- **Replacement wording.**
  - Header L15–16: "Nothing here is banked. After the freeze commit is pushed and verified on the remote, a separate commit adds its `pending` line to `PROGRAM/CHECKS.md` (RULES rule 8)."
  - FZ-1: "**FZ-1** This charter is frozen **alone**: the freeze commit contains no 𝒦 card, draft, candidate or kit artifact. The non-normative working record `charter_workings/`, including `FREEZE_VERIFICATION.md`, is in the freeze commit or an earlier one. After the push is verified on the remote, a separate commit adds the `pending` CHECKS line (RULES 8). Every card cites the freeze SHA."
  - §25 first bullet: "This charter is frozen alone (FZ-1); its `pending` CHECKS line is added after the push is verified on the remote."
  - §18.1 step 2: replace "a CHECKS line" with "its CHECKS line is added after the push is verified on the remote (§23)".
  - Precondition: write `charter_workings/FREEZE_VERIFICATION.md` before the freeze commit.

**2. BLOCKER — R1 integrity: "frozen tiers" mislabels R1, and d_op is undefined at E₂± and T_caus.**
- **Locations:**
  - §1.4 L265–271: "Catalogue: E₂± ⊂ T_caus ⊂ T_lin = T_R1 …"; "Admissible set 𝕃_T^adm := {E₂±, T_caus, T_lin, T_mono} ∪ …"; "**Frozen d_op:** d_q^BL (center, whiten, minimize over O(k)) for T_lin; the normal-score form modulo reflections for T_mono; d_BL with its frozen normalization."
  - "frozen tier(s)/class" at L154, L272, L450, L551, L607, L1351, L1556 and L1628.
  - §2.3 L413: "𝒯 = {E₂±, T_caus, T_lin, T_mono} frozen".
- **Problem.**
  - R1's frozen definition has **two** tiers: T_R1 = GL(k) with translations, and T_mono (R1_SYNTHESIS §1: "Interface class (frozen; two tiers)").
  - The frozen distance is the BL quotient for T_R1 (R1_T_LADDER §0, §8, §11) and the normal-score BL modulo ℛ for T_mono (§9).
  - E₂± and T_caus are ladder rungs whose only R1 distance is the superseded v2 W₃ form. R1_T_LADDER §1 says "the choice of d_op per class … is a definition decision, open to owner veto".
  - The charter therefore (a) calls four classes "frozen tiers", which changes R1's tier vocabulary, and (b) never fixes ε at E₂± and T_caus, although both sit in 𝕃_T^adm, 𝒯, Q8, SCOPE-Q, B-REC and the chart. ε is "computed only by charter code … with no … alternative distance", but that code is undefined for two of the five catalogue entries.
  - Under W₃, DEF-2's "ε_R ≤ 2" and the window [0, 2] are false.
- **Replacement wording.** Replace the "Frozen d_op" bullet at L270–271 with:
  > "- **R1's frozen tiers** are T_R1 = T_lin (Tier 1) and T_mono (Tier 2), with their frozen distances: d_q^BL(P, Q) = min over O ∈ O(k) of d_BL(P̃, O#Q̃) after centering and whitening, and d_BL between normal-score laws minimized over the reflections ℛ, with ‖f‖_BL = max(‖f‖_∞, Lip f) (R1_SYNTHESIS §1). E₂± and T_caus are sub-classes of T_R1 from the R1 ladder (R1_T_LADDER §1). They are **charter catalogue classes, not R1 tiers**. For them this charter fixes the same bounded-Lipschitz quotient on R1's canonical reductions: d_op(P, T·Q) := min over s ∈ {±1}^k of d_BL(s_T P, s·s_T Q), where s_T is per-coordinate standardization (E₂±) or the Cholesky innovations (T_caus). The R1 v1/v2 W₃ forms are not used. This is a Stage-3 convention. It changes no R1 definition, distance, tier or verdict."

  Then:
  - replace "frozen tier(s)" with "catalogue class(es) 𝒯" at L154, L272, L450, L607, L1351, L1556 and L1628;
  - replace "one fixed frozen class" with "one fixed catalogue class" at L551;
  - replace "𝒯 = {E₂±, T_caus, T_lin, T_mono} frozen" with "𝒯 = {E₂±, T_caus, T_lin, T_mono} (the charter catalogue)" at L413.

### MAJOR

**3. MAJOR — R1 integrity: DEF-4 asserts a property that R1 explicitly does not claim.**
- **Location:** §12 L1333: "**DEF-4** Monotonicity in T: T ⊆ T′ ⇒ ε^{T′} ≤ ε^{T}; zero sets are monotone along the ladder."
- **Problem.** R1_T_LADDER §2 (L286–288) says: "**Not claimed:** that the value ε_R^T is monotone in T, since the distances are T-adapted. What is monotone is the zero set." The value inequality is unproved, and in general it fails across canonical reductions (standardized, whitened and normal-score coordinates differ). This breaks CV-3 / RULES 5 and attributes to R1 a theorem it disclaims.
- **Replacement:** "**DEF-4** Zero-set monotonicity in T: if T ⊆ T′ and ε^T = 0, then ε^{T′} = 0 (R1_T_LADDER §2). R1 does not claim that the *value* of ε is monotone in T, because the distances are T-adapted; any cross-class value comparison is assessed under DEF-13 and DEF-14."

**4. MAJOR — R1 integrity: the charter claims that the join trivializes ε.**
- **Locations:**
  - B-NULL L1700: "a maximal-interface null (T ⊇ J or T_univ) gives ε ≡ 0 and voids ε-relations".
  - CT-14 L2104: "A generated T_Π ⊇ J or T_univ, so ε ≡ 0".
  - §1.4 L266: "the join J; T_univ" (neither is defined).
- **Problem.** G2-10, G2-11, SCOREBOARD #11 and R1_SYNTHESIS §9 all say: "**No claim** is made about the group generated by T_lin and T_mono … expected, but not proved, to trivialize ε_R." The charter states it as fact. The voiding rule itself is fine.
- **Replacement.**
  - §1.4 L266: "… the join J := the group generated by T_lin and T_mono (R1 makes no claim about it; R1_SYNTHESIS §9); T_univ := all bimeasurable bijections of the record space (GY-11; Prop. E); and the GY-11/GY-12 classes."
  - B-NULL: "a maximal-interface null (T ⊇ J or T_univ): ε at such a class is void by rule (§1.4) and ε-relations there earn nothing (ε^{T_univ} ≡ 0 is DEF-9; R1 makes no claim about J)".
  - CT-14: "A generated T_Π ⊇ J or T_univ | Q8, DIF-5, B-NULL | ε void by rule (§1.4); relations void; DIF-5 fails".

**5. MAJOR — Addition 3 in the generated-structure credit G (Π term): standard selectors become optional.**
- **Location:** §2.3 L405–411: "If the Intake auditor confirms that the FR11 meaning of 𝒞 admits no standard dynamical reading, every partition with S ≠ ∅ ≠ E is admitted (2^|V| − 2 …). Otherwise the standard selectors (SPS, §5.4) and the STD-10 criteria are applied to the **realized dynamics of Sol** …"
- **Problem.**
  - With an exotic 𝒞, the Π freedom is counted before SPS, which includes conservation-law and symmetry-sector partitions (STD-5, addition 3), and before STD-10 are applied to Sol's realized dynamics. That is up to 16 bits × 48 per card.
  - This contradicts §4.3(b)'s own parenthetical ("𝒜_Π already applies the standard selectors to the realized dynamics") and B-DIF (viii).
  - §4.3(b) also writes "𝒜_Π(ι)/Aut(𝒞_ι)" without a regime class, while §2.3 already quotients by Aut and is indexed by H.
- **Replacement (§2.3):** "… every partition with S ≠ ∅ ≠ E is admitted (2^|V| − 2 with one S; ordered set partitions with a designated E for multi-block embeddings). **In every case** the standard selectors (SPS, §5.4) and the STD-10 criteria are then applied to the realized dynamics of Sol, and also to 𝒞 when its FR11 meaning has a standard dynamical reading. A partition any of them selects from the same data is not a hand choice, and the smaller set governs."
- **Replacement (§4.3(b), first sub-bullet):** "min(16, log₂|𝒜_Π(ι | H(ι))|), with H(ι) the hostile regime class of BP-4 at ι, if Π is GENERATED (§5.5), else 0."

**6. MAJOR — Addition 3 in G (T term): freedom is counted on the pre-standard catalogue.**
- **Locations:**
  - §4.3(b) L780: "log₂|𝒯 ∪ {⊥}| = log₂ 5 if [h] and T_Π are GENERATED".
  - Appendix A L2214: "G caps | … T term log₂ 5".
- **Problem.**
  - The T term is a fixed catalogue count, not |𝒜_T(ι, Π | H)|. 𝒜_T is defined *after* 𝒮: causally implementable (STD-1), CP-implementable (STD-2), and containing the calibrated maps.
  - T_lin contains non-causal smoothing (R1_T_LADDER §1), so 𝒜_T can have 4 or fewer elements. The credit then exceeds the post-standard freedom, contrary to BP-1 and addition 3.
  - §4.3(b) says "=" while Appendix A says "cap".
- **Replacement (§4.3(b)):** "min(log₂ 5, log₂|𝒜_T(ι, Π_ι | H(ι)) ∩ (𝒯 ∪ {⊥})|) if [h] and T_Π are GENERATED, else 0 (𝒜_T after 𝒮, §2.3);"
- **Replacement (Appendix A):** "G caps | Π term ≤ 16 bits; T term ≤ log₂ 5; carrier term 1 bit".
- Also add to STD-11: "(G's T term credits only the removal of a hand choice; it never credits the existence or form of [h]_T.)"

**7. MAJOR — Addition 3: the regime-hypothesis threshold is stated four different ways and is dimensionally ill-defined.**
- **Locations:**
  - BP-4 L366–367: "unless a deviation δ ≥ max(3·r_lock, 2^(−p★)) is certified in its §13.2 surrogate metric".
  - BP-6 L382–383: "A framework applies at x unless the card proves one of its hypotheses fails at x by at least 2^(−p★)".
  - §1.5 L312–313: "every hypothesis not certified to fail by at least 3·r_lock (BP-4)".
  - §13.2 L1388–1389: "certified defect, normalized to [0, 1], is at least max(2^(−p★), 3·r_lock)".
  - §13.5 L1509–1510: "failing by δ in its frozen metric (relative entropy …; entropy-production rate; KMS defect …)".
- **Problem.**
  - BP-6 lets a card escape a standard framework at the weaker bound 2^(−p★), which weakens addition 3.
  - §1.5 drops the 2^(−p★) floor.
  - r_lock is in observable units and is "per observable", but §13.2 compares it with a defect normalized to [0, 1].
  - The §13.5 metrics are unbounded, and no normalization is given.
- **Replacement.** Define the threshold once, in §13.2:
  > "**δ_RH** := max(2^(−p★), 3·r̂_lock), where r̂_lock := max over the card's lock observables of r_lock/|W| (dimensionless). A hypothesis holds unless its certified defect, in the frozen surrogate metric m of this table mapped to [0, 1] by m ↦ m/(1+m) when m is unbounded, is at least δ_RH. (The map is a default the owner may change at review.)"

  Then:
  - BP-4: "… unless a defect ≥ δ_RH (§13.2) is certified …";
  - BP-6: "A framework applies at x unless one of its hypotheses is certified to fail at x by at least δ_RH (§13.2)";
  - §1.5: "… every hypothesis not certified to fail by at least δ_RH (BP-4)";
  - §13.5: "a hypothesis failing by a normalized defect ≥ δ_RH still imposes …".

**8. MAJOR — Addition 3 in the transfer gain: 𝒜_B^base is undefined.**
- **Location:** XS-7 L1236 and L1239: "**TG** := F_p(𝒜_B^base) − F_p(Im_{𝒦,B}(θ̂_A)) ≥ p★"; "band ≤ ¼ of the target's range over 𝒜_B^base".
- **Problem.** This is a freedom count, and nothing says it is taken after 𝒮.
- **Replacement (add to XS-7):** "Here 𝒜_B^base := the post-standard fibered baseline FB of sector B (§2.3) under H_σB, after §13, intersected with the interval the Standard Bridge Panel (SI-3) gives from A's data. Im_{𝒦,B}(θ) is the image of Sol_𝒦 in B's frozen chart coordinates at parameters θ."

**9. MAJOR — Addition 4: Q9 "Any scope" makes SCOPE-G impossible in linear-Gaussian regimes.**
- **Location:** Q9 L566–568: "Any scope: on each lock fiber, FB has points with ℛ★ = 0 and with ℛ★ ≠ 0, and points with ε = 0 and ε > 0."
- **Problem.**
  - STD-3 (L1431–1432) gives 𝒜_ε = {0} under RH-KMS, RH-GAU and linear coupling, and the RH-GAU row gives ε^T = 0 for T ⊇ T_caus.
  - So every SCOPE-G ("response in general") relation fails Q9 on such fibers, although addition 4 exists precisely because ε_R is blind to linear response. This cross-subsidizes scope, contrary to RS-2.
  - The class at which "ε" is evaluated is also unspecified.
- **Replacement:** "**Q9 Non-vacuous.** Any scope: on each lock fiber, FB has points with ℛ★ = 0 and with ℛ★ ≠ 0. Scope Q additionally: every lock fiber has certified realized points with ε^{T_Π} > r_lock; FB has points with ε^{T_Π} = 0 and with ε^{T_Π} > 0; and ℛ★ is not satisfied merely because ε_R ≡ 0."

**10. MAJOR — Batch leftover: multiplicity across cards is undefined under sequential evaluation and triggers LOCK-VOID.**
- **Locations:**
  - MC-9 L665–666: "thresholds are Bonferroni-adjusted across observables and across every card locked in the route."
  - BU-7′ L1067–1068: "Confirmation thresholds are Bonferroni-adjusted across every card locked in the route."
  - MC-5 L638–640: LOCK-VOID if "any threshold … changes after card freeze".
- **Problem.**
  - Under BU-6, picks and locks are sequential (BU-7 allows a second pick after a failure). The number of cards that will be locked is unknown when C13 is frozen.
  - A later lock would change an earlier card's thresholds, which MC-5 makes LOCK-VOID (= LOCK-FALSIFIED).
  - The adjustment's form is also unstated, against the fixed 3σ/2σ multipliers and α = 0.0027 in Appendix A.
- **Replacement (MC-9):** "**MC-9 Multiplicity.** At most 3 lock observables per card. The adjustment is fixed at card freeze and is never changed by a later card. Each lock observable is tested at α_obs := α/(3·n_obs), where 3 is the route's card budget (BU-1). The MC-5 falsification multiplier 3 becomes z_obs := Φ⁻¹(1 − α_obs/2), the confirmation multiplier 2 becomes z_obs − 1, and MC-7 power is computed at α_obs."
- **Replacement (BU-7′, last sentence):** "Lock thresholds use the fixed adjustment of MC-9."

**11. MAJOR — Batch leftover: an earlier card's unsealed items are not excluded for later cards.**
- **Locations:**
  - BU-6 L1060–1062: "sealed items — AI-3 seeds, credit-family draws, holdouts, lock datasets — are drawn fresh after each card's freeze and never shown to an author before that card is frozen."
  - §15.9 pools L1728–1733.
- **Problem.** Card k+1's author may "learn from earlier verdicts". Card k's SEL-H, reciprocity and AI-5 holdouts are then known, but only lock datasets are barred from reuse (BU-7′). "Drawn fresh" does not exclude items already seen.
- **Replacement (append to BU-6):** "Every sealed item that was unsealed or reported for an earlier card (SEL-H and reciprocity holdouts, AI-5 instances, LOCK-H datasets) is added to the exclusion lists of every later card (§15.9, MC-8) and is public development data for it."

**12. MAJOR — Freezability (CV-6): the AI-3 sample size N is not fixed, and "batch" wording remains.**
- **Locations:**
  - IP-13 L766–767: "log₂ C(N, k), where N is the size of the AI-3 batch".
  - AI-3 row L302.
  - Credit-family draws L306–307.
  - DIF-7 L1752–1753: "≥ θ_gen [A] of the AI-3 draws".
  - NR-4 and NR-6: "fraction ≥ p_dec of AI-3".
  - AI-5 count: unset.
- **Problem.**
  - The number of AI-3 draws is fixed nowhere, yet it sets the IP-13 price: ≈ 0.47·N bits at 10% exclusion, so the hostile resolution under CV-1 is unbounded.
  - It also sets DIF-7 coverage and the NR-4/NR-6 fractions.
  - "batch" is a v1 term.
- **Replacement.**
  - Appendix A, new row: "AI-3 sample; AI-5 | N_AI3 = 200 draws per card, seeds committed by the Selector after the card's freeze (default; the owner may change it at review); AI-5: 3 instances".
  - IP-13: "… where N := N_AI3 [A], the number of AI-3 draws committed for the card, and k the number of those draws the predicate excludes."
  - §1.5 credit family: "… N_cred − 1 [A] instances: the first in seed order of the N_AI3 committed AI-3 draws that satisfy the frozen domain predicate (DIF-7)."

**13. MAJOR — Dangling reference: the scope-G chart coordinates point to nothing.**
- **Location:** §1.5 chart L319: "Scope G: the response functionals of Appendix A."
- **Problem.** Appendix A lists no response functionals; it has only a window rule at L2203. The kit must build the chart before Card 1, and MC-1, MC-4 and XS-7 lock on chart coordinates. Under CV-1 (hostile default), SCOPE-G would have no lockable coordinate.
- **Replacement (§1.5):** "Scope G: the response functionals of the driven and recorded variables at the frozen templates and grid: mean response up to order m in the amplitude, two-time linear response functions, susceptibilities, power and cross spectra up to order m, and transport coefficients, in whitened units."
- **Replacement (Appendix A, new row):** "Scope-G chart | the response functionals of §1.5 up to order m at r★ and r★★; windows: each functional's range over B-HB at the standard reference parameters".

**14. MAJOR — Undefined symbol in a gate: σ_tot in MC-4.**
- **Location:** MC-4 L628: "b_meas := log₂( N(J_SRB ∩ W) / N(J_K ⊕ 2σ_tot at N_max) )".
- **Problem.** σ_tot is defined nowhere. b_meas gates b_J (§4.3(a)), Q6, B-SRB and G5-MDL. Under the hostile default, an undefined width makes b_meas fail always.
- **Replacement:** "… N(J_K ⊕ 2σ_tot at N_max) ), where σ_tot := max(σ_pre, σ_stat(N_max)) is σ_eff of MC-5 with the statistical error at N_max effective samples."

**15. MAJOR — BU-8 and IP-12 capture the charter's own self-tests and nulls.**
- **Locations:**
  - BU-8 L1069–1070: "Any artifact that states a law in L₀ for evaluation is a card."
  - IP-12 L760–763: "n_drafts counts every distinct 𝒦 … for which any score, verdict, price or chain output was computed … by any agent or program, since G2-11".
  - §24.2 header: "Known object treated as a card".
  - §19.3: "ST-6 to ST-9 computed".
- **Problem.** The kit must evaluate ST-6 to ST-9 (and the B-NULL nulls) as cards. Read literally, together with CV-1, they consume budget slots and inflate n_drafts.
- **Replacement (append to BU-8):** "Exempt: the §24.2 self-tests, the §19.3 rejection tests and the §15.6 nulls. These are charter controls built from known objects or standard models. They consume no slot, are not 𝒦 drafts for IP-12, and may not be submitted as cards."

**16. MAJOR — The self-test "required verdicts" conflict with the first-failing-screen rule (load-bearing through FZ-2 and CV-7).**
- **Locations:**
  - §24.2: ST-4 "Credited = 0, so ΔL ≤ 0: LOOKUP → RELOCATED; also NONGENERATIVE"; ST-7 "c_J = 0 by §2.5(b); NON-COMPRESSIVE"; ST-1 "S3: CARD-NONGENERATIVE (… Gibbs state … supplied)".
  - T-1 L1257–1258: "The first failing screen (§18.2) names the terminal".
- **Problem.**
  - Under T-1, ST-4 terminates at S3 (CARD-NONGENERATIVE), not S6 (LOOKUP).
  - ST-7 terminates at S3 (supplied rule) or at S5 (Q5 with c_J = 0 is CARD-NONJOINT), never at S6.
  - ST-1 also meets §5.6 "Gibbs … used by ℛ★ → CARD-RELOCATED" inside S3, and §18.2 gives no precedence between terminals within one screen.
  - FZ-2 certifies that the self-tests "return their stated verdicts", and CV-7 voids any interpretation that "changes a self-test verdict". So the verdict semantics must be unambiguous.
- **Replacement.**
  - Add to T-1: "Within one screen, the terminal is the first one listed in §18.2 whose condition holds. All other failures are recorded on the GRAVEYARD line."
  - Add under the §24.2 heading: "'Required verdict' lists the clauses that must fire on the object. The object's terminal follows T-1. FZ-2 and CV-7 compare these clause lists, not terminals."

### MINOR

17. **SC2 points to the wrong section.** L586 "COMPRESSIVE under §4.5" → "COMPRESSIVE under §4.4". (§4.5 is the ledger.)

18. **§1.6 L338 "(R1 §0)".** R1_SYNTHESIS has no §0 → "(R1_T_LADDER §0)".

19. **§1.3 L257 "it counts as a failure (DC-6)".** DC-6 concerns UNSCORABLE → "(T-1)".

20. **MC-6 L647 "as the card's C9".** The state-variable and readout derivation is in C7 → "as derived in the card's C7 and declared for measurement in C9 (RS-6)".

21. **§1.5 L312 "certified under MC-6".** MC-6 is the carrier checklist, not regime certification → "certified under BP-4 from the platform's interface-side data (MC-2)".

22. **Undefined or unanchored symbols:**
    - "𝒮-checker" (L205): → "the regime surrogates and 𝒮 derivations of the kit (§19.3)";
    - N_frozen (L765, L1063): → "N_frozen := the number of frozen CARD-ADMISSIBLE cards at the pick";
    - W in "Y_a = t_a(W)" (L246): → "W := h(Z_Π)";
    - d_rec (Appendix A): define as "record dimension per grid time";
    - E₂±, T_caus and T_mono are named but not defined in the charter: add one line citing R1_T_LADDER §1 and §9;
    - θ_K is used in BP-5 before XS-4: add "(XS-4)".

23. **Symbol collisions.**
    - H is used for the horizon (§1.3) and for the regime class (§1.5, §2).
    - κ is used for κ_J/κ_ι and for the resource multiplier (DC-2).
    - J is used for the join, J_K, J_SRB and J(ω).
    - G is used for the credit and in RH-SYM(G).
    - k is used for grid times, record dimension and the IP-13 exclusion count.
    - "C1–C6" and "D1–D3" (D5 analyses; PV-2, PV-5) collide with card fields C1–C20 and Appendix D rows.

    Fix: rename the horizon H_hor, the multiplier κ_res and the IP-13 count k_ex, and always prefix "D5 C1–C6" and "D5 D1–D3".

24. **Appendix D still references removed appendices and working-record IDs.**
    - D-7 "Separate Appendix F" → "v1 Appendix F".
    - D-8 "Appendix C decision points" → "v1 Appendix C (owner decision points OD-1…OD-15)".
    - D-5 "CT-D02 and CT-D05" → "(working record, REDTEAM_D_definitional.md)".
    - OD-4 (Appendix-A constants) and OD-14 (two relations) are not accounted for: cite OD-4 in D-4 and OD-14 in D-2.

25. **The §0.6 summary misstates the sections.**
    - Item 3: "Required: credit − price ≥ 10 bits" omits "and ΔL > 0 at p = 16".
    - Item 3: "all over 48 independent instances" is wrong for D_sel, which is not multiplied by N_cred.
    - Item 9: "Three failures end the route" omits T-3(a) early final count, T-3(b) and T-3(c).
    - Item 9: "no … rescoring" contradicts PV-3, §13.4 and §19.2 (rescoring toward failure).
    - Item 2 omits Q4 (W-pipe), Q8 and Q12.

    Replace item 3's last line with "Required (§4.4): ΔL ≥ p★ at p = 10 and ΔL > 0 at p = 16; D_sel is not multiplied by N_cred." Replace item 9 with "The route terminates under T-3. No extension stages, prerequisite campaigns, or rescoring except toward failure."

26. **The §18.2 terminal lists are incomplete.**
    - S2 lacks CARD-UNMEASURABLE (DC-8) and BATTERY-TUNED (DC-1).
    - S3 lacks CARD-DEFINITIONAL for PC-7(b) and for protocol-induced maps in T_Π (§1.3 L243–245), and lacks MODE SELECTION (PC-7(d), NR-11).
    - S6 gives no terminal for a failure of the SC1 nontrivial-reduction conditions of §2.5.
    - MC-2's "a pin: DEFINITIONAL" is decided at S7, whose only terminal is UNMEASURABLE.

    Add the missing terminals, or state "a clause's own label is recorded; the terminal is the screen's."

27. **Q10 (L569–570): "Exactly one response scope is declared and frozen with the card, and ℛ★ is consistent with it".** Addition 4 binds *each* relation, and the secondary relation is scored under Q1–Q12. → "The relation declares exactly one response scope (§14), frozen with the card, and is consistent with it. The primary and the secondary relation each carry their own declaration."

28. **MC-4 L633 "Scope Q additionally requires J_K ∩ [0, 3σ_pre] = ∅".** This is asymmetric for signed witness coordinates (it allows (−3σ_pre, 0)), and it rules out locked zero predictions, which tilts against one sign (CV-5). → "J_K is separated by at least 3σ_pre from the value the observable takes on T_Π-separable families (0 for ε; 0 on both sides for a signed witness), unless J_SRB excludes that value by at least 3σ_pre."

29. **§2.5 L475 "One codimension is worth exactly p★ bits"** conflicts with §4.3 L797–798 "b_J uses p bits per codimension" at p = 6 and 16. → "One codimension is worth p bits at sensitivity level p (p★ at the reference level); κ is counted at resolution 2^(−p)."

30. **IP-6 L741 and Appendix B.2 L2282: "VB-17 to VB-21 … cannot be bought".** IP-7 prices declared PS-5 inputs (VB-17). → "are protected: paying for them never makes them generated or creditable (§5.1, §5.6)".

31. **§4.5 L815 "Thresholds are never reopened"** conflicts with §19.2 and Appendix A tightening repairs. → "Thresholds are never loosened. They change only by a tightening repair (§19.2)."

32. **MC-6 L648–651.** "a failed certification … counts as LOCK-FALSIFIED" conflicts with "One preregistered alternate platform is allowed, used only if the primary fails MC-6 before any lock datum is unsealed". → "A certification failure on the primary before any datum is unsealed moves the lock to the alternate. Only a failure on the platform actually used counts as LOCK-FALSIFIED (if the card predicted a certifiable carrier there)."

33. **MC-2 L612 "full admissible range over 𝒜_Π × 𝒜_T"** uses the product, against §2.3 "never against the product". → "over the interface fibers of FB (Π ∈ 𝒜_Π, ([h], T) ∈ 𝒜_T(ι, Π | H))".

34. **Card-added models conflict with the witness rules.**
    - §2.2 L391 ("card-added models that are independently verified") and Q3(a) L523–524 ("or added by the card and verified independently") are broader than the §15.4 witness rules (L1668), which require HB families within the frozen ranges.
    - BP-7 says FB is never enlarged in the card's favour.

    Align §2.2 and Q3(a) with "card-added models from the HB families or their compositions within the frozen ranges (§15.4)".

35. **KU-7 L1103 "ℛ★ fails any of Q1–Q12".** §3.1 says the secondary relation "can kill the card". → "ℛ★, or the declared secondary relation, fails any of Q1–Q12".

36. **NR-11 L951 "Readouts h_a ∉ [h]_{T_Π} give MODE SELECTION for every ε-relation".** R1's table gives R1-NULL for FAIL with the same orbits, and the charter says the table "applies unchanged" (L258). → "… make the carrier FAIL. Every ε-relation then earns no reciprocity credit, the R1 verdict is read from the unchanged table, and the lock is void."

37. **§1.4(iii) L277–278 "… ⇔ P ∈ cl(T_Π·Q), hence ε^{T_Π} = 0 iff the family is T_Π-separable".** This is true only up to orbit closure. → "… iff the family is T_Π-separable up to orbit closure".

38. **Discrete records.** HB-12 L1664 ("discrete records") and the q = 3 row at L2204 (which names B-SEL, whose scenarios fix their own alphabets) conflict with "ε is always computed on continuous records". → "HB-12 serves the discrete-record chart only and is not an ε witness; q = 3 applies to HB-12 and to discretized continuous records; B-SEL uses each scenario's own alphabet."

39. **§1.2 L155 "the ε_R code (the frozen R1 code)".** R1 froze a definition, not a general ε solver. → "the ε_R code (built by the kit from R1's frozen definition, §19.3)".

40. **Dom_gate (L142–144: "the carrier is PASS") against PASS (L254: "iff the card proves from 𝒦 …").** One is per-Ξ, the other card-level. The CT-61 defense (DEF-12, Q4, NR-3) needs the per-Ξ reading. CV-1 picks it, but the text should say so. → Dom_gate: "the carrier form holds at Ξ (the chain at Ξ returns one h and t_a ∈ T_Π with Y_a = t_a(h(Z_Π)) for every a in A_{r★★})". Carrier status: "PASS iff the card proves from 𝒦 that the carrier form holds at every Ξ ∈ Sol, for every a in every A ∈ 𝔄."

41. **Q6 L558 "c_J ≥ 1 or κ_J ≥ log₂ Q_min on every lock fiber"**, while c_J is defined on the lock family. → "c_ι ≥ 1 or κ_ι ≥ log₂ Q_min at every lock-fiber instance, and c_J ≥ 1 or κ_J ≥ log₂ Q_min".

42. **PC-7(d) L195 "each must stay within r_lock".** r_lock is per lock observable. For bit-valued credits use "… and each credited bit count within 1 bit".

43. **CV-6 L68 "fixed in this charter"** conflicts with kit-fixed catalogues: HB-10 "kit-frozen ensemble", the chart, the VB axiom checklists and the regime surrogates. → "fixed in this charter, or by the §19.3 kit before the first draft is logged".

44. **G2-11 asks for "objective *persistent* carrier/readout structure".** Persistence is tested only for Π (DIF-2). → add to NR-10: "(m) Z_Π, [h]_{T_Π} and T_Π are unchanged under horizon doubling (2H) and the scale window, at r★ and r★★."

45. **Other loose ends.**
    - Q3(b) L529: "STANDARD-GENERIC" has no stated consequence → "… is STANDARD-GENERIC and fails Q3".
    - Appendix A L2218: "≤ 30 days in total" → "≤ 30 days per card".
    - IP-12 L765: "At the owner's pick, log₂ N_frozen is added" → add "(this may move a verdict only toward failure)".

46. **Feasibility note L2244–2252.** "Π term at its 6-bit floor" is not a floor that exists: b_Π binds only on the lock fibers. "It is not reachable by tuning" overstates the case, because the 20-constant card passes at c_J = 2 (48 × 29.32 − 1040 ≈ +367). → "(Π term taken at b_Π for illustration; no floor applies on credit instances)" and "a tuned card fails at c_J = 1".

47. **§24.1 L2086–2087 extends the CHARTER TEST presumption to every working-record pattern.** Some v0/v1 classifications differ from this text (for example, two credited relations). Add: "Where a working-record classification conflicts with this text, this text governs."

---

## Part 3. Five-line summary

1. **Conformance.** Every G2-11 item, sentence and addition 1–4 has an implementing clause. 𝒜_ε is consistently the image of 𝒜_Γ × 𝒜_T. "Frozen alone" and "STOP before Card 1" are in place. The gaps are in where addition 3 is imposed (the Π and T terms of G, the regime threshold, TG) and in Q9 blocking SCOPE-G.
2. **R1 integrity.** BLOCKER: the charter calls four classes "frozen tiers" where R1 froze two, and it leaves d_op undefined at E₂± and T_caus. MAJOR: DEF-4 states value-monotonicity in T, which R1 explicitly does not claim, and B-NULL/CT-14 say the join gives ε ≡ 0, although R1 makes no claim about the join. The ladder is not reopened, and the verdict table is unchanged.
3. **Cross-references.** All IDs and § numbers resolve syntactically. These are wrong or dangling: SC2 → §4.5 (should be §4.4); "Scope G … of Appendix A" (nothing there); "R1 §0"; "(DC-6)"; "card's C9"; "certified under MC-6"; Appendix D's references to v1 Appendices C and F and to CT-D02/CT-D05; the undefined symbols σ_tot, 𝒜_B^base, N_frozen, T_univ, J and 𝒮-checker.
4. **Consistency and freezability.** KU-11 matches §4.4. The batch leftovers are the IP-13 wording, MC-9/BU-7′ cross-card Bonferroni (which triggers LOCK-VOID under sequential evaluation) and the missing exclusion of earlier cards' unsealed holdouts. The AI-3 sample size is unfixed. No open owner decision blocks the freeze; everything else is a stated default.
5. **Candidate check: PASS.** There is no candidate law, sketch or example of 𝒦. Fix the 2 BLOCKERs (the freeze act against RULES 8, with the verification record still missing; R1 tiers and d_op) and the 14 MAJORs before freezing; the 31 MINORs can be fixed in the same edit.
