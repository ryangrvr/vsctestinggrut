# 5. Reservoir limit {#sec:reservoir}

<!-- M:prop.reservoir -->
The escape of Theorem 1 is a finite-bath effect. For fixed $t \in (0, \delta)$ the ramp variance tends to $m_2$, so
$$
\gamma_1[F_{\mathrm{ramp}}(t)] = \frac{K(t)}{m_2^{3/2}\, N_B} + O(N_B^{-2}) \longrightarrow 0 \qquad (N_B \to \infty).
$$ {#eq:g1-rate}

<!-- M:eq.C0 -->
More strongly, fix a protocol (the reference or ramp protocol, or any separately fixed admissible bounded clamp for which the same moment estimates hold) and a finite tuple of times in $[0, 2\pi]$. The centred force $N_B^{-1/2} \sum_j (X_j^\varepsilon - \mathbb{E} X^\varepsilon)$ is a triangular array with independent identically distributed rows, uniformly bounded fourth moments, and covariance converging to
$$
C_0(t_a, t_b) = \left\langle x_0(t_a)\, x_0(t_b) \right\rangle_{\mathrm{Gibbs}} .
$$ {#eq:C0}
By the multivariate Lindeberg–Feller central limit theorem [CITATION NEEDED: multivariate Lindeberg–Feller central limit theorem, standard probability text], the centred force converges in finite-dimensional distribution to the centred Gaussian law with covariance $C_0$, which is computed from the unforced equilibrium bath and is therefore the same for every such protocol. The deterministic mean tends to the linear response $\mathbb{E}\, y_1(t)$ [CITATION NEEDED: classical fluctuation–dissipation theorem], which is absorbed by the location functional $M$.

<!-- M:scope.reservoir -->
This is an $\mathcal{E}_1$-type reservoir limit in the following precise sense: for the fixed protocols, the centred finite-dimensional force laws converge to one common Gaussian law. It is not a statement that one shared $\mathcal{E}_1$ representation exists uniformly over the whole infinite class of admissible clamps; the moment bounds depend on the clamp, and no such uniform theorem is claimed. Nor is it a statement about the harmonic, linearly coupled bath model itself: the limit is reached at the level of finite-dimensional force laws, and the finite-$N_B$ model remains anharmonic.
