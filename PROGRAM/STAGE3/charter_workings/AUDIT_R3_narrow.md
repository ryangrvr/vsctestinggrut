# Pre-freeze audit, round 3 (narrow scope): the round-2 replacements

**Subject:** `PROGRAM/STAGE3/STAGE3_CHARTER.md` (2754 lines, untracked, worktree `/tmp/claude-0/mainwt`).
**Scope:** only the text changed in round 2 (FREEZE_VERIFICATION §7, "Where" column). The exact
old/new text was taken from the builder's edit scripts `scratchpad/s3/edits/r2a.py` to `r2j.py`.
**Mode:** read-only. No repository file was edited, created or committed.
**Constraint kept:** no candidate law 𝒦 is proposed, sketched or exemplified. Every construction
below is an abstract **CHARTER TEST** pattern. Candidate check of the charter: PASS.
**Severity:** BLOCKER = must fix before freezing; MAJOR; MINOR. "Hostile reading" means the
reading CV-1 obliges an auditor to adopt when the text is ambiguous. Self-tests are judged under
T-1 and the §24.2 convention.

---

## 1. Question 1: new hidden kills and new loopholes

### BLOCKER

**B1. §1.3 inert-relatum deletion kills the size test on every lock fiber with a unique realized Π (new in round 2).**
- **Text:** "Before this test, every relatum that lies in the same block in every Π realized on
  Sol_ι, and that an RB or SPS template applied to 𝒞_ι alone assigns to that block, is deleted
  from V_ι".
- **CHARTER TEST (coincidental agreement).** The lock fiber has one realized Π (M(ι) = 1), the
  ordinary case for a GENERATED-WEAK card and for the platform-matched fiber. Then every relatum
  meets the first condition. The second condition names "an" template, with no cost bound and no
  uniformity:
  - Per-relatum reading: some template (RB1 label, RB2 threshold at any level, RB6 ball) puts each
    relatum into a block matched to its Π-block, so V_ι is emptied.
  - Most charitable reading (one template for all deletions): any 2-block template output agrees
    with Π on at least n/2 relata once its blocks are matched to S and E, so at least n/2 relata
    are deleted.
- **Arithmetic.** With M = 1 and trivial G_ι, the size test needs log₂(2^n′ − 1) ≥ 6, i.e. n′ ≥ 7
  surviving relata.
  - At n = 8 to 13, at least 4 to 7 relata are always deleted, so n′ ≤ 6 and the test fails
    whatever the template.
  - At n = 16 it fails as soon as the best of the hundreds of RB/SPS outputs agrees with Π on 10
    relata, which is to be expected.
- **Effect.**
  - S4 CARD-UNDIFFERENTIATED for essentially every honest card whose lock fibers have a unique Π.
  - It flips ST-6 (generic lock fiber) and ST-11's second branch to an S4 terminal (§3).
  - It also contradicts §2.3: "𝒜_Π^hand is never reduced by standard selectors; … the b_Π size
    test (§1.3) … use it as defined here."
- **Replacement wording (§1.3, last two sentences of "Nontrivial"):**
  > "Before this test, inert relata are deleted. If one RB or SPS template τ of cost ≤ ℓ_dec, the
  > same template on every lock fiber, applied to 𝒞_ι alone returns a nonempty set D_ι as one whole
  > output block; D_ι lies within a single block of every Π realized on Sol_ι; and, on a fraction
  > ≥ p_dec of the AI-3 draws on which τ's corresponding block is nonempty, that block lies within a
  > single block of every realized Π, then D_ι is deleted from V_ι. At most one template is applied,
  > and no relatum is deleted on its own. 𝒜_Π^hand, G_ι and M(ι) are computed on V_ι ∖ D_ι. This
  > is the only reduction of V_ι or 𝒜_Π^hand by a template (§2.3)."
- **Also:**
  - §2.3: "𝒜_Π^hand is never reduced by standard selectors, except by the inert-relatum deletion
    of §1.3;".
  - D-13: add "inert relata deleted by one uniform template before the size test (§1.3)".
- **Check.**
  - R2-M3's padding (relata isolated by 𝒞, or weakly coupled and always in E) is still deleted:
    an RB3 degree-0 or RB2 weight-threshold block, reliably inside E across AI-3.
  - A template that agrees with the law's Π only by chance on one instance deletes nothing.

**B2. Q5 split test: a trivial split makes every forced relation NONJOINT (the round-2 fix of R2-M7 does not hold).**
- **Text:** "take any L₀ split 𝒦 ≡ 𝒦₁ ∧ 𝒦₂ … in which neither 𝒦₁ nor 𝒦₂ implies 𝒦 on Dom_pre
  (any Ξ-level predicates R₁, R₂ ⊇ Sol with R₁ ∧ R₂ ≡ 𝒦 on Dom_pre may be offered); if, on every
  instance of 𝓘, 𝒦₁ alone fixes the realized interface value and 𝒦₂ alone fixes the response
  values Obs_Π(Ξ) at that instance's realized interface, ℛ★ is NONJOINT."
- **CHARTER TEST (trivial split).** Let u*(ι) be the realized interface value and r*(ι) the
  realized response values read at it. A reviewer offers:
  - R₂ := "Obs read at u*(ι) equals r*(ι)";
  - R₁ := "u(Ξ) = u*(ι) ∧ (𝒦 ∨ ¬R₂)".
- **Why it qualifies.**
  - Both contain Sol.
  - R₁ ∧ R₂ = (u = u*) ∧ R₂ ∧ 𝒦 = 𝒦, because Sol already satisfies the first two conjuncts.
  - Neither part implies 𝒦: Dom_pre has non-solutions with the realized interface and another
    response, and non-solutions with the realized response.
  - R₁ alone fixes the interface and R₂ alone fixes the response, so the text returns NONJOINT.
- **Effect.** This applies to every card whose realized response at the realized interface is
  determined on each instance, which covers every honest forced relation. It is a universal S5
  CARD-NONJOINT for any honest card that reaches Q5. The only guard, "neither implies 𝒦", is
  defeated by mixing 𝒦 into a disjunct, the device NR-17 now forbids but Q5 does not.
- **Replacement wording (Q5, fourth bullet):**
  > "– the coupling is not carried by the instance inputs alone. Take any L₀ split
  > 𝒦 ≡ 𝒦₁ ∧ 𝒦₂ offered by the author or a reviewer in which neither part implies 𝒦 on Dom_pre,
  > and each part's Price_min (the L_stmt of its shortest statement exhibited by any party) is
  > strictly below Price_min(𝒦). Ξ-level predicates R₁, R₂ ⊇ Sol with R₁ ∧ R₂ ≡ 𝒦 on Dom_pre may
  > be offered on the same terms, so a part that restates 𝒦 or contains it as a disjunct never
  > qualifies. If, on every instance of 𝓘, every Ξ ∈ Dom_gate(ι) satisfying 𝒦₁ has that
  > instance's realized interface value, and every Ξ ∈ Dom_gate(ι) satisfying 𝒦₂ has, read at
  > that realized interface, that instance's realized response values, ℛ★ is NONJOINT."
- **Check.**
  - CT-82 (two instance-indexed pins, each cheaper than 𝒦) is still NONJOINT, including the
    one-clause entangled form of R2-M7 reading B.
  - The trivial split is excluded, because each part contains 𝒦.
- **Add a CT row:** "CT-95 | A reviewer's trivial Q5 split: one part fixes the realized interface
  and contains 𝒦 as a disjunct; the other fixes the realized response | Q5 (parts cheaper than
  𝒦) | No effect".

### MAJOR

**M1. §2.5 c_J(b): Obs(M) is undefined, the realization condition can be vacuous, and the NULL-M guard does not cover compositions.**
- **Text:** "(b) for every admissible comparison class M: a B-HB family, a composition of B-HB
  families within the frozen ranges, or a model class of an SFP framework published before the
  card's freeze and stated without reference to the card, to ℛ★ or to any lock observable; that
  realizes Im ∩ FB …; with its constants fitted and with the card's realized interface values u
  (Π, carrier class, [h], T_Π and the declared interface statistics) supplied … the codimension of
  Z(ℛ★) ∩ Obs(M) in Obs(M)."
- **Defects.**
  - (a) **Fitted point.** If "with its constants fitted" fixes M at its fitted values, Obs(M) is
    M's output at the finitely many realized u. Its dimension is 0, so the codimension is 0
    whenever Z(ℛ★) ∩ Obs(M) ⊇ Im ∩ FB is nonempty. Every qualifying M then gives c_J = 0. This
    contradicts the family-cap logic ("credited once"), CT-78, ST-10 and Appendix A. CV-1 selects
    this reading.
  - (b) **Vacuity.** If Im ∩ FB = ∅, every M "realizes" it vacuously. An auditor can then pick a
    class whose image satisfies ℛ★ identically (for example an exogenous, zero-response family),
    and c_J = 0.
  - (c) **Guard scope.** Grammatically, "stated without reference to the card, to ℛ★ or to any
    lock observable" qualifies only SFP classes, but D-13 says the NULL-M guard applies to all
    comparison classes. CHARTER TEST (ℛ★-tailored composition): an auditor writes a B-HB
    composition whose coupling parameter is a function of the supplied u, chosen so that the
    composition's response satisfies ℛ★ for every value of its other constants. It is cheap
    (≈ L_stmt(B-HB) + L★), realizes Im ∩ FB with shared constants, and gives c_J = 0. Q3(b)'s
    "a family" has the same gap (outside scope, but this is how c_J(b) and Q3 become jointly a
    kill).
  - (d) M is not told it receives the card's instance inputs through θ_dict (§2.2(iii)). Without
    them, every instance-varying datum needs a per-instance constant, which prices M out.
  - (e) "The declared interface statistics … supplied" contradicts c_ι ("dynamical interface
    statistics are coordinates computed from the same standard model, not conditioning values")
    and the single-model rule (§2.2).
- **Consistency with Q3 once fixed.** With constants free and the guard applied to every M, an M
  whose image lies in Z(ℛ★) and that realizes nonempty Im ∩ FB is one of two things. Either ℛ★
  holds identically on a standard family, which is STANDARD-GENERIC so Q3(b) fails anyway. Or the
  card's standard-realizable data lie in a standard sub-class that implies ℛ★, the intended NULL-M
  result. No joint kill remains.
- **Replacement wording (§2.5 (b)):**
  > "(b) for every **admissible comparison class** M: a B-HB family, a composition of B-HB
  > families within the frozen ranges, or a model class of an SFP framework published before the
  > card's freeze. Every such M is stated without reference to the card, to ℛ★ or to any lock
  > observable. Its parameters are constants of M, shared across instances or per instance, and
  > are not functions of u, of ℛ★ or of the card's inputs except through θ_dict. M receives at
  > zero price the card's instance inputs through θ_dict (§2.2) and the card's realized Π, carrier
  > class, [h] and T_Π on every instance; its declared interface statistics are computed from M
  > itself under the single-model rule (§2.2); generating the interface is a gate, never a credit
  > (§4.3(b)). M qualifies if it realizes Im ∩ FB (non-standard realizations are scored by their
  > own kill conditions and never disable this clause) and Price(M) ≤ Price(𝒦) at the same p. If
  > Im ∩ FB is empty, (b) does not bind. The value is the codimension of Z(ℛ★) ∩ Obs(M) in Obs(M),
  > where Obs(M) is M's image over the lock family with M's constants free over their ranges; the
  > fitted values only show that M realizes Im ∩ FB, and they enter Price(M). Here Price(M) := …
  > [unchanged]. If no class qualifies, (b) does not bind."
- **Also:** D-13, "NULL-M guard (every comparison class stated without reference to the card or
  ℛ★, with parameters independent of u)". Owner note: give Q3(b)'s "a family" the same guard.

**M2. §2.5 family cap: the price condition reopens CT-78 for compact cards and lets "decorated near-copies" inflate N_dist; ST-10's "credited once" does not follow.**
- **Text:** "c_fam := the minimum, over every admissible comparison class M of (b) … that realizes
  Im ∩ FB on all of I_𝒦 … with each constant shared across instances wherever one shared value
  realizes Im, and per instance otherwise … If no class qualifies, the family cap imposes no
  bound."
- **Defects.**
  - (a) The cap inherits (b)'s condition Price(M) ≤ Price(𝒦). For a compact card (App. A,
    ≈ 720 bits), a B-HB family stated in L₀ with its shared constants can cost more. Then no class
    qualifies, there is no bound, and a law constant pinned on every instance earns
    100 · p★ = 1000 bits. This contradicts CT-78, ST-10 and App. A's "credited once".
  - (b) **CHARTER TEST (decorated near-copies).** The 𝒞 type has few structural classes plus a
    continuous label whose effect on Im is small but nonzero, in directions ℛ★ leaves free. §1.5
    (i) does not delete the label (replacing it changes Im) and (iii) holds (the images differ),
    so N_dist = 100. Any standard M must then fit the label shifts with per-instance constants,
    which prices it out, so the cap does not bind. This is R2-M12 defeated by a tiny effect.
  - (c) "realizes Im" contradicts "realizes Im ∩ FB" in the same sentence. Read literally, one
    non-standard point blocks all sharing, which reopens CT-83 for the cap.
- **Why no price condition is needed.** The cap is a rank count of ℛ★'s equations on shared
  constants. A large M with free constants cannot lower that rank artificially once M is guarded
  as in M1.
- **Replacement wording:**
  > "**Family cap:** c_fam := the minimum, over every class M admissible in (b), its price
  > condition excepted, that realizes Im ∩ FB on all of I_𝒦 (receiving inputs and u as in (b)),
  > of the codimension of Z(ℛ★) ∩ Obs_fam(M) in Obs_fam(M). Obs_fam(M) is M's joint image over I_𝒦
  > with its constants free; each constant takes one value on each group of instances on which one
  > value realizes Im ∩ FB (the coarsest such grouping), and one value per instance otherwise
  > (κ_fam likewise). A freedom that M carries in one shared constant is credited once per group,
  > not once per instance. If no class qualifies, the family cap imposes no bound."
- **Check.**
  - CT-78 is credited once (one group).
  - Near-copies are credited once per structural class: the pins are shared within a class, and
    the label shifts are free per-instance coordinates that ℛ★ does not pin.
  - Honest random instances keep N·c, because their pins are independent.

**M3. §2.5 fixed-class fibers: skipping singleton fibers creates a fragmentation loophole (new in round 2).**
- **Text:** "the minimum is taken over the fibers that contain at least two realized interface
  values differing in Π, carrier class or a declared interface statistic", while
  "b_J := min{N_dist · min over ι of [p★·min(c_ι, c_J, c_lock) …], …}".
- **CHARTER TEST (fragmented class).**
  - X_T makes T_Π instance-specific, so every fiber is a singleton except one pair of instances
    sharing T_Π.
  - ℛ★ is joint on that pair and is a single-axis Γ-pin at every other instance's own T_Π.
- **Effect.**
  - c_J comes from the one qualifying fiber, so it is ≥ 1.
  - c_ι on the singleton instances counts the Γ-pin, because a slice codimension inside FB(u) sees
    single-axis restrictions.
  - Q5's split test needs "every instance", so it does not fire.
  - Result: b_J = N_dist·p★ ≈ 1000 bits, of which 98 % is pins whose jointness is never witnessed
    (DEF-14). Before round 2 the same configuration was a kill (R2-M5); it is now a loophole.
- **Replacement wording (b_J):**
  > "b_J(ℛ★) := min{ N_fib · min over ι ∈ I_𝒦 of [p★·min(c_ι, c_J, c_lock) + min(κ_ι, κ_J,
  > κ_lock)], p★·c_fam + κ_fam }, where N_fib ≤ N_dist counts the structurally distinct credit
  > instances whose realized interface values lie in a fiber that qualifies under the fixed-class
  > rule. The minimum still runs over all of I_𝒦."
- **Also:**
  - §1.5: "multiplied by N_fib".
  - C5 and C11: list N_fib.
  - App. A note: "N_fib = N_dist when ℛ★ uses only catalogue classes, or T_Π is the same on every
    instance".
  - Add CT-96: "Fragmented class: T_Π made instance-specific so that one fiber witnesses jointness
    and the other instances carry single-axis pins | §2.5 N_fib | only instances in a qualifying
    fiber count".
- **Not a kill:** a single odd instance (for example AI-1) merely does not count.

**M4. §1.4 (iv): "whitening first" makes every generated T_Π outside 𝒯 that does not contain T_lin inadmissible (new in round 2).**
- **Text:** "(iv) normalization: s is the frozen centering and whitening of T_lin followed by a map
  built from T_Π alone". Round 1 read "s commutes with the frozen centering and whitening of
  T_lin; otherwise any scale constant … is priced".
- **Why it fails.**
  - Whitening w satisfies w(cP + b) = w(P) for every c > 0 and b, and w(A#P) = w(P) for every
    A = HΣ_P^(−1/2) with H symmetric positive definite: a family of dimension k(k+1)/2 + k.
  - Since s = g∘w, (ii) maximality forces T_Π·P to contain all those images, i.e. most of P's
    T_lin-orbit.
  - Hence a generated class strictly between E₂± and T_lin outside 𝒯, or a generated subclass of
    T_mono larger than E₂±, can never meet (i)–(iv).
  - ε^{T_Π} is then undefined and every ε^{T_Π} relation fails Q8. SCOPE-Q with a non-catalogue
    T_Π is possible only when T_Π ⊋ T_lin (and T_Π ⊉ T_mono, else ⊇ J).
- **Effect:** it closes most of the space of generated interface classes that §1.4 ("Generated
  T_Π outside 𝒯") exists for.
- **Replacement wording:**
  > "(iv) **normalization:** s is the frozen canonical reduction of one catalogue class contained
  > in T_Π and declared in C7 (centering and whitening for T_lin, Cholesky innovations for T_caus,
  > per-coordinate standardization for E₂±, normal scores for T_mono), or the identity if T_Π
  > contains no catalogue class, followed by a map built from T_Π alone; no fixed bijection of
  > record space follows it, and any scale constant in s is a priced IP-5 constant."
- This keeps R2-A m5's protection against a fixed post-map.

**M5. §1.3 T_Π provenance test: "L₀-defines within c_dec bits" reads as definability from X_T's inputs (new in round 2).**
- **Text:** "The test also fails if X_T's definition contains, or L₀-defines within c_dec bits,
  the template-to-Ξ map, a protocol template, or the action of the driven S-variable on Ξ (its
  flow, linearization or response)."
- **Hostile reading.**
  - X_T reads Ξ and Π. When the driven S-variable is identifiable from Π (one S-variable, or a
    canonical sum), its action on Ξ is definable from X_T's inputs in a few tokens.
  - Equally, any X_T that computes the joint linearization as an intermediate, and uses only the
    E–E block, "L₀-defines" the S–E block within c_dec bits.
  - Then carrier PASS is definitional and every reciprocity relation is CARD-DEFINITIONAL.
- This is the definability-closure pattern that round 2 fixed in IP-6 (R2-M1) by adding "and is
  used as that item".
- Second defect: "does not count only if it is an element of a catalogue class" (that is,
  non-catalogue coincidences count as failures) conflicts with the next sentence (a coincidence
  shifts the burden to the card).
- **Replacement wording:**
  > "The test also fails if X_T's definition contains, or computes and uses in building an element
  > or generator of T_Π, a term L₀-equivalent within c_dec bits to the template-to-Ξ map, a
  > protocol template, or the action of the driven S-variable on Ξ (its flow, linearization or
  > response); content merely definable from X_T's inputs does not count. A catalogue-class element
  > that coincides with some protocol's effect does not count if X_T's definition contains none of
  > this content. If T_Π contains, on a lock fiber, a non-catalogue t_a with P_a = t_a#P_{a₀}
  > within 2^(−p★), the card bears the burden of showing that the provenance test passes."

**M6. PC-6 record-factorization test (and the sentence it enforces) literally convicts Obs.**
- **Text:**
  - "No component evaluates, estimates or recomputes (from Ξ or otherwise) a record law P_a, any
    functional of Γ_Π, …".
  - "if an auditor exhibits an L₀ map F of length ≤ c_dec, not constant on Dom_gate, with a
    component's output = F(Γ_Π) on Dom_gate, the component recomputes a functional of Γ_Π".
- **Why it fires.** Obs is a card-supplied component (§1.2) and its output is Γ_Π = id(Γ_Π),
  with F = id short and not constant.
- **Effect.**
  - Read literally, every relation depends on the illicit read, so it is CARD-DEFINITIONAL at S3.
  - This flips ST-6 and ST-11's second branch to S3.
  - The sentence predates round 2; the test was edited in round 2 ("not constant"). It is a
    one-word fix.
- **Replacement wording:**
  > "No component other than Obs evaluates, estimates or recomputes (from Ξ or otherwise) a record
  > law P_a, and no component evaluates, estimates or recomputes any further functional of Γ_Π, ε,
  > d_op, P★, a chart coordinate, a battery verdict or a charter scoring function."

  > "… with the output of X_Π, X_Z, X_h, X_T, s_T or Emb = F(Γ_Π) on Dom_gate, that component
  > recomputes a functional of Γ_Π."

**M7. NR-1's round-2 parenthetical ("flagged only for its PS-5 content") flags every Markov rule under PS-5's operational definition, and flips ST-6.**
- **Text:** "(a stochastic transition rule of 𝒦 is flagged only for its PS-5 content, §4.1)".
- **Why it flags everything.** PS-5 is "any input from which a standard theorem … derives …
  detailed balance … or a fluctuation–response identity of any order".
  - Kolmogorov's criterion derives detailed balance from ST-6's rule.
  - The NESS FDR (Agarwal; Seifert–Speck) is derivable from any Markov generator with a smooth
    stationary law.
  - So the "content" reading flags every stochastic rule. Flagged and undeclared → RELOCATED.
    Declared and used by ℛ★ → §5.6 RELOCATED.
- **Effect.**
  - R2-A m8's purpose (do not flag every stochastic rule) is not met.
  - ST-6, which stipulates "no clause flagged by NR-1", gets terminal S3 instead of S5. NR-1
    itself says "(syntactic …)", so the parenthetical should say so too.
- **Replacement wording:**
  > "(a transition rule of 𝒦, stochastic or not, is flagged only where its unfolded statement names
  > or encodes a PS-5 structure: a temperature; a Gibbs, energy-weighted or maximum-entropy form;
  > an explicit reversibility, detailed-balance or KMS condition; an invariant or reference
  > measure. PS-5 structure that a standard theorem derives from an unflagged rule is generated; it
  > is governed by NR-12(b) and NR-17's last sentence, not flagged here.)"
- **No loophole:** generated PS-5 still makes every claim through it STANDARD-IMPLIED (NR-12(b),
  CT-75).

**M8. NR-10(e) and (n) still demand FAIL; ⊥ is not accepted (residual of R2-B4).**
- **Text:**
  - (e) "the carrier derivation returns FAIL";
  - (n) "on such an instance (… the auditor chooses) … X_h and X_T must return carrier FAIL or
    MODE SELECTION".
- **Problem.** The E2 configuration has an environment law independent of the protocol. For a
  card whose X_Π needs S–E interaction to differentiate, X_Π (or X_Z) returns ⊥ there, so X_h and
  X_T return ⊥, not FAIL. The auditor also chooses the instance and the Ξ.
- **Effect.** Under CV-1, (e)/(n) fail, the carrier is not GENERATED, and the card is
  CARD-NONGENERATIVE. That is a near-universal kill.
- **Rule elsewhere.** HB-8 and DIF-5(e) require only "never returns R1-PASS".
- **Replacement wording:**
  - (e): "… the carrier derivation does not return PASS (it returns FAIL, MODE SELECTION or ⊥);"
  - (n): "… the auditor supplies, at no price to the card, the protocol-indexed readout the
    configuration needs. At a Ξ of such an instance at which X_Π and X_Z are defined (if there is
    none, the card's realized Π and Z_Π from a lock fiber are substituted, as in Q3(c)), X_h and
    X_T, given that readout, must not return carrier PASS."

**M9. NR-10(f): the scope of "named" is ambiguous; on the hostile scope, any branched construction is SUPPLIED (new in round 2).**
- **Text:** "or if it chooses among named classes, groups or readouts by a branch (ite, case split,
  table or threshold) on any condition".
- **Hostile scope.** If "named" qualifies only "classes", then:
  - an X_T whose constructed group depends on a case split inside the construction (for example a
    degenerate-case branch) supplies T_Π;
  - an X_h that picks a Ξ-variable as readout by an extremal or threshold criterion supplies [h].
  Both become CARD-NONGENERATIVE, which kills legitimate constructions.
- **Second defect.** The constant-output clause uses Dom_gate, while NR-3's W-pipe uses
  Dom_gate^X. A construction whose off-Sol group is inadmissible (outside Dom_gate) is "constant on
  Dom_gate" and so SUPPLIED, even though NR-3 passes.
- **Replacement wording:**
  > "A component supplies a class or group (PS-3/PS-4) if its output is the same at every
  > Ξ ∈ Dom_gate^X as a function of its definition alone, or if it selects, by a branch (ite, case
  > split, table or threshold) on any condition, among classes, groups or readouts that its
  > definition names (identifies by a constant symbol, literal or menu index) rather than
  > constructs from Ξ-level structure. A case split inside a construction, or the selection of a
  > Ξ-variable as readout by an extremal or threshold criterion, is not a named choice; it is
  > tested by NR-3, NR-6 and DEF-17(a)."
- CT-91 (a menu branch) is still caught.

**M10. NR-17's round-2 superset guard is over-broad: it reopens CT-77 (new loophole).**
- **Text:** "A Ξ-level predicate R ⊇ Sol may be offered as 𝒦₂ … only if its shortest exhibited
  statement contains no clause of 𝒦 and no condition L₀-equivalent within c_dec bits to one".
- **CHARTER TEST (anchored imposition).**
  - 𝒦 = C₀ ∧ C₁, with C₀ cheap and C₁ costly.
  - The cheap predicate C₀ ∧ R₀, where R₀ is a cheap consequence of C₁, forces ℛ★ on the gate
    domain.
  - C₀ ∧ R₀ contains the clause C₀, so it cannot be offered. C₀ alone and R₀ alone do not force
    ℛ★. C₁ costs more than L★ + c_dec.
  - JN never fires, although ℛ★ is imposed by a predicate as cheap as the target (CT-77).
- **Edge case.** The guard is syntactic, so a reviewer's strictly shorter restatement 𝒦′ ∨ X
  could be offered against a law with L_min(𝒦) ≲ L★ + c_dec.
- **Replacement wording:**
  > "A Ξ-level predicate R ⊇ Sol may be offered as 𝒦₂ (since 𝒦 ≡ 𝒦 ∧ R) only if Price_min(R) is
  > strictly below Price_min(𝒦), the L_stmt of the shortest statement of 𝒦 exhibited by any party.
  > So 𝒦 ∨ X, 𝒦 with points added, or any restatement of 𝒦 is never a split; R may contain clauses
  > of 𝒦."
- **Check.**
  - CT-88 (𝒦 ∨ X) still has no effect, because it is never cheaper than 𝒦.
  - The CT-61/CT-77 gate-maker case is still caught: 𝒦 minus the gate-making clause is cheaper.
  - ST-6 and ST-11 are unchanged.
- **Add:** "CT-97 | JN evasion by anchoring the cheap imposing predicate to one cheap clause |
  NR-17 (length guard) | RELOCATED".

**M11. NR-4 (edited in round 2): "or on every lock-fiber instance" has no measure, so a pointwise reading relocates every Π.**
- **Text:** "If X appears under 𝒦_∅ on a reference-measure fraction ≥ p_dec [A] of Dom_gate^X (for
  X = ℛ★ the threshold p_dec is replaced by 1/Q_min), or on every lock-fiber instance → RELOCATED."
- **Pointwise reading.** For X = Π, "appears on the instance" is true at some Ξ, since
  Sol ⊆ 𝒳 = Sol(𝒦_∅). So every card's Π is RELOCATED at S3. For ℛ★ the next sentence supplies the
  fraction; for Π, [h], T_Π and the carrier nothing does.
- **Replacement wording:**
  > "If X appears under 𝒦_∅ on a reference-measure fraction ≥ p_dec [A] (1/Q_min for X = ℛ★) of
  > Dom_gate^X, or on such a fraction of Dom_gate^X(ι) at every lock-fiber instance ι →
  > RELOCATED."

### MINOR (each with wording)

| # | Location | Defect | Replacement wording |
|---|---|---|---|
| m1 | §1.3 non-vacuous (X_Π-relevant variables) | "Smallest set of which the output is a function" conflicts with excluding variables one at a time; minimal sets need not be unique; a strained reading empties the set for a collectively determined Π. A guard or flat-on-Sol read (a variable read only in a branch not taken on Sol, or through a map flat on its realized range) is caught only through CT-89's presumption | "**non-vacuous:** on every lock fiber and credit instance, X_Π has a relevant variable: a Ξ-variable v, not set directly by a protocol template, such that at some Ξ ∈ Dom_gate(ι) changing v alone to another value it takes on Sol_ι (at another protocol in A_{r★★} or time ≤ H_hor, the realized laws differing by d_BL ≥ 2^(−p★)) moves X_Π's output by more than δ_Π. A Π with no relevant variable is **FROZEN** …" |
| m2 | CV-7 | "applies to the card whose dispute raised it" conflicts with "applies to cards already scored only if it moves their verdicts toward failure". The disputing card is already scored, and CV-1 picks the hostile reading, so R2-M11 is not fixed | "… it applies to **other** cards already scored only if …" |
| m3 | CT-92, CT-93 | CT-92's pattern "a card-designed transplant embedding" covers every E_std (Q3(c) requires the card to design one), so the §24.1 presumption labels every such card STANDARD. CT-93's "Calibrated out" is wrong for per-relatum maps (PC-7(b) removes only the tail) | CT-92: "A transplant embedding that adds structure the draw lacks or fails the Q3(c) conditions, or selective ⊥ … \| Q3(c) \| auditor's substitute embedding and realized-structure substitution govern". CT-93 outcome: "Tested by DIF-5(e): fails if it creates ε on an exogenous control (only the tail is calibrated out)" |
| m4 | §15.3, DIF-5(e) | The text does not say where a control's protocol action enters the per-relatum run, nor what happens when relata cannot carry a continuous control. If the drive enters after aggregation, the check is vacuous | "The control's per-protocol action is applied to each relatum before the per-relatum maps; if the relatum state space cannot carry the control, the control enters at the per-relatum maps' outputs and the check covers the aggregation and tail." |
| m5 | IP-7 | "computed against 𝒟(ι)" conflicts with b_J, which is defined on FB (§2.5) | Delete "computed against 𝒟(ι)"; write "the loss in b_J (§2.5) when …" |
| m6 | IP-13 | With redraws, N can reach ≈ 1160 draws. log₂ C(N, k_ex) grows linearly with N (≈ 540 bits at 10 % exclusion) for a fixed predicate | "log₂ C(N_AI3, ⌈N_AI3·k_ex/N⌉), with N := N_AI3 plus any redraws and k_ex counting every excluded draw" |
| m7 | §2.5 fibers; lock-fiber cap | The qualifying-fiber test admits T-tier verdicts and functions of T_Π, which Q5 excludes. "the fiber's realized u" is singular | "… differing in Π, carrier class or a declared interface statistic that is not a function of T_Π alone (T-tier verdicts excluded)"; "c_f := the minimum, over the realized u of the fiber's instance, of …" |
| m8 | §4.3 against §2.5(b) | "b_J uses p★ bits per codimension at every p; only prices are repriced", but c_J(b) admits M "at the same p", so c_J can change with p | §4.3: "… only prices, and the admissibility of comparison classes in §2.5(b), are recomputed at each p." |
| m9 | Q3(c) E_std | "through the card's Obs" does not say which partition is used; "adds no structure the draw lacks" is not operational | "… through the card's Obs with the draw's own partition and readout mapped by E_std; E_std maps only the draw's degrees of freedom, couplings, state and readout, and reads no record law, response or functional of the draw's Γ." |
| m10 | ST-9 | If the completed card's derivation uses thermal reservoirs or Johnson noise (PS-5), §5.6 gives S3 CARD-RELOCATED before NONGENERATIVE | Object: "… on a standard P-2 model, the cascade relation derived without any thermal, Gibbs or FDT premise (zero environment temperature)" |
| m11 | §1.5 (i) | Deleting "every datum" one at a time can delete jointly relevant redundant data and merge distinct instances | "… after deleting, one at a time and keeping each earlier deletion, every datum whose replacement by a fixed default leaves Im(ι) unchanged …" |
| m12 | D-11, D-13; "both tiers" | D-11 still says "the larger of Aut(𝒞) and the realized symmetry"; D-13 omits the deletion and the scope of the guard. "Both tiers" (B-REC, HB-7, RS-1) is undefined under the new §1.4 terminology | D-11: "modulo the group generated by Aut(𝒞) and the realized symmetry". D-13: per B1 and M1. §1.4 terminology, add: "'both tiers' in R1 records means T_R1 and T_mono." |
| m13 | NR-17, last sentence | "assessed under NR-12(b)" does not make the diverted 𝒦₂ a premise of ℛ★, so a card that writes its derivation around 𝒦₂ escapes both JN and NR-12(b) | "… is assessed under NR-12(b) as a premise of ℛ★'s derivation (STANDARD-IMPLIED; CT-75): JN is recorded for it, not applied." |

**Owner note (not a defect).** Under §2.5's fixed-class rule (DEF-14), a card whose ℛ★ uses
ε^{T_Π}, and whose generated T_Π is injective in Π, can show jointness only through carrier-class
or interface-statistic variation within a class, or by stating ℛ★ at catalogue classes. This
follows from DEF-14, but it limits the G2-11 chain Π → T_Π. The owner should see it.

---

## 2. Question 2: contradictions between round-2 replacements and other clauses

| Round-2 text | Conflicting clause | Item |
|---|---|---|
| §1.3 deletion by RB/SPS template | §2.3 "𝒜_Π^hand is never reduced by standard selectors; … the b_Π size test … use it as defined here" | B1 |
| Q5 "any Ξ-level predicates … may be offered" | NR-17's (round-2) ban on 𝒦 ∨ X; Q5 has no equivalent | B2 |
| c_J(b): guard grammatically on SFP classes only | D-13 "NULL-M guard … now inside c_J(b) and the family cap" | M1 |
| c_J(b) "declared interface statistics supplied" | c_ι "coordinates computed from the same standard model, not conditioning values"; §2.2 single-model rule | M1 |
| Family cap "realizes Im ∩ FB" vs "one shared value realizes Im" | Same sentence; CT-83 | M2 |
| Family cap price condition | CT-78, ST-10 and App. A "credited once" | M2 |
| §1.4 (iv) whitening first | §1.4 "Generated T_Π outside 𝒯"; SCOPE-Q (T_Π ⊇ E₂±) | M4 |
| §1.3 provenance "does not count only if catalogue" | The next sentence (burden on the card) | M5 |
| PC-6 record-factorization / "No component … record law" | §1.2: Obs is a component whose output is Γ_Π | M6 |
| NR-1 parenthetical "PS-5 content" | NR-1 "(syntactic …)"; the ST-6 stipulation; NR-12(b)'s "generated" category | M7 |
| NR-10(e) "returns FAIL"; (n) "FAIL or MODE SELECTION" | HB-8, DIF-5(e) "never returns R1-PASS"; Dom_gate (⊥) | M8 |
| NR-10(f) constant clause on Dom_gate | NR-3 W-pipe on Dom_gate^X | M9 |
| NR-17 clause-containment guard | CT-77, JN's target | M10 |
| NR-4 parenthetical | "or on every lock-fiber instance" (no measure) | M11 |
| §2.5 qualifying fibers | Q5 bullet 1 (T-tier verdicts excluded) | m7 |
| §2.5(b) "at the same p" | §4.3 "only prices are repriced" | m8 |
| CV-7 sentences 2 and 3 | Each other (the disputing card is already scored) | m2 |
| CT-92 pattern; CT-93 outcome | Q3(c) (E_std mandatory); PC-7(b) (only the tail is removed) | m3 |
| §2.3 "group generated by" | D-11 "the larger of" | m12 |
| §1.4 terminology | "both tiers" in B-REC, HB-7, RS-1 | m12 |

**Checked and consistent:**
- §2.3's two uses of standard selectors, with NR-6, §15.7(viii) and §21.2;
- MC-9, with App. A and MC-10;
- §15.9 shortfall; BU-6, with CV-7 (apart from m2);
- the §1.4 covariance clause, with Q8;
- IP-6 closure (non-classical requirement), with B.2 and SEL;
- IP-12;
- §4.1 typing, with VB-4, VB-13 and NR-9;
- NR-6 constant decoders, with NR-3, NR-4 and NR-10(f), (k);
- NR-7;
- the NR-10(n) expressibility rule (apart from M8);
- §5.5 GENERATED-STRONG (arithmetic: log₂(n−1) < 6 for n ≤ 64);
- DIF-5(e); §21.2 GY-10;
- the App. A lock-threshold, t₁ and N_AI3 rows;
- the feasibility arithmetic (1000 − 6n);
- CT-88, CT-89, CT-90, CT-91, CT-94, given their fixes.

---

## 3. Question 3: self-tests changed in round 2, under T-1 and the §24.2 convention

| ST | Follows? | Reason |
|---|---|---|
| ST-1 | **Yes** | S3: RELOCATED is listed first and fires (Gibbs state used in ℛ★'s derivation, §5.6). NONGENERATIVE is recorded. S5 Q3 (STD-3, §13.6) and the STD-9 condition are recorded. B1 and M6 act later in the order. |
| ST-3 | **Yes** | S1: no earlier card, so no VARIANT; GRAVEYARD (GY-6). DC-8 UNMEASURABLE, SEL-10 and B-CF collapse at Hamming 0 are recorded. |
| ST-4 | **Yes** (the convention declares the supplied structures) | S3 NONGENERATIVE. S6: Im = FB ⇒ 𝓗 ⊆ Z(ℛ★) ⇒ c_J(a) = 0 ⇒ b_J = 0 and ΔL ≤ 0. SC1 (UNINFORMATIVE) is the S6 label listed first; LOOKUP is among the recorded S6 failures. |
| ST-6 | **No** | Three round-2 texts pre-empt the S5 terminal: B1 (S4 CARD-UNDIFFERENTIATED on the generic, unique-Π lock fiber); M6 (S3 CARD-DEFINITIONAL via Obs); M7 (S3 CARD-RELOCATED: NR-1 flags a rule that generates detailed balance by Kolmogorov's criterion). With B1, M6 and M7 fixed, the row follows. The JN diversion holds even for an acyclicity-type 𝒦₂, because that is itself PS-5 operationally (NR-17, last sentence). |
| ST-7 | **Yes** | The terminal follows (NR-6 on 𝒞, else CT-13). The recorded S6 "c_J = 0 with M the class itself" holds under M1's free-constant reading, because ℛ★ holds on the whole class. Under the current fitted-point reading it holds trivially. |
| ST-8 | **Yes** | Gibbs is supplied and declared but not used by the Volterra derivation, so there is no RELOCATED; S3 NONGENERATIVE. S5 Q3 (STD-14) is recorded. |
| ST-9 | **Conditional** | NONGENERATIVE holds only if the completed derivation uses no thermal or FDT premise. Otherwise §5.6 gives S3 RELOCATED first (m10). |
| ST-10 | **Partly** | The arithmetic holds (≈ 990 bits at p = 10; 1000 − 6n at p = 16). "Credited once (family cap)" fails for a compact card whose comparison class costs more than the card (M2). "A tabulated card fails before SC2" holds, although S3 (IP-3/NR-6, CT-04) may come before KU-1 or Q1. |
| ST-11 | **First branch yes; second branch no** | NR-17(b) at S3 holds: ℛ★ = D ∧ G holds throughout Dom_gate ∩ Sol(𝒦₂). In the second branch, the S5 CARD-DEFINITIONAL terminal is pre-empted by B1 (S4) and M6 (S3). |

---

## 4. Direct answers to the brief's focus points

- **c_J(b) and family cap: can an auditor always find an admissible M that realizes Im and lies in Z(ℛ★)?**
  - **As written: yes, by three routes.**
    - The fitted-point reading makes the codimension of a finite set 0 (M1a).
    - Im ∩ FB = ∅ makes every M qualify (M1b).
    - A B-HB composition is not bound by "without reference to ℛ★", so a coupling can be tied to
      the supplied u (M1c).
  - **Under the M1 wording: no.** Constants are free, the guard covers every M, and (b) is void
    when Im ∩ FB = ∅. Then an M lying in Z(ℛ★) is either STANDARD-GENERIC under Q3(b), so the card
    already fails, or a standard sub-class containing the card's standard-realizable data (the
    intended NULL-M result). The two clauses are then consistent and not jointly a kill.
  - **Opposite failure:** the family cap can fail to bind (no qualifying M because of price), which
    is M2.
- **Inert-relatum deletion:** a kill (B1), on every reading, for unique-Π lock fibers at the frozen
  sizes.
- **X_Π-relevant-variable rule:** it closes the plain decorative read. Its definition is internally
  inconsistent, and a guard or flat-on-Sol read is caught only by CT-89's presumption (m1).
- **NR-10(f) "chooses among named classes by a branch":** it kills legitimate constructions on the
  hostile scope of "named" (case splits inside a construction; extremal choice of a readout
  variable). The M9 wording keeps CT-91 and frees those constructions.
- **NR-17's L★: does JN fire on every compact law? No.**
  - L★ counts the chain objects as one token each, so the threshold is modest (L★ + 60 bits).
  - A legitimate split fires only if a sub-conjunct that cheap forces ℛ★ on ≥ 90 % of the gate
    domain on every lock fiber.
  - The defects are the opposite way: the clause-containment guard lets an anchored cheap predicate
    escape (M10), and a restatement edge case exists. Both are fixed by the length guard.

---

## 5. Summary (5 lines)
1. **BLOCKER (2).** The §1.3 inert-relatum deletion empties the size test on unique-Π lock fibers (B1). Q5's split test admits a trivial split, so every forced relation is NONJOINT (B2).
2. **MAJOR, hidden kills (7).** c_J(b)'s undefined Obs(M), vacuity and composition guard (M1); §1.4(iv) whitening first (M4); provenance by definability (M5); PC-6 convicting Obs (M6); NR-1 PS-5 content (M7); NR-10(e)/(n) ⊥ ≠ FAIL (M8); NR-10(f) "named" scope (M9). Also NR-4's pointwise lock-fiber clause (M11).
3. **MAJOR, loopholes (3).** The family-cap price condition (CT-78 for compact cards; decorated near-copies) (M2); fragmentation of class fibers (M3); NR-17's clause-containment guard reopening CT-77 (M10). There are also 13 MINOR wording and consistency items.
4. **Self-tests.** ST-1, 3, 4, 7, 8 and ST-11's first branch follow. ST-6 does not (B1, M6, M7). ST-11's second branch does not (B1, M6). ST-9 is conditional (m10). ST-10's "credited once" needs M2.
5. **Verdict: do not freeze as is.** Every fix is sentence-level wording, given above. No candidate law appears in the charter or in this report.
