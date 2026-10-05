# 6. Numerical illustration {#sec:numerics}

<!-- M:scope.numerics -->
The theorem is analytic and does not use the numbers in this section. The computation below illustrates the finite-$N_B$ behaviour at fixed finite times; it is evidence-grade, not certified, and it is not part of the proof. In particular, the primary time $t_\star = 0.5$ and the diagnostic times ${{num.t_diag_1}}$, ${{num.t_diag_2}}$ and ${{num.t_diag_3}}$ were fixed in advance, and none of them is claimed to lie inside the theorem's window $(0, \delta)$.

<!-- M:num.method -->
**Method.** By the single-oscillator reduction, every $N_B$ requires only the one-oscillator process $X^\varepsilon$ at $\varepsilon = N_B^{-1/2}$, and the force cumulants follow exactly from @eq:star. Gibbs expectations over the initial data are evaluated by deterministic tensor quadrature, with every initial condition evolved separately by a fixed-step fourth-order Runge–Kutta integrator; no sampling is involved. The bath sizes are $N_B \in \{4, 8, 16, 32, 64, 128\}$. Supplement S5 gives the method, the controls, a resolution ladder and the full tables; Supplement S6 gives a second, independent code path.

<!-- M:num.controls -->
**Controls.** The reference protocol is stationary on the grid: its variance stays at ${{num.ref_var_t0}}$ with maximal drift ${{num.ref_var_drift}}$ over the sampled times, and its mean and third cumulant remain below ${{num.ref_mean_max}}$ and ${{num.ref_k3_max}}$ in magnitude. The initial variance agrees with an independent one-dimensional quadrature of the Gibbs marginal, $m_2 = {{num.ind1d_m2}}$, to relative discrepancy ${{num.ref_rel_disc}}$, and our own high-precision evaluation gives $m_2 = {{const.m2}}$ and $\operatorname{Var}(x_0^2) = {{const.var_x0sq}}$, inside the certified enclosure recorded with the proof. The exact identity $m_2 + m_4 = 1$ holds on the grid to ${{num.gibbs_residual}}$.

<!-- M:num.results -->
**Results.** At $t_\star = 0.5$ the ramp protocol has negative standardised skewness at every bath size, $\gamma_1 = {{num.g1_tstar_nbmin}}$ at $N_B = 4$ and ${{num.g1_tstar_nbmax}}$ at $N_B = 128$ (Table 3, @fig:scaling). A least-squares fit of $\log|\gamma_1|$ against $\log N_B$ over all six bath sizes gives exponent $p = {{num.global_p}}$, with local exponents between ${{num.local_p_min}}$ and ${{num.local_p_max}}$; across the archived resolution ladder (Supplement S5), $\gamma_1$ at $t_\star$ is unchanged to the printed precision. The product $N_B \gamma_1$ is flat across the grid to relative spread ${{num.nbg1_tstar_relspread}}$, so no finite-$N_B$ correction is resolved at $t_\star$. At the latest diagnostic time ${{num.t_diag_3}}$ a monotone correction is resolved: $N_B \gamma_1$ drifts by a relative ${{num.nbg1_diag_3_drift}}$ between the smallest and largest bath sizes (@fig:residual). All four times show negative skewness and the same $1/N_B$ scaling (Supplement S5).

Table 3: Ramp-protocol standardised skewness at $t_\star = 0.5$. Generated from the authoritative numerical output.

{{table:main_tstar}}

<!-- M:num.crosscheck -->
**Cross-checks.** A separately written implementation (Supplement S6, a reproducibility cross-check rather than additional evidence) agrees with these values to within ${{second.max_rel_diff}}$ in relative terms at both times and all bath sizes. Proposition 1(a) predicts $N_B\gamma_1 \to K(t)/m_2^{3/2}$; evaluating $K(t)$ with the separately written small-time code of Supplement S2 gives $K(t_\star)/m_2^{3/2} = {{x.pred_tstar}}$, against $N_B\gamma_1 = {{x.obs_tstar}}$ at $N_B = 128$, a relative difference of ${{x.reldiff_tstar}}$ that lies within the ${{x.t7_spread_tstar}}$ relative spread of the small-time code's own runs.

![Standardised skewness of the ramp-protocol force at $t_\star = 0.5$ against bath size, on logarithmic axes. Points: authoritative numerical output. Solid line: least-squares power law, $p = {{num.global_p}}$. Dashed line: slope $-1$, offset vertically for visibility. The time $t_\star$ is not claimed to lie inside the theorem's window.](figure:fig2_scaling){#fig:scaling}

![Normalised residual $r(N_B) = N_B\gamma_1(N_B)/N_B\gamma_1(128) - 1$ of the ramp-protocol force at (a) $t_\star = 0.5$ and (b) $t = {{num.t_diag_3}}$. Authoritative numerical output. The panels have their own vertical scales, which differ by three orders of magnitude. At $t_\star$ the residuals scatter at the level of the computation's numerical precision, so no finite-$N_B$ correction is resolved; at $t = {{num.t_diag_3}}$ a monotone correction is resolved.](figure:fig3_residual){#fig:residual}
