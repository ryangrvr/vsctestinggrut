# Pre-freeze audit C: self-tests, feasibility, disguised kills, adaptivity

**Audited:** `PROGRAM/STAGE3/STAGE3_CHARTER.md` (untracked, pre-freeze) in `/tmp/claude-0/mainwt`, branch `grut2-stage3`.
**Background read:** G2-11 (`OWNER_RULINGS.md`), `F0_SD0_COMPACTNESS_ACCOUNTING_01.md`, `F0_SD0_RESULT.md`, `GRAVEYARD.md`, `REDTEAM_C_accounting.md` §0, and `CHARTER_V1_WITH_LEDGER.md` (§4, §24.2, Appendix A).
**Mode:** read-only. Nothing in the repository was edited.
**Constraint kept:** no candidate law is proposed, sketched or exemplified. Sizes are abstract token counts. The self-tests use only the known objects the charter names.

**Severity scale.**
- **BLOCKER:** must be fixed before the freeze. Either it makes FZ-2's attestation false, or it is a disguised kill written in clear text, where no owner interpretation (CV-7) can repair it and §19.2 forbids loosening it once the first draft is logged.
- **MAJOR:** should be fixed before the freeze.
- **MINOR:** clarity fix.

Arithmetic for §2 is in `scratchpad/s3/vc/feas.py`.

---

## 0. Two cross-cutting defects found while tracing the self-tests

**X-1 (part of B5). No completion convention for self-test objects.**
- T-1 names the terminal by the first failing screen.
- S0 requires C1–C20 to be "present and non-empty".
- None of the known objects in §24.2 has those fields. ASP, for example, has no ℛ★, scope, lock register or C13.
- Read literally, every self-test therefore ends at S0 (CARD-INCOMPLETE). The screen-specific verdicts (ST-1 at S3, ST-3 at S1, ST-6 at S5) are never reached.

**X-2 (MINOR, needed for B5). No precedence inside a screen.**
- S3 lists RELOCATED, NONGENERATIVE and DEFINITIONAL. S5 lists ten labels.
- When several tests in one screen fail, the text does not say which label is the terminal.
- This leaves ST-1, ST-2 and ST-11 underdetermined.

---

## 1. Task 1: self-tests ST-1 to ST-11, clause by clause

In the table, **"terminal"** means the label T-1 assigns. **"Finding"** means a failure recorded in S0–S8, which T-1 says always run.

| ST | Required verdict | What the text yields | Mark |
|---|---|---|---|
| ST-1 BRI1 Tier-1 | S3 NONGENERATIVE; independently STANDARD | **S3:** NR-1 flags the S/E labels, readout, temperature and Gibbs state. §5.6 then gives two outcomes: "Π, [h] SUPPLIED, even when declared → CARD-NONGENERATIVE", and "Gibbs/FDT SUPPLIED and declared … if the derivation of ℛ★ uses it → CARD-RELOCATED". The Tier-1 value is a Kubo/FDT third-cumulant quantity, so ℛ★'s derivation does use the Gibbs state. Both labels fire inside S3 and nothing ranks them. Listing order would make the terminal **RELOCATED**, not NONGENERATIVE. **S5 findings:** Q3 fails (STD-3 nonlinear FDR; §13.6; B-SRB gives RESTATED); STD-9 covers the 1/N_B scaling. | **UNDERDETERMINED** (X-1, X-2). If it is read under listing order, the stated label is wrong. |
| ST-2 harmonic R1-NULL | STANDARD (STD-3, STD-6, FKM); RS-1 | **Terminal S3:** Π, readout and Gibbs/Gaussian state are supplied, and the Gibbs state is used. **S5 in Q order:** Q2 fails first through DEF-15 (Gaussian ⇒ ε = 0, which DEF-15 lists as an example), so the label is DEFINITIONAL. Q3 also fails: STD-3 says "Under RH-KMS, RH-GAU and linear coupling, 𝒜_ε = {0}" and puts "harmonic baths are R1-NULL" under no credit; STD-6 applies too. Q9 fails for scope Q (CT-28), and RS-1 applies. | **HOLDS as a finding.** No screen is named, and STANDARD is neither the terminal nor the first S5 label. |
| ST-3 ASP | S1 GRAVEYARD (GY-6); NON-SELECTIVE; B-CF collapse; UNMEASURABLE | **Literally:** S0 CARD-INCOMPLETE, because C7–C9 and C13 are empty and RS-5 applies (X-1). **With a completion convention:** S1 fires CARD-GRAVEYARD, because GY-6 holds by behavioural equivalence and the returning component carries the discriminator. The findings are all present: SEL-10 (theta) and SEL-4 (the 240 tables) are admitted, so the grade is NON-SELECTIVE and S8 fails; ASP is itself a B-CF member, so its Hamming distance is 0 and it collapses with D_sel = 0; DC-8 gives "no weight rule → UNMEASURABLE". DC-8, however, is a DC rule tested in S2, whose terminal is UNDECIDABLE, so the label belongs to the wrong screen (MINOR m-2). | **FAILS literally** (S0). **HOLDS** with X-1 fixed. |
| ST-4 NULL-ΠT | Credited = 0 ⇒ LOOKUP → RELOCATED; also NONGENERATIVE | **Terminal S3 NONGENERATIVE:** Π, Z, [h] and T are all supplied by hand. **S6:** Im = FB, so any ℛ★ that holds on Im has Z(ℛ★) ⊇ 𝓗; c_J(a) = 0 and MC-4 fails, so b_J = 0. G = 0 because nothing is GENERATED and SC1 fails. D_sel = 0: the SEL verdicts come from quantum theory, which IP-6 treats as matching VB-5/7 (selectivity RELOCATED) and which also reproduces them under 𝒦_𝒮 (STD-2 under RH-Q). So Credited = 0 and ΔL = −Price ≤ 0, which is LOOKUP. This holds even if Price = 0, because the test is ≤ 0. | **HOLDS** (needs only X-1). |
| ST-5 product-latent E-B | NR-11 MODE SELECTION; STD-12 no credit | The readouts h_a = π_a are indexed by protocol, so NR-10(a) fails and the readout counts as supplied (PS-3). **Terminal: S3 NONGENERATIVE.** NR-11 gives MODE SELECTION (kit control HB-9), and STD-12 gives no credit. | **HOLDS as findings.** The terminal is not named. |
| ST-6 detailed-balance model with Π from SPS | **S5: CARD-STANDARD** (RH-DB, NR-12(b)); G's Π term = 0 | Listed after the table: five clauses, each read against the card under CV-1, stop the object before S5. | **FAILS** |
| ST-7 k-parameter standard class | c_J = 0 by §2.5(b); NON-COMPRESSIVE | **Terminal S3:** the standard rule for Π reads 𝒞, so the NR-6 SPS template recovers Π and the card is RELOCATED; a T picked by a selector is NONGENERATIVE (CT-13). **S6:** if c_J = 0, then b_J = 0, G = 0 and D_sel ≤ 10 bits, which is below Price. So ΔL ≤ 0, and that is **LOOKUP, not NON-COMPRESSIVE**. **c_J = 0 by §2.5(b) is itself undetermined.** §2.5(b) applies only to classes with Price(M) ≤ Price(𝒦), and the charter never prices the "Π and T chosen by hand" part of M. If a hand choice costs log₂\|𝒜_Π\| per instance (about 48 × 8 bits), M is more expensive than the card's uniform rule, so (b) does not bind. c_J then falls back to (a), which can be ≥ 1 for a relation specific to the class. The class would still fail at S5 through Q3(c) transplant (CARD-STANDARD). | **FAILS** (label wrong; c_J(b) undetermined; MAJOR M5) |
| ST-8 order-2 Volterra on HB-2 | STANDARD (STD-14) | **Terminal S3 NONGENERATIVE** (HB-2's Π, readout and Gibbs state are supplied). Q3 fails: at small α, RH-AN holds with m = 2, and STD-14 makes "the leading amplitude power … the ratios across a₊, a₋, a₊₊ that this power and symmetry fix" standard. MC-4's last sentence applies as well. One wording caveat: at r★★, \|A\| − 1 = 3, so the "order-(\|A\|−1) truncation" clause alone does not imply an order-2 predictor; the hold rests on the leading-power clause (MINOR m-4). | **HOLDS as a finding.** |
| ST-9 BKN cascade on P-2 | STANDARD (STD-7) | **Terminal S3 NONGENERATIVE.** Q3 fails because STD-7 lists FCS and environmental-feedback corrections, and SFP-5 lists BKN. | **HOLDS as a finding.** |
| ST-10 feasibility | SC1–SC3 reachable at c_J = 1; a tabulated card fails SC2 | See §2. The note checks only SC2, omits mandatory priced items, and under hostile readings of IP-6, IP-13, IP-4/14 and IP-12 no card can reach SC2. SC1 is blocked by B1. SC3 is not examined. | **FAILS** |
| ST-11 padding (DEF ∧ Γ-only) | NONJOINT or DEFINITIONAL | **If the Γ-only restriction G is imposed by a target-level clause:** S3 CARD-RELOCATED under NR-2 ("ℛ★ is … a conjunct, or a consequence of the [target-level] clauses"), which is outside the allowed set. **If G is forced by Ξ-level clauses:** in S5, Q2(a) fails through DEF-15 (P = G is single-axis and G ⇒ D ∧ G by DEF), giving DEFINITIONAL. Q3 also fails, because witnesses violate only the single-axis consequence, which Q3(a) excludes, so the constructive rule gives STANDARD. Q5 fails as well: R ⊆ Z(G), so 𝓗 ⊆ Z(ℛ) and c_J = 0. Without a precedence rule, STANDARD could be named as the terminal. | **UNDERDETERMINED** (X-2 plus the construction is not pinned) |

### ST-6: why the object never reaches S5 under the text

Each step below is read against the card, as CV-1 requires.
1. **S3, PS-5 in the inputs.**
   - A textbook detailed-balance model carries its detailed balance in rates, an energy and a temperature, or a reversible kernel. These are inputs (𝒞 or 𝒳) "from which a standard theorem derives … detailed balance" (§5.1 PS-5). That holds even through Kolmogorov's criterion, if the acyclic state structure sits in 𝒳.
   - Declared: §5.6 says "if the derivation of ℛ★ uses it → CARD-RELOCATED".
   - Hidden: NR-12(b) says "A hidden premise → RELOCATED".
   - If detailed balance is instead imposed by a clause of 𝒦, NR-1 (whose scope includes 𝒦) flags any symbol that "names or encodes" PS-5, and that clause is then SUPPLIED with the same consequence.
   - S5 is reached only if detailed balance arises implicitly from structure that 𝒦 generates.
2. **S3, NR-6.**
   - NR-6 says "The RB and SPS templates (§5.4) always run", and §5.4 defines SPS "on any graph or weight structure in 𝒞 **or in the realized dynamics**".
   - In this object Π *is* an SPS output on the realized dynamics, so the template recovers it exactly. The decoder fires and Π is RELOCATED, giving CARD-RELOCATED.
   - This contradicts B-DIF(viii), which calls the same case "STANDARD-MECHANISM (allowed)", and NR-6's own sentence that decoders "may not invoke 𝒦's … evolution step". CV-1 resolves the conflict against the card.
3. **S3, NR-5.**
   - On a symmetric input, a finite irreducible chain has a unique, Aut-invariant stationary solution.
   - A covariant X_Π (PC-3) cannot return a nontrivial partition on vertex-transitive V for an Aut-invariant Ξ. So NR-5 fails and the card is CARD-NONGENERATIVE, unless Sol is a symmetry-broken orbit. The ST row does not say it is.
4. **S4, the b_Π size test.**
   - The ST row itself asserts "𝒜_Π reduced by SPS". §2.3 shrinks 𝒜_Π to the SPS outputs ("the smaller set governs"), and §1.3 requires log₂\|𝒜_Π(ι)\| ≥ b_Π = 6 bits on lock fibers.
   - A Π-term of 0 means \|𝒜_Π/Aut\| = 1, which is below 64. S4 fires **CARD-UNDIFFERENTIATED** before S5.
5. **S1, GY-10.**
   - "A selector card says so and is audited against GY-10's screen", but GY-10 has no frozen test domain in §21.2. A hostile reading can therefore fire CARD-GRAVEYARD on a "standard selector" (MINOR m-3).
6. **"G's Π term = 0".**
   - The formula min(16, log₂\|𝒜_Π/Aut\|) on 𝒜_Π = {⊥} ∪ SPS outputs gives at least 1 bit for a GENERATED Π.
   - G is 0 here only because SC1 fails, not for the reason the row gives.
7. **The S5 finding itself holds** once reached. RH-DB holds (Kolmogorov's criterion), so STD-3 and STD-4(a) impose the FDT and Onsager-regression relation. Q3(e) makes it STANDARD-IMPLIED; NR-12(b)/(c) apply.

**Conclusion.** The verdict is right in spirit, since the object fails. It fails at the wrong screen, and item 4 exposes the real defect, B1.

---

## 2. Task 2: feasibility (ST-10) re-derived under §4.1–§4.3

### 2.1 Appendix A's arithmetic is correct for its own inputs
- Price: 216 + 96 + 264 + 24 + 30 + 10 = 640.
- Credit at c_J = 1: 48 × (10 + 6 + 2.32 + 1) = 927, so ΔL ≈ +287.
- The standard-selector variant: 48 × 13.32 = 639.4, so ΔL ≈ −0.6. That is **LOOKUP** (ΔL ≤ 0), not merely "fails".
- The inputs, however, leave out items §4.1–§4.2 make mandatory.

### 2.2 The honest compact card, itemized under the actual rules

Benign readings, with the fixes proposed below applied.

| Item (rule) | Note | Re-derived | Why |
|---|---|---|---|
| Law clauses (IP-1) | 216 | 216 | Same |
| 𝒳 declaration + 𝒞 and its FR11 meaning (IP-1, IP-2) | 96 | ≈ 104 | Variable-index bits ⌈log₂(v+1)⌉ per occurrence were omitted |
| Ontology (IP-14) | in "10" | 0–30 if charged as max(decl, log₂ m); **+50–100 as written** ("in addition to IP-1") | As written, IP-14 double-charges |
| Six components (IP-2, IP-8) | 264 | ≈ 300 at the note's 44 tokens; **≈ 300–600 at 45–90 tokens** | Variable bits. IP-8 unfolds every named primitive. Emb alone must carry both the abstract-signature map and the template-to-Ξ map, and X_T must construct its group rather than select it (CT-13) |
| θ_dict (IP-2) | 24 | ≈ 45–90 | It maps 𝒞 to β, frequencies and couplings for every B-HB family, and its numeric content is priced under IP-5 |
| Two law constants (IP-5) | 30 | 24–38 | A real literal at p = 10 costs 12–19 bits; tuning over [10⁻³, 10³] costs 8–14 bits |
| Thresholds, scales, truncation, enumeration bounds (IP-2, DC-1) | 0 | ≈ 15–40 | Any X_Π scale or threshold is a priced constant |
| Vocabulary (IP-6) | **0** | **≈ 60–300** | L_stmt(def_v) for each item used: VB-9 (time and unit, unless earned); VB-13 (measures on Ξ, unless generated); VB-8 if real-valued records are used. The note omits IP-6 entirely |
| Selection tax (IP-12) | in "10" | 3–10 | 10–1000 drafts |
| Domain (IP-13) | 0 | 0–26 | With the N_dom fix (B3); see below for the text as written |
| **Total** | **640** | **≈ 830–1450** | |

### 2.3 Credit side, as written and as fixed

| | c_J = 1 | c_J = 2 | c_J = 3 |
|---|---|---|---|
| As written (Π term 6, T and carrier ×48) | 927 | 1407 | 1887 |
| With M4 (T and carrier counted once) | 771 | 1251 | 1731 |
| If AI-1 has \|V\| = 3 (Π term 2.58; M3 not fixed) | 763 | 1243 | 1723 |

**ΔL against 830–1450 bits:**
- **c_J = 1:** from +97 down to −523 as written; from −59 down to −679 with M4. Not reliably reachable. It is reachable only if the whole card fits in about 130 tokens (about 110 with M4), counting components, VB definitions and constants.
- **c_J = 2:** from +577 down to −43 as written; from +421 down to −199 with M4. Reachable over most of the range.
- **c_J = 3:** always reachable.

### 2.4 Verdict on the stated conclusion

- **"Reachable by an honest compact card at c_J = 1"** is **not established**. It holds only if every component and vocabulary definition stays at the note's optimistic size.
- **"Not reachable by a heavily tuned card"** holds only at c_J = 1.
  - At c_J = 2 or 3 the margin absorbs 25–50 tuned constants, at 12–20 bits each.
  - What is actually true: a tuned constant never pays for itself, because it costs at least 12 bits at p = 10 and can buy at most one 10-bit instance-codimension. It cannot create credit either, because Q1 is decided on 47 post-freeze draws.
  - A tabulated card fails Q1 (UNFORCED) before it reaches SC2.
- **SC1 and SC3** are not examined by the note. SC1 is in fact blocked by B1.
- ST-10 claims "SC1–SC3 jointly reachable". **FAILS.**

### 2.5 Hostile readings that push the honest price out of reach (disguised kills)

- **B2: IP-6 ΔF_tgt.** It is defined as "the credit lost when v is replaced by an uninterpreted symbol … with its axioms deleted".
  - For any item without which the chain is undefined, that loss is the whole credit. This covers time or unit (VB-9, unless earned), kernels on Ξ (VB-13 through the §4.1 typing rule), `pair` or `×` applied to relata (§4.1: "priced vocabulary"), a generator's locality graph (VB-12, by the closure rule) and truncation levels (VB-10).
  - Then P_v ≥ Credited for every card that uses even one such item, so ΔL < 0 and the card is LOOKUP.
  - §21.1 explicitly offers FR7 as "Time primitive and priced (VB-9)". That option is fictitious under this rule.
  - The text is clear, so no interpretation can repair it.
- **B3: IP-13.** It charges log₂ C(N, k) where "N is the size of the AI-3 batch", and that size is frozen nowhere, against CV-6.
  - Approximately log₂ C(N, fN) ≈ N·H(f). With a 10 % exclusion: N = 47 costs 17 bits, N = 1000 costs 464, N = 10⁴ costs about 4700.
  - The Evaluator controls a price that grows linearly with N. Any card whose domain predicate excludes anything can be killed. Excluding degenerate random inputs is natural under DIF-7's 0.9 coverage.
- **M1: IP-4 and IP-14.** m is "the largest finite family any auditor exhibits".
  - No length bound applies, so a family of all L₀ items up to 10× the length gives log₂ m ≈ 10 × L_stmt.
  - IP-14 adds its charge "in addition to IP-1", which double-counts the declaration.
  - The owner can bound this by an interpretation (CV-7), so it is MAJOR rather than BLOCKER.
- **M2: IP-12.** "A template counts the size of its instance space."
  - For a real constant that space is a continuum, so the tax is infinite under CV-1.
  - Even discretized at p = 10 over the default range, it re-charges the roughly 14 bits per constant that IP-5 already charges.
- **IP-5's "largest natural range any auditor exhibits"** grows only log-log: [10⁻³⁰⁰, 10³⁰⁰] costs about +4 bits. Not a kill (MINOR m-11).

### 2.6 Places where the bar is too lax

- **M4.** G multiplies the T term (log₂ 5) and the carrier term (1 bit) by N_cred = 48. A baseline modeller picks T and the carrier once, by a uniform hand rule. That is about 156 bits of over-credit, 17 % of the note's credit.
- **M5.** §2.5(b) never prices M's hand-chosen Π and T. Priced per instance, M almost always costs more than the card, so the NULL-M check (b) loses its force.
- **m-9.** The Π term per instance ignores decodability on that instance. Because NR-6 fires only at p_dec = 0.5, a Π that can be decoded from inputs on 49 % of draws still earns G on those draws.
- **m-10.** Pipeline-driven relations that hold on fewer than p_dec = 50 % of Dom_gate escape both NR-4 and DEF-12, which demands "every". The ablation threshold for ℛ★ should match Q3(c)'s 1/Q_min.
- **m-8.** D_sel (up to 10 bits) can supply the whole ΔL ≥ p★ margin (the earlier red-team pattern RT-24). Harmless at the 48× scale, but worth stating.

---

## 3. Task 3: disguised kills and over-lax requirements

### Impossible by construction (as written)

- **B1: §2.3 shrinks 𝒜_Π by SPS and feeds the result into FB, b_Π, SC1, Q3 and Q5.**
  - When 𝒞 has any standard dynamical reading (which the Intake auditor decides, under CV-1), 𝒜_Π becomes the SPS output set.
  - **Case 1: the card's Π is not an SPS output.** No FB point carries the card's Π. Then 𝓗 = FB ∩ (cl U × cl R) = ∅. Q3(a) needs Obs(m*) ∈ 𝓗 ∖ Z, which is impossible, so the constructive rule gives **CARD-STANDARD**. c_J is undefined, so Q5 fails. The SC1 condition "FB ∖ Z meets the region where the card's Π is realized" also fails.
  - **Case 2: the card's Π is an SPS output.** \|𝒜_Π\| is the number of SPS outputs, which is usually below 64, so S4 fires CARD-UNDIFFERENTIATED. This contradicts B-DIF(viii) ("STANDARD-MECHANISM, allowed").
  - **Either way, every card whose 𝒞 has a standard reading fails.**
  - **Cause.** Two red-team fixes were merged into one definition: RT-S-07 meant the SPS reduction to touch credit only ("A STANDARD-MECHANISM verdict sets ΔF_Π := 0"), and RT-L's RT-3 meant b_Π to be an ontology-size test.
- **B2: IP-6 ΔF_tgt** (§2.5 above).
- **B3: IP-13's unfrozen N** (§2.5 above).

### Hard but possible

- **B-SEL with the reciprocity certificates.**
  - SD0 shows that a rule built on arc consistency meets every item except SEL-10.
  - SEL-10 (theta FORBID) and SEL-6 (Peres–Mermin ALLOW) are both GF(2)-inconsistent systems. Separating them needs content equivalent, on these instances, to operator solvability. It must avoid matching VB-5/6/7 and avoid any clause on dimension (SEL-11).
  - Nothing makes this impossible.
  - **Two conditional traps:**
    - **M8.** G-SEL fails on Hamming distance ≤ 1 to *any* B-CF vector, including pairwise combinations. (j,4)-consistency decides any instance with at most 4 variables exactly, and theta has exactly 4 variables. The larger quantum anchors (GHZ with 6 variables, Peres–Mermin with 9, the KS core) are probably invisible to width 4. So a B-CF vector may sit within distance 1 of the all-correct vector. If it does, **every EXACT card fails S8 by construction**, and an OUTER card survives only by being wrong on at least 2 graded items. The kit computes these vectors after the freeze, and the charter has no reachability check.
    - **m-6.** The VB-5 closure ("satisfies an item's frozen axiom checklist on any … battery instance") could treat a card whose support verdicts on (2,2,2) coincide with the quantum-realizable supports as "matching VB-5". That would make correctness itself RELOCATED. Avoidable, but perverse.
  - **SEL-11 against DC-4 (m-5).** If FORBID decidability needs a truncation level, ablating it changes the verdict to UNDECIDED. The truncation clause then sits in the responsibility map. VB-10 calls truncation "dimension-like", so a hostile reading fails SEL-11.
- **Q3's two applicable frameworks with witnesses (M6).**
  - BP-6 makes a framework applicable unless the card disproves one of its hypotheses, so the floor of two is easy.
  - The demand is "for each applicable framework F, a … witness … built in F". Many SFP entries define no model class: Kramers–Kronig and sum rules, Stevens scale types, measurement invariance, constructor theory. "Built in F" is undefined, and read against the card it makes Q3 unsatisfiable.
  - Under the reading "a witness satisfying F's hypotheses; one witness may serve several frameworks", it is hard but possible.
  - The single-model rule pushes cards toward declaring few interface statistics, since every declared statistic must be reproduced by the witness's own dynamics.
- **Dimension certificates on 48 instances within R_card.**
  - Feasible only with uniform, theorem-grade dim_ub.
  - Exact rank at post-freeze points on \|V\| = 16 at r★★ (k = 4, m ≤ 5, d_rec = 2) is plausible within 48 core-hours per item for small parametrizations.
  - dim_lb needs a B-HB witness family matching u_ι on every one of the 48 instances, each one refereed by the skeptic (§15.4). T_audit = 60 days is the binding constraint.
  - Total items: about 48 credit instances + about 20 B-SEL items × 3 truncation levels + B-REC + lock fibers + AI-2 ≈ 150–200, which averages 25–33 core-hours each. Tight but possible.
- **MC-7 with N_max = 10⁹.**
  - A 4th-order whitened witness has σ_stat ≈ √(24/N), which is 1.5 × 10⁻⁴ at 10⁹. With Bonferroni over up to 9 card-observables (z ≈ 3.5) and power 0.9, the detectable witness is ≳ 7–10 × 10⁻⁴ before autocorrelation.
  - Feasible for ε-witnesses ≳ 10⁻³. The 30-day limit binds below about 1 kHz effective rate.
  - Edge case (m-14): a live rival at exactly 3σ_pre gives power below 0.9 at any N.
- **DISTINCTIVE (P) (M7).**
  - OR-6 says "an analyst and a skeptic instructed to argue RESTATED; the more conservative verdict governs". Without CV-3 written into the clause, the skeptic always wins.
  - "Within T_audit … or the card is CARD-RESTATED" turns an auditor-side stall into a card kill. The SD0 precedent is real: the comparator audit was stopped with 1 of 5 agents returned.
  - Hard but possible once both are fixed.
- **Q9 with scope Q.**
  - Satisfiable. Exogenous or Gaussian standard models supply FB points with ε = 0; ε > r_lock needs RH-GAU to fail by at least 3·r_lock.
  - In practice, §13.6 combined with MC-11 forces scope-Q locks onto platforms where RH-KMS is certified to fail, because in KMS fibers J_SRB pins ε through the reference correlators.
  - Hard but possible.
- **T_Π generation against NR-10(f) (M9).**
  - "T_Π ≠ Aut(R) for any record structure R the inputs supply." Obs is an input component, and its ℚ^k codomain carries affine and order structure.
  - Read against the card, every frozen-tier T_Π (T_lin = Aut(affine), T_mono = Aut(order)) is SUPPLIED, giving NONGENERATIVE. This contradicts §1.4: "If T_Π equals T_R1 or T_mono, that is a result to be proved".

### Too loose or trivially met
- Q4: a W-pipe needs only one non-solution. It is backstopped by NR-4, but at a 50 % threshold (m-10).
- NR-16: a binomial test on 3 holdouts is near-vacuous. It is backstopped by "a failure on an item of mandatory type fails the gate".
- Q10 and Q12 are pure bookkeeping, as intended.
- The p = 16 test is implied by the p = 10 test whenever the card has fewer than about 48·c_J real literals, because b_J grows by 6 bits × 48 × c_J while each literal grows by 6 bits.
- None of these is harmful.

---

## 4. Task 4: adaptivity under sequential evaluation (BU-6, §18.1)

What an author of Card j+1 learns from Card j's report, given that T-1 runs and reports S0–S8:
- the holdouts actually drawn (SEL-H and reciprocity) and their outcomes;
- the decoders, witnesses and comparator arguments that were tried;
- the auditor-exhibited family sizes;
- the Evaluator's J_SRB;
- the eligibility of LOCK-H pools.

**A1 (MAJOR). Finite holdout pools are not depleted.**
- §15.9 pools (a) (literature support cases) and (b) (standard environments with exactly computable ε_R) exclude only the §15.1 items, G1–G3, H1–H4 and (2,2,2).
- Items unsealed for an earlier card are **not** excluded from later pools, so:
  - (i) a later card can be tuned to the revealed holdouts;
  - (ii) a fresh draw can return an item the author has already seen.
- A deliberately incomplete Card 1 still triggers Selection (§18.1 step 3 precedes intake) and holdout evaluation. That is sacrificial probing, at the price of one slot.

**A2 (MAJOR). Selector freshness.**
- §0.2 requires "a selector that has not seen the mechanism". §23 says only "Selector: sees card signatures only".
- A Selector context reused across cards has seen Card j's mechanism and report.

**A3 (MINOR). Evasion of known auditor tools.**
- NR-6 passes are "NOT FOUND within the hostile window". A later author who sees which decoders, witness families and comparator arguments were tried can design around exactly those.
- The fix is cumulative re-runs, not secrecy.

**A4 (MINOR). Pick after unsealing.**
- BU-7 lets the owner take "another frozen ADMISSIBLE card" after the first pick fails at Stage 5, that is, after lock data have been unsealed.
- The second pick can be informed by the first card's outcome.
- Commit the pick order by hash before the first G5-LOCK unsealing.

**A5 (MINOR). Retroactive CI-n.**
- CV-7: interpretations "apply to every card". A dispute raised on Card 2 can produce a card-favourable reading that rescores Card 1 upward.
- A card-favourable CI-n should apply only prospectively; retroactive application should move only toward failure.

**A6 (MINOR). Pool shortfall.**
- With exclusion, three cards need at least 9 items per Stage-3 pool. A shortfall is not specified, and CV-1 would score it against the card.

**A7 (MINOR). §19.4 wording.**
- "Authors never see … intake results before the card is frozen" conflicts with BU-6's "may learn from earlier verdicts".
- It should say "of that card".

---

## 5. Findings with replacement wording

### BLOCKERS

**B1. §2.3, §1.3, §4.3(b), NR-6, B-DIF(viii): standard selectors may reduce credit but never the baseline space.**

*§2.3, first bullet.* Replace "If the Intake auditor confirms … and the smaller set governs." with:
> "With Π supplied by hand, this set contains every partition with S ≠ ∅ ≠ E (2^|V| − 2 with one S; ordered set partitions with a designated E for multi-block embeddings), modulo Aut(𝒞_ι). 𝒜_Π is never reduced by standard selectors; FB, the b_Π size test (§1.3), ℓ_dec (NR-6) and §2.5 use it as defined here. **Standard-selector set:** SPS(ι) := the partitions returned by the SPS templates (§5.4) and the STD-10 criteria applied to 𝒞_ι and to the realized dynamics of Sol on ι. Π is **STANDARD-MECHANISM on ι** if VI_norm(Π, Π′) ≤ δ_Π for some Π′ ∈ SPS(ι). This sets Π's §4.3(b) term on ι to 0 and is reported under B-DIF(viii). It is not a relocation."

*§4.3(b), first bullet:*
> "min(16, log₂|𝒜_Π(ι)/Aut(𝒞_ι)|) if Π is GENERATED (§5.5) and not STANDARD-MECHANISM on ι (§2.3), else 0."

*NR-6.* After "always run, whatever their cost" add:
> "; as decoders they read only the inventory. An SPS template applied to the realized dynamics of Sol is not a decoder; a match is STANDARD-MECHANISM (§2.3), never RELOCATED."

*B-DIF(viii).* Replace "𝒜_Π reflects it" with:
> "its §4.3(b) term on that instance is 0".

**B2. IP-6 and §4.1: ΔF_tgt measures target content, not whether the chain survives deleting the item.**

*IP-6, first sentence:*
> "Each item VB-1 to VB-16 used costs P_v := max(L_stmt(def_v), ΔF_tgt(v)). ΔF_tgt(v) is the credit lost when the card's instance of v is replaced by an independent draw, from the charter reference measure, of an instance with the same signature that satisfies v's frozen axiom checklist (two post-freeze seeds; the larger loss governs). For VB-8, VB-9 and VB-10 the replacement ranges only over the declared representation moves (change of unit and origin; refinement of precision; truncation levels n, n+1, 2n). Deleting v or its axioms is not a test of target content."

*§4.1, typing of base tokens:*
> "`pair`, `×` and `⊗` applied to V_Ξ or relata are base tokens when they form tuples or relations; splitting V_Ξ or 𝒳 into blocks is VB-4. `kernel`, `cond-prob`, `E`, `law`, `marginal` and `support` applied to Ξ, 𝒞 or relata are VB-13 when they supply a prior, weight or reference measure that 𝒦 does not generate. 𝒦's own transition rule is priced as law clauses (IP-1), its numbers under IP-5, and its PS-5 content under NR-1 and NR-12. The charter reference measure used unchanged is not VB-13."

**B3. IP-13 and Appendix A: freeze the batch size.**

*IP-13:*
> "max(L_stmt(predicate), log₂ C(N_dom, k)), where N_dom [A] AI-3 instances are drawn by the Selector with a committed seed after the card's freeze and k is the number the predicate excludes. DIF-7's coverage θ_gen is assessed on the same N_dom draws."

*Appendix A, new row:*
> "N_dom (IP-13, DIF-7) | 64"

This bounds IP-13 at about 26 bits when k ≤ 6.

**B4. Appendix A feasibility note and ST-10: the stated conclusion is not established.**
- The note omits IP-6 vocabulary definitions, variable-index bits, θ_dict's constants, priced thresholds and IP-14.
- On the corrected estimate an honest compact card costs about 830–1450 bits, against 771–927 bits of credit at c_J = 1.
- Replace the note's last four bullets with:

> "**Corrected estimate.** Pricing every mandatory item (IP-6 definitions of the vocabulary used, variable-index bits, θ_dict's constants, priced thresholds, IP-14 as max(declaration, log₂ m)), a compact card costs about 830–1450 bits. Credit at c_J = 1 is about 770–930 bits, at c_J = 2 about 1250–1400, at c_J = 3 about 1730–1890. **The bar is reachable at c_J = 2 for a compact card; at c_J = 1 only if the whole card, components and vocabulary definitions included, fits in about 110–130 tokens.** A tuned constant costs at least 12 bits at p = 10 and buys at most one 10-bit instance-codimension, so tuning never pays. A tabulated card fails Q1 on the 47 post-freeze draws before SC2. This note checks SC2 only."

*ST-10 required verdict:*
> "SC2 reachable for a compact card at c_J = 2 under IP-4, IP-6, IP-12, IP-13 and IP-14 as frozen; a tuned card never recovers its tuning price; a tabulated card fails Q1."

*Owner decision before the first draft:* accept c_J ≥ 2 as the effective bar, or rescale N_cred.

**B5. FZ-2 and §24.2: the attestation is false as drafted.**
- ST-6, ST-7 and ST-10 fail.
- ST-1, ST-2, ST-3 and ST-11 are undetermined.
- `charter_workings/FREEZE_VERIFICATION.md` does not exist.
- Apply B1–B4 and the following, write the verification record, and only then commit the freeze.

*§24.2 preamble, new:*
> "**Self-test convention.** Each known object is completed into a card with the most favourable well-formed content for every field it lacks (KP-1 to KP-5 met; the scope, lock register, platform and transfer plan the object best supports), so S0 passes by construction. A required verdict that names a screen is the terminal under T-1. One that names no screen must appear among the recorded S0–S8 failures."

*T-1, add (also fixes X-2):*
> "Within a screen, the terminal is the first entry of that screen's §18.2 list whose test fails; for S5 the order is Q1 to Q12. Every other failure is recorded."

*Replacement rows:*
- **ST-1** → "S3: CARD-RELOCATED (Gibbs state declared and used in ℛ★'s derivation, §5.6); NONGENERATIVE recorded (Π, [h] supplied). S5 findings: STANDARD (STD-3 nonlinear FDR; B-SRB RESTATED, §13.6); STD-9."
- **ST-2** → "Terminal S3 (CARD-RELOCATED). S5 findings: DEFINITIONAL (DEF-15), STANDARD (STD-3, STD-6, Ford–Kac–Mazur), VACUOUS for scope Q (Q9). RS-1 applies."
- **ST-6** → "Construction: detailed balance arises only through Kolmogorov's criterion on state structure that 𝒦 generates; no PS-5 content in 𝒞, 𝒳, priors or Emb, and no clause flagged by NR-1; on the symmetric input Sol is a symmetry-broken orbit (NR-5); the SPS template is not a GY-10 selector. Required: S5 CARD-STANDARD (RH-DB; STD-3, STD-4(a); NR-12(b)); Π STANDARD-MECHANISM, Π term 0. **ST-6′:** the same model with detailed balance carried by 𝒞 → S3 CARD-RELOCATED (§5.6)."
- **ST-7** → "Terminal S3 (CARD-RELOCATED by an NR-6 SPS template on 𝒞, or NONGENERATIVE by CT-13). S6: c_J = 0 by §2.5(b), M = the class with its uniform rule; Credited = 0, so LOOKUP. S5: CARD-STANDARD (Q3(c))."
- **ST-11** → "Γ-restriction forced by Ξ-level clauses: S5 CARD-DEFINITIONAL (Q2(a) via DEF-15); Q5 also fails (c_J = 0 on the product hull). Imposed by a target-level clause: S3 CARD-RELOCATED (NR-2)."

### MAJOR

**M1. IP-4 and IP-14.**

*IP-4, second sentence:*
> "…m is the size of the largest finite family that any auditor exhibits in the same role (by citation or by an L₀ generator), counting only members whose full L₀ unfolding (IP-8) is no longer than the selected item's. The item costs max(L_stmt, log₂ m)."

*IP-14:*
> "…is a selection (IP-4) from the family of types any auditor exhibits. It is charged as max(L_stmt of the declaration of 𝒳, log₂ m), replacing the declaration term of IP-1, not added to it."

**M2. IP-12.** Replace "A template counts the size of its instance space" with:
> "A template counts the number of its instances for which an output was computed. Symbolic evaluation in a free constant that is then priced under IP-5 counts as one draft, since its tuning is charged once, under IP-5. Self-test objects and kit rejection tests are not drafts."

**M3. AI-1 and the Π-term floor.**
- The note's "6-bit floor" is enforced nowhere, because b_Π binds only on lock fibers.

*§1.5 table, AI-1 row:*
> "The smallest instance meeting every §1.3 nontriviality condition, the b_Π size test included, computed exactly."

*§1.3:*
> "log₂|𝒜_Π(ι)/Aut(𝒞_ι)| ≥ b_Π [A] on AI-1 and on the lock fibers."

**M4. §4.3(b): G is too lax.**
> "G := N_cred · min over ι ∈ I_𝒦 of g_Π(ι) + g_T + g_C, where g_Π(ι) is the Π term; g_T := log₂|𝒯 ∪ {⊥}| if [h] and T_Π are GENERATED, counted once per card if the realized class is the same on every ι ∈ I_𝒦 and N_cred times otherwise; g_C := 1 bit, counted once, if carrier PASS is GENERATED."

Update Appendix A "G caps" to match.

**M5. §2.5(b): price M's hand choices.**
> "(b) for every standard model class M realizing Im, with constants fitted and Π, [h] and T supplied by a uniform rule (an SPS or RB template or any L₀ rule, priced as a component under §4.2) or, failing one, by hand at log₂|𝒜_X(ι)| bits per instance, with Price(M) ≤ Price(𝒦): …"

**M6. Q3(a): define "built in F".**
> "For each applicable framework F, a regime-matched witness m*_F ∈ 𝔐_std that satisfies every hypothesis of F at x (so every consequence F imposes at x holds for it), with Obs(m*_F) ∈ 𝓗 ∖ Z(ℛ★), violating ℛ★ by at least 3·r_lock. One witness may serve several frameworks. A framework that defines no model class (a constraint scheme, scale-type or invariance framework) is met by any witness consistent with it."

**M7. OR-6.**
> "…the more conservative of the verdicts that meet CV-3 governs; a RESTATED, KNOWN ASSEMBLY or NO NEW RELATION verdict exhibits the derivation, or the primary-source result, that imposes ℛ★. … Incompleteness at T_audit caused by the author side → CARD-RESTATED; caused by the auditor side → one disclosed re-run of the missing families by fresh panels (as for holdouts, §15.9)."

**M8. §15.1 G-SEL and §19.3.**

*G-SEL PASS:*
> "…at least OUTER, SEL-11 passed, every SEL-H holdout passed, and the card's FORBID verdicts are not bounded-width refutations of width ≤ 4 (responsibility map). Hamming distance ≤ 1 to a B-CF vector sets D_sel = 0 and makes the SFP-10 comparators mandatory; it does not by itself fail G-SEL."

*§19.3 validation list, add:*
> "the Hamming distance from every B-CF vector to the all-correct vector and to the nearest OUTER vector".

Alternative if the owner prefers to keep the Hamming criterion: keep it, but have a CR before Card 1 drop it if any B-CF vector lies within distance 1 of the all-correct vector.

**M9. NR-10(f).**
> "(f) no input names a record-space group action or a readout class; T_Π ≠ Aut(R) for any record structure R that the inputs name or encode beyond the L₀ arithmetic of Obs's codomain (a designated group, metric, order, partition or calibration map); the kit verifies T_Π's generators on the chart. A T_Π equal to a frozen tier is GENERATED when X_T computes it under PC-6 and NR-10 is otherwise clean (§1.4)."

**A1 + A2. BU-6, §15.9, §23.**

*BU-6, last sentence:*
> "…and the rule that sealed items (AI-3 seeds, credit-family draws, holdouts, lock datasets) are drawn after each card's freeze, by a Selector context that has seen no card's statement, evaluation or report, from pools from which every item unsealed or evaluated for an earlier card has been removed. Such items join the public battery for later cards: a later card's verdict on them is a consistency check (KP-3), never holdout evidence. Every decoder, witness family and comparator argument used on an earlier card is re-run on every later card. A pool that cannot supply the required number of fresh items is an auditor-side void (§15.9)."

*§23:*
> "**Selector:** a fresh context per card; sees that card's signature only."

### MINOR (wording only)

- **m-1.** Intra-screen precedence. Included in B5.
- **m-2.** DC-8's "→ CARD-UNMEASURABLE" sits in S2. Either add it to S2's terminal list or move its test to S7.
- **m-3.** GY-10 has no test domain. Add: "SPS-type partition selection is not a GY-10 selector."
- **m-4.** STD-14 should read: "order-m truncation, m the smallest order at which RH-AN's surrogate holds (at most |A| − 1)".
- **m-5.** SEL-11 should add: "A truncation level whose FORBID verdicts are invariant at n, n+1 and 2n (DC-4) is not a clause on dimension."
- **m-6.** VB-5/6/7 matching should be decided on the axiom checklist, never by extensional agreement of support verdicts. Also, q = 3 tertiles are ill-defined for binary-outcome B-SEL scenarios: say that Emb's outcome alphabet governs there.
- **m-7.** Q5's "one fixed frozen class" should read "one fixed class (a frozen tier, or T_Π when T_Π is the same at all compared points)".
- **m-8.** Appendix A's "not reachable by tuning" should be replaced with the B4 wording.
- **m-9.** In the Π term, set g_Π(ι) = 0 on any credit instance where a decoder recovers Π within δ_Π.
- **m-10.** NR-4 for ℛ★: "appears" should mean "holds within r_lock on a fraction ≥ 1/Q_min of Dom_gate".
- **m-11.** IP-5: delete "natural", or bound the range at the default ± 3 decades.
- **m-12.** Self-tests should not count as drafts. Included in M2.
- **m-13.** Adaptivity items A3–A7 (§4).
- **m-14.** MC-4: "the live rival lies strictly more than 3σ_pre outside J_K".
- **m-15.** MC-2: state that the platform's Π is computed by X_Π on Sol_𝒦(𝒞_platform) in silico, where 𝒞_platform is built from structural data only.

---

## 6. Summary (5 lines)

1. **Self-tests.** ST-4, ST-5, ST-8 and ST-9 hold; ST-6, ST-7 and ST-10 fail as written; ST-1, ST-2, ST-3 and ST-11 are underdetermined, because there is no completion convention and no precedence inside a screen. FZ-2's attestation is therefore false, and its verification record does not exist.
2. **Root defect (B1).** §2.3 shrinks 𝒜_Π to standard-selector outputs, and FB, the S4 b_Π gate, SC1, Q3 and Q5 all use that set. A genuinely new Π falls outside FB (no witness is possible, so CARD-STANDARD); a standard-selected Π fails b_Π at S4. This is a disguised kill, and it is why ST-6 cannot reach S5.
3. **Feasibility (B4).** Appendix A's 640-bit price omits mandatory items. The corrected honest price is about 830–1450 bits, against 770–930 bits of credit at c_J = 1. So c_J = 1 is not reliably reachable; c_J = 2 is. "Not reachable by tuning" holds only at c_J = 1, though tuning never pays for itself.
4. **Pricing that kills, and pricing that is too lax.** IP-6 ΔF_tgt with axioms deleted (B2) and IP-13 with an unfrozen N (B3) kill any card in clear text. IP-4 and IP-14 are unbounded and IP-14 double-charges (M1); IP-12 templates have no defined size (M2). In the lax direction, G counts T and the carrier 48 times (M4, about 156 bits), and §2.5(b) never prices M's hand choices (M5).
5. **Adaptivity.** Sequential evaluation leaks finite holdout pools: revealed holdouts are not excluded from later pools (A1), and a Selector context can be reused across cards (A2). The fix is pool exclusion, a fresh Selector per card and cumulative decoder and witness re-runs, plus a committed pick order and prospective-only favourable CI-n (minor).
