# 3. Shared exogenous descriptions {#sec:classes}

Every competitor description below is one model shared by *all* admissible clamps: its objects may depend on the prescribed path up to the present, $q_{[0,t]}$, but not on a protocol label. No Gaussian, Markov, finite-memory or stationarity restriction is imposed. Sharing is essential, because a separate exogenous process fitted to each protocol always succeeds (Supplement S3).

<!-- M:def.classes -->
**The nested ladder.**

<!-- M:def.H -->
- $\mathcal{H}$ — *the harmonic class*: harmonic baths whose coupling is linear in the bath coordinates and in the system coordinate, with counterterm, and whose free-force law does not depend on the system's initial state. Under clamping their force is a free exogenous force minus a deterministic memory term (Supplement S3).
- $\mathcal{E}_1$ — *additive exogenous forcing*: $F_q(t) = M_t[q] + \xi(t)$, with $M$ an arbitrary deterministic causal functional (nonlinear, unlimited memory) and $\xi$ one exogenous process whose law does not depend on $q$.
<!-- M:def.e2pm -->
- $\mathcal{E}_2^{\pm}$ — *shared signed-affine exogenous forcing*:
$$
F_q(t) = M_t[q] + G_t[q]\, \xi(t), \qquad G_t[q] \in \mathbb{R} \setminus \{0\},
$$ {#eq:e2pm}
with $M$ and $G$ arbitrary deterministic causal functionals and $\xi$ one exogenous process with one protocol-independent path law. The *signed causal scale* $G$ may change sign but may not vanish; a zero would make the force degenerate and is not an invertible affine map. Arbitrary nonlinear transformations of $\xi$ are excluded: history may change the location, the magnitude and the sign of the random force, but not its standardised shape.
- $\mathcal{E}_{\mathrm{univ}}$ — *universal causal exogenous representation*: $F_q(t) = \mathfrak{F}_t[q, U]$, with $U$ one exogenous random object of protocol-independent law and $\mathfrak{F}$ any deterministic functional causal in $q$.

<!-- M:prop.ladder -->
These classes form the ladder
$$
\mathcal{H} \subset \mathcal{E}_1 \subsetneq \mathcal{E}_2^{\pm} \subsetneq \mathcal{E}_{\mathrm{univ}},
$$ {#eq:ladder}
where, for the class $\mathcal{H}$ of environments, "$\subset$" means that the interventional force family of every environment in $\mathcal{H}$ lies in $\mathcal{E}_1$, and both inclusions among the $\mathcal{E}$-classes are strict (Supplement S3).
<!-- M:prop.upper -->
Every classical, deterministic, causal environment of the type considered here, reciprocal and energy-absorbing back-reaction included, lies in $\mathcal{E}_{\mathrm{univ}}$; so does model $\mathcal{D}$. Back-reaction as such is therefore never identifiable at the universal level, and the content of the question lies at the boundary between $\mathcal{E}_2^{\pm}$ and $\mathcal{E}_{\mathrm{univ}}$.

<!-- M:prop.c2pm -->
**Operational form and prefix consistency.** Write $Z_q(t) = (F_q(t) - \mathbb{E} F_q(t))/\operatorname{sd} F_q(t)$ for the standardised force at times where the variance is non-zero, and $D_q$ for the set of times where it vanishes. Under clamping, finite second moments and environment causality (the law of $F_q$ on $[0, t]$ depends on $q$ only through $q_{[0,t]}$), and at the level of finite-dimensional distributions, a force family lies in $\mathcal{E}_2^{\pm}$ exactly when (i) $D_q = D$ is common to all protocols, and (ii) there is one shared deterministic causal sign functional $S_t : q_{[0,t]} \mapsto \{+1, -1\}$ such that, with $s_q(t) = S_t[q_{[0,t]}]$, the finite-dimensional laws of $s_q Z_q$ off $D$ are the same for every protocol. Prefix consistency is part of membership: two protocols that agree up to time $t$ must receive the same sign at $t$.

<!-- M:lem.e2pm_necessity -->
**The invariant used here.** Within $\mathcal{E}_2^{\pm}$, a clamped protocol gives $F_q(t) = M_t[q] + G_t[q]\,\xi(t)$ with deterministic numbers $M_t[q]$ and $G_t[q] \neq 0$, so
$$
\gamma_1[F_q(t)] = \operatorname{sgn}\!\left(G_t[q]\right)\, \gamma_1[\xi(t)], \qquad \gamma_1[Y] = \frac{\kappa_3(Y)}{\operatorname{Var}(Y)^{3/2}} .
$$ {#eq:g1-invariant}
The *absolute* standardised skewness is therefore the same for every protocol at every non-degenerate time. A protocol pair with $|\gamma_1|$ zero for one and non-zero for the other, at a time where both variances are positive, proves that no shared signed-affine representation exists. Sign changes alone never count as such a witness, and neither does a protocol-dependent zero of the variance.
