# STAGE-3 CHARTER (GRUT 2): rules for judging law cards · DRAFT 0 · 2026-10-07

> **Status: DRAFT FOR OWNER REVIEW. This charter is written and frozen ALONE (G2-11).**
> - It contains no candidate law. It does not sketch, name or give an example of a 𝒦, and it optimizes nothing.
> - Every construction in §19 is an abstract gaming pattern labeled **CHARTER TEST**. None of them is a physical proposal.
> - After the freeze, STOP for owner review before Card 1 is generated (G2-11).
>
> **Angle of this draft: physics-baseline realist.** The baseline is what established physics already imposes, stated concretely. Nothing that physics imposes earns credit.

**Governing inputs.**
- `PROGRAM/OWNER_RULINGS.md` G2-11 (ruling block and additions 1–4), G2-08 item 8, G2-10.
- `RULES.md`, `NORTH_STAR.md`, `STATE.md`.
- `R1_SYNTHESIS.md` §§1–3, 7, 11, 12.
- `D5_COMPARATOR_AUDIT.md` §§2.3, 3, 6, and `D5_IDENTIFICATION.md`.
- `SCOREBOARD.md`, `GRAVEYARD.md`.
- `F0_REQUIREMENTS_CONSOLIDATION_01.md`. Its requirements are called **FR1–FR15** here.
- The SD0 precedents: charter, compactness accounting, result, reconnaissance, generalization checks and holdout protocol.

**Freeze semantics.**
- **FZ-1.** The charter is frozen at its commit SHA after owner review. Every card cites that SHA.
- **FZ-2.** Before Card 1 is frozen, the charter changes only by a numbered charter repair (CR-n) that the owner authorizes.
- **FZ-3.** Once Card 1 is frozen, the charter is immutable for Stages 3–5.
  - Evaluation tooling may be repaired. Every repair is logged.
  - No repair may change a threshold, a battery item, a baseline rule or a verdict criterion.
- **FZ-4.** Values marked **[P]** are proposed constants. The owner fixes them at freeze (§20), and they bind from then on.
- **FZ-5.** The freeze has one precondition: the charter self-tests ST-1…ST-5 (§19.2) must return their stated verdicts under this text. If any self-test fails, the charter is defective and is repaired before the freeze.
- **FZ-6.** A merge is provenance, not endorsement (§16).

**Traceability.**

| Owner requirement (G2-11) | Where |
|---|---|
| 1. Baseline freedom spaces 𝒜_Π, 𝒜_T, 𝒜_Γ, with 𝒜_ε as an image | §2 |
| 2. Success criterion: freedom reduction + compression + measurable consequence | §3 |
| 3. Compression accounting and information price | §4 |
| 4. Nonrelocation | §5 |
| 5. Budget: at most 3 genuinely distinct cards | §12 |
| 6. Required card contents | §13 |
| 7. Originality judged at the assembled-law level | §10 |
| 8. Cross-sector gold standard: parameter transfer | §11 |
| 9. Stopping rule, no staircase | §15 |
| Addition 1: merge = provenance, not endorsement | §16 |
| Addition 2: ε_R is derived; definitional relations earn nothing | §1.3, §2.4, Q2 |
| Addition 3: baseline computed after standard theory | §2.2–§2.3 |
| Addition 4: response scope per target relation | §6 |
| Carrier derived modulo representation; no presumed monotonic tradeoff | NR-2, NR-4, NR-6, Q5 |
| Stage-4 gates, Stage-5 lock, Stage-6 transfer | §9, §8, §11 |
| Trajectory risks: staircase, consistency-only law, no lock target, no battery | §15, §9.4, §8 (LT-1), §7 and §9.1 |

---

## 1. Objects (frozen notation)

### 1.1 Law and ontology

- **Ξ** is the relational process object. Its kinematic type 𝒳 is declared and priced by the card.
- **C** is the law's input data. Its meaning is declared and priced (FR11). Possibility language means *declared* possibility.
- **𝒦[C, Ξ] = 0** is the law. Sol_𝒦(C) := {Ξ ∈ 𝒳 : 𝒦[C, Ξ] = 0}.
- The card declares 𝒳 and 𝒦 separately, and both are priced. The law must be nonvacuous: ∅ ≠ Sol_𝒦(C) ⊊ 𝒳 on every instance in the declared domain (KC-6).

### 1.2 Generated structures: the chain 𝒦 → Π → [h]_{T_Π} → T_Π → Γ_Π → ε_R

Each structure is a map defined **uniformly** on Sol_𝒦: one L₀ definition for every instance, with no case split keyed to an instance.

**Π(Ξ): the partition.**
- It partitions the instance's relata set V into one designated environment block E and system block(s) S, or S₁…S_m for multipartite embeddings (§9.1).
- An approximate Π is an assignment V → Δ(blocks).
- **Persistence and A-stability (frozen criterion).**
  - VI_norm(Π, Π′) := VI(Π, Π′) / log₂|V|. VI is Meilă's variation of information, with blocks treated as label variables under the uniform measure on V.
  - Π is *(δ_Π, H)-persistent and A-stable* in either of two cases:
    - for a time-indexed Π: VI_norm(Π(Ξ_a)(t), Π_ref) ≤ δ_Π for every protocol a ∈ A and every time t ≤ H;
    - for a global Π: VI_norm(Π(Ξ_a), Π(Ξ_b)) ≤ δ_Π for every pair a, b.
  - Ξ_a is the realization under protocol a. Π_ref comes from the designated reference protocol a₀ ∈ A.
  - H covers the full protocol and record window of every a ∈ A.

**Z_Π: the environment state variable.**
- This is the variable the card *derives* to be protocol-invariant: the environmental identity (NORTH_STAR).
- Its dimension is arbitrary.
- Which variable it is (instantaneous, initial or other) is a **derived output, never a definition** (R1 §12 item 5; D5 Remark D3).

**[h]_{T_Π}: the readout class.**
- h maps states of Z_Π to the record space 𝒴. It is fixed only up to T_Π: h ~ t∘h.
- No card fixes a unique coordinate formula for h (G2-11).

**T_Π: the interface class.**
- It is a group of record maps acting per protocol, generated from (Ξ, Π).
- The card locates T_Π in the closed R1 lattice L_T (§2.3).

**A and the protocols.**
- A is a finite repertoire of interventions on the S-block(s) of Π_ref. Interventions are L₀ vocabulary. a₀ ∈ A is the designated reference protocol.
- The card declares a repertoire class 𝔄 and a grid class 𝔗. 𝔄 is closed under taking sub-repertoires with |A| ≥ 2 that contain a₀.

**Γ_Π := Obs_Π(Ξ) = (P_a)_{a∈A}.**
- P_a is the law of the record Y_a ∈ 𝒴^τ under protocol a.
- **Only per-protocol laws are data.** Joint laws across protocols are inaccessible-context data (FR3) and may not appear in any relation.

**Carrier status.**
- **PASS** requires two things:
  - the card proves from 𝒦 that Y_a = t_a(h(Z_Π)), with one h and t_a ∈ T_Π, for every a in every A ∈ 𝔄;
  - at the lock, the platform passes certification (§8, MC-6).
- **FAIL** if the derivation yields protocol-dependent readouts h_a. **UNRESOLVED** otherwise.
- R1's verdict table applies unchanged: R1-PASS / R1-NULL / NO RECIPROCITY VERDICT / MODE SELECTION.

### 1.3 ε_R is derived (Addition 2)

- **Definition.** ε_R := ε[Γ_Π, T_Π] := inf over P★ of max over a ∈ A of d_op^{T_Π}(P_a, T_Π·P★).
- **d_op is frozen.** It is the bounded-Lipschitz quotient distance: center, whiten, then minimize over O(k) at Tier 1; normal scores minimized over the reflections ℛ at Tier 2 (R1 §1).
- **Generated classes.**
  - If T_Π ∈ {T_R1, T_mono}, the frozen d_op applies.
  - For any other T_Π, the card supplies the maximal-invariant reduction and proves that d_op^{T_Π} is a well-defined orbit pseudometric. Otherwise ε_R is undefined for that card, and S6 fails.
  - **The R1 ladder stays closed** (G2-10). A card's T_Π is an output of the card, not a new R1 tier.
- **𝒜_ε is the image of 𝒜_Γ × 𝒜_T under ε.** It is never an independent axis, and no bits are ever counted on it (§4, FR-4).

### 1.4 Audit instances

An audit instance is ι = (C_ι, V_ι, A_ι ∈ 𝔄, τ_ι ∈ 𝔗, 𝒴_ι, δ_Π, H). These families are required:

| Family | Content |
|---|---|
| AI-1 | The smallest nontrivial instance, computed exactly |
| AI-2 | Symmetric-input instances (RP1) |
| AI-3 | A generic-input ensemble (RP2, RP3) |
| AI-4 | The battery embeddings (B4, B5, B8) |
| AI-5 | Blind holdouts selected after the freeze by an independent selector (§21) |

**Chart φ_ι.**
- A finite chart of 𝒜_Γ built from T-invariant witness coordinates. Examples: whitened cumulants to a declared order; normal-score correlations and the M3 third-order coordinates; per-witness BL functionals with the Theorem-F constants.
- The chart's box ranges and resolution are declared at card freeze.
- The auditor may add coordinates. Credit is computed on whichever admissible chart **minimizes** credited bits.

### 1.5 R1 machinery used here, with its grades (§16)

| Item | Grade |
|---|---|
| T_R1, T_mono, d_op, the verdict table, the common-carrier commitment, Prop. E/E1/E2, the G2-08 certificate | Frozen pre-result |
| Theorem C (`82d311e`) | DERIVED, checked |
| A-BL, F, M1–M3, Prop. G | DERIVED, external check pending |
| BRI1 Tier 2; D5 C1–C6 and D1–D3 | Evidence grade |

- The R1 **10-item certificate checklist** is POST-RESULT SEED. This charter **adopts** it as the lock-platform certification standard (MC-6).
- That adoption is a Stage-3 rule for platforms. It does not edit R1.

---

## 2. Baseline freedom spaces (owner item 1; Additions 2–3)

### 2.1 Principles

- **BP-1. What the baseline is.** It is everything established physics permits for operational data of the same type, in the same regime, from the same inputs, with Π, Z_Π, [h] and T **supplied by hand**.
- **BP-2. Where standard theory leaves freedom.** Standard theory leaves Π, Z_Π, [h] and T free: the modeler chooses them. It constrains Γ. This is R1's lesson: every R1 claim was conditional on a carrier supplied from outside.
- **BP-3. Regime matching (RM).**
  - For each card realization x, the auditor determines H(x), the set of regime hypotheses (§2.2) true at x.
  - Claims about x are compared only with the baseline under H(x).
  - Comparing x against standard models from a different regime is invalid (CT-10).
- **BP-4. Hostile default (HD).** If it is unresolved whether a hypothesis holds at x, it is taken to hold. The exception is when the card proves it fails by more than the lock resolution.
- **BP-5. Same inputs.** At the lock, the standard baseline receives exactly the data the card's prediction consumes (B1).

### 2.2 Standard-theory constraints SC-1…SC-12 and regime hypotheses

**Regime hypotheses (RH).** Each holds at a realization x when the stated condition is true at x.

| RH | Holds when |
|---|---|
| RH-HAM | S+E evolve under a closed generator (Hamiltonian, unitary or Liouvillian) at record resolution |
| RH-KMS | The reference state of E (or of S+E) is KMS (quantum) or Gibbs (classical) for the realized generator, within lock resolution |
| RH-MR | The realized dynamics is microreversible: time-reversal covariant, with parities ε_i and field reversal |
| RH-MK | The record or the reduced dynamics is Markov at record resolution |
| RH-GAU | E is Gaussian or harmonic, with coupling linear in E's variables |
| RH-SYM(G) | The reference law and dynamics are invariant under a group G, e.g. central symmetry |
| RH-CQ | The realized dynamics has conserved quantities |
| RH-WC | Weak coupling or timescale separation holds (Born–Markov / Davies regime) |
| RH-LIN | The readout is a linear detector of a weakly coupled E-observable |
| RH-MF | E consists of N weakly coupled units with a normalized collective readout |
| RH-NESS | Stationary non-equilibrium Markov dynamics |
| RH-ORD | An ordered phase, a critical point or a pattern-forming instability is present |
| RH-TH | Macroscopic thermodynamic regime |

**Standard constraints.** For each: the hypotheses under which it is imposed, what it imposes on each baseline space, and what therefore **earns no credit**.

**SC-1 Causality / non-anticipation.** H: always.
- **Γ.**
  - If protocols a and b agree on [0, t], their record laws agree on τ ∩ [0, t]. Together with SC-2 this is BRI0's grid-level E_univ domain.
  - Linear response functions are retarded, and susceptibilities obey Kramers–Kronig.
  - Multi-block embeddings obey no-signalling, i.e. possibilistic no-signalling (pNS) at support level (B5). Spatial embeddings obey relativistic causality.
- **T.** Physical interface maps are non-anticipating: T_caus ⊂ T_lin in the linear case.
- **No credit for:** non-anticipation; Kramers–Kronig; no-signalling; "records cannot depend on later protocol segments".

**SC-2 Positivity.** H: always. The quantum part applies once Hilbert-space structure is supplied or generated.
- **Γ.**
  - Each P_a is a probability law. Covariances and spectral densities are positive semidefinite (Bochner). Classical kernels are nonnegative.
  - Realized quantum processes are completely positive: a positive, causally ordered process tensor (comb); GKSL form for Markov semigroups.
  - Uncertainty and Tsirelson-type bounds hold once quantum structure is present.
- **T.** Interface maps send valid laws to valid laws. Quantum interface operations must be implementable as CPTP maps.
- **No credit for:** any of these. If quantum structure was supplied as an input, the bounds are also RELOCATED (IP-5).

**SC-3 KMS / FDT / fluctuation relations.** H: RH-KMS (with RH-HAM). The non-equilibrium-steady-state (NESS) forms need RH-NESS and RH-MK.
- **Γ.**
  - KMS holds for every multi-time equilibrium correlator.
  - Linear FDT. Classically, χ_AB(t) = −β·θ(t)·(d/dt)⟨A(t)B(0)⟩. In the quantum case, χ″ and the symmetrized spectrum are related by the KMS factor.
  - Higher-order response functions are fixed by equilibrium correlators: higher-order Kubo formulas, Stratonovich–Efremov, Bochkov–Kuzovlev, and quantum nonlinear FDRs.
  - Fluctuation theorems hold for every protocol (Jarzynski, Crooks, the Bochkov–Kuzovlev generating functional). They tie the whole family Γ together.
  - A Gaussian environment is fixed entirely by its spectral density and temperature (J(ω), β) (Feynman–Vernon; Caldeira–Leggett; Ford–Kac–Mazur), including the exact exogenous decomposition.
  - NESS: Agarwal-type FDRs, Harada–Sasa, and the Baiesi–Maes–Wynants decomposition (entropic plus frenetic response).
- **Generating KMS states from dynamics is itself standard:** canonical typicality, ETH, Davies thermalization, ergodic theory. A card that derives RH-KMS earns RECOVERY, not credit for freedom reduction.
- **Consequences for 𝒜_ε.**
  - Under RH-KMS + RH-GAU + linear coupling: 𝒜_ε = {0} at both tiers (Ford–Kac–Mazur; harmonic control ≈ 1.3×10⁻¹⁴).
  - Under RH-KMS + RH-SYM(Z₂) + RH-MF (the BRI1 class), the leading Tier-1 value is fixed by the reference 4-point function: ε_R = (V*/12)·|γ₁|·(1 + 0.235/N_B + …) at k = 1. The sharpness is D5 evidence grade.
- **No credit for:**
  - an ε_R value or Γ restriction at any order fixed by equilibrium correlators of order ≤ r+1 that are among the same inputs;
  - any fluctuation-theorem identity;
  - "harmonic baths are R1-NULL".

**SC-4 Onsager–Casimir reciprocity.** H: RH-MR + RH-KMS for the linear relations; a current fluctuation theorem for the nonlinear ones.
- **Γ.**
  - L_ij(B) = ε_i·ε_j·L_ji(−B).
  - χ_AB(t; B) = ε_A·ε_B·χ_BA(t; −B).
  - Nonlinear reciprocity identities follow from current fluctuation theorems (Andrieux–Gaspard).
- **Note.** R1's *operational* reciprocity (the environment responds) is a different thing. A relation that reduces to Onsager–Casimir symmetry earns nothing under either name.
- **No credit for:** symmetries of cross-responses; nonlinear reciprocity identities.

**SC-5 Conservation laws and symmetry.** H: RH-CQ, RH-SYM(G).
- **Γ.**
  - Continuity equations, sum rules (f-sum and moment sum rules) and Ward identities.
  - Curie / selection rules: a G-symmetric reference read through a G-covariant interface has no G-odd statistics. This is Theorem C's mechanism.
  - Energy balance: work = ΔE_S + ΔE_E + exchanged heat.
  - Momentum balance between S and E (action–reaction).
- **Π.** Conserved-charge and superselection partitions are standard selectors (SPS, RP2).
- **T.** Interface classes may be symmetry-covariant.
- **No credit for:** odd channels vanishing under a symmetric reference; action–reaction as "mutual response"; moments fixed by sum rules.

**SC-6 Mori–Zwanzig / GLE structure.** H: RH-HAM, with Π supplied.
- **Γ.**
  - Every closed dynamics projected onto S-variables has an exact generalized Langevin (GLE) representation: a memory kernel plus projected noise.
  - With a Gibbs initial state of E, the second FDT links the noise to the kernel.
  - Under RH-WC the Markov limit applies. A harmonic E gives exogenous noise plus linear memory exactly.
- **No credit for:** the existence of memory; non-Markovianity; viscoelastic response; "E carries a record of S's history". STATE rules memory, viscoelasticity and crystalline order to be effective regimes, never inputs.

**SC-7 Standard open-system and measurement response.** The hypotheses are given per item.
- GKSL form and complete positivity (RH-MK).
- Davies thermalization (RH-WC + RH-KMS).
- Redfield / Born–Markov dynamics.
- The quantum regression theorem (RH-MK).
- A process-tensor representation (always available).
- The influence functional (RH-GAU).
- Input–output theory, b_out = b_in + √γ·a: E's records carry input noise plus S's back-action (RH-LIN / RH-WC).
- The linear-detector imprecision–back-action inequality S̄_xx·S̄_FF − |S̄_xF|² ≥ (ħ/2)² and the standard quantum limit (RH-LIN; symmetrized spectra; Clerk et al., RMP 82, 1155).
- Bounds of the form measurement rate ≤ dephasing rate.
- **No credit for:** any interface–response tradeoff that is an imprecision–back-action, SQL or measurement-dephasing relation; "environment records encode system back-action".

**SC-8 Thermodynamic stability and the second law.** H: RH-TH or RH-KMS.
- **Γ.** Nonnegative entropy production; passivity of Gibbs states; Clausius; Landauer; positive-definite static susceptibilities; Le Chatelier–Braun.
- **No credit for:** the signs of dissipative response; "response opposes perturbation"; Landauer-type costs of records.

**SC-9 Large-N / CLT / Edgeworth scaling.** H: RH-MF.
- **Γ.**
  - Normalized collective readouts have r-th cumulants of order O(N^−(r−2)/2), with driven corrections at the coupling order.
  - Reservoir limits are Gaussian.
  - ε_R and its witnesses inherit these rates. BRI1's 1/N_B is "structurally expected" (D5).
- **No credit for:** N-scaling laws of ε_R or its witnesses in such architectures.

**SC-10 Standard differentiation–response relations.** H: RH-ORD.
- **Π and Γ.**
  - Goldstone modes.
  - Mermin–Wagner–Hohenberg.
  - The static scaling relations: Rushbrooke, Widom, Fisher, and Josephson / hyperscaling.
  - Relations between susceptibility and correlation length.
  - Landau mean-field relations.
  - Relations for interface tension and stiffness.
  - Linear-stability (Turing) wavelength selection.
  - Selection of persistent variables by slow manifolds and timescale separation.
- **No credit for:** a relation between the persistence or order of Π and the response that is one of these.

**SC-11 Representation freedom.** H: always.
- **T and [h].**
  - Only T-invariants are observable.
  - Known mathematics already covers: readout equivalence classes; maximal invariants; copulas modulo reflections; "one readout for all protocols" as measurement invariance. References: Stevens scale types, measurement invariance, IRT linking, interventional-CRL classes (D5).
- **No credit for:** the existence or form of [h]_T as such. Any novelty claim for [h]_T must be positioned against these (R1 §12 item 1).

**SC-12 Universal exogenous representation.** H: always; this is mathematics.
- **Γ.**
  - Every non-anticipating family has an exact exogenous representation with protocol-dependent readouts, even causal linear ones (Prop. E/E1; D1; D2).
  - So no record statistic separates mode selection (E-B) from back-reaction (E-C) (D1′).
- **No credit for:** any back-reaction claim made from records alone; any relation that does not involve the derived carrier.

### 2.3 The spaces

**Standard models.** 𝔐_std(ι | H) is the set of models of frameworks in the Standard Framework Panel (SFP, §10.2) that:
- (i) produce operational data of the declared type on ι (same V, A ∈ 𝔄, τ ∈ 𝔗 and 𝒴);
- (ii) satisfy every SC whose hypotheses lie in H;
- (iii) use the card's inputs at the level being compared (BP-5);
- (iv) take Π, Z_Π, [h] and T as supplied by hand.

**𝒜_Π(ι | H): partitions.**
- Definition: all Π that are (δ_Π, H)-persistent and A-stable under some m ∈ 𝔐_std(ι | H).
- **If C_ι fixes no dynamics**, then 𝔐_std contains decoupled dynamics for every partition. So 𝒜_Π = Part*(V_ι), all partitions with nonempty S and E: standard theory leaves Π free.
  - With one S and a designated E, |Part*| = 2ⁿ − 2. For n = 8 that is 254 partitions, ≈ 7.99 bits.
- **If C_ι fixes dynamics**, 𝒜_Π is the set of partitions that standard criteria certify as persistent under that dynamics (SC-6, SC-10, SPS).

**𝒜_T(ι, Π | H): interface structures ([h]_T, T).** This space carries both the readout class and the interface class.
- T ranges over L_T⁺ := L_T ∪ {T_Π}, where L_T has 7 elements (≈ 2.81 bits):
  - {id};
  - E₂±;
  - T_caus;
  - T_R1 = GL(k) with translations;
  - T_mono;
  - T_R1 ∨ T_mono (the join; trivialization is expected but unproved);
  - T_univ (trivial; Prop. E).
- h is any readout of a declared E-state variable, common across A by hand.
- T is restricted by SC-1 (causal implementability) and SC-2 (CP-implementability), and must contain the platform's calibrated maps.

**𝒜_Γ(ι, Π, [h], T | H): record families.**
- Definition: {Obs(m) : m ∈ 𝔐_std(ι | H) with this (Π, Z, [h], T)}.
- With H = ∅ this is the set of non-anticipating, positive families on 𝒴^τ indexed by A (grid-level E_univ).
- Each hypothesis in H intersects that set with its SC constraints.

**𝒜_ε(ι | H): image only.** 𝒜_ε := {ε[Γ, T] : (Γ, ([h], T)) jointly admissible}.

**Joint baseline 𝒜(ι | H).**
- It is the fibered set of triples (Π, ([h], T), Γ), each component admissible given the earlier ones.
- The standard couplings (SC-5, SC-7, SC-10) already live inside the fibers. Q4 credits only coupling beyond them.

### 2.4 Definitional relations (never credited)

A relation earns nothing if it is any of the following:
- **D-1.** ε_R = ε[Γ_Π, T_Π], or any algebraic rewriting of it.
- **D-2.** ε_R ≥ 0; ε_R = 0 exactly when the family is T-separable (Theorems A, A-BL, M1); ε_R ≤ 2.
- **D-3.** ε_R ≡ 0 when |A| = 1.
- **D-4.** Monotonicity in T: if T ⊆ T′, then ε^{T′} ≤ ε^{T}.
- **D-5.** Witness bounds with frozen constants (Theorem F, M2, Prop. B), and their consequences for any family.
- **D-6.** Invariance under h ↦ t∘h for t ∈ T.
- **D-7.** Data-processing / garbling identities and invariance-reduction identities (Blackwell plus Lehmann; D5 §3 B).
- **D-8.** The logic of the R1 verdict table.
- **D-9.** The triviality statements: Prop. E, E1, D1, D2; ε^{T_univ} ≡ 0.
- **D-10.** Any statement true for every well-typed tuple (Π, [h], T, Γ) of the instance. This is the tautology test on the definitional space 𝒟(ι).

---

## 3. Success criterion (owner item 2)

### 3.1 Qualifying relation

A relation ℛ(Π, [h], T_Π, Γ_Π) = 0 has zero set Z(ℛ). ε_R appears only through ε[Γ_Π, T_Π]. 𝒦(ι) denotes the card's realized set. ℛ **qualifies** if and only if all six conditions hold.

**Q1 Forced.**
- 𝒦(ι) ⊆ Z(ℛ) for every instance in the declared domain, including holdouts, for every A ∈ 𝔄 and every grid in 𝔗.
- The proof is at theorem grade or evidence grade, as declared.
- ℛ must hold on all of Sol_𝒦, not on a selected subset (FR8).

**Q2 Non-definitional.**
- After substituting ε_R := ε[Γ_Π, T_Π], some well-typed tuple in 𝒟(ι) violates ℛ.
- ℛ is none of D-1…D-10.
- **ℛ restricts the jointly realized (Π, T_Π, Γ_Π) beyond the definition of ε_R.**

**Q3 Non-standard (regime-matched).**
- Take each regime class H on which ℛ is claimed, and each SFP framework F applicable under H.
- For each such pair, the card exhibits a witness model m*_F ∈ 𝔐_F(ι | H) whose operational data violate ℛ.
- The auditor verifies each witness. If an applicable F has no witness, ℛ is RESTATED by F.

**Q4 Coupling (non-independence).**
- Z(ℛ) ∩ 𝒜(ι | H) is not of the form (Z_I × Z_Γ) ∩ 𝒜(ι | H), where Z_I is any interface-side set (Π, [h], T) and Z_Γ is any response-side set (Γ, ε_R).
- **Finite witness: a rectangle.** Exhibit u₁, u₂ (interface side) and Γ₁, Γ₂ such that:
  - (u₁, Γ₁) and (u₂, Γ₂) lie in Z(ℛ);
  - (u₁, Γ₂) and (u₂, Γ₁) lie in 𝒜(ι | H);
  - at least one of (u₁, Γ₂), (u₂, Γ₁) lies outside Z(ℛ).

**Q5 Representation invariance.**
- ℛ is invariant under h ↦ t∘h (t ∈ T_Π), under the declared representation moves of Ξ and C (FR1), and under relabelings of V.
- ℛ depends on Γ only through the per-protocol laws (FR3).

**Q6 Scope.** ℛ is declared SCOPE-Q or SCOPE-G and is consistent with that scope (§6).

### 3.2 Card admissibility (Stage-3 success)

A card is **ADMISSIBLE**, and so eligible for the owner's pick, if and only if:
- **S1** It is well-formed: every item of §13 is present.
- **S2** It passes nonrelocation at paper level: NR-1…NR-7 and RP1, RP4, RP5, RP6 (§5).
- **S3** It has at least one qualifying ℛ. At most two are declared; one is primary.
- **S4 Nontrivial freedom reduction.** The primary ℛ has b(ℛ) ≥ log₂ Q_min at the lock: ≥ 3.32 bits for Q_min = 10 [P]. A relation that fixes only a sign or a zero carries at most 1 bit and fails.
- **S5 Positive compression** (§4).
- **S6 Measurable consequence.** LT-1 is instantiated and admissible (§8).
- **S7 Battery at paper level.**
  - B1, B2, B3, B4, B8 and B9 return their required outcomes.
  - The predicted verdicts for B5 (selectivity) and B6 (differentiation) are declared. They are verified in Stage 4.
- **S8 Assembled-law audit complete** (§10). The primary ℛ is classed DISTINCTIVE.

### 3.3 Card verdicts

- **ADMISSIBLE.**
- **NOT ADMISSIBLE**, with exactly one reason class:
  - RELOCATED;
  - RESTATED;
  - NON-QUALIFYING (no qualifying ℛ);
  - NON-COMPRESSIVE;
  - NOT MEASURABLE;
  - KILLED;
  - UNRESOLVED.
- **UNRESOLVED counts as NOT ADMISSIBLE.** No campaign to resolve it is authorized.

---

## 4. Compression accounting and information price (owner item 3)

### 4.1 Price, in bits, in L₀ (RULES 2)

- **IP-1 Base language.** L₀ consists of finite sets, maps, interventions, conditional response, composition and logic.
  - What is priced: 𝒳, 𝒦, the type of C, the operational embedding, and every constant.
- **IP-2 Free choice.** A free choice costs log₂ of the size of the smallest natural family it was chosen from. The auditor may substitute the larger family actually searched (IP-8).
- **IP-3 Tables count as tables** (SD0). A symbol that stands for a finite table costs its rows. Hand-listed configurations are tables. A rule quantifying uniformly over all instances is not a table.
- **IP-4 Selected invariant.** Choosing an invariant from a family F costs log₂|F|.
- **IP-5 Target-encoding vocabulary.**
  - The RULES list: Hilbert space, orthogonality, quantum set, GPT cone, Born rule, metric.
  - Stage-3 additions:
    - tensor-product / subsystem factorization;
    - time base or causal order, unless earned (FR7);
    - probability weights, unless generated (FR15(b));
    - the locality graph of a Hamiltonian or generator;
    - a symmetry group and its action;
    - conserved charges.
  - Each item is priced at its specification size at the audit instance (as a table, unless uniformly defined from other priced data). Each use is flagged on the scorecard.
  - **Supplying a quantum set, the Born rule or a GPT cone makes every selectivity result RELOCATED** (SD0 firewall).
- **IP-6 Continuous constants: the tuning price.**
  - Cost: log₂(declared range / passing window).
  - The range is declared at card freeze. The default for a dimensionless positive constant is [10⁻³, 10³] on a log scale [P].
  - A constant whose claimed results hold across the whole range costs 1 bit [P].
- **IP-7 Imported standard components.**
  - Priced as log₂ of the size of the SFP menu, plus their constants.
  - **Their consequences are baseline** (SC, B1) and earn nothing.
  - Familiar components are allowed (§10).
- **IP-8 Search disclosure.**
  - log₂(number of candidate laws generated or examined while producing the card, discarded ones included) is charged to the card.
  - log₂(number of frozen cards) is charged at the owner's pick.
  - Non-disclosure discovered later voids the card (KC-10).
- **IP-9 Case splits.**
  - Each branch costs 1 bit plus the price of its condition.
  - Branches keyed to scenario names, party counts, setting counts, dimensions or capacities are **prohibited** (SD0 firewall 3; GRAVEYARD).
- **IP-10 Operational embedding.**
  - The dictionary that maps scenarios, protocols and records into Ξ is priced like any other input.
  - Scenario-specific clauses count as tables.
- **IP-11 Lock-side fits.**
  - A parameter fitted on any data in the lock pipeline costs log₂(range / posterior width).
  - The prediction it enters becomes a fit, not a prediction.

**Price(card)** is the sum of IP-1…IP-11.

### 4.2 Credited freedom reduction

- **FR-1 Lock bits.**
  - For each independent lock observable o of a qualifying ℛ:
    b(o) := log₂( |I_SRB(o)| / max(|I_K(o)|, 2σ_tot(o)) ).
  - I_SRB comes from B1, under regime matching and the same inputs.
  - An observable implied by the others under SC plus ℛ contributes 0.
- **FR-2 Structural bits.**
  - On a finite instance: b_ι(ℛ) := log₂( |𝒜(ι|H)|_φ / |𝒜(ι|H) ∩ Z(ℛ)|_φ ), counting resolution cells of φ.
  - Bits are summed across instances only when the instances' data are mutually independent.
- **FR-3 Selectivity distinctions.**
  - 1 bit [P] for each core B5 distinction (SB-1…SB-9) that the card predicts at freeze and Stage 4 verifies.
  - SB-10 earns 0, because it is automatic for a card that generates laws.
  - Holdout successes are reported separately: they are generalization evidence, not compression.
- **FR-4 Never counted.**
  - Bits on 𝒜_ε as a separate axis.
  - Restrictions implied by SC (these are RECOVERY).
  - Definitional relations.
  - Restrictions that follow from the priced inputs alone. Test: does the restriction hold for every Ξ ∈ 𝒳 consistent with C?
- **FR_credited** = Σ over qualifying ℛ of max(FR-1(ℛ), FR-2(ℛ)), plus FR-3. Taking the max, not the sum, prevents double counting.

### 4.3 Compression verdict

ρ := FR_credited / Price(card).

| Condition | Verdict |
|---|---|
| ρ ≥ ρ_min = 2 [P] and FR_credited − Price > 0 | **COMPRESSIVE** (S5 met) |
| 1 ≤ ρ < 2 | **NON-COMPRESSIVE** (S5 fails) |
| ρ < 1 | **RELOCATED (lookup structure)**, whatever else passes (SD0 §3) |

**Scorecard table (mandatory).** Columns: free choices · imported structures · priced vocabulary · search bits · credited bits by source (FR-1, FR-2, FR-3) · ρ.

The whole accounting is exposed for hostile review. The owner rules on disputes; thresholds are not reopened.

---

## 5. Nonrelocation (owner item 4)

### 5.1 Prohibited inputs

None of these may appear in C, 𝒳, 𝒦 or the embedding.

| ID | Prohibited input |
|---|---|
| NR-1 | **Partition.** Π itself, or any structure from which Π can be decoded (RP1–RP3) |
| NR-2 | **Carrier / environmental identity.** Which state variable is the environment (Z_Π), including the choice of the instantaneous state (R1 §12 item 5) |
| NR-3 | **Interface class.** T, or its calibration |
| NR-4 | **Readout class.** [h] as such. Also: a common-readout axiom; a designated observable list from which h is read off; any protocol-indexed readout clause |
| NR-5 | **Gibbs / FDT structure.** A temperature, a Gibbs or KMS state, detailed balance, an FDT, or a fluctuation-theorem premise |
| NR-6 | **Target relation.** ℛ, or any monotone of it, penalty on it, objective containing it, or selection criterion based on it. Also any presumed sign or monotone identity–response tradeoff (G2-11) |
| NR-7 | **STATE exclusions.** Memory kernels, viscoelastic constitutive laws, crystalline order |

**Consequence.** A violation makes the affected structure RELOCATED. If the primary ℛ uses that structure, the card is NOT ADMISSIBLE.

### 5.2 Relocation probes (executed by the auditor)

**RP1 Symmetric-input probe.**
- On a symmetric instance C_sym, where Aut(C_sym) acts transitively on V (or on the candidate partitions of the declared size), both must hold:
  - Sol_𝒦(C_sym) contains realizations with a persistent, A-stable Π;
  - the set {Π(Ξ)} is invariant under Aut(C_sym) (equivariance).
- If C contains a symmetry-breaking parameter λ, differentiation must persist as λ → 0. Only which side carries which label may follow the sign of λ.
- If the type of C cannot be symmetric, its asymmetric structure is priced and RP2/RP3 apply at full strength.
- **Fail → G-DIFF fails** (Π is driven by the input).

**RP2 Input-decoder probe (Standard Partition Selector panel, SPS).**
- Decoders that read only C, with no access to 𝒦:
  - min-cut, max-cut, spectral bisection and modularity, on any graph or weight structure in C;
  - partitions by conserved charge or symmetry sector;
  - any explicit labeling in C;
  - slow/fast splits by input timescales;
  - heterogeneity-threshold splits;
  - support co-occurrence partitions;
  - for [h]: "most-coupled variable" readouts and declared observable lists.
- **Fail** if any decoder recovers 𝒦's Π (VI_norm ≤ δ_Π) on at least p_dec = 0.5 [P] of the generic-ensemble instances. The verdict is RELOCATED for Π, and G-DIFF fails.

**RP3 Scramble / ablation probe.**
- Replace each priced input component by an independent draw of its type.
- If Π, T_Π or [h] tracks the scrambled component's features, that component carries the structure (NR-1, NR-3, NR-4).

**RP4 Carrier / readout probe.**
- (a) No clause of 𝒦 or of the embedding is indexed by protocol identity, apart from the protocol's action on S.
- (b) The card proves the common-carrier form for every A ∈ 𝔄.
- (c) **E2 test.** Take any instance on which this two-mode configuration can be expressed:
  - one symmetric mode, read by a₀;
  - the symmetric mode plus a skewed mode, read by the driven protocol;
  - an environment law that does not depend on the protocol.

  On that instance, the card's carrier derivation must return FAIL (MODE SELECTION).
- (d) The carrier variable is derived, not defined.

**RP5 Gibbs / FDT probe.**
- (a) Syntactic absence of NR-5 items.
- (b) The derivation of ℛ uses FDT or KMS only where 𝒦 derives it.
- (c) On an instance whose reference state is not KMS: if ℛ's credited content vanishes there, it lived in FDT and earns nothing.

**RP6 Target probe.**
- (a) Syntactic: neither 𝒦 nor C refers to Π, T, [h], Γ, ε or any functional of them. 𝒦 refers only to Ξ and C, in L₀.
- (b) No objective, penalty or selection criterion is monotone in ℛ.
- (c) ℛ holds on all of Sol_𝒦 (FR8).
- (d) No sign or monotonicity is presumed: any sign in ℛ is an output of the derivation.

**RP7 Exclusion audit.** Check for NR-7 items and for scenario-keyed branches (IP-9).

---

## 6. Response-scope declaration (Addition 4)

Each target relation carries exactly one label.

- **SCOPE-Q (quotient-irreducible back-reaction).**
  - ℛ constrains Γ only through T_Π-invariant content: ε_R, its witnesses, or the maximal invariant.
  - It is silent on mean response of every order, on linear back-reaction, and on affine or Gaussian latent change (R1 §7 item 3).
  - Its lock observables are T-invariant. Linear-response data can neither confirm nor refute it.
- **SCOPE-G (response in general).**
  - ℛ concerns response of every kind, linear and mean response included.
  - Its observables are response functionals: susceptibilities, response functions, noise spectra, transport coefficients. **Never ε_R alone**, because ε_R is blind to linear response.
  - B1 applies at full strength, starting with SC-3 (linear FDT), SC-4, SC-7 (imprecision–back-action) and SC-1 (Kramers–Kronig).

**Rules.**
- **RS-1. R1-NULL does not mean "no response".**
  - Claims of the form "ε_R = 0 ⇒ no back-reaction" or "ε_R > 0 ⇒ the environment is nonlinear" are void.
  - The harmonic bath responds and is R1-NULL. The parametric harmonic control escapes both tiers with linear bath dynamics (D5).
  - A relation whose derivation uses such a claim is NON-QUALIFYING.
- **RS-2. No cross-subsidy.** A card with both scopes declares two relations and they are scored separately. One relation's success is never credited to the other.
- **RS-3. Scope sets the battery emphasis.**
  - SCOPE-Q faces B4 first: it must predict ε_R = 0 wherever RH-GAU with linear coupling holds. Then B8.
  - SCOPE-G faces B1 first: SC-3 (linear FDT) and SC-7.
- **RS-4.** A mismatch between a relation's scope and its lock observable voids the lock (CT-16).

---

## 7. The frozen hostile battery

Every card faces every item. The card predicts the outcomes at freeze (CC-7); the auditor executes. **Required** means the card fails the stated gate otherwise.

### B1. SRB: standard response theory with the same inputs

- **Input.** Exactly the data the card's prediction consumes:
  - (Π, Z, [h], T) as the card generates them, treated as supplied;
  - the reference-protocol laws or correlators the card uses;
  - the platform parameters;
  - H(x).
- **Procedure.** Before anything is unsealed, the auditor computes I_SRB(o) for each lock observable from SC-1…SC-12 under regime matching and the hostile default, using frameworks SFP-1…SFP-6.

| Outcome | Verdict |
|---|---|
| I_K ⊇ I_SRB, or \|I_SRB\|/\|I_K\| < Q_min | **RESTATED** (regime restatement: the precedent is BRI1's Tier-1 value, which is a Kubo/FDT quantity) |
| I_K ∩ I_SRB = ∅ under experimentally established hypotheses | **KC-3**, unless this contradiction is the declared lock and is consistent with existing bounds |
| Otherwise | PASS, with b(o) bits |

### B2. NULL-ΠT: the null law that supplies Π and T by hand

- **Definition.**
  - Ξ is any SFP model of the declared operational type.
  - Π, Z, [h] and T are chosen by hand.
  - Γ = Obs.
  - Its realized set is 𝒜(ι | H).
- **Price(NULL-ΠT)** = log₂|𝒜_Π| + log₂|𝒜_T| at the instance + log₂(φ-cells for Γ) + the price of its framework choice.
- **Required.**
  - (i) 𝒦(ι) ⊊ 𝒜(ι | H).
  - (ii) Some qualifying ℛ holds on 𝒦 and fails somewhere on 𝒜 (Q3, Q4).
  - (iii) Two-part code comparison on AI-1 and AI-3: Price(card) plus the residual bits needed to describe the card's realized data must be less than Price(NULL-ΠT) for the same data.
- **Fail →** NON-QUALIFYING or NON-COMPRESSIVE.

### B3. E-B: the mode-selection explanation

- **Procedure.** For every realized Γ, the auditor constructs:
  - the product-latent representation, μ = ⊗_a P_a with h_a = π_a (D1);
  - its causal prefix-tree version (D2).
- **Required.**
  - (i) Every reciprocity statement rests on a carrier derived from 𝒦 (RP4). Otherwise its verdict is NO RECIPROCITY VERDICT and it earns nothing.
  - (ii) The primary ℛ, or the derived carrier, must exclude the E-B twin that has protocol-dependent h_a. A relation satisfied by the E-B twin of every family is record-only (SC-12) and earns no reciprocity credit.
  - (iii) The E2 test of RP4(c).
- **Fail →** the reciprocity component is RELOCATED (carrier supplied) or NON-QUALIFYING.

### B4. Calibration pair: BRI1 Duffing / harmonic twin, plus the parametric harmonic control

**The BRI1 Duffing bath** (record `92dc6bb`).
- N_B oscillators, H₀ = p²/2 + x²/2 + x⁴/4, Gibbs state ∝ e^(−H₀).
- Coupling −ε·q(t)·x_j with ε = N_B^(−1/2).
- Readout F = N_B^(−1/2)·Σ_j x_j(t).
- Protocols: P0 (q ≡ 0) and the frozen ramps P1, P2. Grid τ = (π, 3π/2, 2π).
- Known results:
  - Tier 1: R1-PASS (Theorem C; checked).
  - Rate: liminf N_B·ε_R ≥ |K|·V*/(12·m₂^(3/2)), V* = 0.943578 (Prop. G; external check pending).
  - Tier 2: R1-PASS at evidence grade (odd channel 7/7, even channel 3/3, scaling as 1/N_B).

**The harmonic twin** (the x⁴ term removed): ε_R = 0 at both tiers (≈ 1.3×10⁻¹⁴), while the bath responds through friction.

**The parametric harmonic control** (D5): ε_R > 0 at both tiers, with linear bath dynamics.

**Use.**
- (i) **Consistency.**
  - A card that claims these environments as effective regimes must reproduce their verdicts and values within their grades. A contradiction is KC-5.
  - A card that places them outside its realizable set must say why. This is recorded as a Stage-6 liability: anharmonic and harmonic baths exist.
- (ii) **Zero credit.** Reproducing these values earns nothing (SC-3, SC-9).
- (iii) **Scope** (RS-1, RS-3).

**Grades.** Any verdict that uses Prop. G or Tier 2 inherits "pending external check" or "evidence grade".

### B5. SD0 selectivity battery

The full list with required verdicts is in §9.1. It runs in Stage 4. The card predicts all verdicts at freeze.

### B6. Standard differentiation baselines (SFP-7)

- **Mechanisms:**
  - symmetry breaking / Landau theory, with Goldstone and Mermin–Wagner–Hohenberg;
  - critical phenomena;
  - Turing and other pattern formation;
  - phase separation (Cahn–Hilliard);
  - timescale separation, slow manifolds and Mori–Zwanzig;
  - einselection and quantum Darwinism;
  - Markov blankets and the free-energy principle;
  - conserved-charge sectors;
  - graph decompositions (min-cut, spectral, modularity).
- **Procedure.** On AI-2 and AI-3, test whether:
  - the card's generation of Π is extensionally equal to one of these mechanisms (same Π from the same Ξ data);
  - the claimed differentiation–response coupling is an SC-10 relation.
- **Outcome.**
  - STANDARD-MECHANISM: allowed; it earns no novelty for differentiation, and originality is judged at the assembled level.
  - NOT-STANDARD.
  - If ℛ is an SC-10 relation: RESTATED.

### B7. The D5 comparator panel applied to ℛ (not to ε_R)

- The ten comparators: nonlinear-response diagnostics; non-Markovianity; process tensors; ICP; ICM; Janzing–Schölkopf; MDL; Blackwell–Le Cam; measurement invariance; ε-transducers.
- **Required.** No comparator RESTATES ℛ. DISTINCTIVE needs ℛ to survive every comparator (the D5 §2.3 standard).

### B8. Exogenous and Markov controls (R1 record)

| Control | Recorded value |
|---|---|
| C2-G (Gaussian exogenous) | ε_R = 0 |
| C2-NG (non-Gaussian exogenous) | ε_R = 0 |
| C2-F (colored AR(1)) | ε_R > 0 under E₂±; ε_R = 0 under T_lin |
| C2-F′ (genuinely non-Markov exogenous) | ε_R = 0 |
| M-A (Markov) | ε_R^{T_R1} ≥ 1.915×10⁻² |
| M-A′ (non-Markov) | ε_R ≥ 1.915×10⁻² |
| M-B | ε_R^mono ≥ 7.98×10⁻³ (evidence grade) |

- **Required.** Applied to these as supplied instances, the card's machinery returns the recorded verdicts.
- Any relation linking ε_R to Markovianity must respect D5's four occupied cells. Only D5's one-way links are allowed:
  - Markovianity that differs across protocols ⇒ ε_R^mono > 0;
  - ε_R^mono > 0 ⇒ restricted process-tensor non-Markovianity.

### B9. Information nulls

| Null | What it tests | Consequence |
|---|---|---|
| B9a Lookup law: "Ξ is one of the listed realizations" | Its price equals the table | The card must beat it (ρ) |
| B9b Definitional law: content = the R1 definitions and verdict table | — | Credited 0 |
| B9c Maximal-interface null: T_Π ⊇ T_univ, or the join until it is proved non-trivial | ε ≡ 0 | ε-relations are vacuous |
| B9d Single-protocol or hand-picked repertoire null | Relation holds only for \|A\| = 1 or for a listed A | It is a table |
| B9e Sign-only null | Relation fixes only the sign or zero-ness of ε_R | ≤ 1 bit, and SC-12 explains it; fails S4 |

---

## 8. Measurable consequence and the named lock target LT-1 (Stage-5 specification)

**LT-1: the Interface–Response Residual (IRR) lock.**

The card's primary qualifying ℛ is evaluated on a physically realized environment with a certified carrier. ℛ predicts a lock observable O_ℛ:
- from interface-side quantities measured independently: the persistence and A-stability statistic of Π, the T_Π tier verdicts under T_R1 and T_mono, and the carrier certification;
- or from response-side data on a protocol subset disjoint from the one used to evaluate O_ℛ.

No parameter is fitted on lock data. **The quantity locked is the SRB residual:** the part of the prediction that B1, given the same inputs, leaves free.

**Rules.**
- **MC-1 Observable type matches scope (§6).**
  - SCOPE-Q: T-invariant, measured with the frozen d_op at a frozen tier (T_R1 or T_mono), or through a witness with a frozen constant (Theorem F; M2).
  - SCOPE-G: a response functional.
- **MC-2 Independence.** At least one input to the prediction is an interface-side measurement made independently of the record laws used to compute O_ℛ. Because ε_R is derived, a lock that predicts ε_R from the same Γ is definitional.
- **MC-3 Prediction.** I_K is stated at card freeze, with all uncertainties propagated, including the truncation error of an evidence-grade derivation.
- **MC-4 Baseline and discrimination.**
  - The auditor computes I_SRB before unsealing.
  - |I_SRB| / |I_K| ≥ Q_min = 10 [P].
  - Locks that test only a sign are inadmissible.
- **MC-5 Thresholds.**
  - **LOCK-FALSIFIED** when dist(O_meas, I_K) > 3σ_tot [P].
  - **LOCK-CONFIRMED** when dist(O_meas, I_K) ≤ 2σ_tot [P], σ_tot ≤ |I_K|/4 [P], and MC-4 holds.
  - **LOCK-INCONCLUSIVE** otherwise.
  - σ_tot is statistical uncertainty combined with preregistered systematics. The systematics include the residuals of the carrier certificate, e.g. residual interface curvature 3σ·|φ″_res/φ′| below the witness.
  - Nothing changes after unsealing: no threshold, observable, tier, protocol set, grid, estimator or exclusion rule. Any change makes the lock **LOCK-VOID, which counts as LOCK-FALSIFIED** (CT-18).
- **MC-6 Carrier certification.**
  - The platform must pass the R1 10-item checklist (adopted here).
  - If it fails, the verdict is NO RECIPROCITY VERDICT, i.e. LOCK-INCONCLUSIVE.
  - One preregistered alternate platform is allowed. There is no third attempt.
- **MC-7 Power and feasibility.**
  - The design must have power ≥ 0.8 [P] at α = 0.0027 to return LOCK-FALSIFIED whenever O lies in I_SRB at distance ≥ |I_K| from I_K.
  - Effective sample size must fit within ≤ 30 days of platform time [P], or ≤ 10¹⁰ effective samples for an in-silico lock [P].
  - Reference: BRI1's Tier-1 single-time witness at N_B = 4 needs about 10¹¹ samples. That design would be inadmissible in silico.
  - Estimation uses per-witness forms, not plug-in d_BL (R1 §7 item 4). **R1's D4 is not a prerequisite.**
- **MC-8 Sealing.**
  - **LOCK-H:** existing experimental datasets, chosen after card freeze by an independent selector under the SD0 holdout protocol adapted to datasets. The designer is blind to them. At least one dataset per lock observable.
  - **LOCK-E:** a new experiment, with its protocol committed before any data.
  - **In-silico locks are evidence grade only and never confer PREDICTIVE.**
- **MC-9 Multiplicity.** At most 2 relations per card. With two lock observables, thresholds are Bonferroni-adjusted.
- **MC-10 Status.**
  - LOCK-CONFIRMED on sealed real data, plus an external check → PREDICTIVE.
  - LOCK-FALSIFIED → KC-8.

**Admissible platform classes for LT-1.** The card chooses one at freeze; certification follows MC-6.
- P-1: classical mechanical or stochastic environments with independently calibrated readouts.
- P-2: mesoscopic electronic environments with calibrated higher-cumulant (counting-statistics) detection.
- P-3: engineered quantum environments with calibrated input–output readout.
- P-4: archived datasets that meet MC-6 (LOCK-H only).

Listing a class is not a claim that any relation is testable there.

---

## 9. Stage-4 gates (frozen now)

### 9.1 G-SEL: selectivity (B5)

**Operational embedding.**
- The card maps every finite scenario Σ = (X, 𝒞, E) into Ξ-instances. Parties are generated blocks of Π; settings are protocols; outcomes are records.
- The admitted support family is 𝔖_𝒦(Σ) := {supp Γ : Ξ ∈ Sol_𝒦(embed(Σ))}.
- **ALLOW** means the card exhibits, or proves the existence of, a realization with exactly that support. **FORBID** means it proves no realization exists.
- If the card cannot embed Bell scenarios, G-SEL is UNRESOLVED, i.e. FAIL.

| ID | Instance (SD0 record) | Required verdict |
|---|---|---|
| SB-0 | Nonvacuity: ∅ ≠ Sol ⊊ 𝒳 on every instance | — |
| SB-1 | The 1721 possibilistically local (2,2,2) tables | ALLOW all |
| SB-2 | Hardy (SD-K2) | ALLOW |
| SB-3 | The 8 PR boxes | FORBID all |
| SB-4 | GHZ (3,2,2) | ALLOW |
| SB-5 | Peres–Mermin square | ALLOW |
| SB-6 | The CHTW 3×3 KS game over the certified 94-ray / 67-triad core | ALLOW |
| SB-7 | The SD-K7(i) family as frozen: PR ×8, the 480 strong XOR-(2,3,2) tables, embedded PR, fine-grained PR | FORBID all |
| SB-8 | Qubit vs gbit (both capacity 2) | Distinguished, and **not** by capacity, dimension, party count or setting count |
| SB-9 | Closure: convex mixing of whole admitted families; independent products (Hardy×GHZ admitted, PR×PR forbidden) | Respected |
| SB-10 | The 240 non-realizable logical pNS (2,2,2) tables | Not admitted as exact supports |
| SB-11 | Theta parity system: {p,q,r} even, {p,q,s} even, {r,s} odd | FORBID |
| SB-12 | Padded-PR (2,2,3) | FORBID |
| SB-13 | G1 GHZ(4,2,2) and H2 Mermin pentagram: ALLOW. H1 C7 anticorrelation box: FORBID | As stated |
| SB-14 | K7(ii): audit against the POVM-inclusive BMT boundary | Recorded; UNRESOLVED is allowed for a dimension-blind card |
| SB-H | At least 3 new blind holdouts (selector after freeze; excludes everything above and the whole (2,2,2) scenario) | The literature status |

**Grading.**
- **SELECTIVE-EXACT:** SB-0…SB-13 all pass.
- **SELECTIVE-OUTER:** SB-0…SB-10 pass, with over-allowance somewhere in SB-11…SB-13. This is recorded as an outer approximation and is **never upgraded to exact** (FR9).
- **NON-SELECTIVE:** any failure in SB-0…SB-10.
- **Over-forbidding** an experimentally realized support among SB-1, SB-2, SB-4 and SB-5 (realization status verified at evaluation) is **KC-4**.
- Over-forbidding quantum-theoretic supports that have not been realized is NON-SELECTIVE, plus a flag that the Stage-6 quantum regime fails.

**G-SEL PASS** requires at least SELECTIVE-OUTER.

### 9.2 G-DIFF: differentiation

- **D-a Existence.**
  - On AI-2 (RP1), and
  - on at least 1/2 [P] of AI-3 instances,

  some realization has a persistent, A-stable Π.
- **D-b Robustness.** It persists under every perturbation of C of size ≤ ε_C (declared). It is an open phenomenon, not a tuned one.
- **D-c Generation.** T_Π is generated and the carrier is derived (RP4).
- **D-d Not decodable from inputs** (RP2, RP3).
- **D-e** The B6 classification is recorded.

**G-DIFF PASS** requires D-a through D-d.

### 9.3 G-NONREL: nonrelocation, computationally

RP1–RP7 are executed computationally on AI-1…AI-5, holdouts included. **PASS** if no prohibited structure is detected.

### 9.4 Consistency-only clause and decidability (trajectory risk)

**Consistency-only laws.** Suppose 𝒦's restriction is a conjunction of local consistency conditions, detectable by bounded-width propagation. Then:
- (i) its selectivity verdicts are credited as **KNOWN SECTOR** (operator assignments and bounded-width CSPs: Atserias–Kolaitis–Severini; Bulatov–Živný), not as novelty;
- (ii) it cannot produce values of ε_R without a weight rule within supports (FR15(b)). That weight rule is then the actual law, and it is priced and judged as such. Without it, S6 fails;
- (iii) its quantum claims are capped at SELECTIVE-OUTER. This follows the SD0 map: strong contextuality that local consistency can see is non-quantum, and quantum strong contextuality lies where it cannot see.

**Decidability.**
- Every card supplies a decision procedure for its battery verdicts on the finite battery instances.
- No card claims exactness beyond the battery: there is a possible undecidability boundary for exact quantum support families (Slofstra-type results; the SD0 audit that was never run), and FR9 applies.

---

## 10. Originality and the assembled-law audit (owner item 7)

**10.1 Rule.**
- Familiar component theories are allowed and expected. They are neither penalized nor credited.
- Novelty is judged **only at the assembled-law level**: on the qualifying relation(s) and on the realized joint set.
- The consequences of components are baseline (IP-7).

**10.2 Standard Framework Panel (SFP).** These are the comparators for Q3, B1, B6 and the audit.

| ID | Frameworks |
|---|---|
| SFP-1 | Linear and nonlinear response theory: Kubo; higher-order FDRs; Kramers–Kronig; sum rules |
| SFP-2 | Equilibrium and non-equilibrium statistical mechanics: KMS, FDT; fluctuation theorems (Jarzynski, Crooks, Bochkov–Kuzovlev, Evans–Searles, Gallavotti–Cohen); NESS response; stochastic thermodynamics; typicality and ETH |
| SFP-3 | Onsager–Casimir and nonlinear reciprocity |
| SFP-4 | Projection operators / GLE: Mori–Zwanzig; Ford–Kac–Mazur; Caldeira–Leggett; Feynman–Vernon |
| SFP-5 | Open quantum systems and measurement: GKSL, Davies, Redfield, process tensors, input–output theory, quantum regression, SQL / imprecision–back-action |
| SFP-6 | Dissipative field theory: Schwinger–Keldysh EFT with dynamical KMS symmetry; MSR / Janssen–De Dominicis; GENERIC |
| SFP-7 | The differentiation mechanisms listed under B6 |
| SFP-8 | The ten D5 comparators |
| SFP-9 | Selectivity comparators: the Abramsky–Brandenburger hierarchy and AvN; KS sets; Local Orthogonality; quantum reconstructions (Hardy; Chiribella–D'Ariano–Perinotti; Masanes–Müller); JGBB polygons and boxworld; operator-assignment / bounded-width CSPs; decidability bounds |
| SFP-10 | Constructor theory (the "CT-restated" line is in GRAVEYARD) |

Citations are bibliographic. Each load-bearing citation must be verified against its primary text before freeze (RULES 5). None of them grants credit.

**10.3 Audit categories** (preregistered; D5 template; mathematics (M) and physical relation (P) classified separately).
- **RESTATED.**
- **STANDARD COMPONENTS, NEW ASSEMBLY:** no relation beyond the components. This does **not** meet "not independently imposed".
- **DISTINCTIVE:** one concrete relation that survives every applicable SFP item.

S8 requires DISTINCTIVE for the primary ℛ.

**10.4 Procedure.**
- Per comparator family: an analyst and a skeptic. The skeptic argues RESTATED. The more conservative verdict governs.
- **The audit must be complete before the owner's pick.** No partial audit (the SD0 terminal hinged on a 1/5 audit).

**10.5 Graveyard: killed ideas do not return.** A card whose discriminator or relation is extensionally equivalent to a GRAVEYARD item is **KC-7**. The relevant items:
- capacity or dimension counting;
- party count;
- "forbid strong contextuality" as a blanket rule;
- the ASP-as-new-law reading;
- pairwise / sub-cover locality and cohomology classes as support laws;
- support determination as a standalone campaign;
- the maximal interface class T;
- a "latent dimension ≤ k" commitment;
- the CT-parallel embedding.

---

## 11. Cross-sector gold standard: parameter transfer (owner item 8)

**11.1 Sector.** A sector is σ = (platform class, regime hypotheses H_σ, standard effective description F_σ ∈ SFP, observable set O_σ, dataset D_σ).

**11.2 Independence.** Sectors A and B are independent only if all four hold.
- **SI-1 Data.** The datasets are disjoint, with frozen hashes. No datum of B is used to fix anything in A.
- **SI-2 Physics.** No physical degree of freedom, sample or apparatus is shared, apart from generic calibration standards (clocks, thermometers). F_A and F_B share no free parameter that standard physics would fit jointly.
- **SI-3 No standard bridge.**
  - The Standard Bridge Panel, applied to A's data together with B's standard parameters, must give an interval for B's observable at least Q_min = 10× [P] wider than the transfer prediction.
  - The panel: FDT/KMS; Onsager; Kramers–Kronig and sum rules; dimensional analysis with universality and scaling; symmetry and Ward identities; conservation laws; ensemble equivalence; Mori–Zwanzig coarse-graining; EFT matching; CLT / large-N.
- **SI-4 Not a replication.** B is not A at another value of a control parameter within the same H and the same F_σ (the same Hamiltonian class or universality class).

**SI-5.** For the **North-Star lock** specifically, A and B must also be different regimes among {quantum, thermodynamic, gravitational}. Analogy and shared vocabulary never count (RULES 3).

**11.3 Parameter ledger.**

| Symbol | Meaning |
|---|---|
| θ_K | Constants of the law |
| θ_dict | Dictionary constants mapping 𝒦's structures to sector observables |
| θ_std,σ | Standard parameters of sector σ, measured by standard calibration that does not use the target observable |
| θ_cal | Calibration of the ε machinery |

The **GRUT-specific parameters** are θ_K, θ_dict, and every discrete choice.

**11.4 Transfer protocol.**
1. Fix θ_K and θ_dict on D_A alone, and freeze them by hash.
2. Measure θ_std,B independently, and freeze it by hash before B's target data are unsealed.
3. Predict o ∈ O_B under the §8 rules.
4. Do not refit anything.

**11.5 What counts as a GRUT-specific fit in B (prohibited).**
- Adjusting any θ_K or θ_dict on any B data.
- Introducing any new constant.
- Making any discrete choice after B's data are accessible, for example:
  - the T tier;
  - which generated Π to use, unless 𝒦 itself selects it;
  - the scope;
  - the protocol subset, the grid or time window, or the coarse-graining level;
  - the carrier variable or the readout representative;
  - the estimator or the exclusion rules.
- Every such choice costs log₂(number of options) bits and turns the prediction into a fit.

**11.6 Transfer degree.** n_B − d_B ≥ 1, where n_B is the number of independent B observables predicted and d_B is the number of GRUT-specific degrees of freedom adjusted in B. The **gold standard is d_B = 0**.

**11.7 Status.**
- **CROSS-SECTOR** requires SI-1 through SI-4, LOCK-CONFIRMED in B on sealed real data, and an external check (RULES 8).
- In Stage 3, cards only *declare* a transfer plan (CC-11).

**11.8 Stage-6 export.**
- The same ε_R, with the same quotient and the same distance, is exported to a gravitational ensemble.
- Local back-reaction data may set θ_cal only. They count toward θ_K only if they qualify as sector-A data under SI-1–SI-4.
- 𝒦 is unmodified. Any change makes a new card, and the budget is spent (§12).

---

## 12. Budget and distinctness (owner item 5)

- **BU-1.** At most **three frozen cards** for the entire Stage-3 generative route, Stages 3–5 included.
- **BU-2.** A card is spent when it is frozen (has a SHA), whatever its outcome.
- **BU-3.** Changing a card after its freeze creates a new card, which consumes a slot and must satisfy BU-4. A patch that fails BU-4 is inadmissible: it gets no slot and cannot be submitted.
- **BU-4 Genuine distinctness of two cards.**
  - **GD-1 Extensional.** Their realized sets differ on at least one AI-1, AI-2 or AI-4 instance.
  - **GD-2 Not a variant.** Neither card comes from the other by changing declared free choices, constants or ladder positions, or by adding or removing clauses worth ≤ 4 bits in total [P].
  - **GD-3 Mechanism.** Their primary relations differ, or their generation of Π differs on the symmetric-input probe.
  - **GD-4 Not a patch.** A card designed after reading another card's evaluation must disclose that. Clauses that address the other card's recorded failures count toward GD-2.
- **BU-5 Sequencing.**
  - Each card is frozen before it is evaluated.
  - The owner picks among the ADMISSIBLE cards once all are evaluated, or once the designer declares there will be no more cards.
  - If the picked card fails Stage 4 or 5, the owner may pick another remaining ADMISSIBLE card, unmodified.
- **BU-6.** The owner's pick costs log₂(number of cards) bits (IP-8).

---

## 13. Required contents of every card (owner item 6)

| ID | Content |
|---|---|
| CC-1 | **Exact law.** 𝒳; the type of C with its meaning (FR11); 𝒦 in L₀ plus any priced vocabulary; the notion of solution; decidability on finite instances; a frozen reference implementation |
| CC-2 | **Information price table** (§4), including search disclosure |
| CC-3 | **Generated structures.** Uniform definitions of Π, Z_Π, [h]_{T_Π}, T_Π, Γ_Π and ε_R. The persistence and A-stability claims. Where T_Π sits in L_T. The carrier derivation. A grade for each |
| CC-4 | **Target relations** (at most 2, one primary). Statement; evidence for Q1–Q6, including the per-framework witnesses m*_F and the rectangle witness; the derivation 𝒦 ⇒ ℛ with its grade |
| CC-5 | **Response scope** of each relation (§6) |
| CC-6 | **Measurable target.** The LT-1 instantiation: observable, platform class, A, tier, I_K, σ budget, power, sealing route |
| CC-7 | **Hostile baseline comparison.** The predicted outcome of each of B1–B9, and a self-assessment against RP1–RP7 |
| CC-8 | **Kill conditions.** Acknowledgement of KC-1…KC-10, plus at least one card-specific *observable* kill condition with its threshold, plus at least one *structural* kill condition (a stated result whose failure kills the derivation) |
| CC-9 | **Selectivity.** The operational embedding (with the compatibility scope declared, FR6) and every SB verdict |
| CC-10 | **Audit instances.** AI-1 to AI-4 instantiated; the chart φ with ranges and resolution |
| CC-11 | **Transfer plan** (§11): the θ ledger, the sector pair, and the transfer observable. A declaration only |
| CC-12 | **FR1–FR15 compliance table** (§17) |
| CC-13 | **Provenance.** How the card was produced; the number of alternatives considered; what earlier evaluations the designer had seen |
| CC-14 | **Distinctness** from the frozen cards (BU-4) |
| CC-15 | **Dependency labels** on pending R1 items (§16) |
| CC-16 | **Regime map.** H(x) for every realization class on which a relation is claimed |

---

## 14. Kill conditions

**Charter-level kills.** These apply automatically to every card.

| ID | Kill condition |
|---|---|
| KC-1 | **Causality violation:** signalling from later protocol segments into earlier records; superluminal signalling between blocks in a spatial embedding; violation of pNS in Bell embeddings |
| KC-2 | **Positivity violation:** negative probabilities; record transformations that are not CP; negative spectral densities; negative entropy production under RH-TH |
| KC-3 | **Contradiction of an experimentally established standard relation within its tested domain** (FDT/KMS in equilibrium, Onsager–Casimir near equilibrium, energy–momentum conservation, the second law). The only exception: the contradiction is the declared primary lock and is consistent with existing experimental bounds cited at freeze |
| KC-4 | **Over-forbidding an experimentally realized support** in B5 |
| KC-5 | **Contradicting the calibration pair** (B4) while claiming those environments as realizable regimes |
| KC-6 | **Vacuity:** Sol_𝒦 is empty on a declared-domain instance, or equals all of 𝒳 |
| KC-7 | **Return of a GRAVEYARD item** (§10.5) |
| KC-8 | **LT-1 falsified** at the preregistered threshold, including LOCK-VOID |
| KC-9 | **A card-specific kill condition fires** |
| KC-10 | **Undisclosed search, or modification after freeze** (the card is void) |

**No rescue.** Once a kill fires, the card is not repaired. A changed card is a new card (BU-3).

---

## 15. Stopping rule and anti-staircase (owner item 9)

**Route terminals.**
- **ROUTE-OPEN.** The owner picks an ADMISSIBLE card, and the route proceeds to Stage 4, then Stage 5.
- **ROUTE-TERMINATED.** Either none of the at most three cards is ADMISSIBLE, or every ADMISSIBLE card that was picked fails Stage 4 or Stage 5.
  - Each card's reason class is recorded in GRAVEYARD, once the external check required by RULES 8 is in.
  - The scoreboard changes only for banked byproducts. Example: a COMPRESSIVE known-sector result, as with SD0's #6. Byproducts do not continue the route.

**Prohibited after termination, and at any time as a "prerequisite".**
- (i) Any further card ("Card 4").
- (ii) Relaxing any threshold, battery item, baseline rule or verdict criterion.
- (iii) Any campaign to supply a "missing ingredient" for a future card. Examples: deriving T, the weights, temporality, the carrier, or Gibbs structure.
- (iv) Reopening R1: no new T class, no change to d_op, no change to the verdict table. The ladder is closed (G2-10).
- (v) Relabeling a failed card's relation as "future work" that opens a new stage.

**Reopening.** It requires a new owner ruling that is explicitly not a continuation of this route (RULES 4).

**Non-blocking items.** The open R1 upgrades (M5, D4, carrier necessity at Tier 2, trivialization of the join, external checks) continue as housekeeping.
- They are **never prerequisites**.
- A verdict that depends on one of them is labeled "conditional on ⟨item⟩" and proceeds.

---

## 16. Provenance, grades and statuses (Addition 1)

- **PV-1. A merge is provenance, not endorsement.** Merging `grut2` into `main`, and merging this charter, changes no status.
- **PV-2. Pending items keep their status.** Every DERIVED item marked "external check pending" keeps that status and its pending CHECKS line: A-BL, F, M1–M3, Prop. G, and the D5 analyses C1–C6 and D1–D3.
- **PV-3. Dependency labels.** A card verdict that uses a pending or evidence-grade item carries that item's label. Examples: B4 rate comparisons (Prop. G); Tier-2 consistency (evidence grade); M1-based zero sets (pending).
- **PV-4. Banking.** Nothing is banked until its CHECKS line shows an external check with no open issue (RULES 8). That includes this charter's freeze commit, which receives a pending CHECKS line.
- **PV-5. Scoreboard mapping** (each after external check):

| Outcome | Status |
|---|---|
| Card frozen and ADMISSIBLE | COMMITMENT (priced) |
| 𝒦 ⇒ ℛ proved | DERIVED (theorem grade), or DERIVED — evidence grade |
| S5 met | COMPRESSIVE |
| LOCK-CONFIRMED on sealed real data | PREDICTIVE |
| Transfer confirmed (§11) | CROSS-SECTOR |
| NR violation or lookup | RELOCATED |
| Restated by B1, B7 or the SFP | RESTATED |
| Kill | GRAVEYARD entry |

---

## 17. FR1–FR15 binding map

| FR | Form in Stage 3 | Type |
|---|---|---|
| FR1 Representation invariance | Q5. No invariance is claimed beyond the declared moves | GATE |
| FR2 Gluing without automatic access | Composing Ξ-instances (products in SB-9, multi-block embeddings) is an explicit act of 𝒦, declared | DECLARATION; gate via SB-9 |
| FR3 No inaccessible-context data | Only per-protocol laws; no joint laws across protocols | GATE (Q5) |
| FR4 Observer independence | No observer-relative clause; modal or counterfactual framing does not count | GATE |
| FR5 No supplied split without pricing | Strengthened to NR-1: Π may not be supplied at all if differentiation credit is claimed | GATE |
| FR6 Scope of compatibility | The B5 embedding declares its compatibility notion | DECLARATION |
| FR7 Temporality must be earned | Time base and causal order are priced unless generated (IP-5) | DECLARATION + price |
| FR8 Constraint ≠ selection | RP6(c) and Q1: ℛ holds on all of Sol_𝒦 | GATE |
| FR9 No outer→exact upgrade | G-SEL grading; §9.4 | GATE |
| FR10 Information price | §4 | GATE |
| FR11 F0-PHYS gate (declared meaning of C) | CC-1: C's meaning is declared and priced | GATE |
| FR12 Conventions | Declared | DECLARATION |
| FR13 Deeper Γ object | Γ_Π is generated as Obs_Π(Ξ). A card that supplies Γ as an empirical model cannot claim generated response | GATE |
| FR14 Subsidiary possibility facts | Dependency declared | DECLARATION |
| FR15 G0 trichotomy | Landing declared. Cards must address weights within supports (b), because ε_R values need laws | GATE |

---

## 18. Non-credit register (consolidated)

The following earn no credit:
- **Definitional relations:** D-1…D-10. This includes any bits counted on 𝒜_ε as an axis.
- **Standard-theory consequences under regime matching:** SC-1…SC-12. Specifically:
  - causality and Kramers–Kronig; positivity, CP and uncertainty bounds;
  - KMS, linear and nonlinear FDRs, fluctuation theorems, Gaussian-bath completeness;
  - Onsager–Casimir; conservation, sum rules, selection rules, action–reaction;
  - Mori–Zwanzig / GLE memory; GKSL, input–output, imprecision–back-action and SQL;
  - the second law and stability; large-N scaling; SSB, critical and pattern relations;
  - representation freedom; E_univ.
- **RECOVERY** of standard structure (Gibbs states, thermalization, memory) derived from 𝒦. It counts toward Stage 6, not toward Stage-3 freedom reduction.
- **The BRI1 Tier-1 value** and its 1/N_B rate, **the harmonic R1-NULL**, and the C2 and M controls. These are calibration only.
- **Consequences of the priced inputs alone.**
- **Selectivity verdicts reached through bounded-width consistency** (KNOWN SECTOR), and over-allowances reported as exact.
- **Relations satisfied by the E-B twin** (record-only), and any back-reaction claim made without a derived carrier.
- **Relations that only fix a sign; relations that hold on a single protocol or a hand-picked repertoire; relations that depend on a representative.**
- **Novelty of components;** STANDARD COMPONENTS, NEW ASSEMBLY.
- **Holdout results** as compression (they are reported separately).
- **In-silico locks** as PREDICTIVE.
- **Same-regime replications** as CROSS-SECTOR.

---

## 19. CHARTER TESTS (red-team gaming patterns) and charter self-tests

### 19.1 CHARTER TESTS

These are abstract patterns only, not physical proposals. Each must be caught by the rule listed.

| ID | CHARTER TEST pattern (abstract) | Caught by | Required verdict |
|---|---|---|---|
| CT-01 | **CHARTER TEST:** the input partition already encodes Π (a weighted structure in C whose cut or community equals Π) | RP2, RP3, NR-1 | RELOCATED; G-DIFF FAIL |
| CT-02 | **CHARTER TEST:** the carrier is stated as an axiom (a clause equivalent to "one readout for all protocols") | NR-2, NR-4, RP4 | RELOCATED |
| CT-03 | **CHARTER TEST:** admissible states restricted to Gibbs/KMS/detailed-balanced states, or a temperature among the inputs | NR-5, RP5 | RELOCATED; any FDT consequence earns 0 |
| CT-04 | **CHARTER TEST:** the target relation enters as an objective or penalty of an extremum principle | NR-6, RP6 | RELOCATED |
| CT-05 | **CHARTER TEST:** ℛ is ε_R − ε[Γ, T] = 0 rewritten, or a consequence of Theorems A, A-BL, F or M1 | Q2, §2.4 | NON-QUALIFYING |
| CT-06 | **CHARTER TEST:** ℛ holds because \|A\| = 1, or only for a listed repertoire | Q1 (uniformity over 𝔄), B9d | NON-QUALIFYING |
| CT-07 | **CHARTER TEST:** ℛ = ℛ_I(Π, T) ∧ ℛ_Γ(Γ), presented as a coupling | Q4 rectangle test | NON-QUALIFYING |
| CT-08 | **CHARTER TEST:** ℛ holds for one representative h but not for the class [h] | Q5 | NON-QUALIFYING |
| CT-09 | **CHARTER TEST:** a linear or nonlinear FDR, fluctuation theorem or Onsager identity rewritten in (Π, T, ε) variables | SC-3, SC-4, B1 | RESTATED |
| CT-10 | **CHARTER TEST:** regime shopping — witnesses m* drawn from a regime other than that of the card's realizations | RM, HD (§2.1) | Witness invalid; Q3 fails |
| CT-11 | **CHARTER TEST:** ℛ holds only in a narrow window of a constant tuned to B4 or B5 | IP-6, IP-11 | Tuning price charged; NON-COMPRESSIVE or RELOCATED |
| CT-12 | **CHARTER TEST:** clauses keyed to protocol identity (h_a in disguise) | RP4(a), B3 | MODE SELECTION; RELOCATED |
| CT-13 | **CHARTER TEST:** selectivity by lookup (scenario name, party or setting count, dimension, capacity) | IP-9, SB-8, KC-7 | RELOCATED or KILLED |
| CT-14 | **CHARTER TEST:** a law that only checks consistency of supports, with no weights | §9.4, S6, FR15 | NOT MEASURABLE; selectivity KNOWN SECTOR |
| CT-15 | **CHARTER TEST:** "ℛ follows once X is derived" (deferral to a prerequisite) | S1, §15 | NOT ADMISSIBLE; no X-campaign |
| CT-16 | **CHARTER TEST:** a SCOPE-Q relation tested on linear-response data, or a SCOPE-G relation tested on ε_R alone | RS-4, MC-1 | LOCK-VOID |
| CT-17 | **CHARTER TEST:** "sector B" is A at another control-parameter value, used B data in the fit, or is linked to A by a standard bridge | SI-1…SI-4 | Not CROSS-SECTOR |
| CT-18 | **CHARTER TEST:** threshold, platform, tier, repertoire or estimator chosen after data access | MC-5, MC-8 | LOCK-VOID = LOCK-FALSIFIED |
| CT-19 | **CHARTER TEST:** many laws generated, the best three submitted, the search not disclosed | IP-8, KC-10 | Card void |
| CT-20 | **CHARTER TEST:** Card n = Card m plus a clause that fixes Card m's recorded failure | GD-2, GD-4, BU-3 | Inadmissible |
| CT-21 | **CHARTER TEST:** a monotone identity–response tradeoff postulated with its sign fixed by hand | NR-6, RP6(d) | RELOCATED |
| CT-22 | **CHARTER TEST:** a vanishing explicit seed in C selects Π, and differentiation is absent at zero seed | RP1 | G-DIFF FAIL |
| CT-23 | **CHARTER TEST:** generated T_Π ⊇ the join or T_univ, so ε ≡ 0 and the relations are vacuous | B9c, §1.3 | NON-QUALIFYING |
| CT-24 | **CHARTER TEST:** the carrier variable declared to be the instantaneous E-state by definition | NR-2, RP4(d) | RELOCATED |
| CT-25 | **CHARTER TEST:** a record-only statement offered as evidence of back-reaction | SC-12, B3 | No reciprocity credit |
| CT-26 | **CHARTER TEST:** the discriminator reduces to capacity or dimension, party count, a blanket ban on strong contextuality, maximal T, or a latent-dimension bound | §10.5 | KC-7 |
| CT-27 | **CHARTER TEST:** ℛ is an N-scaling law of ε_R in a mean-field architecture | SC-9 | RESTATED |
| CT-28 | **CHARTER TEST:** ℛ is "the odd channel vanishes when the reference is symmetric" | SC-5 plus Theorem C | RESTATED |
| CT-29 | **CHARTER TEST:** ℛ uses joint laws across protocols | FR3, Q5 | NON-QUALIFYING |
| CT-30 | **CHARTER TEST:** the lock predicts ε_R from the same Γ it is computed on | MC-2 | NOT MEASURABLE (definitional) |

### 19.2 Charter self-tests (must hold at freeze; FZ-5)

These run on known objects. None of them is a candidate.

| ID | Object | Required verdict |
|---|---|---|
| ST-1 | BRI1's Tier-1 ε_R relation, treated as if it were a card | B1: RESTATED (SC-3 nonlinear FDR plus SC-9). As a card it is also RELOCATED: NR-1 through NR-5 (bath, readout, Gibbs state, partition) are all supplied |
| ST-2 | The harmonic R1-NULL | RESTATED (SC-3 / SC-6, Ford–Kac–Mazur) |
| ST-3 | ASP | G-SEL: SB-10 fails (it admits the 240 non-realizable tables) and SB-11/SB-12 over-allow, so NON-SELECTIVE; KNOWN SECTOR (§9.4). As a card: NOT MEASURABLE (no weights; FR15(b)) |
| ST-4 | NULL-ΠT as a card | FR_credited = 0, so ρ < 1 and it is RELOCATED |
| ST-5 | The product-latent E-B model as a card | B3: MODE SELECTION; SC-12: no credit |

---

## 20. Constants fixed at freeze (proposed)

| Symbol | Meaning | Proposed value |
|---|---|---|
| δ_Π | Persistence tolerance (VI_norm) | 0.05 |
| H | Persistence horizon | At least the full protocol and record window of every a ∈ A |
| Q_min | Discrimination and informativeness ratio | 10 (3.32 bits) |
| z_fal | Falsification threshold | 3σ_tot |
| z_conf | Confirmation | Within 2σ_tot, with σ_tot ≤ \|I_K\|/4 |
| Power | Lock design | ≥ 0.8 at α = 0.0027 |
| ρ_min | Compression ratio | 2 (below 1 → RELOCATED) |
| n_ℛ | Relations per card | 2, one of them primary |
| b_patch | Distinctness threshold for patches | 4 bits |
| T_budget | Lock feasibility | ≤ 30 days of platform time; ≤ 10¹⁰ effective samples in silico |
| p_dec | RP2 decoder recovery fraction | 0.5 |
| Default range | Dimensionless positive constants | [10⁻³, 10³] (log scale) |
| SB credit | Per verified core distinction | 1 bit |
| G-DIFF fraction | Generic instances with persistent Π | ≥ 1/2 |
| n_hold | Blind holdouts per battery family | ≥ 3 |
| N_cards | Budget | 3 |

---

## 21. Procedure and STOP

1. **Charter freeze.** Owner review; the constants of §20 are fixed; the self-tests ST-1…ST-5 are run on paper; the charter is committed; its CHECKS line is added as pending. **STOP for owner review before Card 1 (G2-11).**
2. **Cards.** Each card is generated and frozen (SHA plus reference implementation) before it is evaluated. There are at most three (§12).
3. **Evaluation of each card.**
   - Run the S1–S8 checks, the paper-level battery and the assembled-law audit. An independent auditor does this; for the audit, analyst and skeptic.
   - After the card's SHA exists, an independent selector chooses the holdouts (AI-5, SB-H, LOCK-H datasets). The selector receives only the charter and the card's bare input/output signature (the SD0 holdout protocol).
4. **Checkpoint (RULES (d)).** Report the scorecards of all cards, at most five lines each. The **owner picks one** ADMISSIBLE card (log₂(number of cards) bits).
5. **Stage 4.** G-SEL, G-DIFF and G-NONREL, computationally. **Stop and report** (RULES (e)).
6. **Stage 5.** Unseal the LT-1 lock under §8. **Stop and report.**
7. **Termination.** §15 applies whenever its conditions are met.

**This charter is not:** a candidate law, a change to R1, a change to the scoreboard, or an authorization to generate Card 1.