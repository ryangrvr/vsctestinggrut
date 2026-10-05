# 4. Main result {#sec:main}

Three exact facts reduce the question to a single-oscillator computation.

<!-- M:lem.cumulant_identity -->
*Cumulants scale exactly with bath size.* Because $F_q = \varepsilon \sum_j X_j$ with independent copies $X_j$ of $X^\varepsilon_q$, for every order $n$ and every finite tuple of times
$$
\kappa_n\!\left(F_q(t_1), \dots, F_q(t_n)\right) = N_B^{\,1 - n/2}\; \kappa_n\!\left(X^\varepsilon_q(t_1), \dots, X^\varepsilon_q(t_n)\right).
$$ {#eq:star}

<!-- M:lem.parity -->
*The reference skewness vanishes exactly.* The unforced dynamics and the Gibbs law are invariant under $(x, p) \mapsto (-x, -p)$. Hence $\kappa_3(F_{\mathrm{ref}}(t)) = 0$ for every $t$ and every $N_B$, while $\operatorname{Var} F_{\mathrm{ref}}(t) = m_2 > 0$.

<!-- M:lem.first_order -->
*The ramp third cumulant has an explicit first-order coefficient.* The same reflection combined with $\varepsilon \mapsto -\varepsilon$ makes $\kappa_3(X^\varepsilon(t))$ odd in $\varepsilon$. Moment bounds from the energy estimate and Grönwall's inequality justify differentiating under the expectation, and for each fixed $t \in [0, 2\pi]$
$$
\kappa_3\!\left(F_{\mathrm{ramp}}(t)\right) = \frac{K(t)}{N_B} + O\!\left(N_B^{-2}\right), \qquad K(t) = 3c(t), \qquad c(t) = \operatorname{Cov}\!\left(x_0(t)^2,\, y_1(t)\right),
$$ {#eq:kappa3}
with a remainder constant that depends on $t$.

<!-- M:lem.small_time -->
**The small-time coefficient.** The first non-vanishing Taylor coefficient of $c(t)$ is that of $t^7$:
$$
c(t) = {{sym.C7}}\; t^7 + O(t^8), \qquad K(t) = 3c(t).
$$ {#eq:c-small}
The coefficient follows from an order-by-order solution of the equations for $x_0$ and $y_1$; the lower orders cancel through the Gibbs identity $m_2 + m_4 = 1$, and only the $x_0^2$-dependent part of the response survives (Supplement S1, Lemma 4). Since $\operatorname{Var}(x_0^2) > 0$, $c(t) < 0$ on some interval $(0, \delta)$.

**Physical reading.** The response $y_1$ of an oscillator to the ramp is weaker when its instantaneous stiffness $1 + 3x_0^2$ is larger, that is, when $x_0^2$ is large. The response is therefore anticorrelated with $x_0^2$, which is exactly what $c(t) < 0$ expresses, and this anticorrelation skews the summed force. Supplement S3 maps which parts of the ramp's effect a shared signed-affine model can absorb and which it cannot.

{{include:thm_main}}

<!-- M:proof.thm -->
*Proof sketch.* Fix $t \in (0, \delta)$, so $K(t) < 0$. By @eq:kappa3 there is a finite $N_0(t)$ beyond which the remainder is smaller than $|K(t)|/N_B$, so $\kappa_3(F_{\mathrm{ramp}}(t)) < 0$. The ramp force variance is strictly positive, because the time-$t$ flow map is a diffeomorphism carrying the Gibbs density to a density. Hence $\gamma_1[F_{\mathrm{ramp}}(t)] < 0 = \gamma_1[F_{\mathrm{ref}}(t)]$ at a time where both variances are positive, which contradicts @eq:g1-invariant. Supplement S1 gives every step, including the remainder bounds and the definition $N_0(t) = \lfloor \Theta(t)/|K(t)| \rfloor + 1$. $\square$

<!-- M:scope.theorem -->
The statement is pointwise in $t$: for each fixed short time there is a threshold. It is not a uniform statement over an interval, and neither $\delta$ nor $N_0(t)$ is computed. No time was selected numerically: the interval is forced by the sign of the first non-zero Taylor coefficient, and the protocols were fixed before any computation.
