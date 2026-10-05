# S5. Numerical methods and convergence {#sec:S5}

<!-- M:num.method -->
## S5.1 Method {#sec:S5-method}

By the exact single-oscillator reduction (Lemma 1), every bath size requires only the driven single-oscillator process at $\varepsilon = N_B^{-1/2}$, and the force cumulants follow from @eq:S1-star: $\kappa_3(F) = N_B^{-1/2}\kappa_3(X^\varepsilon)$ and $\operatorname{Var} F = \operatorname{Var} X^\varepsilon$. Gibbs expectations over the initial data $(x_0, p_0)$ are computed by deterministic tensor Gauss–Legendre quadrature on $[-{{num.L}}, {{num.L}}]^2$ with the Gibbs weight, normalised on the grid. Every node pair is evolved separately with a fixed-step classical fourth-order Runge–Kutta integrator. The reference resolution is ${{num.nx}}$ nodes per dimension and step ${{num.dt}}$; no sampling is involved. The times $t_\star = 0.5$ and ${{num.t_diag_1}}$, ${{num.t_diag_2}}$, ${{num.t_diag_3}}$ and the bath sizes $N_B \in \{4, 8, 16, 32, 64, 128\}$ were fixed in advance; none of the times is claimed to lie inside the theorem's window.

<!-- M:num.controls -->
## S5.2 Controls {#sec:S5-controls}

**Gibbs marginal.** High-precision quadrature of $\rho(x) \propto e^{-x^2/2 - x^4/4}$ gives $m_2 = {{const.m2}}$, $m_4 = {{const.m4}}$ and $\operatorname{Var}(x_0^2) = m_4 - m_2^2 = {{const.var_x0sq}}$, so that $c_7 = {{const.C7}}$. The variance lies inside the certified enclosure ${{const.var_cert_mid}}\ldots$ recorded with the proof. On the numerical grid, $m_2 + m_4 - 1 = {{num.gibbs_residual}}$, and an independent one-dimensional quadrature (${{num.gl_1d}}$ nodes) gives $m_2 = {{num.ind1d_m2}}$ and $m_4 = {{num.ind1d_m4}}$.

**Reference stationarity and sign reversal.** The reference-protocol variance stays at its Gibbs value within ${{num.ref_var_drift}}$ over the sampled times (Table S5.3), and its mean and third cumulant stay at round-off level. Reversing the sign of the coupling reverses the single-oscillator third cumulant to within ${{num.odd_ratio_dev}}$ in relative terms (Table S5.4). The stationarity and moment controls are independent of the witness; the sign-reversal check is a symmetry control of the implementation only.

<!-- M:num.convergence -->
## S5.3 Convergence {#sec:S5-convergence}

The computation was run on a ladder of node counts $\{ {{conv.nx_list}} \}$ and steps $\{ {{conv.dt_list}} \}$, and the results archived with the record are reproduced in Table S5.1 without recomputation. In every archived cell, $\gamma_1$ at $t_\star$ is identical to the printed precision for all bath sizes (seven significant figures in ${{conv.cells_sevenfig}}$ cells, five in ${{conv.cells_fivefig}}$ cells), the reference-protocol variance drift stays at ${{conv.ref_drift_max}}$ and the Gibbs identity holds to round-off. The finest cell (${{conv.missing_nx}}$ nodes, step ${{conv.missing_dt}}$) was started but its output is not in the archive, and it is not reported. Convergence shows that the implemented computation is stable; its correctness rests on the controls above and on the cross-check of Supplement S6.

Table S5.1: Archived resolution ladder at $t_\star = 0.5$, extracted from the record's logs: nodes per dimension, RK4 step, $\gamma_1(t_\star)$, reference-protocol variance drift and Gibbs identity residual. $^{\ddagger}$ Five significant figures (the seven-figure log has no output for this cell); "not in log" marks a cell whose run is not archived.

{{table:s5_convergence}}

<!-- M:num.tables -->
## S5.4 Tables {#sec:S5-tables}

All entries below are generated from the authoritative numerical output at the reference resolution, except Table S5.6, which also uses the independent small-time computation of Supplement S2.

Table S5.2: Ramp protocol at $t_\star = 0.5$: single-oscillator and force cumulants.

{{table:s5_full}}

Table S5.3: Reference-protocol stationarity control (Gibbs invariance under the unforced flow).

{{table:s5_ref}}

Table S5.4: Sign-reversal control at $t_\star = 0.5$: the third cumulant is odd in the coupling.

{{table:s5_odd}}

Table S5.5: All fixed times. The relative spread is $(\max - \min)/|\mathrm{mean}|$ of $N_B\gamma_1$ over the bath-size grid.

{{table:s5_diag}}

Table S5.6: Leading-order prediction $K(t)/m_2^{3/2}$ (independent small-time code, Supplement S2) against $N_B\gamma_1$ at the largest bath size.

{{table:s5_cross}}
