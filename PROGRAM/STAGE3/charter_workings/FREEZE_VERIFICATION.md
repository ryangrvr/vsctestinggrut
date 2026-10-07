# Stage-3 charter — pre-freeze verification record

**Subject:** `PROGRAM/STAGE3/STAGE3_CHARTER.md` (charter FZ-2). **Date:** 2026-10-07.
**Status:** non-normative record; the charter governs.

## 1. Round 1 — four independent audits of the pre-freeze draft
All four audits were read-only. Their full reports are in this folder:
`AUDIT_R1_A1_coverage_DL.md`, `AUDIT_R1_A2_coverage_SCM_credit.md`,
`AUDIT_R1_B_conformance.md`, and `AUDIT_R1_C_selftests_feasibility.md` (with
`audit_C_arithmetic/feas.py`). Their line numbers refer to the pre-freeze draft.

| Audit | Scope | Result on the pre-freeze draft |
|---|---|---|
| A1 | Coverage of red-team lenses D (definitional) and L (relocation): 91 patterns and ambiguities | 79 PASS, 11 WEAKENED, 1 UNCAUGHT; 2 BLOCKER, 14 MAJOR, 15 MINOR |
| A2 | Coverage of lenses S, C and M (172 items), plus an attack on the new credit structure | 145 PASS, 24 WEAKENED, 3 UNCAUGHT; about 17 new loopholes (N-01 to N-17) and 8 honest-unreachability defects (O-1 to O-8); 6 BLOCKER, 9 MAJOR, 13 MINOR |
| B | Conformance with G2-11, R1 integrity, cross-references, consistency, freezability, candidate check | 2 BLOCKER, 14 MAJOR, 31 MINOR; candidate check PASS |
| C | Self-tests ST-1 to ST-11, feasibility (ST-10), disguised kills, adaptivity of sequential evaluation | 4 self-tests held as written, 3 failed and 4 were undetermined; 5 BLOCKER, 9 MAJOR, 15 MINOR |

**Every audit concluded "do not freeze as drafted."** All four ran the candidate check
or kept the constraint, and none found a candidate law in the charter.

## 2. The decision that changed the design
- **Credit for generated structure (G) withdrawn.** The pre-freeze draft credited
  generated Π, T and carrier per instance. Audit A2 found that this credit could be
  gamed:
  - credited against the abstract-meaning branch;
  - selector-set counting;
  - unremoved multiplicity;
  - profile inflation;
  - decorative symmetry;
  - a decoder window sized for zero stakes;
  - G earned without any coupling;
  - frozen-field persistence.

  Audit C found G too lax on the T and carrier terms. The fixes (realized-multiplicity
  subtraction, decoder fractions, coupling ties, caps) would have added a large, fragile
  surface. Generation is therefore a **gate, never a credit**, as in v1's FC-3.
- **Feasibility restored instead by scale and caps.** b_J is counted over up to N_cred =
  100 structurally distinct post-freeze instances (N_dist), capped by a family-level
  standard-class comparison (a constant shared across instances counts once) and by the
  codimension surviving on the lock fibers.
- **Compression margin.** ΔL₀ = b_J − Price; D_sel enters only the LOOKUP test.

## 3. Dispositions of BLOCKER and MAJOR findings
"Applied" means the auditor's wording, or an equivalent, is in the charter.

| Finding | Disposition | Where |
|---|---|---|
| B-B1 Freeze act vs RULES 8; this record missing | Applied: the CHECKS line follows a remote-verified push; this record exists | Header, FZ-1, FZ-2, §18.1, §25 |
| B-B2 Four "frozen tiers"; d_op undefined at E₂±, T_caus | Applied: R1's two tiers named; E₂± and T_caus are catalogue classes with BL distances fixed as a Stage-3 convention | §1.4 |
| B-M3 DEF-4 value-monotonicity | Applied: zero-set monotonicity only | DEF-4 |
| B-M4 Claims about the join; J, T_univ undefined | Applied | §1.4, §15.6, CT-14 |
| B-M5/M6 Addition 3 in G | Moot (G withdrawn); 𝒜_Π^hand rule in both branches | §2.3 |
| B-M7 Four regime thresholds | Applied: a single δ_RH | §13.2, BP-4, BP-6, §1.5, §13.5 |
| B-M8 𝒜_B^base undefined | Applied | XS-7 |
| B-M9 Q9 blocked SCOPE-G | Applied | Q9 |
| B-M10 Cross-card Bonferroni | Applied: fixed α_obs = α/(3·n_obs) | MC-9, BU-7′ |
| B-M11 Earlier holdouts not excluded | Applied | BU-6, §15.9 |
| B-M12 AI-3 sample size unfixed | Applied: N_AI3 = 160 | §1.5, IP-13, App. A |
| B-M13 Scope-G chart undefined | Applied | §1.5, App. A |
| B-M14 σ_tot undefined | Applied | MC-4 |
| B-M15 BU-8 captured self-tests and nulls | Applied: exemption | BU-8 |
| B-M16 Self-test verdicts vs T-1 | Applied: precedence and self-test convention | T-1, §24.2 |
| A1-1 BP-5 starved B-SRB | Applied: correlators to order m★★ plus Θ_std, whatever the prediction uses | BP-5, C13 |
| A1-2 JN missed Ξ-level conjuncts | Applied: NR-17(a)/(b), NR-4 "appears", CT-77 | NR-17, NR-4 |
| A1-3 Size test | Applied, modified: log₂ of 𝒜_Π^hand over G_ι, minus log₂ M ≥ b_Π (b_Π 6, n_min 8). v1's comparison with the IP-14 ontology price is dropped, because it would exceed the 16-bit maximum; the ontology is priced in Price | §1.3 |
| A1-4 Fixed-T fibers | Applied | §2.5 |
| A1-5 Q4 second sentence | Applied | Q4 |
| A1-6 DIF-5(e) at S4 | Applied | §15.3, §5.5, DIF-5(e) |
| A1-7 §15.5 closure under DEF; observable independence | Applied | §15.5, MC-9 |
| A1-8 Appendix D incomplete | Applied | App. D (D-10 to D-13) |
| A1-9 Decoder cap on G | Moot (G withdrawn) | — |
| A1-10 c_J(b) "poison pill"; Price(M) undefined | Applied in round 1 but inoperative; corrected in round 2 (§7) | §2.5 |
| A1-11 Inexpressible-type escape | Applied | Q3(c), NR-10(n), C12 (E_std) |
| A1-12 Instance-indexed pin pair | Applied | Q5 |
| A1-13 Hidden kill: "if T_Π contains one" | Applied: provenance test | §1.3 |
| A1-14 s_T law class and normalization | Applied | §1.4 (iv) |
| A1-15 PC-7(b) non-unique factorization | Applied: declared static tail | PC-7(b) |
| A1-16 NR-7 scrambling components | Applied | NR-7 |
| A2 F-1 G's Π term; 𝒜_Π reduced by selectors | G withdrawn; 𝒜_Π^hand never reduced, in the form audit C proposed (B1) | §2.3 |
| A2 F-2 Decoder window; asymmetric types | (a, c) moot; (b) applied | NR-5 |
| A2 F-3 G without coupling | Moot | — |
| A2 F-4 Family cap on b_J | Applied in round 1 but inoperative; corrected in round 2 (§7) | §2.5 |
| A2 F-5 BP-5 | Applied (merged with A1-1) | BP-5 |
| A2 F-6 / C-B2 IP-6 kill | Applied, modified: 4 bits per canonical item; all card-specific content priced as statement or input; truncation priced under IP-5 and DC-4. Neither auditor's replacement test was adopted, because each still priced a law written in a vocabulary item (e.g. a specific Hamiltonian) at the whole credit | IP-6, §4.1 typing |
| A2 F-7 D_sel filling the margin | Applied: ΔL₀ | §4.3, §4.4, KU-11 |
| A2 F-8 Lock-fiber cap | Applied | §2.5, Q6 |
| A2 F-9 Distinct instances only | Applied: N_dist | §1.5, §2.5 |
| A2 F-10 / C-M1 Unbounded selection families | Applied: members no longer than the chosen item; finite and disclosed before S6; IP-14 replaces the declaration term | IP-4, IP-14, IP-1 |
| A2 F-11 Clock between cards | Applied: D_card = 120 days | BU-6, App. A |
| A2 F-12 Collapse coverage at width 6 | Applied: auditor-exhibited | §15.2, App. A |
| A2 F-13 Components evaluating the law | Applied | PC-6, NR-4 |
| A2 F-14 Non-vacuous persistence; τ_slow with conserved charges | Applied (FROZEN Π fails DIF-2) | §1.3 |
| A2 F-15 FB(u) for non-standard u | Applied | §2.5 |
| C-B1 𝒜_Π cliff | Applied | §2.3, NR-6, §15.7(viii) |
| C-B3 IP-13 unfrozen N | Applied (N_AI3) | IP-13 |
| C-B4 Feasibility note | Applied: re-derived | App. A note, ST-10 |
| C-B5 Self-test attestation | Applied; ST-6, ST-8, ST-9 and ST-11 corrected in round 2 (§7) | §24.2, T-1 |
| C-M2 IP-12 template size | Applied | IP-12 |
| C-M3 AI-1 floor | Moot for G; AI-1 is in the credit family only if it has ≥ n_min relata | §1.5 |
| C-M4 G over-credit | Moot | — |
| C-M5 Price(M) hand choices | Superseded in round 2: M receives the card's interface at zero price (§7) | §2.5 |
| C-M6 "Built in F" | Applied | Q3(a) |
| C-M7 OR-6 skeptic always wins; auditor stall | Applied | OR-6 |
| C-M8 B-CF vector near all-correct | Applied: collapse no longer fails G-SEL by itself; Hamming diagnostic | §15.1, §15.2 |
| C-M9 Catalogue T_Π = Aut(codomain) | Applied | NR-10(f) |
| C-A1/A2 Sequential leakage; Selector freshness | Applied | BU-6, §15.9, §23, §18.1 |

## 4. MINOR findings
- **Applied:** all MINOR findings, wholly or in substance. This covers:
  - wrong pointers and undefined symbols (H_hor, κ_res, k_ex, N_frozen, W, d_rec, the
    "D5" prefix);
  - Q2 test domains, Q3 discrete violations and STANDARD-GENERIC, the Q10 per-relation
    scope, MC-2 fibers, the MC-4 log minimum, scope-Q zero separation, MC-6
    alternate-platform order, the MC-6 C7/C9 pointer;
  - the KU-7 secondary relation, NR-11 per the unchanged R1 table, §1.4(iii) orbit
    closure, HB-12 not an ε witness, the discrete alphabet;
  - the Dom_gate per-Ξ carrier form, Q6 per lock fiber, PC-7(d) gate invariance, the
    STD-3 higher-order caveat, the record-level surrogates;
  - b_J at p★ for every p, VAR-1 universe, OR-5 banking condition, IP-5 range bound,
    STD-14 order m, GY-10 versus SPS, the SEL-11 truncation clause, VB closure versus
    verdict patterns, the MC-2 in-silico platform Π;
  - CV-6 kit catalogues, CV-7 prospective favourable interpretations, NR-10(m)
    persistence of the carrier and readout, §19.4 wording, selection after S0, the
    Appendix D completion, and the §0.6 summary corrections.
- **Declined:**
  - A2 F-29: Q2 rectangle form. It is redundant given Q3(a) and the realized-coupling
    c_J.
  - Symbol reuse of J for the join, J_K and J_SRB. The subscripts disambiguate.

## 5. Residual items for the owner's review (none blocks the freeze)
1. **Credit bar** (App. A note). At c_J = 1 a compact card passes if its price is below
   about 1000 − 6n bits, n being its number of real literals (about 150 tokens,
   components included); a heavy card needs c_J = 2. The owner may
   rescale N_cred before the first draft.
2. **Evaluation order** (D-3). Sequential evaluation lets later cards learn from earlier
   intake rulings and verdicts (the intake-oracle trade-off). This is priced by the
   VARIANT rules, the selection tax, and the re-run and exclusion rules. Batch freeze is
   the stricter alternative.
3. **Kit authorization** (OD-12). The §19.3 kit is not authorized by this charter.
4. **Scope-Q practicality** (audit C). Under §13.6 and MC-11, scope-Q locks will in
   practice need platforms where RH-KMS is certified to fail.

## 6. Round 2 — check of the revised text
See §7.

## 7. Round 2 — two independent audits of the revised text
Reports: `AUDIT_R2_consistency_selftests.md` and `AUDIT_R2_adversarial.md`. Their line
numbers refer to the round-1 revision.

| Audit | Scope | Result |
|---|---|---|
| R2-C | Dispositions of round 1, consistency after the edits, self-tests, feasibility, freezability | About 50 of 56 dispositions confirmed; 2 BLOCKER, 4 MAJOR, 12 MINOR; withdrawal of G confirmed clean; candidate check PASS |
| R2-A | Adversarial attack on every rewritten rule | 4 BLOCKER, 12 MAJOR, 17 MINOR; IP-4, IP-6 (canonical, content-free), IP-12, IP-13, IP-14, ΔL₀/D_sel, the E₂±/T_caus conventions, BU-6 sealing, the collapse change, Q3(a), Q4, Q9, NR-7, NR-10(m) and the PC-6 law-evaluation ban found sound |

**Dispositions (all applied unless stated).**

| Finding | Fix | Where |
|---|---|---|
| R2-C F-1 / R2-A B2 Price(M) made c_J(b) and the family cap inoperative (or a kill) | Admissible comparison classes (B-HB, compositions, pre-published SFP classes stated without reference to the card) receive the card's interface at zero price; shared constants priced once; "if no class qualifies, no bound"; v1's NULL-M guard restored | §2.5, D-13 |
| R2-C F-2 ST-8, ST-9 terminals | Terminal S3 NONGENERATIVE; Q3 recorded | §24.2 |
| R2-C F-3 NR-17 pre-empting ST-6, ST-11; Price(ℛ★ stated directly) undefined | L★ defined; a PS-5 sub-conjunct is assessed under NR-12(b) (JN recorded, not applied); ST-6 and ST-11 rows completed | NR-17, §24.2 |
| R2-C F-4 ΔF_tgt orphaned | Defined in IP-7 by random replacement | IP-7 |
| R2-C F-5 / R2-A M1 Closure by definability | Match only when used as the item; VB-5/6/7 need non-classical structure; classical simplex, base tokens and record-law objects never match | IP-6 |
| R2-C F-6 Record accuracy | §3 rows relabelled; this §7; FZ-2 reworded | here, FZ-2 |
| R2-A B1 §2.3 licensed SPS-on-𝒞 | SPS on realized dynamics → STANDARD-MECHANISM; on 𝒞 or the inventory → NR-6 decoder (RELOCATED); NR-6 governs | §2.3, §15.7(viii), §21.2 |
| R2-A B3 NR-17 trivial superset | A superset R may not contain a clause of 𝒦; a disjunction is not a split; measure for (b) specified | NR-17, CT-88 |
| R2-A B4 NR-10(n) universal kill | Expressibility concerns the latent state; the auditor supplies the readout | NR-10(e), (n) |
| R2-A M2 Decorative-read persistence | X_Π-relevant variables | §1.3, CT-89 |
| R2-A M3 Inert-relatum padding; G_ι | Inert relata deleted before the size test; G_ι is the generated group | §1.3, §2.3, CT-90 |
| R2-A M4 Provenance laundering | Drive-map content in X_T fails the provenance test; burden on near-protocol maps | §1.3 |
| R2-A M5 Singleton fibers zeroing c_J | Fixed-class fibers; minimum only over fibers with ≥ 2 differing realized interface values | §2.5 |
| R2-A M6 Constant decoders; menu-branch T_Π | Constant "decoders" are not decoders; branching among named classes supplies them; catalogue T_Π generated only by construction | NR-6, NR-10(f), PC-6, CT-91 |
| R2-A M7 Q5 trivial split | Non-trivial splits only | Q5 |
| R2-A M8 E_std and selective ⊥ | Embedding conditions, auditor substitution, realized-structure substitution | Q3(c), CT-92 |
| R2-A M9 Widened confirmation band | Confirmation multiplier stays 2 | MC-9, App. A |
| R2-A M10 Pre-aggregation static maps | All static maps declared, calibrated and tested | PC-7(b), §15.3, DIF-5(e), CT-93 |
| R2-A M11 Favourable CI-n could not rescue the disputing card | Applies to that card (re-run with Recomputer) and forward; retroactive only toward failure | CV-7, BU-6 |
| R2-A M12 Decorated copies | Distinctness after deleting inert data, and Im not equal | §1.5, CT-94 |
| MINOR (R2-C F-7 to F-18; R2-A m1 to m17) | Applied: lock-threshold row; H_hor leftovers and t₁; feasibility wording at p = 16; "tier" terminology; ST-1/ST-3/ST-4/ST-7 precision; D-13 wording; PV-5; S4/S5 effect of DIF-5(e); NR-4 threshold for ℛ★; redraws as AI-3 draws; C7 pointer; ΔL₀ in §15.9; N_AI3 label; B-HB regime key; in-silico budget cited in MC-8; approximate Π matching; M(ι) by cores; size test versus full symmetry (GENERATED-STRONG); orbit closure; s_T post-map; VB-16 as PS-5; constant kernels as measures; NR-1 measure wording; canonical forms content-free; c_f regime; IP-13 redraws; IP-12 logged artifacts; NR-7 statistic; D_card start; pool shortfall; E₂±/T_caus covariance | various |
| R2-A m11 NR-4 r_lock tie in the weakly coupled corner | Not changed; listed for the owner (§5 item 5) | — |

**Residual items added for the owner.**
- 5. NR-4's ablation test decides "appears" within r_lock. Under log-uniform couplings,
  relations whose two sides vanish together in the weakly coupled corner can reach the
  1/Q_min fraction. The owner may choose to exclude S–E-decoupled points from that test.
- 6. When T_Π is injective in Π, DEF-14 limits jointness for relations stated through
  ε^{T_Π} (round 3).

## 8. Round 3 — narrow check of the round-2 rewrites
Report: `AUDIT_R3_narrow.md` (2 BLOCKER, 11 MAJOR, 13 MINOR; candidate check PASS).
All findings were applied in the auditor's wording, or in equivalent wording:

| Finding | Fix | Where |
|---|---|---|
| R3 B1 Inert-relatum deletion failed the size test everywhere | One template of cost ≤ ℓ_dec, the same on every lock fiber, deleting one whole output block only if it is inert on Sol and on ≥ p_dec of AI-3 | §1.3, §2.3, D-11, D-13 |
| R3 B2 Q5 split test accepted trivial splits | Parts must be strictly shorter than 𝒦 and must not restate it; fixing is tested on Dom_gate | Q5, CT-95 |
| R3 M1 c_J(b) inert or a joint kill with Q3 | Comparison classes: parameters are constants, not functions of u or ℛ★; inputs through θ_dict; Obs(M) taken with constants free; empty Im ∩ FB does not bind; the same guard in Q3(b) | §2.5, Q3(b) |
| R3 M2 Family-cap price escape; decorated near-copies | Price condition dropped for the cap; constants grouped on the coarsest grouping | §2.5 |
| R3 M3 Fragmented fibers | N_fib counts only instances in qualifying fixed-class fibers | §2.5, C5, C11, App. A note, CT-96 |
| R3 M4 §1.4(iv) whitening-first killed non-T_lin classes | s starts with the canonical reduction of one catalogue class declared in C7 (or the identity) | §1.4(iv) |
| R3 M5 Provenance test by definability | "Computes and uses"; content merely definable from the inputs does not count | §1.3 |
| R3 M6 PC-6 convicted Obs | Obs exempted from the record-law ban; factorization test names the other components | PC-6 |
| R3 M7 NR-1 flagged every Markov rule | Flag only named or encoded PS-5 structure; derived PS-5 goes to NR-12(b) and NR-17 | NR-1 |
| R3 M8 NR-10(e)/(n) demanded FAIL | "Does not return PASS"; ⊥ handled by substitution | NR-10(e), (n) |
| R3 M9 NR-10(f) "named" ambiguous | Named = identified by a constant symbol, literal or menu index; case splits inside a construction and extremal readout selection go to NR-3, NR-6 and DEF-17(a) | NR-10(f) |
| R3 M10 NR-17 guard reopened CT-77 | R may contain clauses of 𝒦; only Price_min(R) < Price_min(𝒦) is required | NR-17, CT-97 |
| R3 M11 NR-4 lock-fiber clause pointwise | Fraction rule applied per lock-fiber instance | NR-4 |
| R3 m1–m13 | Applied: relevant-variable definition; CV-7 "other cards"; CT-92/93 wording; control entry point in §15.3; IP-7 on b_J; IP-13 normalized for redraws; fiber statistic and lock-fiber minimum; §4.3 recomputes comparison-class admissibility per p; E_std conditions; ST-9 without thermal premise; sequential datum deletion in §1.5; D-11, D-13 and "both tiers"; NR-17 diverted 𝒦₂ as a premise | various |

**Owner note added by round 3.** When T_Π is injective in Π, DEF-14 limits jointness for
relations stated through ε^{T_Π} (only catalogue-class evaluations can witness
coupling across different Π). This is listed as residual item 6.

## 9. Loop-until-dry rounds (multi-lens find, independent verification)
Each round runs six finding lenses (hidden kills, loopholes, consistency, self-tests,
G2-11/R1 conformance, feasibility arithmetic) over the whole charter. Every BLOCKER or
MAJOR finding is then checked by an independent skeptic, who tries to refute it and
tests the proposed fix for side effects. Confirmed fixes are applied between rounds.
The loop stops when a round confirms no BLOCKER or MAJOR. Results are appended below.

**Round A: stopped unread.** It was stopped before completion to conserve the owner's
usage budget (owner message, 2026-10-07). Its results were not read or used. It can be
resumed later from its cache (workflow run `wf_959efb57-3b2`).

## 10. Freeze status
- The charter is frozen with rounds 1–3 applied. **The loop-until-dry audit was not
  completed.** Each round so far has found real defects, so further defects are
  expected.
- Before the first 𝒦 draft, the owner may amend any rule in either direction (§19.2).
  The recommended next step, budget permitting, is to resume the loop and apply its
  confirmed fixes as a numbered charter repair (CR-1) before Card 1.

## 11. CR-1 (owner ruling G2-12) — too-strict repairs before Card 1
- **Scope (G2-12).** Apply only findings that make a rule too strict. Record loopholes in
  `CR2_QUEUE.md`, unapplied. No loop-until-dry.
- **Round run.** The hidden-kill and feasibility lenses ran once over the frozen text
  (`0bc125a`), and each BLOCKER/MAJOR finding was checked by an independent skeptic.
  Workflow run `wf_2f4534e0-697`; full results in `AUDIT_CR1_too_strict.json`.
- **Result.** 17 findings were confirmed as too strict, with verified final wording;
  none was refuted. All 17 were applied in the skeptics' final wording, which corrects
  the original proposals so that they open no loophole. Two MINOR findings:
  - IP-4 "no longer" is now measured in L_stmt bits (applied).
  - Dimension certificates for sets outside Im (noted for the kit; no text change).
- **G2-12 items 1–6.** Applied: §1.5, C1, §19.3, Appendix A, §14, DEF-14 and NR-4 (with
  the r_lock/σ_pre decoupling).
- **Round A loopholes lens.** Seven loopholes, queued in CR-2 unapplied.
- **Not run.** Round A's consistency, self-test, conformance and remaining lenses were
  not re-run (G2-12 scope; budget). The CR-1 edits were not re-audited.

| # | Too-strict defect | Fix (where) |
|---|---|---|
| 1 | Generated stationary law poisoned every stationary card (NR-12(b)); NR-12(d) existential | Poison only steps that use an FDR, fluctuation theorem, regression or Onsager form derived from a certified non-KMS stationary law; NR-12(d) needs presence on a KMS instance (NR-12) |
| 2 | Inputs outside the HB ranges emptied 𝔐_std, so b_J = 0 | Values fixed by θ_dict or BP-5 inputs are taken even outside the ranges (§2.2, §15.4, §15.5) |
| 3 | Q1 undefined on selectivity embeddings | Exception: Q1 is not evaluated on Emb(Σ) items (Q1) |
| 4 | Appendix G absolutes are unsatisfiable on any platform | Magnitude clauses bounded and propagated; design clauses exact; discrete records (MC-6) |
| 5 | SC1's {ε > r_lock} killed SCOPE-G | Applies to SCOPE-Q only (§2.5) |
| 6 | Weak-coupling draws made Q3(c) and NR-17(b) fire | Decoupled-corner exclusion (Q3(c), NR-17(b)) |
| 7 | AI-2 outside the domain killed threshold-symmetric cards | AI-2 inside the domain, or admitting a zero-mean perturbation (§1.5, NR-5, DIF-7) |
| 8 | Persistence thresholds below one relatum at n = 8–16 | 1/abs(V) floors and the single-relatum allowance (§1.3, §15.7, App. A) |
| 9 | HB-5 exact zero failed every T_Π without filters | Filters removed with their known maps first (§15.3, DIF-5(e)) |
| 10 | G5-HOLD unsatisfiable for card-specific templates | Prospective holdouts allowed; a search shortfall is an auditor-side void (G5-HOLD) |
| 11 | MC-7 power unreachable against a rival near 3σ | Power computed against a rival at least (z_obs + 2)σ_pre outside J_K (MC-4) |
| 12 | 𝓗 required B-HB models to reproduce every chart coordinate | 𝓗 taken in the ℛ★-coordinates; standard consequence of a single-axis property assessed as P (§2.5, Q3(a)) |
| 13 | Composition N_B ≤ 8 blocked instances with more than 8 relata | Per-member ranges; compositions up to abs(V_ι) members (§15.4, App. A) |
| 14 | Q3(c) transplant over-fired near decoupling | As 6, with replacement draws (Q3(c)) |
| 15 | E_std and ℛ★ priced into infeasibility | E_std recorded but not charged unless used; ℛ★ choice priced as a forced-family selection (Q3(c), IP-4, App. A) |
| 16 | IP-5 infinite price for exact values | Zero-width windows priced at L_stmt of the value's expression (IP-5) |
| 17 | R_card summed over Evaluator-controlled runs; T_audit clock | R_card over the minimum list only; T_audit from S0–S8 clearance (DC-2, OR-6, App. A) |

## 12. Kit session (G2-12 item 3) and CR-3
- **Built** (`PROGRAM/STAGE3/kit/`, one session):
  - (a) the L₀ normalizer and price coder;
  - (b) the NR-4 ablation harness, with the decoupled-corner exclusion and the excluded fraction reported;
  - (c), partially: exact ε^{T_lin} zeros on affine-entry HB-3/HB-4 instances, and the static-map witness on HB-4;
  - (d), the SEL part only: the §2.4 counts reproduced with the SD0 code.
- **Not built:** every other item. These take the hostile defaults KD-1 to KD-5 of CR-3 (Appendix H). No extension was taken.
- **Not externally checked.** §19.3 requires that check before the first draft is logged.
- **NR-4 readings.** The harness's readings of NR-4 are listed in `kit/README.md` for owner ruling.

