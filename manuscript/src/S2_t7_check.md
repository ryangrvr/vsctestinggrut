# S2. Small-time consistency check {#sec:S2}

<!-- M:check.t7 -->
Lemma 4 gives the leading behaviour $K(t) = 3c(t) = 3 c_7 t^7 + O(t^8)$ with $c_7 = {{sym.C7}}$. This supplement compares the full first-order coefficient $K(t)$, computed numerically, with the leading term $3 c_7 t^7$ at four short times. The computation was written for this build and shares only the model definition with the code behind Section 6.

**Method.** For each initial condition $z_0 = (a, b)$ we integrate the unforced oscillator together with the response equation @eq:S1-y1 for the ramp protocol, and evaluate
$$
c(t) = \mathbb{E}\!\left[x_0(t)^2\, y_1(t)\right] - \mathbb{E}\!\left[x_0(t)^2\right] \mathbb{E}\!\left[y_1(t)\right]
$$ {#eq:S2-cov}
by quadrature over the Gibbs law at $\beta = 1$. Using the variational equation directly avoids the cancellation of a finite difference in $\varepsilon$. Two independent combinations are used: a probabilists' Gauss–Hermite tensor grid with the quartic Gibbs factor in the weights, integrated by a fixed-step fourth-order Runge–Kutta scheme at two grid sizes and two step sizes (primary); and a Gauss–Legendre tensor grid with the full Gibbs weight, integrated by an adaptive eighth-order Dormand–Prince scheme (method B). As a third, semi-analytic comparison, the exact series $\sum_{k=7}^{ {{sym.order_max}} } c_k t^k$ is summed with the coefficients produced by computer algebra. The constant $c_7$ uses $\operatorname{Var}(x_0^2)$ from a high-precision quadrature of the Gibbs marginal, which lies inside the certified enclosure recorded with the proof.

**Result.** The ratio $K(t)/(3c_7t^7)$ approaches one as $t \to 0$, as Lemma 4 requires:

Table S2.1: Numerical first-order coefficient against the leading small-time term. "Rel. spread" is the largest relative difference in $c(t)$ between all runs of both methods.

{{table:s2_t7}}

The departure from one is linear in $t$ at leading order: the exact next coefficient gives $c_8/c_7 = {{sym.ratio_C8_C7}}$.

<!-- M:check.symbolic -->
**Symbolic cross-check.** The coefficients $c_k$ were recomputed by an independent order-by-order recursion in exact arithmetic, with Gibbs moments reduced to $m_2$ through @eq:S1-moments. They vanish for $k \leq 6$, and every coefficient from $t^7$ through $t^{ {{sym.order_max}} }$ agrees exactly with the computer-algebra output recorded with the proof.
