# S4. Reservoir-limit proof {#sec:S4}

This supplement proves Proposition 1 (stated in Supplement S1 and Section 5). It uses Lemmas 1–3 of Supplement S1 (the exact cumulant identity, reference parity and the first-order expansion with its moment bounds), the window $\delta$ of Lemma 4 for the domain of part (a), and a standard multivariate central limit theorem.

<!-- M:prop.reservoir -->
**Proposition 1 (restated).** (a) For each fixed $t \in (0, \delta)$, $|\gamma_1[F_{\mathrm{ramp}}(t)]| = O(N_B^{-1})$ and tends to zero as $N_B \to \infty$. (b) For the reference and ramp protocols, and for any separately fixed admissible bounded clamp for which the moment estimates of Lemma 3 hold, and for each finite tuple of times in $[0, 2\pi]$, the centred force converges in finite-dimensional distribution, as $N_B \to \infty$, to the centred Gaussian law with covariance $C_0(t_a, t_b) = \langle x_0(t_a)\, x_0(t_b) \rangle_{\mathrm{Gibbs}}$, the same for every such protocol.

<!-- M:proof.prop1 -->
## S4.1 Proof of part (a): the rate {#sec:S4-a}

By Lemma 3, $\kappa_3(F_{\mathrm{ramp}}(t)) = K(t)/N_B + R_N(t)$ with $|R_N(t)| \leq \Theta(t) N_B^{-2}$, and for $t \in (0, \delta)$ Lemma 4 gives $K(t) < 0$. By Lemma 1 with $n = 2$, $\operatorname{Var} F_{\mathrm{ramp}}(t) = \operatorname{Var} X^\varepsilon(t)$ with $\varepsilon = N_B^{-1/2}$; the variance is built from expectations of products of at most two factors $X^\varepsilon$, so by Lemma 3(iii) and dominated convergence it is continuous in $\varepsilon$ and tends to $\operatorname{Var} x_0(t) = m_2 > 0$ (Lemma 2). Hence
$$
\gamma_1[F_{\mathrm{ramp}}(t)] = \frac{\kappa_3(F_{\mathrm{ramp}}(t))}{\operatorname{Var}(F_{\mathrm{ramp}}(t))^{3/2}} = \frac{K(t)}{m_2^{3/2}\, N_B} + o(N_B^{-1}) \longrightarrow 0 ,
$$ {#eq:S4-rate}
and in particular $|\gamma_1[F_{\mathrm{ramp}}(t)]| = O(N_B^{-1})$. $\square$

## S4.2 Proof of part (b): the common Gaussian limit {#sec:S4-b}

Fix one protocol $q$ (the reference protocol, the ramp protocol, or a separately fixed admissible bounded clamp satisfying the moment estimates of Lemma 3) and a finite tuple of times $t_1, \dots, t_k \in [0, 2\pi]$.

*Step 1 (triangular array).* By Lemma 1, $\mathring F_{q} = \sum_{j=1}^{N_B} \zeta_{N,j}$ with $\zeta_{N,j} = N_B^{-1/2}\left(X_j^\varepsilon - \mathbb{E} X^\varepsilon\right) \in \mathbb{R}^k$ (evaluated at the $k$ times), independent and identically distributed within row $N_B$, where $\varepsilon = N_B^{-1/2}$ changes from row to row.

*Step 2 (covariance converges).* The row covariance is $\sum_j \operatorname{Cov}(\zeta_{N,j}) = \operatorname{Cov}\!\big(X^\varepsilon(t_a), X^\varepsilon(t_b)\big)_{a,b}$. Each entry is an expectation of products of at most two factors, finite uniformly in $|\varepsilon| \leq 1$ and continuous in $\varepsilon$ by Lemma 3(iii) and dominated convergence. As $\varepsilon \to 0$ it tends to $\operatorname{Cov}(x_0(t_a), x_0(t_b)) = \langle x_0(t_a)\, x_0(t_b) \rangle_{\mathrm{Gibbs}} = C_0(t_a, t_b)$, using $\mathbb{E}\, x_0 = 0$.

*Step 3 (Lyapunov condition).* The Grönwall bounds behind Lemma 3 also bound $\mathbb{E}|X^\varepsilon - \mathbb{E} X^\varepsilon|^4$ uniformly for $|\varepsilon| \leq 1$. Hence
$$
\sum_{j=1}^{N_B} \mathbb{E}\, |\zeta_{N,j}|^4 = N_B \cdot N_B^{-2}\, \mathbb{E}\, |X^\varepsilon - \mathbb{E} X^\varepsilon|^4 = O(N_B^{-1}) \longrightarrow 0 ,
$$ {#eq:S4-lyapunov}
which is Lyapunov's condition and implies Lindeberg's.

*Step 4 (central limit theorem).* By the multivariate Lindeberg–Feller theorem for triangular arrays [CITATION NEEDED: multivariate Lindeberg–Feller central limit theorem, standard probability text], with converging covariances, the law of $(\mathring F_q(t_1), \dots, \mathring F_q(t_k))$ converges to the centred Gaussian law with covariance matrix $\big(C_0(t_a, t_b)\big)_{a,b}$.

*Step 5 (protocol independence of the limit).* $C_0$ is computed from the unforced trajectory $x_0$ under the Gibbs law, which does not involve $q$. The limit is therefore the same for every protocol to which Steps 1–4 apply. $\square$

<!-- M:mean.response -->
## S4.3 The mean {#sec:S4-mean}

<!-- M:mean.response -->
The mean is not part of the centred limit. For a clamp $q$ satisfying the moment estimates of Lemma 3, write $y_{1,q} = \partial_\varepsilon X^\varepsilon_q\rvert_{\varepsilon=0}$, the first-order response to that clamp (for the ramp protocol this is the $y_1$ of Supplement S1). By Lemma 1, $\mathbb{E} F_q(t) = \sqrt{N_B}\, \mathbb{E} X^\varepsilon_q(t)$, and by Lemma 3(iii) and dominated convergence this tends to $\mathbb{E}\, y_{1,q}(t)$ as $N_B \to \infty$. The limit is the bath's equilibrium linear response to the clamp [CITATION NEEDED: classical fluctuation–dissipation theorem]. It is deterministic and causal, and is absorbed by the location functional $M$ of any shared model.

<!-- M:scope.reservoir -->
## S4.4 Scope {#sec:S4-scope}

- The limit holds protocol by protocol and tuple by tuple. The Grönwall constants depend on bounds for the clamp and its derivatives, so no shared $\mathcal{E}_1$ representation uniformly over the whole infinite clamp class $\mathcal{X}$ is established or claimed.
- The limit is an $\mathcal{E}_1$-type statement about finite-dimensional force laws. It is not a statement that the environment becomes a member of the harmonic class $\mathcal{H}$, and no harmonic-bath realisation of the limit is constructed. Whether the common Gaussian linear-response law admits an effective harmonic-bath description is a separate question, connected to the influence-functional literature [2] [3] and not addressed here.
- The finite-$N_B$ model remains anharmonic for every $N_B$; Theorem 1 shows it is outside $\mathcal{E}_2^{\pm}$ for all sufficiently large finite $N_B$, while its centred force laws approach the common Gaussian limit.
