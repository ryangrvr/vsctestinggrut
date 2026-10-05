# S4. Competitor classes: proofs {#sec:S4}

This supplement proves the statements about the competitor classes used in Section 3. The setting is a clamped protocol family on $[0, T]$ with one shared environment preparation and a causal environment: the law of the force on $[0, t]$ depends on $q$ only through $q_{[0,t]}$.

<!-- M:prop.vacuity -->
**Proposition S4.1 (a single protocol never discriminates).** Fix one protocol: a potential $V$, a drive $u$, deterministic initial data $(q_0, \dot q_0)$ and a horizon $[0, T]$ for $m\ddot q = -V'(q) + u(t) + F_{\mathrm{env}}(t)$, and suppose the equation has a unique solution for every admissible forcing path $f$, with a measurable solution map $q = \Phi(q_0, \dot q_0, f)$. Define the realised environment force $F_{\mathrm{env}} = m \ddot q + V'(q) - u$. Then the additive exogenous model with no memory and $\operatorname{Law}(\xi) = \operatorname{Law}(F_{\mathrm{env}})$ reproduces the reduced path law of that protocol exactly.

*Proof.* In the true system $q = \Phi(q_0, \dot q_0, F_{\mathrm{env}})$ pathwise; in the model $q = \Phi(q_0, \dot q_0, \xi)$. Equal input laws give equal push-forward laws. $\square$ With random initial data the same construction requires $\xi$ to be jointly distributed with the initial data as $F_{\mathrm{env}}$ is; the conclusion is unchanged. Every discriminating statement must therefore compare one shared model across several protocols.

<!-- M:prop.c1 -->
**Proposition S4.2 (characterisation of $\mathcal{E}_1$).** Assume $\mathbb{E} F_q(t)^2 < \infty$. A family lies in $\mathcal{E}_1$ if and only if the finite-dimensional laws of the centred force $\mathring F_q$ are the same for all clamps (equivalently, equal to those of the reference protocol).

*Proof.* If $F_q = M[q] + \xi$, then for a clamped $q$ the number $M_t[q]$ is deterministic, so $\mathring F_q = \xi - \mathbb{E}\xi$ for every $q$. Conversely, set $\xi = \mathring F_{\mathrm{ref}}$ and $M_t[q] = \mathbb{E} F_q(t)$, which is causal by causality of the environment. $\square$

<!-- M:prop.c2pm -->
**Proposition S4.3 (characterisation of $\mathcal{E}_2^{\pm}$).** Assume $\mathbb{E} F_q(t)^2 < \infty$. A family lies in $\mathcal{E}_2^{\pm}$ if and only if (i) the degeneracy set $D_q = D$ is common to all clamps, and (ii) there is one shared deterministic causal sign functional $S_t : q_{[0,t]} \mapsto \{\pm 1\}$ such that, with $s_q(t) = S_t[q_{[0,t]}]$, the finite-dimensional laws of $s_q Z_q$ off $D$ are common to all clamps.

*Proof.* ($\Rightarrow$) For a clamped $q$, $F_q(t) = m_q(t) + g_q(t)\, \xi(t)$ with deterministic causal $m_q, g_q$ and $g_q(t) \neq 0$. Then $\operatorname{Var} F_q(t) = g_q(t)^2 \operatorname{Var}\xi(t)$, so $D_q = \{t : \operatorname{Var}\xi(t) = 0\}$ for every $q$, and off $D$, $Z_q(t) = \operatorname{sgn}(g_q(t))\, Z_\xi(t)$. Put $S_t[q_{[0,t]}] = \operatorname{sgn} G_t[q]$, a functional of the prefix because $G$ is causal; then $s_q Z_q = Z_\xi$ has a protocol-independent law.
($\Leftarrow$) Let $\mathcal{L}$ be the common law of $s_q Z_q$ off $D$; let $\xi$ have finite-dimensional laws $\mathcal{L}$ off $D$ and $\xi = 0$ on $D$. Put $M_t[q] = \mathbb{E} F_q(t)$, and $G_t[q] = S_t[q_{[0,t]}]\, \operatorname{sd} F_q(t)$ off $D$, $G_t[q] = 1$ on $D$, so that $G \neq 0$ everywhere; both are causal. Off $D$, $M + G\xi$ has the finite-dimensional laws of $\mathbb{E} F_q + \operatorname{sd} F_q\, s_q (s_q Z_q) = F_q$ because $s_q^2 = 1$; on $D$ both sides equal $\mathbb{E} F_q$. $\square$

The statement is about finite-dimensional distributions; it is upgraded to path laws only when the force processes have continuous (or càdlàg) versions. Prefix consistency is essential: a family can satisfy the reflection condition at every finite tuple of times separately and still fail (ii), because the per-tuple sign choices need not be causal. A finite family of protocols can prove escape but can never prove membership.

<!-- M:prop.ladder_strict -->
**Proposition S4.4 (strict ladder).** $\mathcal{E}_1 \subsetneq \mathcal{E}_2^{\pm} \subsetneq \mathcal{E}_{\mathrm{univ}}$.

*Proof.* Inclusions: take $G \equiv 1$; and take $U = \xi$, $\mathfrak{F}_t[q, U] = M_t[q] + G_t[q]\, U(t)$. Strictness, with $\xi(t)$ independent standard normal on a time grid: (a) $F_q(t) = (1 + q(t)^2)\, \xi(t)$ lies in $\mathcal{E}_2^{\pm}$ but not in $\mathcal{E}_1$, because $\operatorname{Var} F_q(t) = (1 + q(t)^2)^2$ depends on $q$ while Proposition S4.2 requires a protocol-invariant centred law. (b) $F_q(t) = \xi(t) + q(t)\left(\xi(t)^2 - 1\right)$ lies in $\mathcal{E}_{\mathrm{univ}}$; its variance is $1 + 2q^2$ and its third central moment is $6q + 8q^3$ with $q = q(t)$, so $|\gamma_1|$ vanishes when $q(t) = 0$ and not otherwise. Since $|\gamma_1|$ is invariant under signed-affine maps, the family is not in $\mathcal{E}_2^{\pm}$. $\square$

<!-- M:prop.upper -->
**Proposition S4.5 (universal upper bound).** Let the environment state $Y \in \mathbb{R}^d$ obey $\dot Y = B(Y, q(t))$ with $B$ locally Lipschitz in $Y$ and continuous in $q$, with no blow-up on $[0, T]$ for admissible clamps; let the force be $F = C(Y, q)$ with $C$ measurable, and the initial state $Y(0) = \Psi(q(0), U)$ for one fixed map $\Psi$ and one exogenous random object $U$. Then $F_q(t) = C(\mathcal{Y}_t[q, U], q(t))$ with $\mathcal{Y}$ the solution flow, the pair $(\operatorname{Law} U, \mathfrak{F})$ is shared across clamps, and $\mathfrak{F}$ is causal in $q$. Hence every such environment lies in $\mathcal{E}_{\mathrm{univ}}$.

*Proof.* Existence and uniqueness follow from the Picard–Lindelöf theorem and the no-blow-up hypothesis; two clamps that agree on $[0, t]$ give the same solution on $[0, t]$ by uniqueness, so $\mathcal{Y}_t$ depends only on $q_{[0,t]}$; continuous dependence on initial data and measurability of $\Psi$ give measurability in $U$; and $B$, $C$, $\Psi$, $\operatorname{Law} U$ belong to the environment, not to the protocol. $\square$ Reciprocal, energy-absorbing back-reaction is included, and model $\mathcal{D}$ is of this type. A continuous-time statement for general stochastic environments is not claimed, and quantum environments are out of scope.
