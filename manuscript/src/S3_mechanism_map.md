# S3. Mechanism map {#sec:S3}

This supplement records which effects of a non-trivial protocol a shared signed-affine model can absorb, and at which order in $1/N_B$ each enters the force law of model $\mathcal{D}$.

<!-- M:mech.parity -->
**Expansion and parity.** Expand the driven oscillator as $X^\varepsilon_q = x_0 + \varepsilon y_1 + \varepsilon^2 y_2 + \varepsilon^3 y_3 + \dots$, where $\ddot y_1 + (1 + 3x_0^2)\, y_1 = q(t)$, $\ddot y_2 + (1 + 3x_0^2)\, y_2 = -3x_0 y_1^2$, and so on, all from zero initial data. By induction $y_k$ is even in $x_0$ for odd $k$ and odd in $x_0$ for even $k$, and $y_k$ is homogeneous of degree $k$ in $q$. Gibbs expectations of $x_0$-odd functionals vanish.

<!-- M:mech.orders -->
**Order of each effect.** Combining the exact identity @eq:S1-star with parity gives the following map. Only the third-cumulant row is proved in this work (Lemma 3); the other rows follow from the same expansion *assuming* it holds to all orders in $L^p$ on the finite horizon, which is plausible but not proved here.

| effect relative to the reference protocol | order | absorbed by a shared signed-affine model? |
| :---------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| deterministic mean response $\mathbb{E} F_q(t)$ | linear response at order one, plus $O(N_B^{-1})$ | yes, by $M$ |
| per-time variance change | $O(N_B^{-1})$ | yes, by $\lvert G \rvert$ |
| sign of the random force | any | yes, by the sign of $G$ |
| third cumulants, including mixed ones (proved) | $O(N_B^{-1})$, zero for the reference protocol | **no**: changes standardised shape |
| changes of correlation coefficients between distinct times | $O(N_B^{-1})$ | **no**, if not removable by sign flips |
| fourth and fifth cumulants | $O(N_B^{-2})$ | shape change at higher order |
| cumulant of order $n$ | $N_B^{(1-n)/2}$ for odd $n$; $N_B^{-n/2}$ for even $n$ | |

There is no change of the force law at order $N_B^{-1/2}$: the pathwise correction of that order enters every cumulant only through $x_0$-odd cross terms, which vanish.

<!-- M:mech.physical -->
**Physical mechanism.** The first-order response obeys a linear oscillator equation whose stiffness $1 + 3x_0^2$ is set by the oscillator's own state. Oscillators that are instantaneously stiffer, with larger $x_0^2$ and typically higher energy, respond less to the ramp. The response $y_1$ is therefore negatively correlated with $x_0^2$, which is the content of $c(t) < 0$, and this correlation between the random part of the force and the amplitude of the response skews the force distribution. Equivalently, back-reaction couples the *shape* of the force law to the protocol, not only its location and scale.

<!-- M:mech.control -->
**What does not escape.** A harmonic bath coupled to the system through a nonlinear function $A(q)$ with $A'(q) = 1 + q^2$ produces the force $F_q(t) = M_t[q] + A'(q(t))\, \xi(t)$, with $\xi$ the free bath force and $M$ a deterministic memory term. This lies exactly in $\mathcal{E}_2^{\pm}$ (it escapes $\mathcal{E}_1$, because the variance depends on the protocol). History-dependent noise amplitude, the usual multiplicative response, is therefore not the effect reported in the main text.
