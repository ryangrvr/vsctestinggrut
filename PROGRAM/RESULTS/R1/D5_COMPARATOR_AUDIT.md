# D5 COMPARATOR AUDIT: R1, the operational reciprocity observable (governing) · 2026-10-07

> **Provenance (Claude Code, 2026-10-07).**
> - This is the governing D5 audit (preregistration `D5_PREREGISTRATION.md`, committed at `891193a` before the audit ran).
> - It was produced by a 22-agent workflow: 10 comparator analysts, 10 skeptics each instructed to argue RESTATED, an identification agent, and a synthesizer. Claude Code read it in full before committing.
> - The run hit a session limit partway through. It was resumed from its run record: completed agents replayed from cache, and only the six interrupted agents re-ran.
> - **Evidence.** The agent-written scripts and machine outputs are in `D5_evidence/`. That directory mirrors the scratch paths cited below: read `…/scratchpad/X` as `D5_evidence/X`.
> - Downloaded literature is not committed.
> - The identification agent's full answer to questions C and D is `D5_IDENTIFICATION.md`.
> - D5 ANALYSIS results (C1–C6, the comparator-8 I3 characterization, and the numerical evidence) are **evidence grade and not externally checked**.


**Binding document.** This audit follows `PROGRAM/RESULTS/R1/D5_PREREGISTRATION.md` (ruling G2-10) exactly: its verdict categories, its two separate classifications, its decision rules, questions A–D and its post-result labeling. The early pre-G2-10 D5 run was never opened and is not used.

**Overall verdicts**

| Classification | Verdict |
|---|---|
| **(M) Mathematics.** The quotient construction, the distance, Theorems A, A-BL, C, F, M1–M3 and Prop. G | **STANDARD MATHEMATICS, NEW OPERATIONAL DEFINITION** |
| **(P) Physical interpretation and identification rule.** The common carrier, the mode-stability certificate, the verdict table, and the separation of E-C from E-A and E-B | **STANDARD MATHEMATICS, NEW OPERATIONAL DEFINITION** |
| RESTATED by any single comparator | **No.** No comparator meets the criterion, for either (M) or (P). |
| DISTINCTIVE | **Not awarded.** No candidate relation survives every comparator (§2.3). |
| STATE.md kill condition | **Does not fire** for ε_R as defined. Qualifications are recorded in §4. |

This matches the recorded expectation, which the preregistration calls acceptable and which does not block the R1 terminal or Stage 3.

**How the audit was run**
- There were ten comparators, taken in the G2-10 order. Each had an analyst and an independent skeptic, and the skeptic was instructed to argue RESTATED.
- An identification agent answered questions C and D.
- The synthesizer applied the decision rules mechanically. Spot-checks were limited to:
  - arXiv metadata for 1806.09277, 2609.11959, 2512.02193, 2601.23026 and 1302.6784;
  - the text of Alvarez-Melis–Jegelka–Jaakkola eq. (7) and Lemma 4.1;
  - the scratch outputs `d5c1_skeptic2/epsR_k1_bri1_output.json` and `d5_cd_checks_output.json`.
- The audit was read-only. Nothing in `/tmp/claude-0/f0chain` was edited.

**Abbreviation used in tables.** MID = STANDARD MATHEMATICS, NEW OPERATIONAL DEFINITION.

---

## 1. Decision rules as applied

- **Per comparator.** The verdict is the more conservative of the analyst's and the skeptic's. In all ten comparators both returned MID for (M) and for (P), with no disagreement on category. Every skeptic stated that its RESTATED case fails: restated_succeeds_M = false and restated_succeeds_P = false, ten times each. So the final per-comparator verdict is MID/MID ten times.
- **Overall.** No single comparator restates, so RESTATED does not apply. DISTINCTIVE requires one concrete relation that survives every comparator, and none does (§2.3). The overall verdict is therefore MID for both (M) and (P).
- **Skeptic corrections.** Skeptics corrected several facts in the analyst outputs (§2.1). None of these corrections changes a category.

## 2. Comparator table

| # | Comparator | Primary sources (verification) | Relation to ε_R (implications in both directions; counterexamples used) | Which of E-A / E-B / E-C it separates | Analyst (M)/(P) | Skeptic (M)/(P) | Final (M)/(P) |
|---|---|---|---|---|---|---|---|
| 1 | Generic nonlinear-response diagnostics: Volterra/Wiener; Kubo/Mukamel response functions; nonlinear FDRs; polyspectra and HOS tests; noise spectroscopy | **VERIFIED:** Boyd–Chua, IEEE TCAS 32:1150 (Thm 1); Mukamel, PRA 77 023801, eqs. 14–15; Beenakker–Kindermann–Nazarov, PRL 90 176802, eq. 10; Norris–Paz-Silva–Viola, PRL 116 150503; Hyvärinen–Oja, Neural Netw. 13:411, eqs. 36–37; Saito–Utsumi, PRB 78 115429, eqs. 12–13; Clerk et al., RMP 82 1155, eq. 2.15. **Abstract level:** Reulet, Gabelli–Reulet, Lippiello, Basu. **PARTIAL:** Brillinger 1965 and Hinich 1982. **Primary UNVERIFIED:** Kubo 1957; its classical formula was checked numerically by three routes. **Bibliographic only:** Bochkov–Kuzovlev, Lee–Schetzen, Ford–Kac–Mazur/Zwanzig, Comon, Subba Rao–Gabr, Mendel. **Overall PARTIAL**, but no verdict rests on an unverified item. | **A response signal does not imply ε_R > 0.** Mean (Volterra) response of any order plus protocol-independent noise gives ε_R = 0 in both tiers. Example: the harmonic bath with linear coupling responds through friction yet has ε_R = 0 (WO-002 control at 1.27e-14). C2-F has cumulant response (γ₁ = 0.593 vs 0.299) yet ε_R^lin = 0. The same covariance response is absorbed at Tier 1 and counted at Tier 2. **ε_R > 0 does not imply a comparator signal.** Gaussian families escape Tier 2 while every polyspectrum of order 3 or more is zero; their normalized covariance response still fires. E2 gives ε_R > 0 with no response at all. A zero-skew asymmetric law gives ε_R ≥ 0.0116. Two laws with equal skewness 0.5 give 0.03919 and 0.04203. Parametric coupling to a harmonic (linear) bath escapes both tiers. **Regime restatement, recorded honestly.** BRI1's K is a classical Kubo response of x³ − 3m₂x, fixed by P0's connected 4-point function; three routes agree to ≤ 3.5e-12. At k = 1, Tier-1 ε_R = (V*/12)·abs(γ₁)·(1 + 0.235/N_B + …), with ratio 1.0307 at N_B = 8 falling to 1.0018 at N_B = 128. | **None from the records.** Response theory presupposes a fixed observable and coupling, i.e. it assumes the common readout. Noise spectroscopy adopts the E-A null as an assumption. Normalized polyspectra carry an LTI quotient, but for one series only. Beenakker–Kindermann–Nazarov separate intrinsic noise from environmental backaction through a calibrated circuit model; that is a physical precedent for R1's logic, but it is model-based. | MID/MID | MID/MID | **MID/MID** |
| 2 | Non-Markovianity measures: BLP, RHP, classical Markov property, memory kernels (GLE, Mori–Zwanzig, Ford–Kac, Kac–Zwanzig) | **VERIFIED, full text:** BLP, PRL 103 210401, eqs. 10–12; RHP, PRL 105 050403; Vacchini et al., NJP 13 093004, eq. 46; Benedetti–Paris–Maniscalco, PRA 89 012114, eq. 26; Breuer–Laine–Piilo–Vacchini, RMP 88 021002, eq. 33; Pollock et al., PRL 120 040405; Leimkuhler–Sachs, arXiv:1804.04029, eqs. 14–19. **Metadata only:** Mori, Ford–Kac–Mazur, Zwanzig 1973. **UNVERIFIED, not load-bearing:** Darsow–Nguyen–Olsen. **Overall PARTIAL**, with no load-bearing gap. | **All four cells have exact members.** **(a) Non-Markov with ε_R = 0:** the harmonic bath for any memory kernel; an exogenous telegraph field (N_BLP > 0 for γ < 2); C2-F′, a genuinely non-Markov record. **(b) Markov with ε_R = 0:** C2-F as implemented, an exact AR(1) chain. **(c) Markov in all three senses with ε_R^T_R1 ≥ 1.915e-2:** M-A. **(d) Non-Markov with ε_R ≥ 1.915e-2:** M-A′. **Singleton argument:** ε_R ≡ 0 on any one-protocol family, while every non-Markovianity measure is a nontrivial functional of one process. GL(k) time-mixing creates or destroys record Markovianity without moving ε_R^T_R1. **Only surviving link:** Markovianity that differs across protocols implies ε_R^mono > 0. This is sufficient only; M-B is a counterexample to the converse, with ε_R^mono ≥ 7.98e-3 (evidence). The RMP eq. 33 environment term gives a one-way data-processing implication only: the harmonic bath has D_E > 0 and ε_R = 0. | **None.** Exogenous fields produce backflow, and a memoryless responding environment is exactly Markov. The GLE friction kernel detects linear E-C under offset-calibrated interfaces, which is exactly the channel ε_R discards. Kac–Zwanzig configuration-dependent coupling is an h_a, so its verdict is MODE SELECTION. | MID/MID | MID/MID | **MID/MID** |
| 3 | Process tensors, quantum combs and process distances | **VERIFIED, full text:** Pollock et al., PRA 97 012127 and PRL 120 040405; Chiribella–D'Ariano–Perinotti, PRL 101 060401 and 180501; Gutoski, JMP 53 032202; Milz–Modi, PRX Quantum 2 030201; Zambon, PRA 110 042210; Berk et al., Quantum 5 435; Barsse et al., PRR 6 043305; Giarmatzi–Costa, Quantum 5 440; Budini, PRA 108 042203; Taranto et al., Quantum 8 1328; White et al., PRX Quantum 3 020344; White et al., PRX 15 021047; Jenčová, IEEE TIT 67 3945. **Abstract level:** Pérez-García et al., Milz–Pollock–Modi 2018, Kofler–Brukner. **Overall VERIFIED.** | **Only a template is shared:** distance to a free set over a tester family. In Jenčová's form, ε_R = inf over P* of δ_{F_T}(C_{P*} → P). **T-trivial core.** With T = {id}, ε_R is a restricted classical analogue of the Barsse signalling distance. ε_R is strictly coarser than signalling: C2-NG, C2-F and the harmonic bath all signal and have ε_R = 0. **Against PRL-120 non-Markovianity.** Tier 1 is incomparable with it: the memoryless model F = ξ + c·q·(ξ² − 1) has N = 0 and ε_R ≥ 0.0645 (optimal odd witness ≥ 0.124). Tier 2 implies restricted non-Markovianity, but not the converse. Tier 2 does not imply violation of NS (common-cause example). **Against comb distances.** d_q has a nontrivial quotient zero set that is not stable under processing: N(0,1) and N(0,4) lie in one orbit, but after y ↦ y + y³, d_q ≥ 0.0660. F_T contains anticipating families, so it is not a set of combs. | **None at record level.** PT's causal-break logic with known instruments gives the T-trivial argument for E-C against E-A. Mode selection lies outside PT's system-only control set. Taranto's NS set is incomparable with ε_R: model (i) is in NS with ε_R > 0, and the harmonic bath violates NS with ε_R = 0. GST calibration and self-consistency checks are PT's partial certificate, and they need informationally complete controls. | MID/MID | MID/MID | **MID/MID** |
| 4 | Invariant causal prediction (ICP) and variants | **VERIFIED:** Peters–Bühlmann–Meinshausen, JRSS-B 78:947 (arXiv v3; Assumption 1 = eq. 3; eqs. 4, 5, 12, 25, 28/29, 31, 32; Thm 1; §6.2–6.3); Heinze-Deml–Peters–Meinshausen, J. Causal Inf. 6 (Def. 1; E ∩ S = ∅ after eq. 4); Pfister et al., JASA 114; Kook et al., JASA 120 (Defs. 3, 4, 11; Prop. 20); Henzi et al., Biometrika 112; Zhang et al., ICML 2013; Gong et al., ICML 2016. **PARTIAL:** Borriero et al. 2025 (abstract). **Overall VERIFIED.** | **ε_R = 0 is an instance of the shared-noise schema** (eq. 28) with mechanism class G_T. That null makes the protocol a parent of the record, which nonlinear ICP excludes (E ∩ S = ∅) and for which TRAM-ICP returns no invariant set. ICP's realized classes are identity, translations, one shared h, Gaussian-linear, or unrestricted (vacuous); none equals T_R1 or T_mono. **Implications.** S = ∅ invariance implies ε_R = 0. The converse fails: C2-NG, C2-F and the harmonic bath. The unrestricted schema holds for every family, including BRI1 X1 and E2; it is the k = 1 instance of Prop. E / D1. **Residual-group minimization is necessary.** Whitening without the O(k) minimization falsely rejects a T_R1-null pair: KS p = 1.2e-43, while Mardia √β₁ = 1.3952 for both. | **None from the records.** S = ∅ rejects all three explanations; the unrestricted schema accepts all three. In the idealization where the latent Z is observed, ICP rejects E-A (p = 0) and E-B (p = 8.7e-129) and accepts E-C (p = 0.52). So it is the declared T that separates E-A from E-B. ICP's "no intervention on the target, known by design" is the same epistemic type as the carrier. | MID/MID | MID/MID | **MID/MID** |
| 5 | Independent causal mechanisms (ICM) and descendants (SMS, group genericity, SIC, interventional CRL) | **VERIFIED:** Peters–Janzing–Schölkopf 2017 (Principle 2.1; eq. 6.7; §2.3.4; Prop. 4.1; Def. 6.12 and Prop. 6.13(ii); §7.1.6), read from a DSpace mirror because OAPEN returned 403; Schölkopf et al., ICML 2012; Schölkopf et al., Proc. IEEE 109; Besserve et al., AISTATS 2018; Shajarisales et al., ICML 2015; von Kügelgen et al., NeurIPS 2023 (Asm. 2.8, Def. 2.6); Squires et al., ICML 2023; Zhang et al. 2013; Gong et al. 2016; Budhathoki et al. 2021 (venue confirmed by search only). **Overall VERIFIED.** | **ICM and ε_R are logically independent.** ICM holds with ε_R > 0 (BRI1 X1). ICM holds with ε_R = 0 in the harmonic bath, which has a total causal effect in the sense of PJS Def. 6.12 yet is classed R1-NULL. Readout modularity is violated with ε_R = 0 in C2-F (the violation is inside T) and with ε_R > 0 in E2. **R1-PASS** is a one-sided, T-quotiented sufficient certificate of a total causal effect. **Information-branch contrasts are orthogonal to ε_R.** The Trace contrast takes the values 0, 1.5 and −0.245 across one GL(2) orbit, where ε_R = 0. **Component restatement:** Prop. E/E1 and D1 are PJS Prop. 4.1 universality. **Closest single object:** Gong 2016 (shared readout W, per-domain diagonal location-scale map, MMD). There W is fitted, not certified; the class is diagonal; and the residual has no verdict role. The LS-ConS null and the frozen null disagree on C2-F. | **None from the records.** ICM supplies vocabulary only: E-C is an effect propagating through invariant mechanisms; E-B is a non-elementary intervention on the readout, which PJS §2.3.4 says must be settled "by physics"; E-A is declared non-elementariness confined to T. | MID/MID | MID/MID | **MID/MID** |
| 6 | Janzing–Schölkopf algorithmic causal inference and AIC, with decidable surrogates | **VERIFIED:** Janzing–Schölkopf, IEEE TIT 56:5168, DOI 10.1109/TIT.2010.2060095, read via arXiv:0804.3678v1 (Defs. 2–4; Postulates 5 and 7; §2.3; §3.2; §4.1 Defs. 9–10, Lemma 10, eq. 26; §4.2); Lemeire, JMLR 17; Janzing–Chaves–Schölkopf, NJP 18 093052; trace method (arXiv:0909.4386); SIC (arXiv:1503.01299). **Bibliographic only:** Lemeire–Janzing 2013. **UNVERIFIED:** J-S refs [33]–[35]. **Overall VERIFIED** (arXiv numbering). | **All four (AIC satisfied or violated) × (ε_R zero or positive) cells are occupied:** harmonic bath and C2-F; BRI1 and E2; C2-F-tuned; E2-tuned. **Harmonic vs Duffing:** identical AIC profiles up to O(1), yet ε_R = 0 vs ε_R ≥ c/N_B. **No group G** has a G-covariant class equal to T_R1. **ε_R is not a function of reference information.** N(0,1) vs Z³/√15 has I_Z2 = 0 for both and ε_R^T_R1 ≥ 0.0866. Gaussian copulas with ρ = 0.3 vs 0.6 have I_R = 0 and ε_R^mono ≥ 0.0405. **Lemma 10** (a common map cannot add information about the index) is the data-processing skeleton of the carrier inference. **Shared core:** the asymmetry monotone and the twirl of J-S §4.1 are the core of Theorem C, F1/F3 and M2. | **None on the program controls**, because every kernel there is O(1). The §4.1 symmetry lemma separates E-C from E-A given a symmetric reference and an injective interface, but it does not separate E-B. AIC could separate some E-C from E-B only in the uncomputable complex-parameter regime. | MID/MID | MID/MID | **MID/MID** |
| 7 | MDL causal discovery (bivariate rules; multi-context Vario, LINC, ORION, SpaceTime; CoCa) | **VERIFIED:** Slope (ICDM 2017); CISC (ICDM 2017); Origo (ICDM 2016 / KAIS 2018); Ergo (SDM 2015); Mooij et al. (NIPS 2010; JMLR 17); Vario; LINC; ORION; SpaceTime (arXiv); CoCa; HEC; SAM; CoCo (AISTATS 2024); Pérez-Ortiz et al., Ann. Statist. 52; JCI (JMLR 21); Suhr et al., arXiv:2601.23026 (preprint). **Crossref or abstract only:** Slope-KAIS, Sloppy. **Primaries UNVERIFIED:** Rissanen 1996, Barron–Cover, Hyvärinen–Pajunen. **Overall VERIFIED.** The brief's citation is corrected: the ICDM 2017 Budhathoki–Vreeken paper is CISC. | **Multi-context invariance** is literal equality, i.e. T = {id}. With a universal, well-specified code, "shared" implies ε_R = 0, and ε_R > 0 implies a detected change; both converses fail (C2-F, C2-NG, harmonic bath). **Published Gaussian-coded instances are orthogonal to ε_R.** For {N(0,1), standardized Exp} the shared model wins by 15 bits while ε_R = 0.150. For {N(0,1), N(0,4)} a change is detected by 64661 bits while ε_R = 0. **A constructed "MDL modulo T"** (the Sibson radius modulo T) has ε_R's zero set but not its values: lattice or Rademacher laws against N(0,1) give D_KL^T = log 2 for every member, while ε_R ranges from 0.0125 to 0.2673. **Limit restated:** CoCa §2.2 and Mooij 2010 eq. 3 restate the E1 limit. | **Only "law changed" versus "unchanged."** E2 and its responding-environment twin produce identical records, so every MDL score agrees on them. Causal sufficiency fails by construction for a latent environment, and a simplicity prior is a preference, not identification. | MID/MID | MID/MID | **MID/MID** |
| 8 | Blackwell–Le Cam comparison of experiments, maximal invariants, IPM and quotient metrics | **VERIFIED:** Mariucci, arXiv:1605.03301 (Defs. 2.5–2.6; Thm 2.7); Lehmann 1959, ch. 6 (Thms 1 and 3; pp. 217, 234, 235); Cahill et al., arXiv:2205.14039; Grave et al., arXiv:1805.11222; Alvarez-Melis–Jegelka–Jaakkola, arXiv:1806.09277, eq. 7, which is posed for a general cost c but worked for squared Euclidean, with Lemma 4.1 condition 2 whitened (also spot-checked by the synthesizer); Birrell et al., arXiv:2202.01129; Sriperumbudur et al.; Remillard–Scaillet, JMVA 100; Henze–Mayer, arXiv:1807.06367. **Abstract level:** Gupta–Henze–Klar, Henze–Klar–Meintanis, Genest–Nešlehová. **PARTIAL:** Blackwell 1951 and 1953, and Le Cam 1964 via Mariucci. **Content UNVERIFIED:** Torgersen, Boll 1955, Hall–Wijsman–Ghosh. **Overall PARTIAL.** | **Raw experiment {P_a}: deficiency and ε_R are unrelated.** Under contamination the TV radius is ≤ η/2 → 0 while ε_R ≥ 0.0861. In a location family ε_R = 0 while the deficiency reaches 1 − 1/abs(A). The common bijection y ↦ y³ is a Le Cam equivalence but moves ε_R from 0 to > 0 (skewness 3.950). **Nuisance-augmented experiment E_T:** ε_R = 0 exactly when the protocol label is unidentified, and this zero set is Le Cam-invariant. The maximal invariant is then uninformative at every n (Lehmann Thm 3). **The zero set is a set of classical nulls:** affine equivalence; copula equality modulo the 2^k reflections; the Henze–Klar–Meintanis symmetry null behind F3; the Genest–Nešlehová null behind M2. **Two-protocol Tier 1:** ε_R is half of AMJJ eq. 7 at population level, with cost min(abs(x−y), 2), F = O(k) and whitened inputs. **Not an invariant IPM:** for the square vs triangle configuration, Birrell's IPM is 0 while d_q ≥ 1/3. | **Raw deficiency: none.** Invariance reduction under the declared T separates E-A from {E-B, E-C}, with the same zero set as ε_R. Blackwell garbling separates E-B from E-C only under a θ-independent readout, which is the carrier. The exact identity is that the T-reduced record experiment is a garbling of the latent experiment at every n. | MID/MID | MID/MID | **MID/MID** |
| 9 | Measurement invariance (MI) and latent-measurement identification | **VERIFIED:** Lubke et al., BJMSP 56, eq. 1 (the Mellenbergh/Meredith definition); Borsboom et al., Psychol. Methods 13, eq. 4; Asparouhov–Muthén, SEM 21, eqs. 5–9; Verdam–Oort–Sprangers, QoLR 25; Suppes–Zanotti, Synthese 48; Stevens, Science 103; Wu–Estabrook, Psychometrika 81 (eq. 11; Prop. 5). **Abstract level:** Meredith–Teresi, Vandenberg–Lance, Bechger–Maris, Oort 2005, Rupp–Zumbo, Meredith 1964a and 1964b, Santos et al. 2013, van der Linden 2019. **UNVERIFIED:** Meredith 1993 full text, the Vandenberg–Lance body, Millsap's content. **Overall PARTIAL.** | **The frozen carrier is Mellenbergh/Meredith MI** of the readout, with the protocol as grouping variable. It is required at the full distributional level, which is stronger than strict factorial invariance: readout noise with equal variance but different skewness passes SFI yet can give ε_R > 0 (example skewness 0.179). **Saturated configural substitution** (η := W, Λ_a := K_a, Θ = 0): ε_R^T_R1 = 0 holds exactly when a configural model with a group-invariant latent law exists. This is an exact zero-set equivalence, but no MI source uses that model, and it is trivial under normal theory. **ε_R is not a function of MI statistics.** The alignment zero sets are incomparable: non-proportional Gaussian loadings give ε_R = 0 with F > 0, and an equal-moment shape change gives F = 0 with ε_R > 0. Ordinal MI's Gaussian latent responses force radial symmetry, so BRI1's odd channel cannot be expressed there. The even channel's twin is a polychoric-correlation comparison, which is signed rather than taken modulo reflections. The harmonic bath and Gaussian latent change count as MI impact while ε_R = 0. | **E-B vs E-C:** separated only conditionally on invariance constraints. These are partially testable in overidentified parametric models, but not in R1, where the latent dimension is unrestricted. **E-A vs E-B:** not separated, since both are non-invariance. **E-A vs E-C:** separated only if the interface maps are known and removed. **E2** is configural non-invariance (reconceptualization) and is unidentified in both frameworks; this is an agreement case. | MID/MID | MID/MID | **MID/MID** |
| 10 | Input-output predictive states: ε-transducers, causal states, controlled PSRs | **VERIFIED:** Barnett–Crutchfield, J. Stat. Phys. 161:404 (Defs. 1–4, 8; eq. 9; Props. 2–3; Thms 1–3; §III, §IV.C, §XII, §XIV, §XV); Shalizi–Crutchfield, J. Stat. Phys. 104:817; Littman–Sutton–Singh, NIPS 14 (eq. 1; Thm 1; action-indexed O^{a,o}); Singh–James–Rudary, UAI 2004. **Verified, but preprints and not established objects:** Boyd et al., arXiv:2512.02193 (Thm 1; Defs. 4 and 6); Yang et al., arXiv:2609.11959. **Abstract or structure level:** Boots et al., Brodu–Crutchfield, Ferns et al. **UNVERIFIED:** Givan et al. definition; Jaeger's OOM gauge. **Overall VERIFIED.** | **ε_R is a function of the transducer only trivially**, as every record functional is, so this is not "a known function" in the criterion's sense. Barnett–Crutchfield define no interface class and leave any process distance to future work. **ε_R is not a function of the transducer's structural invariants.** M1 (Y = S + xU) and M2 (Y = S + x) both have a single causal state and C_μ = 0, yet ε_R = 0.1721 vs 0 (exact LP, re-checked). **Converse:** M3, the harmonic bath and C2-F are memoryful, with ε_R = 0. **Transducer structure is not T_R1-invariant:** a history-dependent translation raises C_μ. **Zero set at T = {id}:** an input-independent (generator-type) restriction. | **None.** Every causal channel has two presentations: exogenous noise with an input-dependent readout, and a responding state with a common readout (Boyd Thm 1; state enlargement). POMDP observation matrices are indexed by action, so E-B is native to this formalism. Barnett–Crutchfield pose the separation of instrument from system as an open question (§XIV.C.1, §XV). | MID/MID | MID/MID | **MID/MID** |

### 2.1 Skeptic corrections adopted

None of these changes a category.
- **Comparator 1.**
  - Counterexample 4 (non-Gaussian P0) is degenerate: a single protocol gives ε_R ≡ 0. It is replaced by C2-NG / C2-F.
  - The Tier-2 escape in counterexample 7 comes from time-mixing gains lying outside T_mono, not from φ.
  - The Gaussian Tier-2 example still fires the normalized covariance response, which is itself a comparator-1 quantity.
  - Ariel–Vanden-Eijnden eq. 1.7 is an N → ∞ weak limit. The exact harmonic shift is derived in R1_T_LADDER §4.
- **Comparator 2.**
  - Cell 4 is supplied exactly by M-A′; BRI1's non-Markovianity is not proved.
  - The M-B bound is tightened to 7.98e-3, because the BL norm of the witness is exactly 1.
  - Pollock et al. is upgraded to VERIFIED.
- **Comparator 3.**
  - The numbers become 0.0645 and 0.0660; the earlier values were Gauss–Hermite artifacts on kinked witnesses.
  - IQI is from Berk–Milz–Pollock–Modi, npj QI 9, 104 (2023), not from Quantum 5, 435.
  - Choi-divergence non-Markovianity can increase under IQI (Zambon §III).
  - Schatten-p non-Markovianity (Milz–Modi eq. 228) is not CP-contractive. So what is distinctive is the quotient zero set, not non-contractivity.
  - F_T contains anticipating families.
  - The Tier-1 invariance argument must use causal mixing.
  - "Nine theories" has seven distinct free sets.
- **Comparator 4.**
  - "S = {protocol}" is not an admissible ICP null.
  - Multivariate-response ICP exists (Borriero et al.), but it is Gaussian-linear.
  - The C2-F floor of 7.384e-2 is a skewness-difference floor, not a KS floor.
  - ICP statistics are not all "after one shared fit".
- **Comparator 5.**
  - The (P) margin is narrower than the analyst stated, because of Gong 2016 and Zhang 2013.
  - E1 is a PJS Prop. 4.1-type universal SCM. It is not the 2012 noise-switching construction.
  - D1's strict monotonicity requires continuous, strictly increasing CDFs.
- **Comparator 6.**
  - J-S Lemma 10 and eq. 26 were missed.
  - "Roles reversed" is replaced by the impossibility of a G-covariant class equal to T_R1.
  - "AIC cannot separate E-B from E-C" is too absolute: it holds at O(1) and fails in principle in the uncomputable regime.
- **Comparator 7.**
  - Counterexample 6 fails as stated, because D_KL^T ≤ log(number of protocols). It is replaced by the lattice / Rademacher family.
  - R2(b) holds only for universal, well-specified codes.
- **Comparator 8.**
  - "Not a Le Cam invariant / coordinate-free" applies only to the raw experiment. In E_T the zero set is Le Cam-invariant.
  - The location-family deficiency is ≤ 1 − 1/abs(A).
  - The Gupta–Henze–Klar tests cover elliptical laws only.
- **Comparator 9.**
  - MI does have an indicator-side per-group group (Wu–Estabrook Δ^(g), γ^(g)).
  - "Record-side vs latent-side" is cosmetic for invertible t_a.
  - The E-A absorption logic is MI's own configural logic.
- **Comparator 10.**
  - 0.2946 is C2-F's E₂± skewness witness, not ε_R^(E₂±); only ε_R^(E₂±) ≥ 0.2946/(2L) > 0 follows.
  - Bijective output relabelings indexed by the current input symbol preserve transducer structure.
- **Program-record erratum** (comparator 2; independently confirmed). C2-F as implemented in `R1/c2_controls.py` has K_a[k,j] = r^(k−j). Its records are exact AR(1) Markov chains: in continuous time, a Lévy-driven OU process. They are colored, not non-Markov. The docstring label "non-Markovian" is wrong at grid level and at path level. Numbers and verdicts are unchanged.

### 2.2 Thinnest margins

These are recorded because each is the closest any comparator came to RESTATED.
- **(M), comparator 8.** For two protocols at Tier 1, ε_R equals half the population version of Alvarez-Melis–Jegelka–Jaakkola eq. 7, using:
  - ground cost min(abs(x−y), 2), which is d_BL in coupling form;
  - invariance set F = O(k);
  - whitened inputs.

  It is not a known quantity only because nobody has defined or studied that cost. The Chebyshev form for three or more protocols and the Tier-2 copula/reflection form are absent from that literature.
- **(M), comparators 6 and 8.** The symmetry core of Theorem C, F1/F3 and M2 is known:
  - the J-S §4.1 asymmetry monotone and twirl;
  - Birrell symmetrization;
  - the HOS principle that a linear image of a symmetric law has no odd cumulants.

  The verdict-relevant zero set is a classical invariant-test null. In the nuisance-augmented experiment it is even Le Cam-invariant.
- **(P), comparator 9.** MI restates the **schema** of all five (P) ingredients:
  - carrier = MI;
  - mode selection = DIF / response shift;
  - back-reaction = impact / true change;
  - the identification limit = configural / Suppes–Zanotti triviality;
  - E-A absorption = configural / partial-invariance logic.

  It does not restate them as an **object**. No MI level equals T_R1 or T_mono on a continuous record, and ε_R is not a function of any MI statistic.
- **(P), comparator 8.** R1-PASS is, exactly, Blackwell garbling monotonicity applied after a Lehmann invariance reduction (§3, B).
- **(P), comparator 5.** Gong 2016 combines a shared readout, a per-domain declared class and an IPM fit. It fails RESTATED only because:
  - the readout is fitted, not certified;
  - its class is diagonal location-scale;
  - its residual plays no identification role.

### 2.3 DISTINCTIVE check

Each candidate is exhibited and tested against every comparator.

| Candidate statement | Defeated by | Reason |
|---|---|---|
| Theorem C: BRI1 escapes every linear interface class (symmetric P0, injective linear maps) | 1, 6, 8 | The HOS principle (Hinich; Subba Rao–Gabr). The Kubo/FDT prediction that the third-cumulant response K is nonzero, verified to ≤ 3.5e-12. J-S §4.1 Z₂-covariance. The Henze–Klar–Meintanis symmetry null read through Blackwell plus Lehmann. |
| Prop. G: liminf N_B·ε_R ≥ abs(K)·V*/(12 m₂^(3/2)) | 1; prior BRI1 supplement (ingredient J) | The FDT gives the coefficient from P0's 4-point function. At k = 1 the bound is asymptotically sharp (D5 analysis, evidence grade). The 1/N_B rate was already graded "structurally expected". |
| Tier-2 copula escape (7/7 A_abc, 3/3 Δρ, 1/N_B scaling) | 1, 9 | A_abc is a projected multi-time third-order response tensor, and Δρ is a second-order covariance response. The even channel's parametric twin is the polychoric comparison. It is evidence grade in any case. |
| Harmonic bath R1-NULL vs Duffing R1-PASS | 1, 2 | The Ford–Kac–Mazur / Zwanzig exogenous decomposition, plus Kubo. |
| An exactly Markov responding environment with ε_R > 0 (M-A); the four-cell independence results | 2 | These are consequences of the definition, not physical relations. |
| ε_R^mono > 0 implies restricted PT non-Markovianity | 3 | A short consequence of the PRL 120 Definition plus M1; PT can state it. |
| The carrier modulo T_R1 is the unique weakest readout-only sound assumption (Theorem C1; D5 analysis) | 8, 9 | It is a property of R1's own definition and elementary (atom counting, rank arguments). Its type is restated by MI and by Blackwell θ-independence. It is not part of the frozen R1 either. |
| The identification limit (Prop. E / E1) | 4, 5, 6, 7, 9, identification agent | Restated by Balke–Pearl, PJS Prop. 4.1, ICP's quantile construction, J-S eq. 26, CoCa §2.2, and Suppes–Zanotti / configural non-identification. |

**Reverse direction**, recorded for completeness. Some comparators yield relations that R1 does not:
- **Comparator 1:** for a Gibbs environment driven through the recorded variable, the leading-order Tier-1 ε_R is predicted from undriven 4-point correlations.
- **Comparator 2:** the GLE/linear-response route detects linear back-reaction, which ε_R discards.
- **Comparator 3:** PT signalling detects the harmonic bath's response.

---

## 3. Answers to the preregistered questions

**A. Is ε_R merely an existing generic nonlinear-response or process-distance quantity under renamed variables? — NO.**

Decisive arguments:
- **ε_R is not a response functional.** It annihilates mean response of every order and annihilates linear back-reaction: for Y_a = V[q_a] + ξ, ε_R = 0, and the harmonic bath has ε_R = 0 (comparator 1).
- **Its zero set depends on the declared T.** C2-F is nonzero under E₂± and zero under T_lin. The same covariance response is absorbed at Tier 1 and counted at Tier 2.
- **It neither implies nor is implied by** non-Gaussianity, cumulant response, non-Markovianity or signalling (comparators 1–3; all four cells occupied).
- **It cannot be a process functional.** ε_R ≡ 0 on every single-protocol family, while every process functional is a nontrivial functional of one process.
- **It is not a process distance.** Comb, strategy and Zambon distances are faithful and contractive. d_q has a nontrivial quotient zero set that does not survive processing: N(0,1) and N(0,4) lie in one orbit, but after y ↦ y + y³, d_q ≥ 0.0660. F_T is not a set of combs.
- **It is unrelated in magnitude** to Le Cam deficiency (comparator 8), and orthogonal to Gaussian-coded MDL (comparator 7).

Honest qualifications:
- **(i) A regime restatement holds.** BRI1's single-time Tier-1 calibration value is a renamed, normalized Kubo/FDT third-cumulant susceptibility: (V*/12)·abs(γ₁)·(1 + O(1/N_B)), with γ₁ set by P0's connected 4-point function. The calibration content is therefore standard physics.
- **(ii) The T-trivial core** of ε_R is a restricted classical analogue of a signalling distance (Barsse).
- **(iii) Two-protocol Tier-1 ε_R** is an instance of an invariant-OT discrepancy with a non-standard cost (§2.2).

None of these makes ε_R, with its quotient, distance and rule, an existing quantity.

**B. Is the quotient construction known mathematics, with the identification rule new only in application? — YES.**

The quotient is known mathematics:
- maximal invariants and invariant tests (Lehmann ch. 6);
- admissible-transformation groups (Stevens);
- quotient metrics and invariant OT (Cahill; Grave; Alvarez-Melis et al.);
- IPMs and symmetrization (Müller; Birrell);
- whitening that leaves O(k) (ICA prewhitening, Hyvärinen–Oja; affine-invariant scaled residuals, Henze–Klar–Meintanis);
- copulas, ranks and radial symmetry (Sklar; Rémillard–Scaillet; Genest–Nešlehová);
- the asymmetry monotone and twirl (J-S §4.1);
- Gaussian integration by parts, and Barbour's expansion.

The inferential form of the identification rule is also known:
- Blackwell garbling plus Lehmann invariance. Exact identity: under a common h, the maximal invariant of the T-reduced record sample is a θ-independent function of the latent sample.
- Measurement invariance.
- ICM modularity and shared mixing in interventional CRL.
- PT causal-break logic with known instruments.
- The exclusion restriction and nondifferential measurement.
- The physical precedent of "odd cumulants beyond a calibrated linear chain mean environmental backaction" (Beenakker–Kindermann–Nazarov 2003; Reulet et al. 2003).

What is new is operational only:
- a declared, independently calibrated, record-side interface group acting per protocol, behind one certified readout of the environment's instantaneous state, inside a two-layer readout Z → W = h(Z) → Y = t_a(W);
- a nonparametric minimax comparison of the maximal invariant;
- the verdict table, with MODE SELECTION and NO RECIPROCITY VERDICT;
- application to clamped physical environments.

**C. Is the common-carrier/readout certificate an unavoidable identifying assumption? — YES, in a qualified sense.** This answer follows the identification agent.

- **Some assumption from outside the records is unavoidable.**
  - By D1′, E-B and E-C have identical observational images at every family, so any level-α test of E-B has power ≤ α at every E-C alternative.
  - Every sufficient assumption is unrefutable from records. It must also declare which state variable counts as "the environment". For BRI1 itself, BRI-UPPER gives an exact E-B representation with the initial state as latent, and an exact E-C representation with the instantaneous state (Remark D3).
- **The carrier is the unique weakest readout-only assumption for Tier 1.** If only readouts are restricted and the environment law is left free, the carrier modulo T_R1 is necessary and sufficient for "ε_R^T_R1 > 0 ⇒ not exogenous" (Theorem C1). Two versions are proved:
  - **(a)** affine readouts and environment laws with densities. The obstruction is generically E2's mechanism.
  - **(b)** measurable readouts and finitely supported environment laws (atom counting).

  The synthesizer re-checked both proofs. Necessity for Tier 2 (T_mono) is **OPEN**.
- **Weaker readout-only assumptions** give only graded partial identification:
  - m possible readouts: counting of distinct orbits (C3);
  - mode-selection excess e: an exact common-marginal criterion, which is vacuous for single-time witnesses at e ≥ 1 (C4);
  - the reference-only kernel inclusion ker K₀ ⊆ ker K_a collapses to the carrier under the standing assumption (C5);
  - anchor channels remain carrier-type.
- **The carrier is not the only route.** An environment-side premise — global central symmetry of the whole environment law plus affine (or monotone∘affine) readouts — is incomparable with the carrier (C6). The disjunction of the two is strictly weaker than the carrier and still certifies:
  - BRI1's Tier 1;
  - BRI1's Tier-2 odd channel.

  **Only the Tier-2 even channel (Δρ) needs the carrier itself.**
- **Comparator support for unavoidability:**
  - MI is a "logical prerequisite" for comparing latent quantities;
  - PJS §2.3.4: whether an intervention is elementary must be settled by appeal to physics;
  - ICP: "known by design";
  - Blackwell's θ-independence;
  - universal transducer presentations;
  - J-S AIC is an alternative family of assumptions, but it is uncomputable and silent at BRI1's O(1) scale.
- **Category input.**
  - (M): STANDARD.
  - (P): the **type** of the certificate is restated (measurement invariance; exclusion of the protocol from the measurement equation; nondifferential outcome measurement). Its **form** — invariance modulo a declared, calibrated, protocol-dependent T, targeting the whole latent law, on a declared instantaneous state — is stated by no comparator. Hence MID.
- **Provenance.** Results C1–C6 are D5 ANALYSIS, derived in this audit and not externally checked. They do not change any verdict criterion.

**D. Does the product-latent construction prove non-identifiability when protocol-dependent readouts h_a are unrestricted? — YES.**

- **Theorem D1.** Take μ = ⊗_a P_a and h_a = π_a. Then h_a#μ = P_a exactly, for:
  - any family;
  - any index set (Łomnicki–Ulam product);
  - path level as well as grid level.

  The readouts are linear and surjective, so ε vanishes for every d_op with d_op(P, P) = 0.
- **Causal version (D2).** On BRI0's non-anticipating domain, a prefix-tree latent with 0/1 selection readouts gives an exact causal linear representation. The set of families with a causal-linear representation equals the non-anticipating families, which is grid-level E_univ. The exact rational checks K1 and K2 pass.
- **This is not new mathematics.** It is an instance of:
  - response-function / potential-outcome representations (Balke–Pearl 1994; Pearl 2009 Def. 4), where only the marginals are constrained (Holland 1986);
  - Kallenberg's randomization lemma and transfer theorem;
  - PJS Prop. 4.1;
  - CoCa §2.2;
  - Suppes–Zanotti;
  - J-S eq. 26;
  - configural non-identification;
  - Boyd et al. Thm 1;
  - BRI0's E_univ remark.

  It was correctly frozen pre-result (`82d311e`) and correctly not claimed as new. The only specialization R1 adds is that the readouts may be taken linear. So protection comes from the readout being common, not from linearity, and Theorem C1 locates that protection exactly.
- **Wording precision.** "zero set = E_univ" in R1_SYNTHESIS §2 should read "families with a causal linear representation = non-anticipating families = grid-level E_univ". With unrestricted linear readouts the zero set is every family.

---

## 4. Kill-condition check

STATE.md: "R1 is killed only if the object is trivial, unidentifiable, or reduces to non-Markovianity or to generic nonlinear response."

| Condition | Result | Decisive argument | Residue, stated plainly |
|---|---|---|---|
| Reduces to non-Markovianity | **Does not fire** | ε_R ≡ 0 on single-protocol families, while every non-Markovianity measure is a nontrivial functional of one process. All four (Markov or not) × (ε_R zero or positive) cells have exact members: harmonic bath and C2-F′; C2-F; M-A, which is Markov in all three senses with ε_R^T_R1 ≥ 1.915e-2; M-A′. GL(k) time-mixing moves record Markovianity without moving ε_R. | One-way links only. Protocol-dependent Markovianity implies ε_R^mono > 0. ε_R^mono > 0 implies restricted PT non-Markovianity. Neither converse holds. |
| Reduces to generic nonlinear response | **Does not fire for ε_R as defined** | Mean response of every order and linear back-reaction give ε_R = 0. C2-F has cumulant response and ε_R^lin = 0. The zero set depends on T. Gaussian families escape Tier 2. E2 gives ε_R > 0 with no response. The parametric harmonic control escapes with linear bath dynamics. A zero-skew asymmetric law is detected, and equal skewness can give different ε_R. | **BRI1's Tier-1 single-time PASS amounts to an FDT-predicted third-cumulant response plus Theorem C.** That is standard physics: ε_R = (V*/12)·abs(γ₁)·(1 + 0.235/N_B + …). The §6 flag also stands: ε_R^lin's power to discriminate back-reaction rests entirely on independent interface calibration. An uncalibrated nonlinear detector fires Tier 1 on an exogenous environment, which is why the frozen empirical rule requires the certificate. |
| Trivial | **Does not fire within the declared scope** | The zero set is nontrivial. Exact controls give 0 (C2-G, C2-NG, C2-F under T_lin, harmonic bath), and BRI1 gives > 0 at Tier 1 (derived) and at Tier 2 (evidence grade). | These triviality boundaries were all declared pre-result: Tier 2 at k = 1 (D1), unrestricted readouts (Prop. E / E1), and the expected trivialization at the join of T_lin and T_mono (unproved). ε_R is blind by design to every T-explainable response, including affine and Gaussian latent change and linear back-reaction. **R1-NULL does not mean "no response."** This is a narrowness, not triviality. |
| Unidentifiable within the declared scope | **Does not fire** | The certificate belongs to the frozen pre-result scope: the G2-08 certificate, the h ↦ h_a exclusion, and NO RECIPROCITY VERDICT when the carrier is unresolved. Given carrier PASS, ε_R > 0 soundly implies that Law(Z) depends on the protocol (Theorem A-BL; Theorem C1). | The identification is **conditional and cannot be tested from records**: no record statistic separates E-B from E-C (D1′). That is a portability limit. Which state counts as "the environment" must be declared (Remark D3); the pre-result G2-08 certificate does this implicitly by naming the instantaneous readout. Statistically, the finite-sample test (D4) is OPEN, and BRI1's single-time witness at N_B = 4 needs about 10¹¹ samples. That is an estimation problem, not an identification failure. |

No RESTATED verdict arose relative to any comparator, so there is no kill consequence for the owner to rule on.

---

## 5. Post-result items (POST-RESULT SYNTHESIS / STAGE-3 SEED)

None of the items below was used to set or change any verdict. Every classification above rests on frozen pre-result items only: T_R1, T_mono, d_op, the verdict table, "one latent-to-record map h for all protocols; no h_a", Prop. E, §10 E1/E2, and the G2-08 certificate.

- **Z_A** (interventionally sufficient predictive carrier state relative to a repertoire A). **Label: POST-RESULT SYNTHESIS / STAGE-3 SEED. RESTATED by comparator 10.**
  - It is Barnett–Crutchfield's causal equivalence (eq. 9) with the quantifier over future inputs restricted to A — the partial-channel case that Barnett–Crutchfield name and set aside.
  - Its sufficiency, minimality and uniqueness are their Prop. 3 and Thms 1–3, and Shalizi–Crutchfield Thms 1–3.
  - Restricting to a repertoire is native to controlled PSRs, which make predictions "upon doing" a test set.
  - A policy-class-relative interventional version is written out in Yang et al. 2026 (a preprint), whose Remark 3.2b concedes that it is not new.
  - **Caveat.** If "carrier" means the physical identity of the environment across protocols, comparator 10 neither supplies nor can supply it. Causal states are selected by predictive minimality, and state enlargement makes any channel look like a common readout of a responding state.
- **[h]_T** (the protocol-invariant readout equivalence class). **Label: POST-RESULT SYNTHESIS / STAGE-3 SEED.**
  - **Comparator 10: NOT restated.** The ε-transducer is unique up to state isomorphism and has no calibrated per-protocol readout class.
  - **Comparator 9: KNOWN-IN-NEARBY-FORM, not adjudicable as RESTATED**, because [h]_T has no frozen definition. Informally, "a readout defined only up to a declared group, and the same class in every group" is the conjunction of Stevens' admissible-transformation scale type and measurement invariance. The nearest formal objects are:
    - Lord equity and equating (van der Linden 2019, abstract level);
    - IRT invariance "up to linear transformations" (Rupp–Zumbo);
    - the Wu–Estabrook identified invariants;
    - Meredith 1964's GL(m) pattern indeterminacy;
    - and, from comparator 5, the interventional-CRL identifiability class ~CRL (von Kügelgen et al. Def. 2.6; Squires et al.).
  - Any Stage-3 novelty claim must be positioned against these. Not anticipated by any comparator is the program goal of **deriving** the class from 𝒦; that is a Stage-3 aim, not a result.
- **Measurement-invariance framing** (R1_SYNTHESIS §3(a), G2-09). **Label: POST-RESULT SYNTHESIS / STAGE-3 SEED. RESTATED by comparator 9.**
  - "One readout h for all protocols" is the Mellenbergh/Meredith definition f(Y given η, v) = f(Y given η), with V = protocol and η = environment state.
  - "Without it a protocol difference cannot be attributed" is Vandenberg–Lance's "logical prerequisite".
  - **Recommended wording** (credit, do not claim): "an instance of measurement invariance (Mellenbergh 1989; Meredith 1993) with the intervention protocol as grouping variable."
  - The limits to record alongside it:
    - **(i)** the record-side vs latent-side distinction is cosmetic for invertible t_a (saturated configural equivalence). The added structure is the nonparametric comparison of the maximal invariant, the declared, calibrated status of T inside a two-layer readout, and the external certificate;
    - **(ii)** R1 needs full distributional MI of h, which is stronger than strict factorial invariance;
    - **(iii)** no part of R1's certificate can be tested from records, because the latent dimension is unrestricted;
    - **(iv)** affine and Gaussian latent change are invisible to ε_R.
- **Other post-result items, discussed only.**
  - The "why instantaneous" clause is mirrored by the NJP 2016 restriction to a state that "has not interacted with the dynamics". SCM-sense independent noise holds for every closed system (PJS Principle 2.2), so R1's null is strictly stronger.
  - Checklist items 7, 9 and the injectivity condition parallel Meredith 1964a ("selection does not occur directly on the observables and does not reduce the rank").
  - The 10-item checklist has no comparator-10 counterpart. PT's GST calibration (White et al. 2022 §II D) is its closest analogue.
- **D5 ANALYSIS, NUMERICAL EVIDENCE.** These are scratch computations, not committed, and they change no definition, no WO-002 result and no part of the ladder. Base directory: `/tmp/claude-0/-home-user-vsctestinggrut/1a09ed24-aca1-5a3e-824d-0bafde87a0b5/scratchpad/`.
  - Kubo/FDT identity for K, three routes (`d5c1/`, `d5c1_skeptic2/k_three_routes.py`).
  - k = 1 BRI1 ε_R ratio (`d5c1_skeptic2/epsR_k1_bri1.py`).
  - Parametric harmonic control (`d5c1/parametric_harmonic_check.py`, `d5c1_skeptic2/parametric_check2.py`).
  - M-A, M-B, C2-F′ (`c2nm/`, `skep2/code/`).
  - PT examples (`pt_scripts/`, `sk3/scripts/`).
  - ICP checks (`skeptic/icp_checks.py`).
  - Trace contrast (`d5c5_skgov/code/trace_check.py`).
  - J-S counterexamples (`sk_scripts/cx.py`).
  - MDL (`c7mdl/`, `c7sk3/code/`).
  - Le Cam examples (`c8/check.py`, `sk8v2/skcheck.py`).
  - Transducer LP (`d5c10/scripts/c10_check.py`, `skep10/scripts/m1check.py`).
  - Identification checks K1–K5 (`d5_cd_checks.py`, `d5_cd_checks_output.json`).

---

## 6. What R1 borrows, and what is its own

**Borrowed.**
- **Mathematics.** Everything listed under B. Its Tier-1 mechanism is the classical HOS principle and the J-S Z₂-covariance fact. Its zero sets are classical nulls: affine equivalence, copula equality modulo reflections, group families.
- **Identification logic.**
  - measurement invariance;
  - Blackwell θ-independence plus invariance reduction;
  - ICM modularity / shared mixing;
  - PT causal-break attribution;
  - the exclusion restriction / nondifferential measurement;
  - the necessity of an extra-statistical assumption: PJS Prop. 4.1, Suppes–Zanotti, Balke–Pearl, configural non-identification.
- **Non-identifiability.** Prop. E / E1 / D2 are standard representation results.
- **BRI1 calibration physics.**
  - K is a classical Kubo response fixed by P0's connected 4-point function (FDT).
  - C2 and Δρ are second-order noise responses; A_abc is a projected third-order response tensor.
  - The 1/N_B rate is structurally expected.
  - The harmonic zero is the Ford–Kac–Mazur / Zwanzig exogenous decomposition.
  - "Odd cumulants beyond a calibrated chain signal backaction" has a mesoscopic precedent (Beenakker–Kindermann–Nazarov 2003; Reulet et al. 2003).
- **Post-result.** Z_A comes from causal states / PSRs; the MI framing comes from MI.

**Its own** (operational content only, stated without inflation):
- **One physical observable assembled from standard parts:**
  - a declared, independently calibrated, record-side interface group acting per protocol (Tier 1: GL(k) with translations; Tier 2: coordinatewise strictly monotone maps modulo reflections);
  - placed behind one certified common readout of the environment's instantaneous state;
  - with a minimax bounded-Lipschitz quotient radius over one shared law.
- **The verdict table:** R1-PASS / R1-NULL / NO RECIPROCITY VERDICT / MODE SELECTION.
- **A deliberately conservative null.** T-explainable response — linear back-reaction, affine and Gaussian latent change — is classed R1-NULL. This departs from the comparator-1, MI, PT and ICM/SMS readings of "response". It makes R1-PASS a strictly narrower, one-sided certificate of a total causal effect.
- **Derived constants and rates for its own object:** Theorem F (constants 1 and 1/2) and Prop. G. These apply standard tools.
- **Placement of one known environment (BRI1) on the declared ladder:** Tier 1 derived, Tier 2 at evidence grade.

**Not its own:** any new mathematics, and any new physical relation, constraint or prediction.

---

## 7. Unverified citations and open items

**UNVERIFIED or PARTIAL citations.** No verdict rests on any of these alone.
- **Comparator 1.**
  - Kubo 1957 primary text (publisher returned 403); the classical formula was confirmed numerically by three routes.
  - Bochkov–Kuzovlev 1977; Lee–Schetzen 1965.
  - Ford–Kac–Mazur 1965 and Zwanzig 1973 primaries.
  - Brillinger's filter theorem (derived instead).
  - Hinich's normalized-bispectrum null (secondary source).
  - Subba Rao–Gabr 1980; Comon 1994; Mendel 1991.
- **Comparator 2.** Mori 1965, Ford–Kac–Mazur 1965 and Zwanzig 1973 content; Darsow–Nguyen–Olsen 1992; Laine–Piilo–Breuer EPL 2010 (via RMP); Kiefer et al. arXiv:2505.15665 (reused, not re-verified).
- **Comparator 3.** Milz–Pollock–Modi PRA 98; White et al. Nat. Commun. 2020; Breuer–Amato–Vacchini NJP 2018; Kofler–Brukner (abstract). Budini D_Q for classical baths is an interpretation, not a computation.
- **Comparator 4.** Borriero et al. 2025 (abstract only); JRSS-B typeset equation numbering.
- **Comparator 5.** PJS was read from a mirror: SHA-256 identical across the two auditors' copies, but not byte-compared with OAPEN. The Budhathoki 2021 venue was confirmed by search only.
- **Comparator 6.** J-S IEEE typeset numbering; Lemeire–Janzing 2013 full text; J-S refs [33]–[35].
- **Comparator 7.** Slope (KAIS) and Sloppy texts; Rissanen 1996; Barron–Cover 1991; Hyvärinen–Pajunen 1999; Reisach et al. 2021 (cited only as quoted); von Davier–Holland–Thayer 2004; StruBI arXiv:2606.18834 (abstract).
- **Comparator 8.** Blackwell 1951 and 1953 full texts; Le Cam 1964 (via Mariucci); Torgersen 1991 content; Boll 1955; Hall–Wijsman–Ghosh 1965; Lehmann–Casella §1.4 (via Duerinckx–Ley–Swan); Lehmann–Romano numbering. The I3 zero-set characterization is at sketch grade.
- **Comparator 9.** Meredith 1993 full text; Vandenberg–Lance body; Millsap 2011/2012 content; Mellenbergh 1989 (via Lubke); Reiersøl 1950; Jennrich 1970; Byrne–Shavelson–Muthén 1989 (DOI unverified); Millsap–Yun-Tein 2004; Bauer 2017; Azevedo et al. 2012; Santos et al. 2013 full text.
- **Comparator 10.** Jaeger's OOM GL(n) gauge; Givan et al. definition; the Barnett–Crutchfield sequel (ref. [86]); Boots et al. and Brodu–Crutchfield (abstract level); Venegas-Li et al. venue.
- **Identification agent.** Pearl, *Causality* book text; Kallenberg 2002 (secondary statements only); Kechris Thm 17.41 (not re-inspected); Robins 1986 content; Meredith via Merkle–Zeileis; Comon (secondary); Angrist–Imbens–Rubin published-version numbering.
- **Preprints**, verified as text but not established objects: Yang et al. arXiv:2609.11959; Boyd et al. arXiv:2512.02193; Suhr et al. arXiv:2601.23026.

**Open items.**
1. **Tier-2 necessity of the carrier** (a T_mono analogue of Theorem C1) — OPEN.
2. **M5**, a uniform multivariate Edgeworth expansion for Tier-2 theorem grade — OPEN (pre-existing).
3. **D4**, a finite-sample test of ε_R = 0 — OPEN. Candidate templates: ICP's Theorem 1 coverage machinery; GROW e-statistics (Pérez-Ortiz et al. 2024); the classical nulls behind F3 and M2 (Henze–Klar–Meintanis; Genest–Nešlehová). Estimation should use the per-witness form, not plug-in d_BL.
4. **Exit-gate item (iii):** the external check of A-BL, F, M1–M3 and Prop. G is still pending. The D5 analysis results C1–C6 and the comparator-8 I3 characterization are not externally checked either.
5. **Trivialization of the join of T_lin and T_mono** — expected, not proved.
6. **The C6 disjunctive certificate** (carrier OR global environment symmetry plus affine readouts) is strictly weaker than the carrier and covers Tier 1 and the Tier-2 odd channel. It is recorded for the owner. It is not a definition change.
7. **The FDT route** (comparator 1) is a possible cross-check of E-C for thermal environments, conditional on the common readout. It is a Stage-3 seed.

**Recommended record edits.** None were made here; this audit is read-only.
- R1_SYNTHESIS §5: fill from this audit.
- R1_SYNTHESIS §2: precise wording for the E_univ statement (see D).
- R1_SYNTHESIS §3(a): MI wording and limits (see §5).
- Harmonic-bath note: "R1-NULL does not mean no causal response".
- Prop. G: describe it as asymptotically sharp at k = 1 on BRI1 (evidence grade), not only as a lower bound.
- `R1/c2_controls.py` docstring: C2-F is colored, not non-Markov. Numbers unchanged. C2-F′ is proposed as the genuine non-Markov-record zero control; it has been checked only by exact predictor weights and has not been run as a work order.