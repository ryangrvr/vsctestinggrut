# Round-2 hostile red-team of the revised Stage-3 charter (rewritten rules only)

**Subject:** `PROGRAM/STAGE3/STAGE3_CHARTER.md` (worktree `/tmp/claude-0/mainwt`, branch
`grut2-stage3`, untracked revision of 2026-10-07 14:37). **Mode:** read-only; no repository file
was edited, created or committed. **Constraint kept:** no candidate law 𝒦 is proposed, sketched,
named or exemplified. Every construction below is an abstract gaming pattern or reading, labelled
**CHARTER TEST**.

**Method.**
- I read the whole charter, G2-11, `FREEZE_VERIFICATION.md`, and the round-1 audit proposals
  (A1 fixes 2–16, A2 F-1 to F-15, C B1–B5 and M1–M9).
- I also read the builder's own edit scripts (`scratchpad/s3/edits/*.py`, `sec4_old.md`). They
  give the exact old/new text of each rewritten rule.
- I attacked only the rules on the brief's list.
- Severity scale: **BLOCKER** = must fix before freezing; **MAJOR**; **MINOR**. "Hostile reading"
  means the reading CV-1 obliges an auditor to adopt when the text is ambiguous.

---

## A. BLOCKERS

### R2-B1. §2.3 explicitly licenses a partition read off 𝒞 by a standard selector
**CHARTER TEST (selector in the inputs).**
- 𝒞 carries a weight, graph or charge structure. Its min-cut, spectral split, modularity optimum
  or conserved-charge sector *is* Π, and X_Π returns that partition.
- The card cites §2.3 and §21.2: the match is STANDARD-MECHANISM, which "is never a relocation".

**Clauses in conflict.**
- §2.3: "The standard selectors enter only through the STANDARD-MECHANISM test (§15.7(viii)),
  applied to 𝒞 and to the realized dynamics of Sol: a match is recorded (no differentiation
  novelty) and is never a relocation."
- §21.2: "Selecting a partition by an SPS template is not a GY-10 selector (it is
  STANDARD-MECHANISM, §15.7(viii))."
- §15.7(viii): "(same Π from the same data) … never a relocation".
- NR-6 says the opposite: "The RB and SPS templates … always run …; as decoders they read only the
  inventory (an SPS template applied to the realized dynamics of Sol is not a decoder …)". So an
  SPS template run on 𝒞 *is* a decoder, and a match fires as RELOCATED.
- ST-7's required terminal rests on NR-6 firing on 𝒞 ("an RB/SPS decoder recovers Π from 𝒞").

**Effect.**
- The charter gives a card explicit text that a partition hidden in 𝒞 (decodable by a standard
  selector) is not relocated. This contradicts PS-1 and G2-11 item 4.
- ST-7's terminal becomes indeterminate.
- CV-1 only sends the conflict to the owner. It does not resolve the conflict in the frozen text.

**Replacement wording.**
- §2.3: "… The standard selectors enter only through the STANDARD-MECHANISM test (§15.7(viii)),
  applied to the realized dynamics of Sol: a match there is recorded (no differentiation novelty)
  and is never a relocation. A standard selector (an SPS or RB template) applied to 𝒞 or to any
  other item of the §5.2 inventory is an NR-6 decoder: a match there is RELOCATED. Where both
  apply, NR-6 governs."
- §15.7(viii): "an SPS comparison on the realized dynamics of Sol on AI-2 and AI-3 instances. If Π
  is extensionally the output of an SPS template applied to those dynamics, the result is
  STANDARD-MECHANISM (…); an SPS match on the inputs is decided by NR-6."
- §21.2: "Selecting a partition by an SPS template applied to the realized dynamics of Sol is not
  a GY-10 selector (it is STANDARD-MECHANISM, §15.7(viii)). Applied to the inputs, it is an NR-6
  decoder."

### R2-B2. Price(M) charges M a per-instance Π table, so neither c_J(b) nor the family cap ever binds on a card whose Π is generated
**CHARTER TEST (uncappable shared-constant pin; the CT-78 / A2 N-09 pattern in the regime the
fix was meant for).**
- The card's Π passes NR-6, so no RB or SPS selector returns it.
- On every credit instance, ℛ★ coincides with a standard response form except for one constant.
  That constant is shared across instances and fixed by the law. So c_ι = c_J = c_lock = 1.
- Any standard class M that "realizes Im ∩ FB" must reproduce the card's Π on each of about 100
  instances. No RB or SPS selector returns it, so M pays the fallback:
  "log₂|𝒜_Π^hand/G_ι| + log₂ 5 per instance".
- That is about 100 × (8 to 16 + 2.3) ≈ 1 000–1 800 bits, more than the whole Price(𝒦)
  (≈ 720–1 220 bits, App. A).
- M is therefore excluded from c_J(b) and from c_fam. c_fam then becomes a minimum over an empty
  set, which the text leaves undefined.
  - Read as "no cap": b_J = 100 × 10 = 1 000 bits for content worth one constant. CT-78
    ("Credited once") fails for exactly the cards that pass NR-6.
  - Read as 0 under CV-1: every card with a generated Π has b_J = 0, a hidden kill.
  - Either way, the round-1 BLOCKER fix A2 F-4 is ineffective.

**Clauses.**
- §2.5 c_J(b): "with constants fitted, Π, [h] and T fixed by hand or by a priced rule, and
  Price(M) ≤ Price(𝒦) … + the price of the rule fixing Π, [h] and T (the cheapest RB/SPS selector
  returning them, else log₂|𝒜_Π^hand/G_ι| + log₂ 5 per instance)".
- Family cap: "over every standard class M with Price(M) ≤ Price(𝒦) that realizes Im ∩ FB on all
  of I_𝒦".

**Why the fix is principled.**
- c_ι is already measured inside FB(u), with the card's interface given.
- §4.3(b) makes generating the interface a gate, never a credit.
- The standard-class comparison must therefore receive the same u. Otherwise it charges M for the
  gate as though the gate were credit.

**Replacement wording.**
- §2.5 c_J(b): "(b) for every standard model class M that realizes Im ∩ FB (non-standard
  realizations are scored by their own kill conditions and never disable this clause), with
  constants fitted and with the card's realized interface values u (Π, carrier class, [h], T_Π
  and the declared interface statistics) supplied on every instance at zero price, since
  generating the interface is a gate, never a credit (§4.3(b)), and with Price(M) ≤ Price(𝒦): the
  codimension of Z(ℛ★) ∩ Obs(M) in Obs(M). Here Price(M) := the IP-4 framework choice
  + L_stmt(M) + the IP-5 price of M's fitted constants (a constant shared across instances is
  priced once, a per-instance constant once per instance). It is computed at the same p as
  Price(𝒦), with every VB item M uses, VB-17 to VB-21 included, at P_v."
- Family cap, append: "M receives u as in (b). If no class qualifies, the family cap imposes no
  bound."
- ST-7 still holds: M is the class itself, so c_J = 0.

### R2-B3. NR-17(b): the "any R ⊇ Sol" licence lets a reviewer RELOCATE any compact law with a trivial superset
**CHARTER TEST (trivial-superset JN).**
- A reviewer offers 𝒦₂ := R := 𝒦 ∨ X, where X is any cheap Ξ-level predicate: one fixed
  degenerate configuration outside Dom_gate, or a null set.
- R ⊇ Sol, R does not imply 𝒦 on Dom_pre, and Price_min(R) ≤ L_stmt(𝒦) + L_stmt(X) + 6.
- On every lock fiber, Dom_gate ∩ Sol(R) equals Dom_gate ∩ Sol up to a null set. So:
  - if Sol has positive measure, ℛ★ holds on 100 % of it by Q1 and (b) fires;
  - if Sol has measure zero, the fraction is 0/0, and CV-1 resolves it against the card.
- (b) therefore fires whenever L_stmt(𝒦) + L_stmt(X) + 6 ≤ "Price(ℛ★ stated directly)" + c_dec.
- That comparator is undefined:
  - Read as a card Price (IP-1 to IP-14; the components alone cost ≈ 300–600 bits), it exceeds
    the L_stmt of every compact law (≈ 216 bits in App. A). Every card that could pass SC2 is
    RELOCATED.
  - Read as an L_stmt, every law within about c_dec − 12 bits of ℛ★'s length is RELOCATED.

**Clause.** NR-17: "Any Ξ-level predicate R ⊇ Sol may be offered as 𝒦₂, since 𝒦 ≡ 𝒦 ∧ R. …
If Price_min(𝒦₂) ≤ Price(ℛ★ stated directly) + c_dec, and either … (b) on every lock-fiber
instance, Dom_gate(ι) ∩ Sol(𝒦₂) is nonempty and ℛ★ holds … on … a reference-measure fraction
≥ 1 − 1/Q_min of it".

**Analysis.**
- JN's target (CT-77) is a cheap *weakening* that forces ℛ★ wherever the chain is defined.
- A superset that contains 𝒦 itself is no weakening and carries no evidence.
- The fraction must stay on Dom_gate ∩ Sol(𝒦₂), not on Sol(𝒦₂) ∖ Sol(𝒦). Otherwise CT-77 escapes
  whenever the omitted conjunct is exactly what makes the chain defined.

**Replacement wording.**
> "**NR-17 Joint necessity (JN).** Consider any L₀ split 𝒦 ≡ 𝒦₁ ∧ 𝒦₂ offered by the author or a
> reviewer in which 𝒦₂ does not imply 𝒦₁ on Dom_pre. A Ξ-level predicate R ⊇ Sol may be offered as
> 𝒦₂ (since 𝒦 ≡ 𝒦 ∧ R) only if its shortest exhibited statement contains no clause of 𝒦 and no
> condition L₀-equivalent within c_dec bits to one. A disjunction 𝒦 ∨ X, or 𝒦 with points added,
> is not a split. Let Price_min(𝒦₂) be the L_stmt of the shortest L₀ statement equivalent to 𝒦₂ on
> Dom_pre exhibited by any party. Let L★ be the L_stmt of ℛ★ written with Π, Z_Π, [h], T_Π, Γ_Π,
> ε, d_op and the frozen chart coordinates as primitive symbols, one token each. If
> Price_min(𝒦₂) ≤ L★ + c_dec, and either (a) … or (b) on every lock-fiber instance ℛ★ holds within
> r_lock on the defined pipeline image of a fraction ≥ 1 − 1/Q_min of Dom_gate(ι) ∩ Sol(𝒦₂)
> (reference measure if that set has positive reference measure; otherwise the natural measure of
> its top-dimensional part; if neither exists, (b) does not fire), then ℛ★ is imposed, not
> forced: RELOCATED on the target relation."

### R2-B4. NR-10(n) kills every card under the hostile reading
**CHARTER TEST (charter-imposed inexpressibility, read against the card).**
- Every card's Obs is protocol-uniform. PC-7(c): "Obs reads E-relata through one uniform map per
  relatum and one fixed symmetric aggregation declared at freeze". NR-10(a) bans protocol
  indexing.
- The E2 configuration of (e) needs "an environment law independent of the protocol" read
  differently by a₀ and by the driven protocol.
- The product-latent twin of (l) needs readouts h_a = π_a.
- Neither record family can come from a protocol-independent E through a protocol-uniform Obs.
  So, for every realized family with ε > 0, "the declared type cannot express" them.
- (n) attributes that to the type, so the carrier is SUPPLIED and the card is
  CARD-NONGENERATIVE. This applies to every card.
- Separately, (e) asks the derivation to "return FAIL". On such configurations the card's own
  pipeline gives Γ_Π constant across A, so the configuration lies outside Dom_gate and the result
  is ⊥, not FAIL.

**Clauses.**
- NR-10(n): "if the declared type cannot express the configuration of (e) or the product-latent
  twin of (l) for some realized record family, the exclusion is carried by the type: the carrier
  is SUPPLIED (→ CARD-NONGENERATIVE)."
- NR-10(e) and (l), and PC-7(c).

**Replacement wording (NR-10(n)).**
> "(n) Expressibility in (e), (l) and (n) concerns the environment's latent state, not the readout.
> The configuration of (e), or the twin of (l), is expressible if, on some instance of the declared
> type (any size the type admits; the auditor chooses), the E-state space can carry the
> configuration's latent state. The auditor supplies, at no price to the card, the
> protocol-indexed readout the configuration needs. On such an instance, with that readout, X_h and
> X_T return carrier FAIL or MODE SELECTION. If no instance of the declared type can carry that
> latent state for some realized record family, and the card's carrier derivation (C7) uses that
> inexpressibility, the exclusion is carried by the type: the carrier is SUPPLIED
> (→ CARD-NONGENERATIVE)."

Apply the same reading to (e): replace "on any instance that can express the two-mode
configuration" with "on any instance on which the configuration is expressible in the sense of
(n)".

---

## B. MAJOR

### R2-M1. IP-6 closure by c_dec-definability: VB-5/6/7 "matching" can be read into every card, and the declare-or-relocate trap widens
**CHARTER TEST (classical-simplex match).**
- Every card's record laws form a simplex. The positive cone of laws, with total mass as order
  unit, is a GPT cone with an order unit.
- That cone is L₀-definable from the base tokens `law` and `support` in about c_dec bits.
- Under CV-1 the card "matches VB-6". Then "Supplying or matching VB-5, VB-6 or VB-7 makes every
  selectivity result RELOCATED", and G-SEL fails for every card.

**Secondary effect.**
- "An undeclared match → RELOCATED" now covers every VB item L₀-definable within 60 bits from any
  of the card's structures: a metric from any weighted relation, an involution from any temporal
  order, and so on.
- Declaring defensively has side effects: VB-13 brings NR-9, VB-14 brings RH-SYM, and VB-16 brings
  PS-5.
- The outcome depends on the kit's VB-6 checklist, but the charter must not leave a rule to the
  kit (CV-6 lets the kit fix catalogues, not rules).

**Clause.** IP-6: "**Closure:** a defined symbol whose interpretation satisfies an item's frozen
axiom checklist …, or any structure from which such an item is L₀-definable within c_dec bits,
*is* that item; an undeclared match → RELOCATED."

**Replacement wording.**
> "**Closure:** a defined symbol, or a structure that the card's derivations or components use
> (responsibility map), whose interpretation satisfies an item's frozen axiom checklist on any
> audit or battery instance, or from which the item is L₀-definable within c_dec bits and is used
> as that item, *is* that item; an undeclared match → RELOCATED. A structure from which an item is
> merely definable, but which no derivation uses as that item, is not a match. For VB-5, VB-6 and
> VB-7 a match is decided on the checklist alone. A classical state space (a simplex of
> probability laws), the base tokens of B.1 and the charter's record-law objects never match
> VB-6. Closure never applies to verdict patterns."

In B.2, after VB-6, add "(a non-simplicial cone)".

### R2-M2. §1.3 non-vacuous persistence is met by a decorative read
**CHARTER TEST (decorative-read persistence; reopens CT-80).**
- Π is set by Ξ-variables the law holds exactly invariant.
- X_Π also takes the protocol-driven S variable (or Ξ as a whole, as PC-6's "X_Π reads (Ξ, 𝒞)"
  allows) as an argument that never changes its output.
- "The Ξ-variables X_Π reads" then have laws that differ between a₀ and a±, because the template
  moves the driven variable by α = 1 SD. So the clause is met and FROZEN is never declared.

**Clause.** "**non-vacuous:** on every lock fiber and credit instance, the Ξ-variables X_Π reads
have realized laws differing by d_BL ≥ 2^(−p★) between some pair of protocols in A_{r★★} or some
pair of times ≤ H_hor."

**Replacement wording.**
> "**non-vacuous:** on every lock fiber and credit instance, the **X_Π-relevant variables** have
> realized laws differing by d_BL ≥ 2^(−p★) between some pair of protocols in A_{r★★} or some pair
> of times ≤ H_hor. These are the smallest set of Ξ-variables of which X_Π's output is a function
> on Dom_gate. A variable whose replacement by an independent draw of its type never moves the
> output by more than δ_Π is not relevant, and variables that the protocol templates set directly
> are excluded."

### R2-M3. §1.3 size test inflated by inert-relatum padding (the hand set is never reduced)
**CHARTER TEST (inert-relatum padding).**
- The declared lock-fiber instances carry extra relata. Each is distinguishable, so no symmetry in
  G_ι absorbs it.
- 𝒞 isolates each extra relatum (an RB2 threshold or RB3 component read), so every solution puts
  it in E.
- Each padded relatum adds one bit to log₂|𝒜_Π^hand/G_ι|, while M(ι) is unchanged.
- Example: 4 core relata, every core partition realized, plus 10 padded relata. Then
  log₂|𝒜/G| ≈ 14 and log₂ M ≈ 3.8, so b_Π = 6 passes with no selection on the core.
- NR-6 does not fire, because no decoder recovers the core.
- The padding was previously absorbed by the selector reduction. It is new with D-11.

**Clause.** "on the lock fibers log₂|𝒜_Π^hand(ι)/G_ι| − log₂ M(ι) ≥ b_Π [A] … the law's selection
must remove at least b_Π bits of hand choice."

**Replacement wording.**
- §1.3, append: "Before the size test, delete from V_ι every relatum that lies in the same block
  in every Π realized on Sol_ι and that an RB or SPS template applied to 𝒞_ι alone assigns to that
  block. 𝒜_Π^hand, G_ι and M(ι) are then computed on the remaining relata."
- §2.3 (also fixes an ambiguity, since two groups need not be comparable): replace "the larger of
  Aut(𝒞_ι) … and the symmetry group of the realized dynamics of Sol_ι" with "the group generated
  by Aut(𝒞_ι) (computed by the kit) and the symmetry group of the realized dynamics of Sol_ι,
  acting on V_ι".

### R2-M4. §1.3 T_Π provenance test: the coincidence exemption launders protocol-induced maps
**CHARTER TEST (provenance laundering; reopens CT-67).**
- X_T carries, as its own priced literal content, a copy of the template-to-Ξ drive direction. Or
  it computes from Ξ the flow or linearization along the driven S-variable, written without naming
  a protocol.
- It returns the group generated by the record maps this induces.
- Its L₀ definition never "refers to a protocol". The induced maps then "merely coincide" with the
  protocol-induced maps and are exempted.
- The PC-6 substitution test passes, because X_T reads no output of Obs.

**Clause.** "If X_T's L₀ definition … refers to a protocol, a protocol's action on Ξ, a solution's
response or a record law … A map that merely coincides with some protocol's effect (e.g. a
translation in E₂±) does not count."

**Replacement wording (append).**
> "The test also fails if X_T's definition contains, or L₀-defines within c_dec bits, the
> template-to-Ξ map, a protocol template, or the action of the driven S-variable on Ξ (its flow,
> linearization or response). A map that coincides with some protocol's effect does not count only
> if it is an element of a catalogue class of 𝒯 and X_T's definition contains none of this
> content. If T_Π contains, on a lock fiber, a t_a with P_a = t_a#P_{a₀} within 2^(−p★), the card
> bears the burden of showing that the provenance test passes."

### R2-M5. §2.5 fixed-T fibers: one singleton fiber zeroes c_J (hidden kill)
**CHARTER TEST (singleton T-fiber).**
- The generated T_Π takes a different value on one instance of 𝓘: AI-1 with its degenerate
  record structure, or one value of Π for which X_T's construction yields another group.
- That fiber holds one realized u. Its hull is {u} × (cl R_u ∩ FB(u)), which Q1 places wholly in
  Z(ℛ★), so its codimension is 0.
- "The minimum over the fixed-T fibers that contain realized points" then gives c_J = 0. Q5 fails
  (CARD-NONJOINT) and b_J = 0.
- A T_Π that depends on Π, as in G2-11's schematic chain Π → [h]_{T_Π} → T_Π, fragments every
  fiber. Jointness through variation of Π then becomes impossible.
- The rule binds even when ℛ★ uses only catalogue classes, where DEF-14 cannot arise.
- §2.5 is also stricter than Q5, which allows comparison "at a catalogue class".

**Clause.** "𝓗 contains a cross pair (u₁, r₂) only if u₁ and u₂ carry the same T_Π … the minimum
over the fixed-T fibers that contain realized points is taken."

**Replacement wording.**
> "**Fixed-class fibers (DEF-14).** A cross pair (u₁, r₂) enters 𝓗 only if every ε value and
> T-invariant functional in ℛ★ is evaluated at one class for both points. When ℛ★ uses only
> catalogue classes, any cross pair qualifies. When ℛ★ uses T_Π, u₁ and u₂ must carry the same
> T_Π. Codimensions are computed fiberwise. The minimum is taken over the fibers that contain at
> least two realized interface values differing in Π, carrier class or a declared interface
> statistic; if no fiber does, c_J := κ_J := 0."

**Joint effect with R2-M6(a).**
- A T_Π that is constant across instances and is a catalogue class dies by the constant decoder.
- A T_Π that varies across instances dies by singleton fibers.
- The only survivor is a constant, non-catalogue T_Π longer than 60 bits with a valid s_T.

### R2-M6. NR-10(f) on catalogue T_Π: hidden kill on one reading, menu-selector loophole on the other
**(a) Kill (CHARTER TEST: constant decoder).**
- A decoder that outputs "T_lin" (≤ 3 tokens, reading nothing) recovers T_Π "on every lock-fiber
  instance". NR-6 then fires as RELOCATED.
- PC-6's record-factorization test accepts a constant F.
- NR-10(f)'s "decodable within c_dec bits from its own definition alone, independent of Ξ" is
  satisfied by the same constant decoder.
- All three contradict (f)'s new sentence "A T_Π equal to a catalogue class is GENERATED when …".
  That sentence also requires that "NR-10 is otherwise clean", which makes it self-defeating.
- The same applies to a constant carrier class or [h] class. It is exactly the G2-11 target
  ("derive objective persistent carrier/readout structure") when the derived structure is the same
  on every instance.

**(b) Loophole on the charitable reading (CHARTER TEST: menu branch; reopens CT-13).**
- X_T := ite(C(Ξ), T_lin, T_mono), where C is a cheap Ξ-level consequence of 𝒦 that is rare off
  Sol. C is not L₀-equivalent to a clause, so PC-6 is silent.
- The output depends on Ξ. NR-3 sees a change off Sol, NR-4 sees no appearance under 𝒦_∅, so T_Π
  counts as GENERATED although it was picked from the menu.

**Replacement wording.**
- NR-10(f): "… a component supplies a class or group (PS-3/PS-4) if its output is the same at
  every Ξ ∈ Dom_gate as a function of its definition alone, or if it chooses among named classes,
  groups or readouts by a branch (ite, case split, table or threshold) on any condition. A T_Π
  equal to a catalogue class is GENERATED only when X_T computes it as the group generated by maps
  it constructs from Ξ-level structure without naming any class, NR-3 shows that the same
  construction yields a different group off Sol, and NR-10 is otherwise clean (§1.4)."
- NR-6, add: "For T_Π, [h] and the carrier, a decoder must read some instance input. A decoder
  whose output is the same on every instance is not a decoder. Whether a structure that is the
  same on every instance was supplied is decided by NR-3, NR-4 and NR-10(f), (k)."
- PC-6: "if an auditor exhibits an L₀ map F of length ≤ c_dec, **not constant on Dom_gate**, with
  a component's output = F(Γ_Π) on Dom_gate …"

### R2-M7. Q5 split test: no non-triviality condition
**CHARTER TEST (trivial split).**
- Reading A (hostile): the reviewer offers 𝒦₁ = 𝒦₂ = 𝒦. For a law with one solution per
  instance, 𝒦 fixes both the realized interface and the realized response, so the result is
  NONJOINT. Every unique-solution law dies.
- Reading B: "with Π … free" means Γ_Π must be fixed for every Π. But Γ_Π = Obs_Π(Ξ) depends on
  Π, so no 𝒦₂ ever qualifies.
  - CT-82 (two instance-indexed single-axis pins) is then uncaught when the law is written as one
    entangled clause pinning u = f(𝒞) and r = g(𝒞).

**Clause.** "if, for some L₀ split 𝒦 ≡ 𝒦₁ ∧ 𝒦₂ …, 𝒦₁ fixes the realized interface value of
every instance of 𝓘 (with Γ_Π free) and 𝒦₂ fixes the realized response slice of every instance of
𝓘 (with Π, Z_Π, [h] and T_Π free), ℛ★ is NONJOINT."

**Replacement wording.**
> "– the coupling is not carried by the instance inputs alone. Take any L₀ split 𝒦 ≡ 𝒦₁ ∧ 𝒦₂
> offered by the author or a reviewer, in which neither 𝒦₁ nor 𝒦₂ implies 𝒦 on Dom_pre. Any
> Ξ-level predicates R₁, R₂ ⊇ Sol with R₁ ∧ R₂ ≡ 𝒦 on Dom_pre may be offered. If, on every
> instance of 𝓘, 𝒦₁ alone fixes the realized interface value and 𝒦₂ alone fixes the response
> values Obs_Π(Ξ) at that instance's realized interface, ℛ★ is NONJOINT."

### R2-M8. Q3(c): E_std is unconstrained, and components can shape the denominator
**CHARTER TEST A (card-shaped embedding).**
- A declared type that cannot express the B-HB families routes every transplant draw through
  E_std.
- E_std is designed by the card. For instance, it adds to each embedded model a fixed structure on
  which the card's components return an interface that violates ℛ★.
- Q3(c) then passes for any ℛ★.

**CHARTER TEST B (selective ⊥).**
- X_Z, X_h or X_T returns ⊥, or the carrier form fails, on draws with a Ξ-level feature
  correlated with ℛ★ holding.
- Those draws leave the denominator. Up to half of all draws can be removed, so a 10 % CARD-STANDARD
  rate becomes 0 %.
- The substitution "the card's realized Π where X_Π is undefined" covers X_Π only.

**Clause.** Q3(c): "If a draw cannot be expressed in the declared type, the card's frozen, priced
standard-model embedding E_std … is used. Draws on which a component returns ⊥ or the carrier form
fails are excluded from the denominator."

**Replacement wording.**
> "… E_std (declared in C12) is used. E_std must be uniform, must preserve the draw's per-protocol
> record laws through the card's Obs within 2^(−p★), and adds no structure the draw lacks. Any
> auditor may substitute another embedding that meets these conditions at no greater price, and
> the transplant fraction is the largest over the embeddings exhibited. Where X_Z, X_h or X_T
> returns ⊥, or the carrier form fails, the card's realized Z_Π, [h] and T_Π from the lock fiber
> are substituted (as for Π). A draw leaves the denominator only if the chain is still undefined.
> If no E_std is declared, or fewer than half the draws are scorable, Q3(c) returns
> CARD-STANDARD."

### R2-M9. MC-9 widens the confirmation band
**CHARTER TEST (observable padding).**
- The card registers three independent lock observables: two easy ones and one discriminating
  one.
- With n_obs = 3, α_obs = 0.0003 and z_obs = 3.615. MC-9 turns MC-5's confirmation multiplier 2
  into z_obs − 1 = 2.615 (2.32 at n_obs = 1).
- Suppose the data come from a live rival exactly 3σ_pre outside J_K, with σ_eff = σ_pre. The
  one-sided probability of a false LOCK-CONFIRMED on the discriminating observable rises from 0.16
  to 0.35 (0.25 at n_obs = 1; values computed).
- Bonferroni is right for falsification: KU-12 fires on any observable. Confirmation already
  requires every observable (MC-10), an intersection test, so it needs no correction and must not
  be loosened.

**Clause.** "The MC-5 multipliers 3 and 2 become z_obs := Φ⁻¹(1 − α_obs/2) and z_obs − 1".

**Replacement wording.**
> "The MC-5 falsification multiplier 3 becomes z_obs := Φ⁻¹(1 − α_obs/2). The confirmation
> multiplier stays 2, because confirmation requires every observable (MC-10). MC-7 power is
> computed at α_obs."

### R2-M10. PC-7(b) static tail defined by syntactic position: CT-68 reopens
**CHARTER TEST (pre-aggregation static map).**
- Obs applies a fixed nonlinear map to each E-relatum's read value, then aggregates. PC-7(c)
  allows "one uniform map per relatum".
- Each per-relatum map precedes a later read, so it is not "applied after Obs's last read of Ξ".
  It is therefore not in the static tail and is not removed from Obs′.
- §15.3 and DIF-5(e) pass the exogenous controls only "through the card's static record maps",
  so the controls never meet this map.
- An exogenous E read through a sum of nonlinear per-relatum maps gives ε^{T_lin} > 0, because a
  static nonlinearity breaks affine separability. That is CT-68 ("ε produced by a static readout
  nonlinearity").

**Clause.** PC-7(b): "every map on record space, applied after Obs's last read of Ξ, that depends
on neither protocol nor state."

**Replacement wording.**
- PC-7(b): "… The card's **static maps** are every map that depends on neither protocol nor
  state: the declared static tail (record-space maps applied after Obs's last read of Ξ), and the
  per-relatum maps and the aggregation of PC-7(c). Obs′ is Obs with the tail removed. …"
- DIF-5(e) and §15.3, add: "Each exogenous control (HB-3, HB-4, HB-5 with calibrated filters,
  C2-F′) is also run, as an exogenous E-relatum process on AI-1, through the per-relatum maps, the
  aggregation and the tail. A non-zero ε^{T_Π} on any of them fails DIF-5(e)."

### R2-M11. CV-7 and BU-6: a favourable ruling can never rescue the card that raised the dispute
**CHARTER TEST (dispute without remedy; a hidden kill through governance).**
- A card meets a genuinely ambiguous clause, and CV-1 scores it against the card.
- The owner rules for the card.
- CV-7 and BU-6 say a favourable interpretation "applies only going forward", and that
  retroactive application "moves verdicts only toward failure".
- The card's verdict was computed under the hostile default before the ruling, so the ruling helps
  only later cards. The one remedy CV-1 names is closed to the card that exposed the defect.

**Clauses.** CV-7 "an interpretation that favours a card applies only going forward, and
retroactive application moves verdicts only toward failure"; BU-6 "an owner interpretation that
favours a card applies only going forward".

**Replacement wording.**
- CV-7: "… It applies to the card whose dispute raised it, whose affected screens are re-run under
  it with the Recomputer's confirmation, and to every later card, null and self-test. It applies
  to cards already scored only if it moves their verdicts toward failure. It is void if it changes
  a self-test verdict (§24.2)."
- BU-6: "… an owner interpretation that favours a card applies to that card and going forward
  (CV-7)."

### R2-M12. N_dist defeated by decorative labels
**CHARTER TEST (decorated copies; reopens CT-85).**
- The 𝒞 type includes a continuous label that the law, every component and θ_dict ignore.
- Every AI-3 draw is then non-isomorphic and seed-disjoint, so N_dist = 100.
- Yet the realized images repeat across a few structural classes, for example one per relata
  count: 9 classes for 8–16 relata.
- Until R2-B2 is fixed, the family cap does not intervene.

**Clause.** §1.5: "Instances are **structurally distinct** iff their 𝒞 are non-isomorphic and their
seeds are disjoint."

**Replacement wording.**
> "Instances are **structurally distinct** iff (i) their 𝒞 are non-isomorphic after deleting every
> datum whose replacement by a fixed default leaves Im(ι) unchanged up to relabelling; (ii) their
> seeds are disjoint; and (iii) their realized images Im(ι) are not equal up to relabelling of V
> and the declared moves."

---

## C. MINOR (each with replacement wording)

- **m1. Approximate Π falls outside the hand set.**
  - 𝒜_Π^hand contains only crisp partitions, but §1.3 allows a boundary ∂ ≠ ∅.
  - Under the hostile reading, the card's u ∉ FB. Then FB(u) has no model, so c_ι := 0, and 𝓗 = ∅.
  - The card can avoid this by returning crisp partitions.
  - Add to §2.3: "A realized Π with boundary ∂ is matched in 𝒜_Π^hand by the crisp partition that
    assigns ∂ to E."
- **m2. M(ι) "distinct Π" is undefined for approximate Π.** Wording: "M(ι) := the number of
  distinct persistent cores (∂ assigned to E) realized on Sol_ι, modulo G_ι."
- **m3. Size test against full symmetry.**
  - With G_ι = S_n the size test is capped at log₂(n − 1), which is below 6 for n ≤ 64.
  - So a GENERATED-STRONG lock fiber cannot be fully symmetric.
  - State it in §5.5: "the transitive lock fiber must also pass the b_Π size test."
- **m4. §1.4 (ii) and (iii) jointly require T_Π-orbits closed on the declared law class.** Add
  "(so T_Π-orbits are closed in the declared law class)" to (iii), or weaken (ii) to
  "⇒ P ∈ cl(T_Π·Q)".
- **m5. §1.4 (iv) admits a scale-free fixed post-map after the canonical form.** Such a map
  distorts d_op without introducing any priced constant. Wording: "(iv) s is the frozen centering
  and whitening of T_lin followed by a map built from T_Π alone; no fixed bijection of record space
  follows it."
- **m6. IP-6 and PS-5 conflict on VB-16.** VB-16 "microscopic reversibility" costs 4 bits, but it
  is PS-5 content (priced under IP-7). Wording in IP-6: "VB-16 used as microscopic reversibility,
  rather than as a parity label, is a PS-5 input priced under IP-7 and governed by NR-12."
- **m7. §4.1 typing carve-out ("𝒦's own transition rule").** An input-independent kernel is a
  prior, priced at L_stmt and outside NR-9. Add: "A kernel whose output law does not depend on its
  input on Dom_pre is a measure (VB-13; NR-9), not a transition rule."
- **m8. NR-1's flag list includes bare "measures, weights".** Under CV-1 that list flags every
  stochastic transition rule. Wording: "invariant, thermal, prior or reference measures and
  weights (a stochastic transition rule of 𝒦 is flagged only for its PS-5 content, §4.1)".
- **m9. The charter does not constrain canonical forms.** The kit sets them, but no rule limits
  their content. Add to IP-6: "A canonical form is the generic structure with its defining axioms.
  It fixes no instance, parameter, graph, group, measure, unit or value."
- **m10. c_f's regime is ambiguous.** "FB(u | H_f) on the hostile fiber" mixes H_f and H_host.
  Wording: "inside FB(u | H_host(ι_f))".
- **m11. NR-4 "appears within r_lock" ties a mathematical ablation to σ_pre.**
  - A noisier lock gives a larger r_lock, and then more relocation.
  - Relations whose two sides vanish together in the weakly coupled corner can reach 1/Q_min under
    log-uniform couplings.
  - Owner to consider excluding from both numerator and denominator the points where every lock
    observable is within r_lock of its value on S–E-decoupled families.
- **m12. IP-13 ignores exclusions among redraws.** Domain exclusions among the up to 10·N_cred
  redraws beyond N_AI3 are unpriced. Wording: "k_ex counts every excluded draw, committed or
  redrawn; N := N_AI3 + redraws."
- **m13. IP-12's "estimated … by any agent" is unbounded.** It includes unlogged reasoning, which
  risks KU-10. Wording: "computed or estimated by a program, or recorded in any logged artifact".
- **m14. NR-7's "X tracks the component" is undefined.** Wording: "if a decoder of cost ≤ ℓ_dec
  that reads the scrambled datum recovers the scrambled instance's X on a fraction ≥ p_dec of
  draws".
- **m15. The D_card clock runs while owner-side CI-n recording blocks drafting.** It cannot be
  extended after the first draft. Wording: "D_card runs from the later of the checkpoint and the
  recording of every CI-n that BU-6 requires before the next draft."
- **m16. §15.9 pool shortfall after the single reselection is unspecified.** Wording: "If the
  reselection still cannot supply fresh items, the gate is decided on the fresh items available,
  provided at least one exists; otherwise the item class is reported void for that card and does
  not count against it."
- **m17. The E₂± and T_caus canonical forms need finite, nonsingular covariance.** Wording: "on
  laws without finite nonsingular covariance, ε at E₂± and T_caus is undefined and the claim fails
  Q8."

---

## D. Rewritten rules checked and found sound (apart from the items above)
- **§2.3, partly sound:**
  - 𝒜_Π^hand is never reduced, and STANDARD-MECHANISM is recorded on the realized dynamics.
  - This removes audit C's B1 cliff and the A2 N-01 to N-05 problems.
  - The defects are confined to R2-B1 and R2-M3.
- **§1.4 catalogue conventions:**
  - The E₂± per-coordinate standardization with residual {±1}^k is consistent.
  - So is the T_caus Cholesky innovation with residual {±1}^k. Invariance and maximality hold:
    for A lower-triangular, the Cholesky factor of AΣAᵀ is AL·D with D a diagonal sign matrix.
  - They are consistent with E₂± ⊂ T_caus ⊂ T_lin and with DEF-4 zero-set monotonicity.
  - No R1 tier is altered.
- **§2.5:**
  - The per-instance c_ι definition, including the non-standard rule "c_ι := 0".
  - The lock-fiber cap c_lock (modulo m10).
  - The b_J min-structure, given R2-B2 and R2-M12.
  - "c_J never exceeds the number of … scalar equations …".
- **§4:**
  - IP-6's flat 4-bit price as such: I found no route to smuggle target content through a canonical
    item, provided m9 holds. The decoders (RB5 orbits, RB6 balls, SPS charge and locality reads)
    still catch Π hidden in VB-12, VB-14 and VB-15 content.
  - IP-4 and IP-14 bounded families: log₂ m ≈ L_stmt at most, and there is no double charge.
  - IP-12 template counting: encoding clause choices as priced switch constants costs more under
    IP-5 than under IP-12, so it gives no advantage.
  - IP-13 with N_AI3 = 160 (k = 16 costs ≈ 72 bits).
  - ΔL₀ = b_J − Price with D_sel in LOOKUP only.
- **NR-7 scramble scope:** no longer a universal kill.
- **NR-10(m):** horizon doubling and scale window.
- **PC-6 law-evaluation ban:** consistent with NR-3 and NR-4.
- **Q3(a) witness wording:** "satisfies every hypothesis of F" is satisfiable, and a framework
  without a model class is met by any consistent witness.
- **Q4:** the second sentence.
- **Q9:** the any-scope part now covers SCOPE-G.
- **BU-6:**
  - a fresh Selector, and exclusion of earlier unsealed items;
  - cumulative re-runs of decoders, witnesses, transplants and comparators;
  - the pick order committed before any lock unsealing (lock data are unsealed only after the pick,
    §18.1 step 8).
- **§15.1/§15.2:** collapse no longer fails G-SEL by itself. It sets D_sel = 0 and makes SFP-10
  mandatory. GY-6 still catches ASP-type collapse through KU-9. The Hamming diagnostic is harmless.

---

## E. Five-line summary
1. **Four BLOCKERs.**
   - §2.3 tells a card that a standard selector reading Π off 𝒞 is "never a relocation",
     contradicting NR-6 and ST-7 (R2-B1).
   - Price(M)'s per-instance hand-Π charge makes c_J(b) and the family cap vacuous for every card
     whose Π is generated, reopening CT-78 at about 1 000 bits (R2-B2).
   - NR-17's "any R ⊇ Sol" lets a trivial superset 𝒦 ∨ X RELOCATE compact laws (R2-B3).
   - NR-10(n) makes every card NONGENERATIVE, because the charter's own uniform Obs can never
     express E2 or the twin (R2-B4).
2. **Hidden kills (MAJOR).** VB-6 matching through c_dec-definability (M1); singleton fixed-T
   fibers zeroing c_J (M5); constant decoders defeating catalogue-class T_Π (M6a); Q5's trivial
   split (M7); favourable CI-n unable to rescue the disputing card (M11).
3. **New loopholes (MAJOR).** Decorative-read persistence (M2); inert-relatum padding of the size
   test (M3); provenance laundering into T_Π (M4); a menu-branch T_Π (M6b); card-shaped E_std and
   selective ⊥ in transplants (M8); a Bonferroni-widened confirmation band (M9); a pre-aggregation
   static nonlinearity escaping PC-7(b) and DIF-5(e) (M10); decorated copies inflating N_dist (M12).
4. **Sound.** IP-6's flat price (no target smuggling through canonical items, given m9), IP-4,
   IP-12, IP-13, IP-14, ΔL₀/D_sel, the catalogue conventions, the BU-6 sealing machinery, the §15
   collapse change, Q3(a), Q4, Q9, NR-7, NR-10(m) and the PC-6 law-evaluation ban.
5. **Verdict: do not freeze as drafted.** Each BLOCKER is a one-paragraph textual fix, given above.
   No candidate law appears in this report or, on my reading, in the charter.
