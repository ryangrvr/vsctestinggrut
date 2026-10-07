# OWNER RULINGS (GRUT 2) — append-only log

Each entry records the owner's text verbatim, followed by where it was implemented.
Pre-GRUT-2 rulings stay on their F0 branches (`F0_OWNER_RULING_0X.md`).

---

## G2-01 — T freeze for R1 · 2026-10-07

**Owner text (verbatim):**

> Let me look at the T-ladder note itself before weighing in, since "BRI1 escapes every linear interface: proved" is the load-bearing claim.I checked the ladder note. Theorem C is correct as stated — and the place it's correct is the key to the T decision.
> C2 is clean. All four controls behave as designed, and the scale reporting makes the point vivid: the C2-F signal under signed-affine T is about 55,000 times BRI1's genuine effect. Claude Code is right about the terminology, too: it isn't a "false positive," it's the correct nonzero value for that class. It shows what the class choice does, not a malfunction.
> Theorem C holds, but only because of an assumption that has to become an explicit part of the T commitment. The note defines T_lin as GL(k): invertible linear maps on the observed grid, with nonsingular covariances. With that, the symmetry argument is airtight — an invertible linear map can't turn a symmetric law into a skewed one.
> The catch is what GL(k) silently assumes: that the shared environment has no more independent components than the observed record. Real environments have many modes. If the shared exogenous process is allowed to live in a larger space, and protocols act by linear maps from it onto the observed record, two things follow:
>
> * BRI1's escape can fail physically. Take a two-mode exogenous environment — one symmetric mode, one skewed. If the undriven protocol couples only to the symmetric mode and the driven protocol couples to both, you get a symmetric reference law and a skewed driven law with no back-reaction at all. That's protocol-dependent mode selection, and it's an ordinary physical possibility.
> * With latent dimension unrestricted, linear T is already trivial. Take a latent space made of independent copies of every protocol's observed law, and let each protocol's interface be the projection onto its own copy. Those maps are linear, so every intervention family is absorbed — exactly the universal-exogenous ceiling, reached without any nonlinearity.
>
> So the decision isn't just "linear versus nonlinear." It's also "how many environmental modes can a protocol select from?" Claude Code's recommendation implicitly answers "none — protocols filter a fixed record; they don't choose which modes are read." That's a defensible commitment, but it's the one ε_R's ability to detect back-reaction actually rests on, and it limits where the measure applies: an experiment has to establish that its protocols don't change which environmental modes couple. That belongs next to the "nonlinear detector" risk Claude Code already named.
> My recommendation: freeze T as Claude Code proposes, with the latent-dimension condition written in and priced.
> FOR CLAUDE CODE — T freeze (owner decision, recommended)
>
> 1. Freeze T for R1: T = GL(k) on the observed grid (protocol-dependent invertible linear interfaces), with independently calibrated nonlinearities removed by their known maps (not fitted).
> 2. Add the latent-dimension condition explicitly, as a priced commitment: the shared exogenous process lives in the same space as the observed record — protocols act by invertible maps on a fixed record and do not select among additional environmental modes. Physical meaning: protocols change how a fixed environment is filtered, not which environmental modes are read.
> 3. Record two trivializations next to Prop. E:
>    * (a) Latent dimension unrestricted ⇒ linear T is trivial. Construction: a product latent space carrying each protocol's law, with protocol-dependent coordinate projections. Every family is absorbed (the E_univ ceiling reached linearly).
>    * (b) A physical counterexample to Theorem C outside the commitment: a two-mode exogenous environment (one symmetric mode, one skewed) with protocol-dependent mode selection reproduces "symmetric reference, skewed driven" without back-reaction.
> 4. Applicability statement for experiments (Stage R3): a reciprocity claim from ε_R requires calibration showing (i) the interface nonlinearity is known, and (ii) protocols do not change which environmental modes couple. Both go in the D5 comparator audit under "reduces to generic nonlinear response / mode selection."
> 5. Terminology: C2-F is the correct nonzero ε_R under E₂±, and ε_R = 0 under T_lin. Not a false positive.
>
> FOR VS CODE — no change: proceed with the C2 process fixes and C3 per Amendment A, then C4, then WO-002.
> This is a good sign for the program, not a setback. Each step is making precise exactly what has to be true of the world for "this environment responds" to be a measurable statement — and that's the content a reciprocity law would eventually have to earn.

**Implemented in:** the commit listed for rulings G2-01 … G2-08 in `PROGRAM/CHECKS.md`.

---

## G2-02 — R1 decisions (ChatGPT + Claude review) · 2026-10-07

**Owner text (verbatim; the review notes precede the directive block):**

> some notes: This is a good update. The most important result is not the BRI calibration itself; it is that the T-ladder has exposed exactly where reciprocity becomes identifiable and where it becomes representation-dependent.
> My three decisions are:
> \[ \boxed{\textbf{1. ACCEPT THE T FREEZE, BUT REPLACE “LATENT-DIMENSION COMMITMENT.”}} \]\[ \boxed{\textbf{2. USE A BOUNDED PROCESS-LEVEL IPM FOR }d_{\rm op}\textbf{, NOT RAW SKEWNESS/TV.}} \]\[ \boxed{\textbf{3. STAGE 3 SHOULD WAIT FOR WO-002, BUT NOT FOR EVERY POSSIBLE R1 EXTENSION.}} \]
> (Full review text as sent by the owner on 2026-10-07: common carrier \(Y_a=t_a\circ h(Z)\) with one \(h\) for all protocols, \(h\to h_a\) excluded; mode-stability certificate, else NO RECIPROCITY VERDICT; D5 explanations A/B/C; \(d_{\rm op}=d_{\rm BL}\) theoretically, MMD as a calibrated proxy; skewness demoted to analytic calibration witness; bounded odd surrogate \(\tanh[cH_3]\) or \(\operatorname{clip}(H_3/M,-1,1)\); formal Stage 3 waits for WO-002; R1 exit gate of four items; C4 as laboratory preparation; the bridge \(\mathcal K\to\) stable subsystem identity \(\to\) stable interface carrier \(\to T\to\epsilon_R\).)
>
> FOR CLAUDE CODE — R1 decisions (from ChatGPT + Claude review)
>
> 1. T freeze: T = GL(k) on the observed path record, with independently calibrated nonlinearities and filters removed by their known maps or included in T. Replace the "latent-dimension" wording with the common-carrier / mode-stability commitment: arbitrary latent dimension allowed; one common latent-to-record map h for all protocols; protocol-dependent mode selection (h_a) excluded. Note in `R1_T_LADDER.md`: with common h, set W = h(Z); Theorem C then applies verbatim with P★ = Law(W).
> 2. Empirical rule: every reciprocity claim requires a mode-stability certificate; without one the verdict is NO RECIPROCITY VERDICT, not ε_R > 0. D5 must discriminate three explanations: (A) unchanged environment + calibrated interface transformation; (B) unchanged environment + protocol-dependent mode selection; (C) responding environment.
> 3. d_op: bounded-Lipschitz distance on the full finite-grid path law, applied to whitened laws and minimized over rotations (the T_lin maximal invariant). Skewness stays as the analytic BRI calibration witness. MMD only as a frozen-kernel computational proxy, after its connection is shown.
> 4. Witness-to-bound theorem to derive: using central symmetry of the undriven orbit, prove ε_R^(T_lin) ≥ c·|E_{P1}[f_odd]| / ‖f‖_BL for any bounded-Lipschitz f on whitened coordinates, with c explicit. Then show a bounded odd surrogate (e.g., tanh(c·H₃)) has |ΔE f| = C·N_B⁻¹ + o(N_B⁻¹), C ≠ 0, in BRI1. Record why the route fails under T_mono (monotone maps don't commute with negation).
> 5. R1 exit gate: (i) T scope fixed; (ii) WO-002 decides multi-time survival under T_mono, or identifies precisely why it trivializes; (iii) d_op frozen with the proved inequality; (iv) D5 complete including mode selection. Then R1 terminates and Stage 3 opens. C4 continues as laboratory preparation and does not block Stage 3.
> 6. North star addition: "Environment responds" is meaningful only relative to a specified environmental identity across interventions; at the operational level this is the common carrier, and at the fundamental level 𝒦 must generate it.
>
> R1 now has a finite exit, a well-defined distance, and a precise statement of what "the same environment" means. When Claude Code pushes the next piece, send it over and I'll check it against the remote.

**Supersedes:** G2-01 item 2's "latent-dimension" wording, which is replaced by common carrier / mode stability.

---

## G2-03 — handoff check (forwarded review) · 2026-10-07

**Owner text (verbatim excerpt of the rulings and corrections):**

> COMMON-CARRIER FREEZE — ACCEPTED with arbitrary latent dimension and mandatory mode-stability certification.
> BL QUOTIENT METRIC — ACCEPTED IN PRINCIPLE with centering/whitening assumptions stated and the reflection constant re-derived; expect \(c=1\) under the ordinary normalization.
> WO-002 — ADD COPULA FORMULATION because coordinatewise monotone interfaces have a natural maximal invariant at multi-time level.
> STAGE 3 STILL WAITS FOR R1 CLOSEOUT.
>
> Corrections:
> - The bounded-Lipschitz reflection bound probably has \(c=1\), not \(1/2\): \(d(P,R_\#P)\le 2d(P,Q)\) for symmetric \(Q\); for odd \(f\), \(d_{\rm BL}(P,R_\#P)\ge 2|E_Pf|/\|f\|_{\rm BL}\); hence \(d_{\rm BL}(P,Q)\ge|E_Pf|/\|f\|_{\rm BL}\) and \(\epsilon_R^{(T_{\rm lin})}\ge|E_{P_1}f|/\|f\|_{\rm BL}\). "That should be derived rather than hard-coded as 1/2." The normalization must be stated.
> - Whitening requires a finite, nonsingular covariance on the observed record (if singular: work on the support subspace or define the quotient there). With translations in the class, the canonical reduction is centering + whitening, leaving an orthogonal quotient.
> - The rotation issue is manageable; the theorem uses the symmetry of the entire null orbit, not invariance of the witness.
> - WO-002: "Determine whether \(T_{\rm mono}\) is exactly coordinatewise monotone. If yes, formulate the null in copula space and test whether the BRI1 protocols have identical copulas after marginal standardization. Prove equivalence where regularity assumptions permit. Treat the archived low-order multi-time cumulant/correlation channels as witnesses of copula difference, not as the definition." Caveats: discrete variables need generalized copulas; non-strict transformations destroy information; path-dependent nonlinear filters are not covered by the copula argument.

**Implemented in:** the commit listed for rulings G2-01 … G2-08 in `PROGRAM/CHECKS.md`.

---

## G2-04 — R1 update (ChatGPT + Claude review) · 2026-10-07

**Owner text (verbatim):**

> ChatGPT's corrections are mostly right, the copula idea is excellent, and putting the two together gives WO-002 a clean theorem target. One correction goes back the other way, though.
> 1. The constant: both are right, about different quantities. The reflection step is exactly as ChatGPT shows — the two factors of 2 cancel, so the distance from the driven law to the symmetric orbit is at least |E f|/‖f‖_BL, with constant 1. But ε_R isn't that distance. In ε_R, the shared process P★ has to approximate both protocols at once, and it can split the error between them. That gives Theorem A's factor: ε_R ≥ ½ × (quotient distance between the two protocols' orbits). Chaining the two:
> ε_R ≥ ½ · |E_{P1}[f_odd]| / ‖f‖_BL (constant 1 for the orbit distance, ½ for ε_R).
> ChatGPT's main point stands, though: the constant should be derived and the normalization stated, not hard-coded.
> Conceded: with translations in the class, the reduction is centering plus whitening, leaving a rotation quotient — and nonsingular covariance (or restriction to its support) needs to be an explicit assumption.
> 2. Copulas are the right object for T_mono — and they unify the two channels. Coordinatewise strictly monotone maps can change the marginals arbitrarily but leave the copula unchanged (decreasing maps reflect coordinates of it). That explains D1 immediately: at a single time the copula is trivial, so nothing survives. And it turns WO-002 from exploration into a theorem, because Theorem C has an exact copula analog:
>
> * If the undriven law is centrally symmetric, its copula is radially symmetric (the vector of uniform scores has the same law as one minus itself).
> * Radial symmetry of a copula is preserved by every coordinatewise monotone map, increasing or decreasing.
> * So under the null, the shared copula is radially symmetric, and therefore so is the driven protocol's.
> * So BRI1 escapes T_mono if its driven copula is radially asymmetric — exactly parallel to Theorem C.
>
> This also shows what Claude Code's two "channels" actually are. At leading order (near-Gaussian, small non-Gaussianity), a copula difference splits into:
>
> * a correlation-change part — the Gaussian-copula piece, where the copulas differ but both are radially symmetric; and
> * a third-order part — the third-cumulant tensor modulo what per-coordinate quadratic deformations x → x + a(x² − 1) can generate. Each coordinate gets one such deformation, so the surviving part has dimension (number of third-cumulant components) − k = C(k+2, 3) − k.
>
> For k = 1 that's 1 − 1 = 0, which is D1 again. For k = 2 it's 4 − 2 = 2, so two genuinely multi-time components survive. The two channels aren't alternatives to the copula view; they're its leading-order coordinates, and the dimension count says exactly how many independent quantities WO-002 has to check.
> FOR CLAUDE CODE — R1 update (ChatGPT + Claude review)
>
> 1. Freezes accepted: common carrier with arbitrary latent dimension and a mandatory mode-stability certificate; bounded-Lipschitz quotient metric.
> 2. Metric details: canonical reduction is centering + whitening (translations are in the class), leaving an O(k) quotient: d_quot(P, Q) = inf over O ∈ O(k) of d_BL(P̃, O#Q̃). State nonsingular covariance (or support-subspace restriction) explicitly. State the BL normalization.
> 3. Constants — derive, don't hard-code. Expected: distance from the driven law to the symmetric orbit ≥ |E f_odd| / ‖f‖BL (constant 1); ε_R^(T_lin) ≥ ½ · |E{P1} f_odd| / ‖f‖_BL (the ½ from Theorem A's two-protocol split).
> 4. WO-002 reformulated in copula space (if T_mono is exactly coordinatewise strictly monotone, continuous margins):
>    * Theorem C-mono (to prove): a centrally symmetric undriven law has a radially symmetric copula; radial symmetry is invariant under coordinatewise monotone maps (increasing and decreasing); hence radial asymmetry of the driven copula implies ε_R^(T_mono) > 0.
>    * Second route: copula difference within the radially symmetric sector (correlation change) also implies escape.
>    * Leading-order coordinates: the copula difference decomposes into (i) the Gaussian-copula / correlation-change term and (ii) the third-cumulant tensor modulo per-coordinate quadratic deformations, of dimension C(k+2, 3) − k (zero at k = 1, reproducing D1; two at k = 2).
>    * Computation: evaluate both leading-order terms for BRI1 from the archived third-cumulant tensor and covariance; report each surviving component and its N_B scaling.
>    * Caveats to record: discrete variables need generalized copulas; non-strict maps can destroy information; path-dependent nonlinear filters are outside this argument.
> 5. Stage 3 waits for R1 closeout (unchanged).
>
> The progression is now very clean. Each larger interface class has a matching symmetry invariant — odd cumulants for signed-affine maps, central symmetry after whitening for GL(k), radial symmetry of the copula for monotone maps — and BRI1's reference protocol is symmetric at every level. Whether its driven protocol is asymmetric at the copula level is now a single, well-posed calculation.

**Implemented in:** the commit listed for rulings G2-01 … G2-08 in `PROGRAM/CHECKS.md`.

---

## G2-05 — narrow amendment to the copula formulation (forwarded review) · 2026-10-07

**Owner text (verbatim excerpt of the amendment):**

> Accept C-mono and the copula reformulation. Replace “copula difference” by “difference modulo the coordinate-reflection orbit.” Treat \(\binom{k+2}{3}-k\) as a conjectured/generic raw-coordinate tangent count until the nuisance-map rank is derived; for the exact monotone quotient, work in copula-normalized coordinates where marginal nonlinearities are eliminated exactly.
> Everything else can proceed.

**Supporting points (verbatim excerpt):**

> \( C_1\notin \operatorname{Orb}_{\mathcal R}(C_0) \Rightarrow \epsilon_R^{(T_{\rm mono})}>0 \), where \(\mathcal R\) is the permitted coordinate-reflection group. … a “correlation-change” witness is valid only if the changed dependence parameter is not obtainable by the allowed reflections … magnitude/structure rather than naïve signed difference is what matters. … \( \dim(\text{raw third-order quotient}) = \binom{k+2}{3} - \operatorname{rank}J \), with \(J\) the nuisance tangent map. … WO-002 three levels: exact theorem (maximal dependence invariant = copula modulo permitted coordinate reflections); cheap symmetry witness (radial asymmetry); perturbative BRI coordinates (rank/normal-score correlation change; odd multi-time rank cumulants; other copula asymmetry functionals) as witnesses of the exact statement, not its foundation. … if the low-order witnesses happen to vanish, BRI could still have a higher-order copula difference. … Stage 3 still waits. … WO-002 endpoint: determine whether the BRI intervention family changes its copula class after the allowed monotone/reflection quotient. If it does not, this branch of reciprocity dies. If it does, R1 has survived a substantially harder null.

**Implemented in:** the commit listed for rulings G2-01 … G2-08 in `PROGRAM/CHECKS.md`.

---

## G2-06 — WO-002 amendment (owner, after the forwarded review) · 2026-10-07

**Owner text (verbatim directive block):**

> FOR CLAUDE CODE — WO-002 amendment
>
> 1. Accept Theorem C-mono and the copula reformulation. Exact theorem: for continuous margins and coordinatewise strictly monotone T_mono, the maximal dependence invariant is the copula modulo the permitted coordinate-reflection group ℛ. Sufficient condition for escape: C₁ ∉ Orb_ℛ(C₀).
> 2. Witnesses. Cheap witness: radial symmetry of C₀ with radial asymmetry of C₁ ⇒ ε_R^(T_mono) > 0. A correlation-change witness counts only if the change can't be produced by an allowed reflection (use magnitude/structure, not signed differences).
> 3. Exact computations in copula-normalized coordinates (U_i = F_i(X_i), or normal scores Z_i = Φ⁻¹(U_i)); marginal nonlinearities are then eliminated exactly.
> 4. Leading-order count — derive and verify: in the Gaussian reservoir-limit regime, by Stein's identity a smooth per-coordinate deformation g changes the third-cumulant tensor only through E[g″(X_m)] times a fixed pattern T^(m); odd g contribute nothing; T^(m)_mmm = 3σ_m⁴ separates the k directions, so rank J = k for nondegenerate variances, and the surviving leading-order third-order invariant has dimension C(k+2, 3) − k. Label this as the leading-order coordinate count, subordinate to the exact copula theorem.
> 5. Then evaluate BRI1's surviving components (normal-score correlation change modulo reflections; odd multi-time normal-score cumulants outside span{T^(m)}) from the archived covariance and third-cumulant tensor, with their N_B scaling.
> 6. Exit: WO-002 ends with a yes/no — does the BRI1 intervention family change its copula class modulo ℛ? If not, this branch of reciprocity is killed; if so, R1 has survived T_mono. Stage 3 still waits for R1 closeout.
>
> That makes WO-002 a theorem with a computable leading-order check and a single yes/no endpoint.

**Owner preface (verbatim excerpt):** "I stated the dimension count C(k+2, 3) − k as fact before proving the nuisance map has full rank. That was ahead of the proof. … Claude Code should verify this derivation rather than take it from me."

**Implemented in:** the commit listed for rulings G2-01 … G2-08 in `PROGRAM/CHECKS.md`.

---

## G2-07 — WO-002 freeze · 2026-10-07

**Owner text (verbatim directive block; preceded by a forwarded review and the owner's two points):**

> 1. Tidy the "if and only if." ε_R is an infimum, so M1 should say what "= 0" means: either the matching maps exist exactly, or the copula lies in the closure of the reflection orbit. Since the reflection group is finite, the orbit is closed, and with continuous margins the copula depends continuously on the law, so the two readings agree — but that's worth one sentence in the proof. And M1 should be stated for the whole intervention family (all protocols' copulas in one orbit), not only for two protocols.
> 2. Preregister what a zero at leading order means. … WO-002 needs three preregistered outcomes, so a vanishing perturbative witness can't be misread as a kill.
>
> FOR CLAUDE CODE — WO-002 freeze
> Scope: T_mono = coordinatewise strictly monotone maps (increasing or decreasing) on the finite observed time grid; continuous, atomless margins with interval supports.
> Propositions to prove:
>
> * M1 — Exact quotient. ε_R^(T_mono) = 0 if and only if all protocols' copulas lie in one coordinate-reflection orbit. Include: attainment versus closure (finite reflection group ⇒ orbit closed; copula continuity under continuous margins), quantile-map construction for the converse, and the family-wide statement.
> * M2 — Symmetry certificate. Radially symmetric C₀ and radially asymmetric C₁ ⇒ ε_R^(T_mono) > 0.
> * M3 — Gaussian tangent structure. For X ~ N(0, C), Y_i = X_i + a δ_im g(X_m):
> ∂_a κ(Y_i, Y_j, Y_ℓ)|₀ = E[g″(X_m)]·[δ_im C_jm C_ℓm + δ_jm C_im C_ℓm + δ_ℓm C_im C_jm].
> With C_mm > 0 for all retained coordinates, rank J = k and the surviving leading-order third-order dimension is C(k+2, 3) − k. State the regularity condition: x + a·g(x) strictly monotone for small a (control of g′), and the integrability needed for the Gaussian identity. M3 is a leading-order diagnostic, subordinate to M1.
>
> Computation: BRI1's normal-score dependence (correlation of Z_i = Φ⁻¹(F_i(X_i)), assessed modulo reflections) and the third-order normal-score tensor projected off span{T^(m)}, with N_B scaling.
> Preregistered outcomes:
>
> 1. Leading-order surviving component nonzero → escape established at leading order (via M2 or M1).
> 2. Leading-order component zero → compute the exact copula radial asymmetry from finite-N_B dynamics before any verdict. A zero perturbative witness is not a kill.
> 3. Copulas exactly in one reflection orbit → this reciprocity branch is KILLED.
>
> After WO-002: freeze T, d_op (with the derived constants), complete D5 including mode selection → R1 terminal → Stage 3.
> That's ready to send. The next substantive thing to look at is WO-002's result, and I'll check it against the remote when it lands.

**Forwarded-review points adopted:** M1 as an exact iff; use normal-score correlation (not Pearson) for the even channel; the strict-monotonicity regularity of x + a·g(x).

**Implemented in:** the commit listed for rulings G2-01 … G2-08 in `PROGRAM/CHECKS.md`.

---

## G2-08 — R1 boundary (two-tier T, verdict logic, stopping rule) · 2026-10-07

Recorded verbatim in its own file, as the owner directed:
`PROGRAM/OWNER_RULING_R1_BOUNDARY.md`. It was committed before the WO-002 result was
read.

---

## G2-09 — WO-002 external check and R1 closeout · 2026-10-07

**Owner text (verbatim directive block; preceded by the owner's remote verification of `cb81a3b`):**

> FOR CLAUDE CODE — WO-002 external check and R1 closeout
>
> 1. CHECKS: `cb81a3b` → checked: Claude (external), no issues. Verified on remote: preregistered reading applied correctly (odd 7/7, even 3/3, both protocols; ratios ≥ 2×10⁶ against a 10² threshold); all exact controls pass (diagonal A, marginal-only control, parity, Gibbs identity, harmonic control, K reproduction); base correlations not near zero, so reflections cannot absorb Δρ; N_B·A converges to the leading coefficients. Note: P2(π, 2π) has |Δρ| ≫ |ρ|, so the leading-order formula is stretched at small N_B; this is consistent with the evidence-grade label.
> 2. Scoreboard: enter Tier 2 R1-PASS (readout-robust reciprocity), evidence grade, with the grading: odd channel = dual-branch escape (T_lin and T_mono separately); even channel = T_mono-only; no claim about the generated join; conditional on the carrier certificate; theorem grade pending M5.
> 3. R1 synthesis must state four things: (i) the observable ε_R^(T)(S:E) as failure of protocol separability modulo a declared calibrated interface class; (ii) the identification limit — with unrestricted protocol-dependent readouts, the test records admit an exact mode-selection representation, so reciprocity is not identifiable from them alone; (iii) conditional inference — R1-PASS requires both an independently established carrier/readout invariance (the dynamical analog of measurement invariance) and quotient separation; (iv) the BRI1 calibration with its tiers and grades.
> 4. Remaining gate: D5, the comparator audit, now explicitly including generic nonlinear response, measurement non-invariance, process non-Markovianity, causal-identification quantities, and mode selection. After D5: R1 terminal, then the `grut2` → `main` merge decision, then Stage 3 (evidence-grade R1 is sufficient to open it, clearly labeled).

**Owner context (verbatim excerpt):** "the measurement-invariance analogy is the established name for exactly the identification issue we found, and Stage 3 should aim to derive an objective equivalence class of readouts, [h]_T, rather than a unique formula." … "This is the first result in the program's history that is both genuinely positive and fully checked … It isn't new fundamental physics yet — but it's a real, defensible operational object, which is exactly what Stage 3 needed to start from."

**Implemented in:** the SCOREBOARD #11 / CHECKS commit after `eb980f1`; `PROGRAM/RESULTS/R1/R1_SYNTHESIS.md`; D5 (`PROGRAM/RESULTS/R1/D5_COMPARATOR_AUDIT.md`).

---

## G2-10 — Post-WO-002 R1 boundary (with labeling and D5 preregistration additions) · 2026-10-07

**Owner text (verbatim):**

> Let me confirm the remote state and one labeling detail before weighing in.Confirmed on the remote: `7c2b447` records G2-09 and scoreboard row #11 exactly as ChatGPT describes. I agree with the ruling — WO-002 is done, the interface ladder is closed at T_mono, D5 is the next gate, and the frozen-versus-post-result distinction is the right protection. Two refinements, one of them a labeling correction in R1's favor.
> 1. The non-identifiability result is pre-result, not a post-result refinement. I checked the frozen record at `82d311e`, committed before the WO-002 numbers were opened. It already contains Prop. E ("unrestricted interfaces trivialize R1"), the explicit exclusion of protocol-dependent mode selection (h ↦ h_a), and D5's mandate to include mode selection. So "with unrestricted protocol-dependent readouts, any record family has an exogenous explanation" — and therefore "every reciprocity claim is conditional on a certified common readout" — is a consequence of the frozen definition and can be cited as such. What genuinely emerged after the result is narrower: the interventional carrier state Z_A, the readout equivalence class [h]_T, and the measurement-invariance framing. Those are the parts to label POST-RESULT SYNTHESIS / STAGE-3 SEED.
> 2. Preregister D5's verdict categories before the audit starts. D5 is now the gate most exposed to pressure, because it runs right after a positive result and the natural wish is for R1 to come out "new." The categories should be fixed in advance:
>
> * RESTATED — ε_R is an existing quantity under new names, with no added structure.
> * STANDARD MATHEMATICS, NEW OPERATIONAL DEFINITION — the mathematics is known (maximal invariants, copulas, statistical-experiment comparison, measurement invariance), but the combination — certified common readout plus quotient-irreducible process change — defines a useful physical observable with an explicit identifying assumption.
> * DISTINCTIVE — R1 yields a relation or prediction the comparators don't.
>
> My honest prior is the middle category, and that's a perfectly good outcome. R1's job was never to be new physics by itself; it was to supply a well-defined observable that a future law has to explain. Writing that expectation down beforehand keeps D5 from inflating it.
> FOR CLAUDE CODE — additions to the post-WO-002 boundary ruling (adopt with ChatGPT's text)
>
> 1. Labeling: the non-identifiability under unrestricted protocol-dependent readouts (Prop. E; mode-selection exclusion h ↦ h_a; D5 mode-selection mandate) is part of the frozen pre-result record (`82d311e`) and is cited as such. Only Z_A, [h]_T, and the measurement-invariance framing are labeled POST-RESULT SYNTHESIS / STAGE-3 SEED.
> 2. D5 preregistration (commit before the audit begins): verdict categories — RESTATED / STANDARD MATHEMATICS, NEW OPERATIONAL DEFINITION / DISTINCTIVE — each with its criterion as above. The mathematics and the physical interpretation are classified separately. The middle category is recorded in advance as an expected and acceptable outcome; it does not block the R1 terminal or Stage 3.
> 3. Everything else in ChatGPT's ruling stands: no WO-002 extension, ladder closed at T_mono, D5 comparator list A–D and items 1–10, R1 terminal synthesis contents, stop for owner review, no Stage 3 card before review, no merge yet, M5 and Prop. G continue in parallel.
>
> The question has changed, as ChatGPT says: not "does BRI1 survive?" but "is what survived the right thing for a law of reality to explain?" D5 answers that, and preregistering its categories makes sure the answer is honest. OWNER RULING — POST-WO-002 R1 BOUNDARY
> WO-002 is accepted as complete and banked under G2-09.
> Current earned state:
>
> * Tier 1: BRI1 R1-PASS under calibrated linear/common-carrier interface class — DERIVED conditional on the frozen carrier commitment.
> * Tier 2: BRI1 R1-PASS at EVIDENCE GRADE under T_mono.
> * Odd channel = dual-branch escape: T_lin and T_mono separately.
> * Even channel = T_mono-only escape.
> * No claim about the generated join.
> * Theorem grade for Tier 2 remains OPEN pending M5.
>
> Do not rerun, extend, reinterpret, or enlarge WO-002.
> Do not introduce any interface class beyond T_mono. The R1 nuisance ladder is closed.
> Do not modify the frozen pre-result R1 definition to incorporate post-result conceptual refinements.
> The interventional-carrier / protocol-invariant readout-class formulation is accepted only as a POST-RESULT SYNTHESIS / STAGE-3 SEED:
>
> * Z_A = interventionally sufficient predictive carrier state relative to a frozen intervention repertoire A;
> * [h]_T = protocol-invariant physical readout/interface equivalence class;
> * unrestricted protocol-dependent h_a makes reciprocity non-identifiable from the test intervention-record family alone;
> * therefore every R1 reciprocity claim is conditional on an independently certified common carrier/readout class.
>
> This is not retroactive input to WO-002.
> NEXT REQUIRED TASK: D5 — comparator / identification audit.
> D5 must explicitly compare R1 against:
>
> 1. generic nonlinear-response diagnostics;
> 2. non-Markovianity measures;
> 3. process tensors / quantum combs;
> 4. invariant causal prediction;
> 5. independent causal mechanisms;
> 6. Janzing–Schölkopf algorithmic causal inference;
> 7. MDL causal discovery;
> 8. Blackwell–Le Cam / statistical-experiment comparison;
> 9. measurement-invariance / latent-measurement identification analogues;
> 10. input-output predictive-state / epsilon-transducer formalisms.
>
> D5 must answer:
> A. Is epsilon_R merely an existing generic nonlinear-response or process-distance quantity under renamed variables?
> B. Is the quotient construction itself known mathematics but the physical identification rule new only in application?
> C. Is the common-carrier/readout certificate an unavoidable identifying assumption?
> D. Does the product-latent construction prove non-identifiability when protocol-dependent readouts h_a are unrestricted?
> If D5 shows R1 is merely RESTATED with no additional physically meaningful structure, record that honestly.
> If D5 shows the mathematics is largely standard but the operational combination
> common-carrier/readout invariance + quotient-irreducible process change
> defines a genuinely useful physical observable, classify the mathematics and the physical interpretation separately.
> After D5, produce an R1 TERMINAL SYNTHESIS with:
>
> * exact definition;
> * identifying assumptions;
> * no-go / non-identifiability statement;
> * Tier 1 result;
> * Tier 2 result;
> * evidence/theorem-grade distinction;
> * portability limits;
> * common-carrier requirement;
> * no-claim-about-join statement;
> * M5 status;
> * what Stage 3 must derive rather than assume.
>
> Then STOP for owner review.
> Do not open or optimize any Stage-3 K card before the R1 terminal is reviewed.
> Do not merge grut2 into main yet.
> M5 and Prop. G may continue as theorem-grade upgrades, but they do not alter the already banked evidence-grade WO-002 result unless they uncover a substantive contradiction.

**Implemented in:**
- `PROGRAM/RESULTS/R1/D5_PREREGISTRATION.md`, committed before the governing D5 audit.
- The labeling block in `R1_T_LADDER.md` §0.
- The D5 audit, then `R1_SYNTHESIS.md` as the R1 TERMINAL SYNTHESIS.

---

## G2-11 — R1 TERMINAL ACCEPTED / STAGE-3 OPENING (with additions) · 2026-10-07

**Owner text (verbatim; the ruling block followed by the additions block):**

> OWNER RULING — R1 TERMINAL / STAGE-3 OPENING
> R1 TERMINAL SYNTHESIS at `dbfd64b` is ACCEPTED.
> Scientific ruling:
> R1 TERMINAL — ACCEPT.
> R1 earns:
> a conditional operational reciprocity observable, built from standard mathematics, with an explicit identifying assumption and a calibrated BRI1 realization.
> R1 does NOT earn:
> new mathematics, a fundamental GRUT law, a distinctive physical relation, a confirmed prediction, or CROSS-SECTOR status.
> D5's governing classification is accepted at its stated grade:
>
> * mathematics: STANDARD MATHEMATICS, NEW OPERATIONAL DEFINITION;
> * physical identification rule: STANDARD MATHEMATICS, NEW OPERATIONAL DEFINITION;
> * DISTINCTIVE: not earned;
> * R1 kill condition: does not fire.
>
> The following remain open upgrades and do not block Stage 3 unless they uncover a contradiction:
>
> * M5 theorem-grade Tier-2 expansion;
> * D4 finite-sample testing;
> * Tier-2 carrier-necessity question;
> * remaining external theorem checks.
>
> Before merge, make one housekeeping repair only:
>
> * clean stale `PROGRAM/STATE.md` language that still says Stage 2 is next / D5 is not started;
> * update CHECKS to record this owner review and any external-check status justified by it;
> * do not alter the scientific contents or grading of the R1 terminal.
>
> Then freeze/tag the R1 terminal boundary and merge `grut2` into `main` with history preserved. Do not squash the scientific provenance. Keep `grut2` as a historical branch after merge.
> STAGE 3 — AUTHORIZED TO OPEN.
> However, do NOT generate, freeze, score or optimize a 𝒦 candidate yet.
> First write and freeze a Stage-3 charter ALONE.
> The charter must fix, before any candidate exists:
>
> 1. the ordinary baseline freedom spaces for: 𝒜_Π, 𝒜_T, 𝒜_ε, 𝒜_Γ;
> 2. the success criterion: nontrivial freedom reduction + positive compression + measurable consequence;
> 3. the compression accounting and information-price rules;
> 4. the nonrelocation rule: carrier, partition, interface class, readout class, Gibbs/FDT structure and target relation may not be hidden in inputs;
> 5. the maximum candidate budget: at most three genuinely distinct 𝒦 cards;
> 6. the required contents of every card: exact law, information price, generated structures, measurable target, hostile baseline comparison and kill condition;
> 7. the Stage-3 originality rule: familiar component theories are allowed and expected; novelty is judged only at the assembled-law level;
> 8. the cross-sector gold standard: parameter transfer — quantities fixed in sector A must predict sector B without a new GRUT-specific fit;
> 9. the stopping rule: if the authorized candidate budget fails to produce a law meeting the frozen gates, this generative route terminates. Do not create a new "deeper prerequisite" staircase.
>
> The central Stage-3 task is: Find a compact selective law 𝒦 that generates persistent differentiation and makes interface/response structure non-independent.
> A successful candidate should eventually produce something schematically like 𝒦 → Π → [h]_{T_Π} → T_Π → Γ_Π → ε_R and force at least one measurable relation ℛ(Π, T_Π, ε_R, Γ_Π) = 0 that existing frameworks do not independently impose.
> R1's identifying assumption becomes a Stage-3 target: derive objective persistent carrier/readout structure rather than supplying it.
> Do not assume a unique coordinate formula for h; derive physical structure modulo representation.
> Do not presume any monotonic identity–response tradeoff. If 𝒦 forces such a relation, its sign and functional form must come from the law.
> After the Stage-3 charter is frozen, STOP for owner review before generating Card 1.
> Operational housekeeping:
> Disable the two-hourly "review VS Code" routine. VS Code is paused and repeated checks are no longer informative. Do not replace it with another recurring review routine unless the role becomes active again.
>
> FOR CLAUDE CODE — additions to the R1 TERMINAL / STAGE-3 OPENING ruling (adopt with ChatGPT's text)
>
> 1. Merge = provenance, not endorsement. After merge, every DERIVED item marked "external check pending" (A-BL, F, M1–M3, Prop. G, D5 analyses) keeps that status and its `CHECKS.md` line stays pending. If tag pushes are blocked (403), record the R1 boundary `dbfd64b` in `STATE.md` and the merge commit message instead; the owner will tag locally.
> 2. Stage 3 charter — ε_R is derived. ε_R = ε[Γ_Π, T_Π] by definition. The baseline freedom spaces are 𝒜_Π, 𝒜_T, 𝒜_Γ; ε_R is not an independent axis. Definitional relations do not count. A qualifying relation ℛ must restrict the jointly realized (Π, T_Π, Γ_Π) beyond the definition of ε_R.
> 3. Stage 3 charter — baseline after standard theory. Baseline freedom spaces are computed after imposing causality, positivity, KMS/FDT, Onsager reciprocity, and conservation laws. Relations implied by these earn no credit (D5: BRI1's Tier-1 value is a standard Kubo/FDT quantity).
> 4. Stage 3 charter — response scope. Each target relation declares whether it concerns quotient-irreducible (nonlinear / non-Gaussian) back-reaction detected by ε_R, or response in general, since ε_R is blind to linear response (R1-NULL ≠ no response).
> 5. Disable the two-hourly "review VS Code" routine (owner decision, as ChatGPT ruled).

**Owner context (verbatim excerpts):** "R1 is its own observable, but not yet its own physics." … "Stage 3 should not begin by inventing a 𝒦 card immediately. First freeze the Stage-3 null space and scoring charter … before any candidate is generated. Otherwise the candidate itself can redefine what counts as impressive freedom reduction." … "With those in the charter, Stage 3 can't win on a definition or on the fluctuation-dissipation theorem — it has to find a relation that standard physics genuinely leaves free."

**Reconciliation note (Claude Code).**
- The ruling block lists 𝒜_ε among the baseline spaces. Addition 2 (owner) rules that ε_R is derived and not an independent axis.
- The charter therefore treats 𝒜_ε as the **image** of 𝒜_Γ × 𝒜_T under ε, not as a free axis. This satisfies both texts.

## G2-12 — STAGE-3 §5 RESIDUAL ITEMS (pre-Card-1, §19.2) · 2026-10-07

**Owner text (verbatim ruling block):**

> OWNER RULING — STAGE-3 §5 RESIDUAL ITEMS (pre-Card-1, §19.2)
>
> 1. Credit bar: N_cred = 100, no rescaling.
> 2. Evaluation order: sequential (D-3 as frozen). Each later card's preregistration
>    lists which earlier rulings/verdicts it used.
> 3. Kit (OD-12): AUTHORIZED after CR-1 re-freeze. T_kit = one session.
>    Priority: (a) L0 normalizer + price coder on App. B; (b) NR-4 ablation harness;
>    (c) B-HB rejection tests; (d) SEL/B-CF reproductions. Unfinished items take
>    hostile defaults by CR; no extension.
> 4. Scope-Q: accepted unchanged. Card authors target a platform where RH-KMS is
>    certified to fail.
> 5. NR-4: adopt R2-A m11 — exclude from numerator and denominator every point where
>    all lock observables are within r_lock of their S–E-decoupled values. Report the
>    excluded fraction with the NR-4 verdict.
> 6. DEF-14: kept. If T_Π is injective in Π, state ℛ★ at a catalogue class (default
>    T_mono); T_Π enters through generation gates only.
>
> CR-1 SCOPE: one round over cached Round A (wf_959efb57-3b2). Apply ONLY findings
> that make a rule too strict (hidden kills, infeasible arithmetic, an honest card
> failing), including the NR-4 r_lock/σ_pre coupling. Record loopholes in a CR-2
> queue, unapplied (tightening stays available under §19.2). No loop-until-dry.
> Then re-freeze → kit → STOP before Card 1.

**Owner context (verbatim excerpts):** "Under §19.2, once the first 𝒦 draft is logged,
repairs can only tighten. A loophole found later can still be closed, and Card 1 gets
rescored toward failure. A rule that is too strict, one that kills an honest card, can
never be loosened after that point. So before Card 1, only the too-strict defects have to
be fixed." … "I wouldn't resume loop-until-dry. On a 2,800-line charter it may never come
back clean."

**Builder notes (Claude Code).**
- Only one of round A's six finding lenses (loopholes) completed before the stop. All
  seven of its findings are loopholes; they go to the CR-2 queue, unapplied.
- For CR-1's too-strict scope, the hidden-kill and feasibility lenses are run once on
  the frozen text. The other lenses are not re-run, to conserve the owner's budget.
