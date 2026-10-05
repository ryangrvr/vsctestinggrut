# 6. Numerical illustration {#sec:numerics}

<!-- M:scope.numerics -->
The theorem is analytic and does not use the numbers in this section. The computation below illustrates the finite-$N_B$ behaviour at fixed finite times; it is evidence-grade, not certified, and it is not part of the proof. In particular, the primary time $t_\star = 0.5$ and the diagnostic times ${{num.t_diag_1}}$, ${{num.t_diag_2}}$ and ${{num.t_diag_3}}$ were fixed in advance, and none of them is claimed to lie inside the theorem's window $(0, \delta)$.

<!-- M:num.method -->
**Method.** By the single-oscillator reduction, every $N_B$ requires only the one-oscillator process $X^\varepsilon$ at $\varepsilon = N_B^{-1/2}$, and the force cumulants follow exactly from @eq:star. Gibbs expectations over the initial data $(x_0, p_0)$ are evaluated by deterministic tensor Gauss–Legendre quadrature on $[-{{num.L}}, {{num.L}}]^2$ with ${{num.nx}}$ nodes per dimension, every node pair being evolved separately with a fixed-step fourth-order Runge–Kutta integrator of step ${{num.dt}}$. No sampling is involved. The bath sizes are $N_B \in \{4, 8, 16, 32, 64, 128\}$. Details and the full tables are in Supplements S5 and S6.

<!-- M:num.controls -->
**Controls.** The reference protocol is stationary on the grid: its variance stays at ${{num.ref_var_t0}}$ with maximal drift ${{num.ref_var_drift}}$ over the sampled times, its mean and third cumulant remain below ${{num.ref_mean_max}}$ and ${{num.ref_k3_max}}$ in magnitude, and the initial variance agrees with an independent one-dimensional quadrature of the Gibbs marginal (${{num.gl_1d}}$ nodes), ${{num.ind1d_m2}}$, to relative discrepancy ${{num.ref_rel_disc}}$. Our own high-precision evaluation of the marginal gives $m_2 = {{const.m2}}$ and $\operatorname{Var}(x_0^2) = {{const.var_x0sq}}$, the latter inside the certified enclosure recorded with the proof. The exact identity $m_2 + m_4 = 1$ holds on the grid to ${{num.gibbs_residual}}$. Reversing the sign of the coupling reverses the third cumulant: $\kappa_3(X^{-\varepsilon}) / \kappa_3(X^{+\varepsilon}) + 1$ is at most ${{num.odd_ratio_dev}}$ in magnitude for $N_B \in \{ {{num.odd_nbs}} \}$. The stationarity and moment controls are independent of the witness; the sign-reversal check is a symmetry control of the implementation only.

<!-- M:num.results -->
**Results.** At $t_\star = 0.5$ the ramp protocol has negative standardised skewness at every bath size, $\gamma_1 = {{num.g1_tstar_nbmin}}$ at $N_B = 4$ and ${{num.g1_tstar_nbmax}}$ at $N_B = 128$ (Table 1, @fig:scaling). A least-squares fit of $\log|\gamma_1|$ against $\log N_B$ over all six bath sizes gives exponent $p = {{num.global_p}}$, with local exponents between ${{num.local_p_min}}$ and ${{num.local_p_max}}$. The product $N_B \gamma_1$ is flat across the grid to relative spread ${{num.nbg1_tstar_relspread}}$ (@fig:scaling-flat), so no finite-$N_B$ correction is resolved at $t_\star$. At the latest diagnostic time ${{num.t_diag_3}}$ a monotone correction is resolved: $N_B \gamma_1$ drifts by a relative ${{num.nbg1_diag_3_drift}}$ between the smallest and largest bath sizes. All four times show negative skewness and the same $1/N_B$ scaling (Supplement S5).

Table 1: Ramp-protocol standardised skewness at $t_\star = 0.5$. Generated from the authoritative numerical output.

{{table:main_tstar}}

<!-- M:num.crosscheck -->
**Independent cross-check.** Proposition 1(a) predicts $N_B\, \gamma_1 \to K(t)/m_2^{3/2}$. Evaluating $K(t)$ with separately written small-time code (Supplement S2) and $m_2$ from our marginal quadrature gives $K(t_\star)/m_2^{3/2} = {{x.pred_tstar}}$, against $N_B\gamma_1 = {{x.obs_tstar}}$ at $N_B = 128$: relative difference ${{x.reldiff_tstar}}$. At $t = {{num.t_diag_1}}$ the relative difference is ${{x.reldiff_t025}}$. The two computations share only the model definition.

![Standardised skewness of the ramp-protocol force at $t_\star = 0.5$ against bath size, on logarithmic axes. Points: authoritative numerical output. Solid line: least-squares power law, $p = {{num.global_p}}$. Dashed line: slope $-1$, offset vertically for visibility. The time $t_\star$ is not claimed to lie inside the theorem's window.](figure:fig2_scaling){#fig:scaling}

![The product $N_B\, \gamma_1$ at $t_\star = 0.5$ against bath size. Points: authoritative numerical output. Dashed line: the leading-order value $K(t_\star)/m_2^{3/2}$ computed independently from the small-time code of Supplement S2. The vertical window spans the mean value plus or minus a fifth of it, a display choice.](figure:fig3_flat){#fig:scaling-flat}
