# 5. Reservoir limit {#sec:reservoir}

<!-- M:prop.reservoir -->
The escape of Theorem 1 is a finite-bath effect; the two statements of this section together form **Proposition 1**, proved in Supplement S4. (a) For fixed $t \in (0, \delta)$, $\kappa_3(F_{\mathrm{ramp}}(t)) = K(t)/N_B + O(N_B^{-2})$ and the ramp variance tends to $m_2 > 0$, so
$$
\gamma_1[F_{\mathrm{ramp}}(t)] = \frac{K(t)}{m_2^{3/2}\, N_B} + o(N_B^{-1}) \longrightarrow 0 \qquad (N_B \to \infty);
$$ {#eq:g1-rate}

in particular $|\gamma_1[F_{\mathrm{ramp}}(t)]| = O(N_B^{-1})$.

<!-- M:eq.C0 -->
(b) More strongly, fix a protocol (the reference or ramp protocol, or any separately fixed admissible bounded clamp for which the same moment estimates hold) and a finite tuple of times in $[0, 2\pi]$. The centred force $N_B^{-1/2} \sum_j (X_j^\varepsilon - \mathbb{E} X^\varepsilon)$ is the row sum of a triangular array whose entries are independent and identically distributed within each row (with $\varepsilon = N_B^{-1/2}$ changing from row to row), with uniformly bounded fourth moments and covariance converging to
$$
C_0(t_a, t_b) = \left\langle x_0(t_a)\, x_0(t_b) \right\rangle_{\mathrm{Gibbs}} .
$$ {#eq:C0}
By the multivariate Lindeberg–Feller central limit theorem [CITATION NEEDED: multivariate Lindeberg–Feller central limit theorem, standard probability text], the centred force converges in finite-dimensional distribution to the centred Gaussian law with covariance $C_0$, which is computed from the unforced equilibrium bath and is therefore the same for every such protocol. The deterministic mean tends to the bath's equilibrium linear response to the clamp — for the ramp protocol, $\mathbb{E}\, y_1(t)$ [CITATION NEEDED: classical fluctuation–dissipation theorem] — which is deterministic and causal and is absorbed by the location functional $M$ (proof of Proposition 1 in Supplement S4).

<!-- M:scope.reservoir -->
This is an $\mathcal{E}_1$-type reservoir limit in the following precise sense: for the fixed protocols, the centred finite-dimensional force laws converge to one common Gaussian law. It is not a statement that one shared $\mathcal{E}_1$ representation exists uniformly over the whole infinite class of admissible clamps; the moment bounds depend on the clamp, and no such uniform theorem is claimed. Nor is it a statement that the environment enters the harmonic class $\mathcal{H}$: the limit is reached at the level of finite-dimensional force laws, no harmonic-bath realisation of it is constructed, and the finite-$N_B$ model remains anharmonic.
