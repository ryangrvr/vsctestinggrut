# S5. Numerical tables {#sec:S5}

<!-- M:num.tables -->
All entries are generated from machine-readable output: the authoritative numerical output of the finite-$N_B$ computation of Section 6, and, for Table S5.5, the independent small-time computation of Supplement S2 together with the marginal quadrature below. None is transcribed by hand. Times are fixed in advance; none is claimed to lie inside the theorem's window.

**Gibbs marginal.** High-precision quadrature of $\rho(x) \propto e^{-x^2/2 - x^4/4}$ gives $m_2 = {{const.m2}}$, $m_4 = {{const.m4}}$ and $\operatorname{Var}(x_0^2) = m_4 - m_2^2 = {{const.var_x0sq}}$, so that $c_7 = {{const.C7}}$. The variance lies inside the certified enclosure ${{const.var_cert_mid}}\ldots$ recorded with the proof. On the numerical grid, $m_2 + m_4 - 1 = {{num.gibbs_residual}}$, and the independent one-dimensional quadrature gives $m_2 = {{num.ind1d_m2}}$ and $m_4 = {{num.ind1d_m4}}$.

Table S5.1: Ramp protocol at $t_\star = 0.5$: single-oscillator and force cumulants. $\kappa_3(F) = N_B^{-1/2}\kappa_3(X^\varepsilon)$ and $\operatorname{Var} F = \operatorname{Var} X^\varepsilon$ by the exact identity @eq:S1-star.

{{table:s5_full}}

Table S5.2: All fixed times. The relative spread is $(\max - \min)/|\mathrm{mean}|$ of $N_B\gamma_1$ over the bath-size grid.

{{table:s5_diag}}

Table S5.3: Reference-protocol stationarity control (Gibbs invariance under the unforced flow).

{{table:s5_ref}}

Table S5.4: Sign-reversal control at $t_\star = 0.5$: the third cumulant is odd in the coupling.

{{table:s5_odd}}

Table S5.5: Leading-order prediction against finite-$N_B$ values. The prediction $K(t)/m_2^{3/2}$ uses the independent small-time code of Supplement S2.

{{table:s5_cross}}
