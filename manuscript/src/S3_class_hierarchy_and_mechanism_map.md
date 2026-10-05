# S3. Class hierarchy and mechanism map {#sec:S3}

This supplement proves the nested ladder of Section 3 and assigns each environment mechanism used in the paper to the smallest class that is proved to contain it. Every assignment below is a proved statement; nothing in this supplement rests on an unproved expansion. Throughout, the setting is a clamped protocol family with one shared environment preparation and a causal environment: the law of the force on $[0, t]$ depends on $q$ only through $q_{[0,t]}$.

## S3.1 The proved class hierarchy {#sec:S3-ladder}

<!-- M:def.H -->
**The class $\mathcal{H}$.** An environment belongs to $\mathcal{H}$ if it is a harmonic bath whose coupling is linear in the bath coordinates and in the system coordinate, with the usual counterterm, and whose free-force law does not depend on the system's initial state. For classes of environments, "$\subset$" below means that the interventional force family of every environment in the smaller class lies in the larger class.

<!-- M:prop.vacuity -->
**Proposition S3.1 (a single protocol never discriminates).** Fix one protocol: a potential $V$, a drive $u$, deterministic initial data $(q_0, \dot q_0)$ and a horizon $[0, T]$ for $m\ddot q = -V'(q) + u(t) + F_{\mathrm{env}}(t)$, and suppose the equation has a unique solution for every admissible forcing path $f$, with a measurable solution map $q = \Phi(q_0, \dot q_0, f)$. Define the realised environment force $F_{\mathrm{env}} = m \ddot q + V'(q) - u$. Then the additive exogenous model with no memory and $\operatorname{Law}(\xi) = \operatorname{Law}(F_{\mathrm{env}})$ reproduces the reduced path law of that protocol exactly.

*Proof.* In the true system $q = \Phi(q_0, \dot q_0, F_{\mathrm{env}})$ pathwise; in the model $q = \Phi(q_0, \dot q_0, \xi)$. Equal input laws give equal push-forward laws. $\square$ With random initial data the same construction requires $\xi$ to be jointly distributed with the initial data as $F_{\mathrm{env}}$ is; the conclusion is unchanged. Every discriminating statement must therefore compare one shared model across several protocols.

<!-- M:prop.affine_bath -->
**Lemma S3.2 (harmonic bath coupled through a function of $q$).** Let the bath be harmonic, $H_B = \sum_j \big[ p_j^2/2 + (\omega_j^2/2)\big(x_j - c_j A(q)/\omega_j^2\big)^2 \big]$, with $A$ smooth and $A(0) = 0$, prepared at $q(0) = 0$ from one fixed law, and let the force be $F = -\partial H_B / \partial q$. Then for every clamp $q \in \mathcal{X}$
$$
F_q(t) = A'(q(t)) \left[ \xi(t) - \int_0^t \gamma(t - s)\, \frac{\mathrm{d}}{\mathrm{d}s} A(q(s))\, \mathrm{d}s \right],
$$ {#eq:S3-affine}
with
$$
\xi(t) = \sum_j c_j \left[ x_j(0) \cos \omega_j t + \frac{p_j(0)}{\omega_j} \sin \omega_j t \right], \qquad
\gamma(t) = \sum_j \frac{c_j^2}{\omega_j^2} \cos \omega_j t .
$$ {#eq:S3-xi-gamma}

*Proof.* The bath obeys $\ddot x_j = -\omega_j^2 x_j + c_j A(q(t))$, a linear equation driven by the deterministic path $A(q(\cdot))$. Variation of constants and one integration by parts, using $A(q(0)) = 0$, give $\sum_j c_j (x_j - c_j A(q)/\omega_j^2) = \xi(t) - \int_0^t \gamma(t-s)\, \tfrac{\mathrm{d}}{\mathrm{d}s} A(q(s))\, \mathrm{d}s$, and $F = A'(q) \sum_j c_j (x_j - c_j A(q)/\omega_j^2)$. The process $\xi$ depends only on the bath's initial data, whose law does not depend on the protocol. $\square$

<!-- M:prop.H_in_E1 -->
**Proposition S3.3 ($\mathcal{H} \subset \mathcal{E}_1$).** Under clamping, every environment in $\mathcal{H}$ has $F_q(t) = \xi(t) - \int_0^t \gamma(t - s)\, \dot q(s)\, \mathrm{d}s$, with $\xi$ the free force; hence its force family lies in $\mathcal{E}_1$, with $M_t[q] = -\int_0^t \gamma(t-s)\, \dot q(s)\, \mathrm{d}s$.

*Proof.* Lemma S3.2 with $A(q) = q$ (so $A' \equiv 1$). The counterterm and initial-slip terms are deterministic in $q$ or vanish at $q(0) = 0$. $\square$

<!-- M:prop.c1 -->
**Proposition S3.4 (characterisation of $\mathcal{E}_1$).** Assume $\mathbb{E} F_q(t)^2 < \infty$. A family lies in $\mathcal{E}_1$ if and only if the finite-dimensional laws of the centred force $\mathring F_q$ are the same for all clamps (equivalently, equal to those of the reference protocol).

*Proof.* If $F_q = M[q] + \xi$, then for a clamped $q$ the number $M_t[q]$ is deterministic, so $\mathring F_q = \xi - \mathbb{E}\xi$ for every $q$. Conversely, set $\xi = \mathring F_{\mathrm{ref}}$ and $M_t[q] = \mathbb{E} F_q(t)$, which is causal by causality of the environment. $\square$

<!-- M:prop.c2pm -->
**Proposition S3.5 (characterisation of $\mathcal{E}_2^{\pm}$).** Assume $\mathbb{E} F_q(t)^2 < \infty$. A family lies in $\mathcal{E}_2^{\pm}$ if and only if (i) the degeneracy set $D_q = D$ is common to all clamps, and (ii) there is one shared deterministic causal sign functional $S_t : q_{[0,t]} \mapsto \{\pm 1\}$ such that, with $s_q(t) = S_t[q_{[0,t]}]$, the finite-dimensional laws of $s_q Z_q$ off $D$ are common to all clamps.

*Proof.* ($\Rightarrow$) For a clamped $q$, $F_q(t) = m_q(t) + g_q(t)\, \xi(t)$ with deterministic causal $m_q, g_q$ and $g_q(t) \neq 0$. Then $\operatorname{Var} F_q(t) = g_q(t)^2 \operatorname{Var}\xi(t)$, so $D_q = \{t : \operatorname{Var}\xi(t) = 0\}$ for every $q$, and off $D$, $Z_q(t) = \operatorname{sgn}(g_q(t))\, Z_\xi(t)$. Put $S_t[q_{[0,t]}] = \operatorname{sgn} G_t[q]$, a functional of the prefix because $G$ is causal; then $s_q Z_q = Z_\xi$ has a protocol-independent law.
($\Leftarrow$) Let $\mathcal{L}$ be the common law of $s_q Z_q$ off $D$; let $\xi$ have finite-dimensional laws $\mathcal{L}$ off $D$ and $\xi = 0$ on $D$. Put $M_t[q] = \mathbb{E} F_q(t)$, and $G_t[q] = S_t[q_{[0,t]}]\, \operatorname{sd} F_q(t)$ off $D$, $G_t[q] = 1$ on $D$, so that $G \neq 0$ everywhere; both are causal. Off $D$, $M + G\xi$ has the finite-dimensional laws of $\mathbb{E} F_q + \operatorname{sd} F_q\, s_q (s_q Z_q) = F_q$ because $s_q^2 = 1$; on $D$ both sides equal $\mathbb{E} F_q$. $\square$

The statement concerns finite-dimensional distributions; it is upgraded to path laws only when the force processes have continuous (or càdlàg) versions. Prefix consistency is essential: a family can satisfy the reflection condition at every finite tuple of times separately and still fail (ii), because the per-tuple sign choices need not be causal. A finite family of protocols can prove escape but can never prove membership.

<!-- M:prop.ladder_strict -->
**Proposition S3.6 (strict ladder).** $\mathcal{E}_1 \subsetneq \mathcal{E}_2^{\pm} \subsetneq \mathcal{E}_{\mathrm{univ}}$.

*Proof.* Inclusions: take $G \equiv 1$; and take $U = \xi$, $\mathfrak{F}_t[q, U] = M_t[q] + G_t[q]\, U(t)$. Strictness, with $\xi(t)$ independent standard normal on a time grid: (a) $F_q(t) = (1 + q(t)^2)\, \xi(t)$ lies in $\mathcal{E}_2^{\pm}$ but not in $\mathcal{E}_1$, because $\operatorname{Var} F_q(t) = (1 + q(t)^2)^2$ depends on $q$ while Proposition S3.4 requires a protocol-invariant centred law. (b) $F_q(t) = \xi(t) + q(t)\left(\xi(t)^2 - 1\right)$ lies in $\mathcal{E}_{\mathrm{univ}}$; its variance is $1 + 2q^2$ and its third central moment is $6q + 8q^3$ with $q = q(t)$, so $|\gamma_1|$ vanishes when $q(t) = 0$ and not otherwise. Since $|\gamma_1|$ is invariant under signed-affine maps, the family is not in $\mathcal{E}_2^{\pm}$. $\square$

<!-- M:prop.upper -->
**Proposition S3.7 (universal upper bound).** Let the environment state $Y \in \mathbb{R}^d$ obey $\dot Y = B(Y, q(t))$ with $B$ locally Lipschitz in $Y$ and continuous in $q$, with no blow-up on $[0, T]$ for admissible clamps; let the force be $F = C(Y, q)$ with $C$ measurable, and the initial state $Y(0) = \Psi(q(0), U)$ for one fixed map $\Psi$ and one exogenous random object $U$. Then $F_q(t) = C(\mathcal{Y}_t[q, U], q(t))$ with $\mathcal{Y}$ the solution flow, the pair $(\operatorname{Law} U, \mathfrak{F})$ is shared across clamps, and $\mathfrak{F}$ is causal in $q$. Hence every such environment lies in $\mathcal{E}_{\mathrm{univ}}$.

*Proof.* Existence and uniqueness follow from the Picard–Lindelöf theorem and the no-blow-up hypothesis; two clamps that agree on $[0, t]$ give the same solution on $[0, t]$ by uniqueness, so $\mathcal{Y}_t$ depends only on $q_{[0,t]}$; continuous dependence on initial data and measurability of $\Psi$ give measurability in $U$; and $B$, $C$, $\Psi$, $\operatorname{Law} U$ belong to the environment, not to the protocol. $\square$ Reciprocal, energy-absorbing back-reaction is included, and model $\mathcal{D}$ is of this type. A continuous-time statement for general stochastic environments is not claimed, and quantum environments are out of scope.

Together, Propositions S3.3, S3.6 and S3.7 give the ladder of Section 3,
$$
\mathcal{H} \subset \mathcal{E}_1 \subsetneq \mathcal{E}_2^{\pm} \subsetneq \mathcal{E}_{\mathrm{univ}} .
$$ {#eq:S3-ladder}

## S3.2 Mechanism map {#sec:S3-map}

<!-- M:mech.map -->
Each row assigns a mechanism to the smallest class proved to contain it, or records a proved escape.

| mechanism | class assignment | basis |
| :------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| harmonic bath, coupling linear in bath and system coordinates | $\mathcal{H}$, hence $\mathcal{E}_1$ | Proposition S3.3 |
| additive exogenous forcing with deterministic causal memory | $\mathcal{E}_1$ | definition of $\mathcal{E}_1$ |
| deterministic, protocol-dependent multiplicative modulation (magnitude and sign) of one shared noise | $\mathcal{E}_2^{\pm}$; does not escape it | definition of $\mathcal{E}_2^{\pm}$; Proposition S3.8 |
| finite reciprocal Duffing bath, model $\mathcal{D}$ | escapes $\mathcal{E}_2^{\pm}$ for every sufficiently large finite $N_B$ | Theorem 1 |
| model $\mathcal{D}$ in the reservoir limit, fixed protocols | centred laws converge to one common Gaussian law | Proposition 1, Supplement S4 |
| any deterministic causal environment of the parent type, model $\mathcal{D}$ included | $\mathcal{E}_{\mathrm{univ}}$ | Proposition S3.7 |

<!-- M:mech.control -->
**Proposition S3.8 (multiplicative modulation does not escape).** The harmonic bath coupled through $A(q) = q + q^3/3$ has, by Lemma S3.2, $F_q(t) = M_t[q] + G_t[q]\, \xi(t)$ with $G_t[q] = A'(q(t)) = 1 + q(t)^2 \geq 1$ and the deterministic causal memory $M_t[q] = -A'(q(t)) \int_0^t \gamma(t-s)\, A'(q(s))\, \dot q(s)\, \mathrm{d}s$. Its force family therefore lies in $\mathcal{E}_2^{\pm}$. With a thermal preparation, $\operatorname{Var}\xi(t) > 0$ is constant in time, so the degeneracy set is empty for every protocol; and the family does not lie in $\mathcal{E}_1$ once it contains a protocol with $q \not\equiv 0$, because $\operatorname{Var} F_q(t) = (1 + q(t)^2)^2 \operatorname{Var}\xi(t)$ then depends on the protocol. $\square$

History-dependent noise amplitude, including sign changes of the amplitude, is therefore ordinary multiplicative response and is not the effect of Theorem 1. What model $\mathcal{D}$ adds is a protocol-dependent change of the *standardised shape* of the force, which no shared signed-affine modulation can produce.
