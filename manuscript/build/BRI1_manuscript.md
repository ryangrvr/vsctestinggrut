---
title: "Finite-bath escape of reciprocal anharmonic back-reaction from shared signed-affine exogenous forcing"
author: "[AUTHOR — to be completed by the author]"
date: "Working draft"
geometry: margin=1in
fontsize: 11pt
colorlinks: true
header-includes:
  - \usepackage{fancyhdr}
  - \usepackage{amsmath}
  - \pagestyle{fancy}
  - \fancyhf{}
  - \fancyhead[C]{\footnotesize Working draft --- not for submission. AI-assisted; disclosure statements pending.}
  - \fancyfoot[C]{\thepage}
  - \renewcommand{\headrulewidth}{0.4pt}
  - \fancypagestyle{plain}{\fancyhf{}\fancyhead[C]{\footnotesize Working draft --- not for submission. AI-assisted; disclosure statements pending.}\fancyfoot[C]{\thepage}}
---

**Working draft — not for submission. AI-assisted; disclosure statements pending.**

## Abstract {.unnumbered}

Reduced descriptions of open systems routinely replace an environment by deterministic memory plus an exogenous random force. For a harmonic bath with linear coupling this replacement is exact, so reduced data cannot distinguish a reacting environment from an externally supplied noise. We ask whether reciprocal back-reaction from a *finite anharmonic* environment can be distinguished from the broadest affine version of that replacement: one exogenous process, shared across a family of interventions, modulated by deterministic causal location and by a deterministic causal scale whose sign may change. For a bath of $N_B$ Duffing oscillators coupled with strength $N_B^{-1/2}$ to a clamped coordinate, we prove that the interventional force laws under a smooth ramp protocol and under the at-rest reference protocol admit no common representation of this kind for every sufficiently large finite $N_B$. The witness is the standardised skewness at a single short time: it vanishes exactly for the reference protocol, while for the ramp its leading coefficient is $K(t)/N_B$ with $K(t) = 3c(t)$ and $c(t) = - \frac{\operatorname{Var}(x_0^2)}{28 \pi^{3}}\, t^7 + O(t^8) < 0$. The effect is mesoscopic: it decays as $O(N_B^{-1})$, and in the reservoir limit the centred force laws of the fixed protocols converge to a common Gaussian law with the equilibrium covariance of the unforced bath. Deterministic finite-$N_B$ quadrature illustrates the $1/N_B$ scaling at fixed finite times that are not claimed to lie inside the theorem's short-time window.

# 1. Introduction {#sec:intro}

A standard route from microscopic dynamics to a reduced equation of motion eliminates the environment and keeps its effect as a memory kernel plus a random force [CITATION NEEDED: generalized Langevin equation from a harmonic bath with linear coupling (Zwanzig; Caldeira–Leggett)] [CITATION NEEDED: Mori–Zwanzig projection-operator formalism]. When the bath is harmonic and the coupling is linear in both the bath and system coordinates, the reduced path law is exactly that of a generalized Langevin equation driven by an exogenous force whose law does not depend on the system's history. Reduced data then identify the effective forcing law but not whether the environment "reacts": an exogenous noise with the right law and memory reproduces everything.

That indistinguishability depends on what is compared. For a *single* experimental protocol nothing can be distinguished at all: whatever force the environment exerts, an exogenous process with exactly that law, and no memory, reproduces the reduced path (Supplement S4). Any meaningful comparison must therefore fix one environment and probe it with a *family* of interventions, and ask whether one shared exogenous description serves the whole family.

We adopt that interventional setting. The system coordinate is clamped to prescribed trajectories, all starting from one common environment preparation, and the environment force needed to hold each trajectory is the observable. The competitor descriptions form a nested ladder (Section 3): additive exogenous forcing with arbitrary deterministic causal memory; the same with an arbitrary deterministic causal scale whose *sign* may change (the shared signed-affine class $\mathcal{E}_2^{\pm}$); and an arbitrary causal transformation of one exogenous random object. The last class contains every classical deterministic causal environment, so back-reaction as such can never be identified at that level. The informative question is whether back-reaction leaves the shared signed-affine class.

Our main result (Theorem 1) answers this for a concrete model: a finite bath of $N_B$ Duffing oscillators coupled reciprocally, with strength $N_B^{-1/2}$, to the clamped coordinate. For each fixed sufficiently small time, and every sufficiently large finite $N_B$, the force law under a smooth ramp protocol has non-zero standardised skewness while the reference (at-rest) protocol has exactly zero third cumulant. Since the absolute standardised skewness is invariant under every deterministic location, scale and sign modulation, no shared signed-affine exogenous process can represent both. The leading coefficient is explicit, $K(t) = 3c(t)$ with $c(t) = - \frac{\operatorname{Var}(x_0^2)}{28 \pi^{3}}\, t^7 + O(t^8)$, and the witness decays as $O(N_B^{-1})$, so that in the reservoir limit the centred force laws of the fixed protocols return to a common Gaussian description (Section 5).

**Relation to prior work.** Several ingredients are known, and we credit them rather than claim them. Anharmonic or nonlinearly coupled environments produce non-Gaussian forces, and Gaussian or Markovian embeddings can fail for kinetic observables [CITATION NEEDED: generalized Langevin equations with non-Gaussian orthogonal forces, Kiefer et al., arXiv:2505.15665 — full bibliographic details to be verified]. Influence-functional treatments organise anharmonic corrections around an effective harmonic (linear-response) description [2] [3]. Finite baths show departures from ideal fluctuation–dissipation behaviour [4]. In statistics, models in which location and scale depend on a covariate while the standardised noise shape is fixed are standard [CITATION NEEDED: location-scale / conditional-transformation regression literature], and causal location-scale noise models identify causal direction under that assumption [1]; identifiability of interventional stochastic differential equations concerns recovering model components from interventions [CITATION NEEDED: identifiability of interventional stochastic differential equations, Zweig et al., arXiv:2505.15987 — full bibliographic details to be verified]. The invariance of standardised shape under location-scale maps, which our witness uses, is therefore not new. What we add is a dynamical, process-level non-representability statement: an explicit reciprocal Hamiltonian environment is proved to leave a shared causal signed-affine class across an intervention family, with a shape-invariant witness, an explicit $1/N_B$ rate, and a stated return to the Gaussian linear-response description in the reservoir limit.

**Outline.** Section 2 defines model $\mathcal{D}$ and the protocols, Section 3 the competitor classes, Section 4 states and explains Theorem 1, Section 5 the reservoir limit, Section 6 a deterministic numerical illustration, and Section 7 discusses scope and limitations. Supplement S1 contains the complete statements and proofs with a notation table; S2 a small-time consistency check; S3 a map of which effects a shared signed-affine model can and cannot absorb; S4 proofs for the competitor classes; S5 the numerical tables; S6 methods and provenance.

# 2. Model and protocols {#sec:model}

**Parent Hamiltonian.** Model $\mathcal{D}$ couples a system coordinate $q$ (momentum $p_q$, mass $M$) reciprocally to $N_B$ identical Duffing oscillators:
$$
H = \frac{p_q^2}{2M} + V(q) + \sum_{j=1}^{N_B} \left[ \frac{p_j^2}{2} + \frac{x_j^2}{2} + \frac{x_j^4}{4} \right] - \frac{1}{\sqrt{N_B}}\, q \sum_{j=1}^{N_B} x_j, \qquad V(q) = \frac{q^2}{2} + \frac{q^4}{4}.
\tag{1}
$$
The coupling per oscillator is $\varepsilon = N_B^{-1/2}$, so the equilibrium force fluctuation is of order one at every bath size while each oscillator is perturbed only at order $\varepsilon$. The Hamiltonian is bounded below for every $N_B$, and the single coupling term produces both the force on the bath and the force on the system: the coupling is reciprocal. The system potential $V$ defines the autonomous parent model and plays no role once $q$ is clamped.

**Clamped dynamics and the force.** Under a prescribed trajectory $q(t)$ each oscillator obeys
$$
\ddot x_j + x_j + x_j^3 = \frac{q(t)}{\sqrt{N_B}},
\tag{2}
$$
and the environment force on the clamped coordinate is
$$
F_q(t) = -\frac{\partial H_{\mathrm{int}}}{\partial q} = \frac{1}{\sqrt{N_B}} \sum_{j=1}^{N_B} x_j(t).
\tag{3}
$$
It is measured interventionally, as the force needed to hold the prescribed trajectory; no hidden bath variable is read.

**Preparation.** At $q(0) = 0$ the coupling vanishes, and the oscillators are prepared independently in the single-oscillator Gibbs law at inverse temperature $\beta = 1$,
$$
\rho(x, p) \propto e^{-\beta H_0(x,p)}, \qquad H_0(x, p) = \frac{p^2}{2} + \frac{x^2}{2} + \frac{x^4}{4}, \qquad \beta = 1 .
\tag{4}
$$
The preparation is the same for every protocol. We write $m_2 = \langle x^2 \rangle_{\mathrm{Gibbs}}$ and $m_4 = \langle x^4 \rangle_{\mathrm{Gibbs}}$; integration by parts gives $m_2 + m_4 = 1$, hence $\operatorname{Var}(x_0^2) = m_4 - m_2^2 = 1 - m_2 - m_2^2 > 0$. Outside Section 6 and Supplement S5, $m_2$ is kept symbolic.

**Protocols.** Admissible clamps are $C^2$ trajectories with $q(0) = \dot q(0) = 0$ and bounded $q, \dot q, \ddot q$ on $[0, 2\pi]$, all applied to the one preparation (4). Two are used:
$$
q_{\mathrm{ref}}(t) \equiv 0, \qquad
q_{\mathrm{ramp}}(t) = \begin{cases} s(t/\pi), & 0 \leq t \leq \pi, \\ 1, & \pi < t \leq 2\pi, \end{cases} \qquad s(u) = 10u^3 - 15u^4 + 6u^5 .
\tag{5}
$$
The *reference protocol* holds the coordinate at rest; the *ramp protocol* moves it smoothly from $0$ to $1$. Theorem 1 uses only the polynomial part $s(t/\pi)$ of the ramp, at short times.

![Model, protocols and witness (schematic). (a) The clamped coordinate exerts the force $q(t)/\sqrt{N_B}$ on each of $N_B$ Duffing oscillators and receives the force $F_q$ of (3). (b) The two protocols, drawn exactly from their definitions (5); the theorem concerns a short initial time window $(0, \delta)$ whose size is existential and is not drawn to scale. (c) The witness logic: the reference protocol has zero third cumulant for every $N_B$; the ramp protocol has a non-zero third cumulant for all sufficiently large $N_B$; since the absolute standardised skewness is invariant under shared location, scale and sign modulation, the two cannot share one signed-affine exogenous representation. The panel contains no data.](../figures/fig1_schematic.pdf){#fig:schematic}

**Single-oscillator reduction.** Under a clamp, all oscillators obey the same deterministic equation, driven by the same $\varepsilon q(t)$, from independent identically distributed initial data. Hence $F_q = \varepsilon \sum_j X_j$ with $X_j$ independent copies of one driven-oscillator process $X^{\varepsilon}_q$, exactly, for every finite $N_B$ (Lemma 1 of Supplement S1). We write $x_0(t)$ for the unforced trajectory ($\varepsilon = 0$) and $y_1 = \partial_\varepsilon X^\varepsilon\rvert_{\varepsilon = 0}$ for the first-order response, which solves $\ddot y_1 + (1 + 3x_0^2)\, y_1 = q(t)$ with $y_1(0) = \dot y_1(0) = 0$.

# 3. Shared exogenous descriptions {#sec:classes}

Every competitor description below is one model shared by *all* admissible clamps: its objects may depend on the prescribed path up to the present, $q_{[0,t]}$, but not on a protocol label. No Gaussian, Markov, finite-memory or stationarity restriction is imposed. Sharing is essential, because a separate exogenous process fitted to each protocol always succeeds (Supplement S4).

**The nested ladder.**

- $\mathcal{E}_1$ — *additive exogenous forcing*: $F_q(t) = M_t[q] + \xi(t)$, with $M$ an arbitrary deterministic causal functional (nonlinear, unlimited memory) and $\xi$ one exogenous process whose law does not depend on $q$. The harmonic bath with linear coupling lies here.
- $\mathcal{E}_2^{\pm}$ — *shared signed-affine exogenous forcing*:
$$
F_q(t) = M_t[q] + G_t[q]\, \xi(t), \qquad G_t[q] \in \mathbb{R} \setminus \{0\},
\tag{6}
$$
with $M$ and $G$ arbitrary deterministic causal functionals and $\xi$ one exogenous process with one protocol-independent path law. The *signed causal scale* $G$ may change sign but may not vanish; a zero would make the force degenerate and is not an invertible affine map. Arbitrary nonlinear transformations of $\xi$ are excluded: history may change the location, the magnitude and the sign of the random force, but not its standardised shape.
- $\mathcal{E}_{\mathrm{univ}}$ — *universal causal exogenous representation*: $F_q(t) = \mathfrak{F}_t[q, U]$, with $U$ one exogenous random object of protocol-independent law and $\mathfrak{F}$ any deterministic functional causal in $q$.

These classes are nested and the inclusions are strict, $\mathcal{E}_1 \subsetneq \mathcal{E}_2^{\pm} \subsetneq \mathcal{E}_{\mathrm{univ}}$ (Supplement S4).
Every classical, deterministic, causal environment of the type considered here, reciprocal and energy-absorbing back-reaction included, lies in $\mathcal{E}_{\mathrm{univ}}$; so does model $\mathcal{D}$. Back-reaction as such is therefore never identifiable at the universal level, and the content of the question lies at the boundary between $\mathcal{E}_2^{\pm}$ and $\mathcal{E}_{\mathrm{univ}}$.

**Operational form and prefix consistency.** Write $Z_q(t) = (F_q(t) - \mathbb{E} F_q(t))/\operatorname{sd} F_q(t)$ for the standardised force at times where the variance is non-zero, and $D_q$ for the set of times where it vanishes. Under clamping and finite second moments, a force family lies in $\mathcal{E}_2^{\pm}$ exactly when (i) $D_q = D$ is common to all protocols, and (ii) there is one shared deterministic causal sign functional $S_t : q_{[0,t]} \mapsto \{+1, -1\}$ such that, with $s_q(t) = S_t[q_{[0,t]}]$, the finite-dimensional laws of $s_q Z_q$ off $D$ are the same for every protocol. Prefix consistency is part of membership: two protocols that agree up to time $t$ must receive the same sign at $t$.

**The invariant used here.** Within $\mathcal{E}_2^{\pm}$, a clamped protocol gives $F_q(t) = M_t[q] + G_t[q]\,\xi(t)$ with deterministic numbers $M_t[q]$ and $G_t[q] \neq 0$, so
$$
\gamma_1[F_q(t)] = \operatorname{sgn}\!\left(G_t[q]\right)\, \gamma_1[\xi(t)], \qquad \gamma_1[Y] = \frac{\kappa_3(Y)}{\operatorname{Var}(Y)^{3/2}} .
\tag{7}
$$
The *absolute* standardised skewness is therefore the same for every protocol at every non-degenerate time. A protocol pair with $|\gamma_1|$ zero for one and non-zero for the other, at a time where both variances are positive, proves that no shared signed-affine representation exists. Sign changes alone never count as such a witness, and neither does a protocol-dependent zero of the variance.

# 4. Main result {#sec:main}

Three exact facts reduce the question to a single-oscillator computation.

*Cumulants scale exactly with bath size.* Because $F_q = \varepsilon \sum_j X_j$ with independent copies $X_j$ of $X^\varepsilon_q$, for every order $n$ and every finite tuple of times
$$
\kappa_n\!\left(F_q(t_1), \dots, F_q(t_n)\right) = N_B^{\,1 - n/2}\; \kappa_n\!\left(X^\varepsilon_q(t_1), \dots, X^\varepsilon_q(t_n)\right).
\tag{8}
$$

*The reference skewness vanishes exactly.* The unforced dynamics and the Gibbs law are invariant under $(x, p) \mapsto (-x, -p)$. Hence $\kappa_3(F_{\mathrm{ref}}(t)) = 0$ for every $t$ and every $N_B$, while $\operatorname{Var} F_{\mathrm{ref}}(t) = m_2 > 0$.

*The ramp third cumulant has an explicit first-order coefficient.* The same reflection combined with $\varepsilon \mapsto -\varepsilon$ makes $\kappa_3(X^\varepsilon(t))$ odd in $\varepsilon$. Moment bounds from the energy estimate and Grönwall's inequality justify differentiating under the expectation, and for each fixed $t \in [0, 2\pi]$
$$
\kappa_3\!\left(F_{\mathrm{ramp}}(t)\right) = \frac{K(t)}{N_B} + O\!\left(N_B^{-2}\right), \qquad K(t) = 3c(t), \qquad c(t) = \operatorname{Cov}\!\left(x_0(t)^2,\, y_1(t)\right),
\tag{9}
$$
with a remainder constant that depends on $t$.

**The small-time coefficient.** The first non-vanishing Taylor coefficient of $c(t)$ is that of $t^7$:
$$
c(t) = - \frac{\operatorname{Var}(x_0^2)}{28 \pi^{3}}\; t^7 + O(t^8), \qquad K(t) = 3c(t).
\tag{10}
$$
The coefficient follows from an order-by-order solution of the equations for $x_0$ and $y_1$; the lower orders cancel through the Gibbs identity $m_2 + m_4 = 1$, and only the $x_0^2$-dependent part of the response survives (Supplement S1, Lemma 4). Since $\operatorname{Var}(x_0^2) > 0$, $c(t) < 0$ on some interval $(0, \delta)$.

**Physical reading.** The response $y_1$ of an oscillator to the ramp is weaker when its instantaneous stiffness $1 + 3x_0^2$ is larger, that is, when $x_0^2$ is large. The response is therefore anticorrelated with $x_0^2$, which is exactly what $c(t) < 0$ expresses, and this anticorrelation skews the summed force. Supplement S3 maps which parts of the ramp's effect a shared signed-affine model can absorb and which it cannot.

**Theorem 1 (finite-bath escape from the shared signed-affine class).** Consider model $\mathcal{D}$ with bath size $N_B$, prepared in the Gibbs state at $\beta = 1$, together with the reference protocol $q_{\mathrm{ref}} \equiv 0$ and the ramp protocol $q_{\mathrm{ramp}}$, which equals $s(t/\pi)$ on $[0,\pi]$. There exists $\delta \in (0, 1]$ such that, for each fixed $t \in (0, \delta)$, there is a finite integer $N_0(t)$ with the following property: for every bath size $N_B \geq N_0(t)$, the interventional force laws of model $\mathcal{D}$ under the reference and ramp protocols admit no common representation in the class $\mathcal{E}_2^{\pm}$. Equivalently, the interventional force family of model $\mathcal{D}$ lies outside $\mathcal{E}_2^{\pm}$ for all finite $N_B \geq N_0(t)$. The witness is the standardised skewness at the single time $t$: $\gamma_1[F_{\mathrm{ref}}(t)] = 0$ for every $N_B$, whereas $\gamma_1[F_{\mathrm{ramp}}(t)] < 0$ for every $N_B \geq N_0(t)$, and both force variances are strictly positive. The numbers $\delta$ and $N_0(t)$ are existential: no value of either is claimed, and $N_0(t)$ is not claimed to be uniform in $t$.

*Proof sketch.* Fix $t \in (0, \delta)$, so $K(t) < 0$. By (9) there is a finite $N_0(t)$ beyond which the remainder is smaller than $|K(t)|/N_B$, so $\kappa_3(F_{\mathrm{ramp}}(t)) < 0$. The ramp force variance is strictly positive, because the time-$t$ flow map is a diffeomorphism carrying the Gibbs density to a density. Hence $\gamma_1[F_{\mathrm{ramp}}(t)] < 0 = \gamma_1[F_{\mathrm{ref}}(t)]$ at a time where both variances are positive, which contradicts (7). Supplement S1 gives every step, including the remainder bounds and the definition $N_0(t) = \lfloor \Theta(t)/|K(t)| \rfloor + 1$. $\square$

The statement is pointwise in $t$: for each fixed short time there is a threshold. It is not a uniform statement over an interval, and neither $\delta$ nor $N_0(t)$ is computed. No time was selected numerically: the interval is forced by the sign of the first non-zero Taylor coefficient, and the protocols were fixed before any computation.

# 5. Reservoir limit {#sec:reservoir}

The escape of Theorem 1 is a finite-bath effect. For fixed $t \in (0, \delta)$ the ramp variance tends to $m_2$, so
$$
\gamma_1[F_{\mathrm{ramp}}(t)] = \frac{K(t)}{m_2^{3/2}\, N_B} + O(N_B^{-2}) \longrightarrow 0 \qquad (N_B \to \infty).
\tag{11}
$$

More strongly, fix a protocol (the reference or ramp protocol, or any separately fixed admissible bounded clamp for which the same moment estimates hold) and a finite tuple of times in $[0, 2\pi]$. The centred force $N_B^{-1/2} \sum_j (X_j^\varepsilon - \mathbb{E} X^\varepsilon)$ is a triangular array with independent identically distributed rows, uniformly bounded fourth moments, and covariance converging to
$$
C_0(t_a, t_b) = \left\langle x_0(t_a)\, x_0(t_b) \right\rangle_{\mathrm{Gibbs}} .
\tag{12}
$$
By the multivariate Lindeberg–Feller central limit theorem [CITATION NEEDED: multivariate Lindeberg–Feller central limit theorem, standard probability text], the centred force converges in finite-dimensional distribution to the centred Gaussian law with covariance $C_0$, which is computed from the unforced equilibrium bath and is therefore the same for every such protocol. The deterministic mean tends to the linear response $\mathbb{E}\, y_1(t)$ [CITATION NEEDED: classical fluctuation–dissipation theorem], which is absorbed by the location functional $M$.

This is an $\mathcal{E}_1$-type reservoir limit in the following precise sense: for the fixed protocols, the centred finite-dimensional force laws converge to one common Gaussian law. It is not a statement that one shared $\mathcal{E}_1$ representation exists uniformly over the whole infinite class of admissible clamps; the moment bounds depend on the clamp, and no such uniform theorem is claimed. Nor is it a statement about the harmonic, linearly coupled bath model itself: the limit is reached at the level of finite-dimensional force laws, and the finite-$N_B$ model remains anharmonic.

# 6. Numerical illustration {#sec:numerics}

The theorem is analytic and does not use the numbers in this section. The computation below illustrates the finite-$N_B$ behaviour at fixed finite times; it is evidence-grade, not certified, and it is not part of the proof. In particular, the primary time $t_\star = 0.5$ and the diagnostic times $0.25$, $0.75$ and $1.0$ were fixed in advance, and none of them is claimed to lie inside the theorem's window $(0, \delta)$.

**Method.** By the single-oscillator reduction, every $N_B$ requires only the one-oscillator process $X^\varepsilon$ at $\varepsilon = N_B^{-1/2}$, and the force cumulants follow exactly from (8). Gibbs expectations over the initial data $(x_0, p_0)$ are evaluated by deterministic tensor Gauss–Legendre quadrature on $[-6, 6]^2$ with $240$ nodes per dimension, every node pair being evolved separately with a fixed-step fourth-order Runge–Kutta integrator of step $5\times 10^{-4}$. No sampling is involved. The bath sizes are $N_B \in \{4, 8, 16, 32, 64, 128\}$. Details and the full tables are in Supplements S5 and S6.

**Controls.** The reference protocol is stationary on the grid: its variance stays at $0.4679199170$ with maximal drift $1.2\times 10^{-8}$ over the sampled times, its mean and third cumulant remain below $5.6\times 10^{-17}$ and $7.8\times 10^{-17}$ in magnitude, and the initial variance agrees with an independent one-dimensional quadrature of the Gibbs marginal ($4000$ nodes), $0.4679199170$, to relative discrepancy $2.4\times 10^{-16}$. Our own high-precision evaluation of the marginal gives $m_2 = 0.467919916974$ and $\operatorname{Var}(x_0^2) = 0.313131034326$, the latter inside the certified enclosure recorded with the proof. The exact identity $m_2 + m_4 = 1$ holds on the grid to $6.7\times 10^{-16}$. Reversing the sign of the coupling reverses the third cumulant: $\kappa_3(X^{-\varepsilon}) / \kappa_3(X^{+\varepsilon}) + 1$ is at most $3.3\times 10^{-11}$ in magnitude for $N_B \in \{ 4, 16 \}$. The stationarity and moment controls are independent of the witness; the sign-reversal check is a symmetry control of the implementation only.

**Results.** At $t_\star = 0.5$ the ramp protocol has negative standardised skewness at every bath size, $\gamma_1 = -5.338\times 10^{-6}$ at $N_B = 4$ and $-1.668\times 10^{-7}$ at $N_B = 128$ (Table 1, Fig. 2). A least-squares fit of $\log|\gamma_1|$ against $\log N_B$ over all six bath sizes gives exponent $p = 1.000000$, with local exponents between $1.000000$ and $1.000000$. The product $N_B \gamma_1$ is flat across the grid to relative spread $1.7\times 10^{-10}$ (Fig. 3), so no finite-$N_B$ correction is resolved at $t_\star$. At the latest diagnostic time $1.0$ a monotone correction is resolved: $N_B \gamma_1$ drifts by a relative $1.4\times 10^{-7}$ between the smallest and largest bath sizes. All four times show negative skewness and the same $1/N_B$ scaling (Supplement S5).

Table 1: Ramp-protocol standardised skewness at $t_\star = 0.5$. Generated from the authoritative numerical output.

| $N_B$ | $\gamma_1[F(t_\star)]$ | $N_B\,\gamma_1[F(t_\star)]$ |
| ---: | ---: | ---: |
| 4 | $-5.33829\times 10^{-6}$ | $-2.135314464\times 10^{-5}$ |
| 8 | $-2.66914\times 10^{-6}$ | $-2.135314464\times 10^{-5}$ |
| 16 | $-1.33457\times 10^{-6}$ | $-2.135314464\times 10^{-5}$ |
| 32 | $-6.67286\times 10^{-7}$ | $-2.135314464\times 10^{-5}$ |
| 64 | $-3.33643\times 10^{-7}$ | $-2.135314464\times 10^{-5}$ |
| 128 | $-1.66821\times 10^{-7}$ | $-2.135314464\times 10^{-5}$ |

**Independent cross-check.** Proposition 1(a) predicts $N_B\, \gamma_1 \to K(t)/m_2^{3/2}$. Evaluating $K(t)$ with separately written small-time code (Supplement S2) and $m_2$ from our marginal quadrature gives $K(t_\star)/m_2^{3/2} = -2.13531\times 10^{-5}$, against $N_B\gamma_1 = -2.13531\times 10^{-5}$ at $N_B = 128$: relative difference $1.3\times 10^{-7}$. At $t = 0.25$ the relative difference is $2.0\times 10^{-8}$. The two computations share only the model definition.

![Standardised skewness of the ramp-protocol force at $t_\star = 0.5$ against bath size, on logarithmic axes. Points: authoritative numerical output. Solid line: least-squares power law, $p = 1.000000$. Dashed line: slope $-1$, offset vertically for visibility. The time $t_\star$ is not claimed to lie inside the theorem's window.](../figures/fig2_scaling.pdf){#fig:scaling}

![The product $N_B\, \gamma_1$ at $t_\star = 0.5$ against bath size. Points: authoritative numerical output. Dashed line: the leading-order value $K(t_\star)/m_2^{3/2}$ computed independently from the small-time code of Supplement S2. The vertical window spans the mean value plus or minus a fifth of it, a display choice.](../figures/fig3_flat.pdf){#fig:scaling-flat}

# 7. Discussion {#sec:discussion}

**What is shown.** A finite reciprocal anharmonic environment can produce interventional force laws that no single shared causal signed-affine modulation of one exogenous process represents. For model $\mathcal{D}$ this holds for each fixed short time and every sufficiently large finite bath size, with a standardised third-cumulant witness whose leading coefficient is explicit and negative. The distinguishing contribution is mesoscopic: it scales as $1/N_B$ and vanishes in the reservoir limit, where the centred force laws of the fixed protocols return to one common Gaussian law with the equilibrium covariance $C_0$ of the unforced bath. The result therefore quantifies why linear-response, effective-harmonic descriptions are hard to escape for large reservoirs, while showing that they are escaped, at a known rate, for finite ones.

**What is not shown.** The result is relative to $\mathcal{E}_2^{\pm}$. It makes no claim against the universal class $\mathcal{E}_{\mathrm{univ}}$, which contains model $\mathcal{D}$: back-reaction in a classical deterministic causal environment is always representable as a causal transformation of one fixed exogenous random object. It does not identify randomness of any special origin or a unique microscopic description of the environment. The constants $\delta$ and $N_0(t)$ are existential; no finite-$N_B$ detection threshold and no experimentally observable effect size are claimed. The numerical times are not certified to lie inside the theorem's window. No uniform statement over the full clamp class is made in the reservoir limit, and quantum environments are not treated.

**Relation to known results.** The harmonic, linearly coupled bath lies in $\mathcal{E}_1$, and a harmonic bath with a nonlinear system coupling still lies exactly in $\mathcal{E}_2^{\pm}$ (Supplement S3): history-dependent noise amplitude, including sign changes, is ordinary multiplicative response and is not the effect reported here. The invariance of standardised shape under location-scale maps is standard in statistics [CITATION NEEDED: location-scale / conditional-transformation regression literature], and the causal location-scale noise model of [1] has the same functional form as a single-time slice of (6). Their identifiability theorem, however, assumes that the model holds in one causal direction and identifies that direction; the present theorem is a non-representability result for a shared *process* across an intervention family, constructed from Hamiltonian dynamics. Non-Gaussian corrections from anharmonic environments [2] [3] [CITATION NEEDED: generalized Langevin equations with non-Gaussian orthogonal forces, Kiefer et al., arXiv:2505.15665 — full bibliographic details to be verified] and finite-bath departures from ideal fluctuation–dissipation behaviour [4] are known; what is new here is their role as a quantified escape from a defined shared competitor class.

**Limitations of the present draft.** The proofs were reproduced by an independent internal re-derivation, not by external review. The literature comparison is a targeted search, not an exhaustive one, and several citations below are placeholders. A certified-error evaluation of the third-cumulant coefficients at finite times, which would turn the numerical illustration into a certified statement at those times, has not been carried out.

## Acknowledgments {.unnumbered}

[AI-USE DISCLOSURE — manuscript preparation]

## Data and code availability {.unnumbered}

[DATA/CODE AVAILABILITY — to be completed by the author: repository location, commit, and licence for the numerical output, the build scripts and the build manifest.]

## References {.unnumbered}

<!-- refs:begin -->
[1] A. Immer, C. Utans, I. Khemakhem, B. Schölkopf, "On the Identifiability and Estimation of Causal Location-Scale Noise Models," ICML 2023 (PMLR 202); arXiv:2210.09054.

[2] N. Makri, "The Linear Response Approximation and Its Lowest Order Corrections: An Influence Functional Approach," J. Phys. Chem. B 103, 2823 (1999). doi:10.1021/jp9847540.

[3] N. Makri, "Parsing the Influence Functional: Harmonic Bath Mapping and Anharmonic Small Matrix Path Integral," J. Phys. Chem. Lett. 15, 4616 (2024). doi:10.1021/acs.jpclett.4c00908.

[4] A. Carcaterra, A. Akay, "Fluctuation-dissipation and energy properties of a finite bath," Phys. Rev. E 93, 032142 (2016). doi:10.1103/PhysRevE.93.032142.
<!-- refs:end -->

All other citations in this draft are visible placeholders marked CITATION NEEDED; the literature sweep has not been done.

# Supplementary material {#sec:supp .unnumbered}

The supplement contains: S1, the theorem and notation sheet with complete proofs; S2, a small-time consistency check of the leading coefficient; S3, a map of which effects of the ramp protocol a shared signed-affine model absorbs; S4, proofs for the competitor classes; S5, the numerical tables; S6, numerical methods and provenance. Equations are numbered within each supplement section.

# S1. Theorem and notation sheet {#sec:S1}

This supplement states the main result and every lemma it uses, defines each symbol exactly once, and gives a complete proof written to be worked through line by line. Every load-bearing definition, equation and statement carries an entry in the build manifest that traces it to the proof record (file, commit, section). Throughout this supplement $m_2$ is kept symbolic; numerical values appear only in Section 6 and Supplement S5.

**How to read the proof.** The argument has one idea and four supporting facts. The idea: a shared signed-affine modulation of one exogenous process cannot change the *absolute* standardised skewness of the force, so if one protocol has zero skewness and another has non-zero skewness, no such shared representation exists. The four facts are: (i) an exact identity that turns cumulants of the bath force into cumulants of a single oscillator (Lemma 1); (ii) a symmetry that makes the reference protocol's skewness vanish exactly (Lemma 2); (iii) a first-order expansion of the ramp protocol's third cumulant in $1/N_B$ with a controlled remainder (Lemma 3); and (iv) a small-time computation showing that the first-order coefficient is strictly negative (Lemma 4). Lemma 5 makes sure the standardisation is legitimate, and Lemma 6 is the precise form of the idea.

## S1.1 Notation {#sec:S1-notation}

| Symbol | Meaning |
| :---------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $t$, $T$ | time; the horizon is $[0, T]$ with $T = 2\pi$ |
| $q(t)$ | prescribed (clamped) trajectory of the system coordinate; a *protocol* |
| $\mathcal{X}$ | class of admissible clamps (Definition 2) |
| $q_{\mathrm{ref}}$, $q_{\mathrm{ramp}}$ | reference protocol and ramp protocol (Definition 2) |
| $s(u)$ | smooth ramp polynomial used by $q_{\mathrm{ramp}}$ |
| $N_B$ | number of bath oscillators (bath size) |
| $\varepsilon$ | coupling per oscillator, $\varepsilon = N_B^{-1/2}$ |
| $x_j, p_j$ | position and momentum of bath oscillator $j \in \{1, \dots, N_B\}$ |
| $H_0(x,p)$ | single-oscillator energy, (S1.4) |
| $\beta$ | inverse temperature; $\beta = 1$ throughout |
| $\rho$ | single-oscillator Gibbs law at $\beta = 1$, (S1.5) |
| $z_0 = (a, b)$ | initial position and momentum of one oscillator, drawn from $\rho$ |
| $E_0$ | initial energy $H_0(z_0)$ |
| $X^{\varepsilon}_q(t)$ | position at time $t$ of one oscillator driven by $\varepsilon q$ |
| $x_0(t)$ | unforced trajectory, $X^{0}_q(t)$ (it does not depend on $q$); not an oscillator label |
| $y_1(t)$ | first-order response $\partial_\varepsilon X^\varepsilon_q(t)\rvert_{\varepsilon = 0}$ for the ramp protocol |
| $F_q(t)$ | interventional environment force under protocol $q$, (S1.3) |
| $\mathring F_q(t)$, $Z_q(t)$ | centred and standardised force (Definition 3) |
| $m_k$ | Gibbs moment $\mathbb{E}[a^k]$ of the initial position |
| $\operatorname{Var}(x_0^2)$ | $m_4 - m_2^2$, the variance of $a^2$ (equal to that of $x_0(t)^2$ for every $t$) |
| $\kappa_n$ | joint cumulant of order $n$; $\kappa_2$ is the (co)variance |
| $\gamma_1[Y]$ | standardised skewness $\kappa_3(Y) / \operatorname{Var}(Y)^{3/2}$ |
| $c(t)$ | $\operatorname{Cov}(x_0(t)^2, y_1(t))$, (S1.8) |
| $K(t)$ | $3c(t)$, the first-order coefficient of the third cumulant |
| $c_k$ | Taylor coefficient of $t^k$ in $c(t)$ |
| $\alpha_k$, $\eta_k$ | Taylor coefficients of $t^k$ in $x_0(t)$ and $y_1(t)$ |
| $\Lambda$ | constant in the order-eight Taylor remainder of $c(t)$ |
| $\Theta(t)$ | constant in the order-three remainder of the third cumulant in $\varepsilon$ |
| $\delta$, $N_0(t)$ | existential time window and bath-size threshold of Theorem 1 |
| $\mathcal{E}_1$, $\mathcal{E}_2^{\pm}$, $\mathcal{E}_{\mathrm{univ}}$ | competitor classes (Definition 4) |
| $M_t[q]$, $G_t[q]$, $\xi$ | deterministic location, signed scale, shared exogenous process |
| $S_t$ | shared causal sign functional (Definition 4) |
| $D_q$ | degeneracy set $\{t : \operatorname{Var} F_q(t) = 0\}$ |
| $C_0(t_a, t_b)$ | reservoir-limit covariance $\langle x_0(t_a)\, x_0(t_b) \rangle_{\mathrm{Gibbs}}$, (S1.13) |

## S1.2 Definitions {#sec:S1-defs}

**Definition 1 (model $\mathcal{D}$).** A system coordinate $q$ with momentum $p_q$ and mass $M$ is coupled reciprocally to $N_B$ identical Duffing oscillators,
$$
H = \frac{p_q^2}{2M} + V(q) + \sum_{j=1}^{N_B} \left[ \frac{p_j^2}{2} + \frac{x_j^2}{2} + \frac{x_j^4}{4} \right] - \frac{1}{\sqrt{N_B}}\, q \sum_{j=1}^{N_B} x_j, \qquad V(q) = \frac{q^2}{2} + \frac{q^4}{4}.
\tag{S1.1}
$$
The system potential $V$ only defines the autonomous parent model; it plays no role once $q$ is clamped. Under a clamp the oscillators obey
$$
\ddot x_j + x_j + x_j^3 = \varepsilon\, q(t), \qquad \varepsilon = N_B^{-1/2},
\tag{S1.2}
$$
and the environment force on the clamped coordinate is
$$
F_q(t) = -\frac{\partial H_{\mathrm{int}}}{\partial q} = \frac{1}{\sqrt{N_B}} \sum_{j=1}^{N_B} x_j(t).
\tag{S1.3}
$$
The single coupling term produces both the force on the bath ($+\varepsilon q$ per oscillator) and the force on the system, so the coupling is reciprocal. With
$$
H_0(x, p) = \frac{p^2}{2} + \frac{x^2}{2} + \frac{x^4}{4},
\tag{S1.4}
$$
the preparation is the same for every protocol: at $q(0) = 0$ the coupling vanishes, and the pairs $(x_j(0), p_j(0))$ are independent and identically distributed with law
$$
\rho(x, p) \propto e^{-\beta H_0(x, p)}, \qquad \beta = 1.
\tag{S1.5}
$$

**Definition 2 (clamps and protocols).** The admissible clamps $\mathcal{X}$ are the prescribed trajectories $q : [0, T] \to \mathbb{R}$ that are $C^2$, satisfy $q(0) = \dot q(0) = 0$, have bounded $q$, $\dot q$, $\ddot q$, and are applied to the one fixed preparation (S1.5). Two members of $\mathcal{X}$ are used:
$$
q_{\mathrm{ref}}(t) \equiv 0, \qquad
q_{\mathrm{ramp}}(t) = \begin{cases} s(t/\pi), & 0 \leq t \leq \pi, \\ 1, & \pi < t \leq 2\pi, \end{cases} \qquad s(u) = 10u^3 - 15u^4 + 6u^5 .
\tag{S1.6}
$$
Only the restriction of $q_{\mathrm{ramp}}$ to $[0, \pi]$, where it is the polynomial $s(t/\pi)$, enters Theorem 1; the plateau is part of the protocol's definition and is used only in Proposition 1 and in the numerical illustration.

**Definition 3 (centred and standardised force; degeneracy set).** For a protocol $q$ and a time $t$, $\mathring F_q(t) = F_q(t) - \mathbb{E} F_q(t)$. The degeneracy set is $D_q = \{ t : \operatorname{Var} F_q(t) = 0 \}$, and for $t \notin D_q$ the standardised force is $Z_q(t) = \mathring F_q(t) / \operatorname{sd} F_q(t)$.

**Definition 4 (competitor classes).** Every class below is a single model shared by *all* protocols in $\mathcal{X}$: its objects may depend on the prescribed path up to the current time, $q_{[0,t]}$, but not on a protocol label, and no Gaussian, Markov, finite-memory or stationarity restriction is imposed.

- $\mathcal{E}_1$ (additive exogenous): $F_q(t) = M_t[q] + \xi(t)$, with $M$ an arbitrary deterministic causal functional and $\xi$ one exogenous process whose law does not depend on $q$.
- $\mathcal{E}_2^{\pm}$ (shared signed-affine exogenous): $F_q(t) = M_t[q] + G_t[q]\, \xi(t)$, with $M$ an arbitrary deterministic causal functional, $G$ an arbitrary deterministic causal functional with $G_t[q] \in \mathbb{R} \setminus \{0\}$ (a *signed causal scale*: sign changes are allowed, zero is not), and $\xi$ one exogenous process with one protocol-independent path law. Equivalently, under clamping and finite second moments, $\mathcal{E}_2^{\pm}$ membership holds exactly when (i) the degeneracy set $D_q = D$ is common to all $q$, and (ii) there is one shared deterministic causal sign functional $S_t : q_{[0,t]} \mapsto \{+1, -1\}$ such that, with $s_q(t) = S_t[q_{[0,t]}]$, the finite-dimensional laws of $s_q Z_q$ off $D$ are the same for every $q \in \mathcal{X}$. *Prefix consistency* is part of membership: if $q_{[0,t]} = q'_{[0,t]}$ then $s_q(t) = s_{q'}(t)$.
- $\mathcal{E}_{\mathrm{univ}}$ (universal causal exogenous): $F_q(t) = \mathfrak{F}_t[q, U]$, with $U$ one exogenous random object of protocol-independent law and $\mathfrak{F}$ an arbitrary deterministic functional that is causal in $q$.

The classes are nested and both inclusions are strict, $\mathcal{E}_1 \subsetneq \mathcal{E}_2^{\pm} \subsetneq \mathcal{E}_{\mathrm{univ}}$.
Every classical, deterministic, causal environment whose state obeys $\dot Y = B(Y, q)$ with force $C(Y, q)$ and initial state $\Psi(q(0), U)$ (with the regularity that excludes blow-up on $[0, T]$) lies in $\mathcal{E}_{\mathrm{univ}}$; model $\mathcal{D}$ is of this type. The question is therefore whether it lies in $\mathcal{E}_2^{\pm}$.

**Definition 5 (response objects).** Write $X^{\varepsilon}_q(t)$ for the position of one oscillator obeying (S1.2) from $z_0 = (a, b) \sim \rho$, and $x_0(t) = X^{0}_q(t)$ for the unforced trajectory. For the ramp protocol the first-order response $y_1 = \partial_\varepsilon X^\varepsilon\rvert_{\varepsilon=0}$ solves
$$
\ddot y_1 + \left(1 + 3 x_0^2\right) y_1 = q_{\mathrm{ramp}}(t), \qquad y_1(0) = \dot y_1(0) = 0,
\tag{S1.7}
$$
and we set
$$
c(t) = \operatorname{Cov}\!\left(x_0(t)^2,\, y_1(t)\right) = \mathbb{E}\!\left[\left(x_0(t)^2 - m_2\right) y_1(t)\right], \qquad K(t) = 3\, c(t).
\tag{S1.8}
$$
The second form of $c(t)$ uses $\mathbb{E}\, x_0(t)^2 = m_2$ for every $t$, which holds because the Gibbs law is invariant under the unforced flow.

**Gibbs moments.** Integration by parts against $e^{-a^2/2 - a^4/4}$ (the boundary terms vanish) gives
$$
m_{k+1} + m_{k+3} = k\, m_{k-1}, \qquad \text{in particular} \qquad m_2 + m_4 = 1, \quad \operatorname{Var}(x_0^2) = m_4 - m_2^2 = 1 - m_2 - m_2^2 .
\tag{S1.9}
$$
Odd moments vanish by symmetry, and the momentum $b$ is standard normal and independent of $a$.

## S1.3 Statements {#sec:S1-statements}

**Theorem 1 (finite-bath escape from the shared signed-affine class).** Consider model $\mathcal{D}$ with bath size $N_B$, prepared in the Gibbs state at $\beta = 1$, together with the reference protocol $q_{\mathrm{ref}} \equiv 0$ and the ramp protocol $q_{\mathrm{ramp}}$, which equals $s(t/\pi)$ on $[0,\pi]$. There exists $\delta \in (0, 1]$ such that, for each fixed $t \in (0, \delta)$, there is a finite integer $N_0(t)$ with the following property: for every bath size $N_B \geq N_0(t)$, the interventional force laws of model $\mathcal{D}$ under the reference and ramp protocols admit no common representation in the class $\mathcal{E}_2^{\pm}$. Equivalently, the interventional force family of model $\mathcal{D}$ lies outside $\mathcal{E}_2^{\pm}$ for all finite $N_B \geq N_0(t)$. The witness is the standardised skewness at the single time $t$: $\gamma_1[F_{\mathrm{ref}}(t)] = 0$ for every $N_B$, whereas $\gamma_1[F_{\mathrm{ramp}}(t)] < 0$ for every $N_B \geq N_0(t)$, and both force variances are strictly positive. The numbers $\delta$ and $N_0(t)$ are existential: no value of either is claimed, and $N_0(t)$ is not claimed to be uniform in $t$.

**Lemma 1 (exact cumulant identity).** Under any clamp $q$ and for every finite $N_B$, $F_q = \varepsilon \sum_{j} X_j$ with $X_1, \dots, X_{N_B}$ independent copies of the process $X^{\varepsilon}_q$. Consequently, for every order $n$ and every finite tuple of times,
$$
\kappa_n\!\left(F_q(t_1), \dots, F_q(t_n)\right) = N_B^{\,1 - n/2}\; \kappa_n\!\left(X^\varepsilon_q(t_1), \dots, X^\varepsilon_q(t_n)\right).
\tag{S1.10}
$$

**Lemma 2 (reference parity).** Under the reference protocol, $\kappa_3(F_{\mathrm{ref}}(t)) = 0$ exactly for every $t$ and every $N_B$, and $\operatorname{Var} F_{\mathrm{ref}}(t) = m_2 > 0$.

**Lemma 3 (first-order third cumulant).** Let $q \in \mathcal{X}$ satisfy $|q| \leq Q$ on $[0, 2\pi]$ (the ramp protocol qualifies), and let $|\varepsilon| \leq 1$. Then (i) for each $z_0$ the clamped solution exists on $[0, 2\pi]$ and is $C^\infty$ in $(z_0, \varepsilon)$; (ii) $y_1$ solves (S1.7); (iii) every moment $\mathbb{E}\big[\prod_{i \leq 3} \partial_\varepsilon^{k_i} X^\varepsilon(t_i)\big]$ with $t_i \in [0, 2\pi]$ and $\sum_i k_i \leq 3$ is finite, uniformly in $|\varepsilon| \leq 1$, and differentiation in $\varepsilon$ commutes with $\mathbb{E}$ up to third order; (iv) $\kappa_3(X^\varepsilon(t))$ is an odd $C^3$ function of $\varepsilon$ with derivative $K(t)$ at $\varepsilon = 0$. Hence for each fixed $t \in [0, 2\pi]$ there is $\Theta(t) < \infty$ with
$$
\kappa_3\!\left(F_{\mathrm{ramp}}(t)\right) = \frac{K(t)}{N_B} + R_N(t), \qquad |R_N(t)| \leq \Theta(t)\, N_B^{-2} .
\tag{S1.11}
$$

**Lemma 4 (small-time sign).** The Taylor coefficients of $c(t)$ satisfy $c_0 = c_1 = \dots = c_6 = 0$ and
$$
c(t) = - \frac{\operatorname{Var}(x_0^2)}{28 \pi^{3}}\; t^7 + O(t^8), \qquad\text{more precisely}\quad \left| c(t) - c_7 t^7 \right| \leq \Lambda\, t^8 \ \text{ on } [0, 1], \quad c_7 = - \frac{\operatorname{Var}(x_0^2)}{28 \pi^{3}} .
\tag{S1.12}
$$
Since $\operatorname{Var}(x_0^2) > 0$, $c_7 < 0$, and there exists $\delta \in (0, 1]$ such that $c(t) < 0$, hence $K(t) = 3c(t) < 0$, for every $0 < t < \delta$.

**Lemma 5 (positive variances).** For every $N_B$ and every $t \in [0, 2\pi]$, $\operatorname{Var} F_{\mathrm{ramp}}(t) = \operatorname{Var} X^\varepsilon(t)$ is finite and strictly positive.

**Lemma 6 (an invariant of $\mathcal{E}_2^{\pm}$).** If a force family lies in $\mathcal{E}_2^{\pm}$, then at every time $t$ outside the common degeneracy set the absolute standardised skewness $|\gamma_1[F_q(t)]|$ takes the same value for every protocol $q$.

**Proposition 1 (reservoir limit; $\mathcal{E}_1$-type, finite-dimensional).** (a) For each fixed $t \in (0, \delta)$, $|\gamma_1[F_{\mathrm{ramp}}(t)]| = O(N_B^{-1})$ and tends to zero as $N_B \to \infty$. (b) For the reference and ramp protocols, and for any separately fixed admissible bounded clamp for which the moment estimates of Lemma 3 hold, and for each finite tuple of times in $[0, 2\pi]$, the centred force $\mathring F_{q}$ converges in finite-dimensional distribution, as $N_B \to \infty$, to the centred Gaussian law with covariance
$$
C_0(t_a, t_b) = \left\langle x_0(t_a)\, x_0(t_b) \right\rangle_{\mathrm{Gibbs}},
\tag{S1.13}
$$
which is the same for every such protocol. No statement is made that one shared $\mathcal{E}_1$ representation holds uniformly over the whole infinite clamp class $\mathcal{X}$.

## S1.4 Proofs {#sec:S1-proofs}

### Proof of Lemma 1 {#sec:S1-proof-1}

*Step 1 (independence).* Under a clamp, every oscillator obeys the same deterministic equation (S1.2), driven by the same prescribed $\varepsilon q(t)$, from independent and identically distributed initial data. The solution map $z_0 \mapsto X^\varepsilon_q(t; z_0)$ is deterministic, so the trajectories are independent copies of one process, and $F_q = \varepsilon \sum_j X_j$ exactly. No approximation is involved.

*Step 2 (cumulant generating function).* For the vector $(F_q(t_1), \dots, F_q(t_n))$, independence gives
$\log \mathbb{E}\exp\big(\sum_a \theta_a F_q(t_a)\big) = N_B \log \mathbb{E} \exp\big(\varepsilon \sum_a \theta_a X(t_a)\big)$.
Differentiating $n$ times in $\theta$ at zero brings down $\varepsilon^n$, so $\kappa_n(F) = N_B \varepsilon^n \kappa_n(X) = N_B^{1 - n/2} \kappa_n(X)$. $\square$

*Why it matters.* For $n = 2$ the force variance equals the single-oscillator variance, so the force fluctuation is of order one at every bath size; for $n = 3$ the force cumulant is $N_B^{-1/2}$ times the single-oscillator cumulant. Everything below is about one oscillator.

### Proof of Lemma 2 {#sec:S1-proof-2}

The unforced vector field $(\dot x, \dot p) = (p, -x - x^3)$ is odd, so $(x, p) \mapsto (-x, -p)$ maps solutions to solutions, and $\rho$ is even. Hence $x_0(t)$ has a law symmetric about zero at every $t$, $\mathbb{E}\, x_0(t) = 0$, and $\kappa_3(x_0(t)) = 0$. By Lemma 1, $\kappa_3(F_{\mathrm{ref}}(t)) = N_B^{-1/2} \cdot 0 = 0$. The Gibbs law is invariant under the Hamiltonian flow, so $\operatorname{Var} F_{\mathrm{ref}}(t) = \operatorname{Var} x_0(t) = m_2$, and $m_2 > 0$ because $a^2 \geq 0$ is not almost surely zero. $\square$

### Proof of Lemma 3 {#sec:S1-proof-3}

*Step 1 (energy bound and global existence).* Along the forced flow $\mathrm{d}H_0/\mathrm{d}t = \varepsilon q p$, so $\mathrm{d}\sqrt{H_0}/\mathrm{d}t = \varepsilon q p / (2\sqrt{H_0}) \leq |\varepsilon| Q / \sqrt{2}$. Hence $\sqrt{H_0(t)} \leq \sqrt{E_0} + c_Q$ on $[0, 2\pi]$ with $c_Q = \sqrt{2}\, Q \pi$. Orbits stay in a compact set, so solutions are global on $[0, 2\pi]$, and because the vector field is polynomial in $(z, \varepsilon)$ the flow is $C^\infty$ in $(z_0, \varepsilon)$. This is (i).

*Step 2 (variational equation).* Differentiating (S1.2) in $\varepsilon$ at $\varepsilon = 0$ gives (S1.7). The initial data do not depend on $\varepsilon$, because the preparation precedes the protocol and the coupling vanishes at $t = 0$; hence $y_1(0) = \dot y_1(0) = 0$. This is (ii).

*Step 3 (moment bounds).* Let $w_k = \partial_\varepsilon^k z$. Each $w_k$ solves a linear equation $\dot w_k = A(t) w_k + f_k$ from zero, with $A = \begin{pmatrix} 0 & 1 \\ -1 - 3x^2 & 0 \end{pmatrix}$, $f_1 = (0, q)$, and, for $k = 2, 3$, inhomogeneities $f_k$ that are polynomials in $x$ and the lower-order $w_j^{x}$ obtained by differentiating $-x^3$ (for example $f_2 = (0, -6x (w_1^{x})^2)$). Since $x^4/4 \leq H_0$, $x^2 \leq 2\sqrt{H_0} \leq 2(\sqrt{E_0} + c_Q)$, so $\|A(t)\|$ and $|x|$ are bounded by a constant of the form $\mathrm{const} \cdot (1 + \sqrt{E_0})$. Grönwall's inequality on $[0, 2\pi]$ then bounds every $|w_k|$, $k \leq 3$, and $|X^\varepsilon|$ by $P(E_0)\, e^{\lambda \sqrt{E_0}}$ for a polynomial $P$ and a constant $\lambda$, uniformly in $|\varepsilon| \leq 1$.

*Step 4 (integrability).* Under $\rho$, $E_0 = H_0(z_0)$ and $e^{-E_0 + \lambda\sqrt{E_0}} \leq e^{\lambda^2/2} e^{-E_0/2}$; the phase-space area of $\{H_0 \leq e\}$ grows polynomially in $e$. So $\mathbb{E}[P(E_0) e^{\lambda \sqrt{E_0}}] < \infty$, and dominated convergence allows differentiating under $\mathbb{E}$ up to third order, with continuous derivatives. This is (iii).

*Step 5 (oddness).* The map $(x, p, \varepsilon) \mapsto (-x, -p, -\varepsilon)$ maps solutions to solutions and $\rho$ is even, so $(X^{-\varepsilon}(t))_t$ has the law of $(-X^{\varepsilon}(t))_t$. Hence $\kappa_3(X^{-\varepsilon}) = -\kappa_3(X^\varepsilon)$: the third cumulant is odd in $\varepsilon$, vanishes at $\varepsilon = 0$, and $\mathbb{E}\, x_0 = 0$.

*Step 6 (the derivative is $K$).* Write $\kappa_3(X) = \mathbb{E} X^3 - 3\, \mathbb{E} X\, \mathbb{E} X^2 + 2 (\mathbb{E} X)^3$ at one time $t$. Differentiate at $\varepsilon = 0$ using (iii) and $\partial_\varepsilon X\rvert_0 = y_1$: the first term gives $3\,\mathbb{E}[x_0^2 y_1]$; the second gives $-3\,\mathbb{E}[y_1]\, \mathbb{E}[x_0^2]$, because the other term carries the factor $\mathbb{E}\, x_0 = 0$; the third vanishes for the same reason. So
$\partial_\varepsilon \kappa_3(X^\varepsilon(t))\rvert_{\varepsilon=0} = 3\left(\mathbb{E}[x_0^2 y_1] - \mathbb{E}[x_0^2]\, \mathbb{E}[y_1]\right) = 3 c(t) = K(t)$.
(For three distinct times the same computation gives the symmetric sum of three such covariances; Theorem 1 needs only the one-time case.)

*Step 7 (Taylor in $\varepsilon$ and conversion to $N_B$).* Being $C^3$ and odd, $\kappa_3(X^\varepsilon(t)) = \varepsilon K(t) + R_3(\varepsilon)$ with $|R_3(\varepsilon)| \leq \Theta(t)\, |\varepsilon|^3$, where $\Theta(t) = \sup_{|\varepsilon| \leq 1} |\partial_\varepsilon^3 \kappa_3| / 6 < \infty$ by (iii). Lemma 1 with $n = 3$ and $\varepsilon = N_B^{-1/2}$ gives $\kappa_3(F_{\mathrm{ramp}}(t)) = N_B^{-1/2} \kappa_3(X^\varepsilon(t)) = K(t)/N_B + N_B^{-1/2} R_3(N_B^{-1/2})$, and the last term is bounded by $\Theta(t) N_B^{-2}$. $\square$

*Remark.* $\Theta(t)$ is finite but enormous (it comes from Grönwall); it certifies the *order* of the remainder, not its size at any particular $N_B$.

### Proof of Lemma 4 {#sec:S1-proof-4}

*Step 1 (pathwise smoothness).* For fixed $z_0$, $x_0$ solves a polynomial ODE and $y_1$ solves the linear ODE (S1.7) with polynomial forcing $s(t/\pi)$ on $[0, 1] \subset [0, \pi]$. Both are $C^\infty$, hence so is $g(t; z_0) = (x_0(t)^2 - m_2)\, y_1(t)$, and $c(t) = \mathbb{E}\, g(t; z_0)$.

*Step 2 (a derivative bound on $[0, 1]$).* Energy conservation gives $x_0^2 \leq 2\sqrt{E_0}$ and $p_0^2 \leq 2E_0$. With $k(t) = 1 + 3x_0^2 \leq \bar k = 1 + 6\sqrt{E_0}$ and $|q_{\mathrm{ramp}}| \leq 1$, Grönwall gives $|y_1|, |\dot y_1| \leq e^{1 + \bar k}$ on $[0, 1]$. Every time derivative of order at most eight of $x_0, \dot x_0, y_1, \dot y_1$ is, by repeated use of the equations, a polynomial in $(x_0, p_0, y_1, \dot y_1)$ and in derivatives of $q_{\mathrm{ramp}}$, which are bounded on $[0, 1]$. So $\sup_{[0,1]} |\partial_t^8 g(\cdot\,; z_0)| \leq D(z_0) = P(E_0)\, e^{1 + \bar k}$ for a polynomial $P$.

*Step 3 (integrability).* Because $-E_0 + 6\sqrt{E_0} \leq -E_0/2 + \max_{u \geq 0}\left(6u - u^2/2\right)$ and phase-space volume grows polynomially in $E_0$, $D$ is $\rho$-integrable; likewise $|\partial_t^k g(0; z_0)|$ is a polynomial in $z_0$ for $k \leq 7$.

*Step 4 (Taylor first, expectation second).* For each $z_0$, $g(t) = \sum_{k=0}^{7} g^{(k)}(0)\, t^k/k! + r(t; z_0)$ with $|r| \leq D(z_0)\, t^8/8!$. Take expectations of this pointwise identity; every term is integrable, so no interchange of derivative and expectation is needed:
$$
c(t) = \sum_{k=0}^{7} c_k\, t^k + R(t), \qquad |R(t)| \leq \Lambda\, t^8, \qquad c_k = \frac{\mathbb{E}[g^{(k)}(0)]}{k!}, \qquad \Lambda = \frac{\mathbb{E} D}{8!} < \infty .
\tag{S1.14}
$$

*Step 5 (the coefficients).* Expand $x_0(t) = \sum_k \alpha_k t^k$ and $y_1(t) = \sum_k \eta_k t^k$. The equations give the recursions
$$
(k+2)(k+1)\, \alpha_{k+2} = -\alpha_k - \left(x_0^3\right)_k, \qquad (k+2)(k+1)\, \eta_{k+2} = -\eta_k - 3\left(x_0^2 y_1\right)_k + q_k ,
\tag{S1.15}
$$
with $\alpha_0 = a$, $\alpha_1 = b$, $\eta_0 = \eta_1 = 0$, where $(\cdot)_k$ denotes the coefficient of $t^k$ and $q_k$ those of $s(t/\pi)$: $q_3 = \frac{10}{\pi^{3}}$, $q_4 = - \frac{15}{\pi^{4}}$, $q_5 = \frac{6}{\pi^{5}}$, all others zero through the orders needed. Because $\eta_j = 0$ for $j \leq 4$, the first non-zero response coefficients are forced by $q$ alone until the $x_0^2 y_1$ term switches on:
$$
\eta_5 = \frac{1}{2 \pi^{3}}, \qquad \eta_6 = - \frac{1}{2 \pi^{4}}, \qquad \eta_7 = -\frac{1 + 3a^{2}}{84\pi^{3}} + \frac{1}{7\pi^{5}} .
\tag{S1.16}
$$
Writing $x_0(t)^2 = \sum_i d_i t^i$, one has $d_0 = a^2$, $d_1 = 2ab$ and, using $\alpha_2 = - \frac{a^{3}}{2} - \frac{a}{2}$, $d_2 = - a^{4} - a^{2} + b^{2}$. The coefficient of $t^n$ in $c(t) = \mathbb{E}[x_0^2 y_1] - m_2\, \mathbb{E}[y_1]$ is
$$
c_n = \operatorname{Cov}(a^2, \eta_n) + \sum_{i=1}^{n} \mathbb{E}\left[d_i\, \eta_{n-i}\right].
\tag{S1.17}
$$

- For $n \leq 4$ every $\eta_j$ that appears vanishes, so $c_0 = \dots = c_4 = 0$.
- $c_5 = \operatorname{Cov}(a^2, \eta_5) = 0$ and $c_6 = \operatorname{Cov}(a^2, \eta_6) + \eta_5\, \mathbb{E}[2ab] = 0$, because $\eta_5, \eta_6$ are constants and $\mathbb{E}[ab] = \mathbb{E} a\, \mathbb{E} b = 0$.
- For $n = 7$ only $i \leq 2$ can contribute. The $i = 1$ term is $\eta_6 \mathbb{E}[2ab] = 0$. The $i = 2$ term is $\eta_5\, \mathbb{E}[b^2 - a^2 - a^4] = \eta_5 (1 - m_2 - m_4) = 0$ by (S1.9). What remains is $\operatorname{Cov}(a^2, \eta_7)$; only the $a^2$ part of $\eta_7$ (coefficient $- \frac{1}{28 \pi^{3}}$) is random, so
$$
c_7 = \left(- \frac{1}{28 \pi^{3}}\right) \operatorname{Var}(a^2) = - \frac{\operatorname{Var}(x_0^2)}{28 \pi^{3}} = \frac{m_{2}^{2} + m_{2} - 1}{28 \pi^{3}} .
\tag{S1.18}
$$
The constant parts of $\eta_7$, including the $\pi^{-5}$ term, cancel between $\mathbb{E}[a^2 \eta_7]$ and $m_2\, \mathbb{E}[\eta_7]$; this cancellation is a useful arithmetic check. The same coefficients, through $t^{ 14 }$, are produced by an exact computer-algebra recursion (Supplement S2).

*Step 6 (sign).* $a$ has a strictly positive density, so $a^2$ is not almost surely constant and $\operatorname{Var}(x_0^2) = \operatorname{Var}(a^2) > 0$; hence $c_7 < 0$. No numerical value of $m_2$ is needed.

*Step 7 (the window).* Put $\delta = \min(1, |c_7| / (2\Lambda))$. For $0 < t < \delta$, (S1.14) gives $c(t) \leq c_7 t^7 + \Lambda t^8 = t^7 (c_7 + \Lambda t) < t^7 c_7 / 2 < 0$. $\square$

*Remarks.* $\delta$ is existential, because $\Lambda$ is an existence bound that is not computed. No complex-time radius and no all-orders expansion is used.

### Proof of Lemma 5 {#sec:S1-proof-5}

By Lemma 1 with $n = 2$, $\operatorname{Var} F_{\mathrm{ramp}}(t) = \operatorname{Var} X^\varepsilon(t)$, which is finite by Lemma 3(iii). The time-$t$ map $z_0 \mapsto z(t; z_0, \varepsilon)$ of the smooth global flow is a $C^1$ diffeomorphism of $\mathbb{R}^2$, and $\rho$ has a density. A diffeomorphism carries a law with a density to a law with a density, so $(x, p)(t)$ has a density, $x(t)$ is not almost surely constant, and the variance is strictly positive. $\square$

### Proof of Lemma 6 {#sec:S1-proof-6}

Suppose $F_q(t) = M_t[q] + G_t[q]\, \xi(t)$ with one shared law for $\xi$. For a clamped protocol, $M_t[q]$ and $G_t[q]$ are deterministic numbers, and $G_t[q] \neq 0$. Then $\operatorname{Var} F_q(t) = G_t[q]^2 \operatorname{Var}\xi(t)$, so the degeneracy set is that of $\xi$ for every $q$, and off it
$$
\kappa_3(F_q(t)) = G_t[q]^3\, \kappa_3(\xi(t)), \qquad \gamma_1[F_q(t)] = \operatorname{sgn}\!\left(G_t[q]\right) \gamma_1[\xi(t)].
\tag{S1.19}
$$
Hence $|\gamma_1[F_q(t)]| = |\gamma_1[\xi(t)]|$ for every $q$. $\square$

*Why the absolute value.* The sign of $G$ is allowed to depend on the protocol (that is what "signed" means), and a sign flip reverses the skewness. The absolute standardised skewness is invariant under every deterministic location shift, rescaling and sign flip, so it is exactly the kind of quantity that a shared signed-affine model must hold fixed across protocols. This is the one-time case of the reflection-orbit criterion for $\mathcal{E}_2^{\pm}$.

### Proof of Theorem 1 {#sec:S1-proof-thm}

Take $\delta$ from Lemma 4 and fix $t \in (0, \delta)$.

1. *Non-zero first-order coefficient.* By Lemma 4, $K(t) = 3c(t) < 0$.
2. *Threshold.* With $\Theta(t)$ from Lemma 3, set $N_0(t) = \lfloor \Theta(t)/|K(t)| \rfloor + 1$, a finite integer. For every $N_B \geq N_0(t)$ we have $N_B > \Theta(t)/|K(t)|$, so $|R_N(t)| \leq \Theta(t) N_B^{-2} < |K(t)| N_B^{-1}$, and (S1.11) gives $\kappa_3(F_{\mathrm{ramp}}(t)) \neq 0$ with the sign of $K(t)$, that is, negative.
3. *Standardisation is legitimate.* By Lemma 5, $0 < \operatorname{Var} F_{\mathrm{ramp}}(t) < \infty$, so $\gamma_1[F_{\mathrm{ramp}}(t)] < 0$. By Lemma 2, $\operatorname{Var} F_{\mathrm{ref}}(t) = m_2 > 0$ and $\gamma_1[F_{\mathrm{ref}}(t)] = 0$. In particular $t$ is a non-degenerate time for both protocols, so the conclusion below is not a degeneracy artefact.
4. *Contradiction.* If the two force laws had a common $\mathcal{E}_2^{\pm}$ representation, Lemma 6 would give $|\gamma_1[F_{\mathrm{ramp}}(t)]| = |\gamma_1[F_{\mathrm{ref}}(t)]| = 0$, contradicting step 3.

Hence no common $\mathcal{E}_2^{\pm}$ representation exists for $N_B \geq N_0(t)$; a fortiori the whole interventional family over $\mathcal{X}$ lies outside $\mathcal{E}_2^{\pm}$. The witness is a violation at a single non-degenerate time: the standardised law of the ramp protocol lies outside every reflection image of the reference law. $\square$

*Quantifiers, made explicit.* $\exists\, \delta > 0$ such that $\forall$ fixed $t \in (0, \delta)$, $\exists\, N_0(t) < \infty$ such that $\forall N_B \geq N_0(t)$: $\kappa_3(F_{\mathrm{ramp}}(t)) \neq 0$. The threshold depends on $t$ because $\Theta(t)$ does; no uniform $N_0$ over the interval is claimed. Nothing in the proof uses a numerically chosen time.

### Proof of Proposition 1 {#sec:S1-proof-prop}

(a) By Lemma 3, $\kappa_3(F_{\mathrm{ramp}}(t)) = K(t)/N_B + O(N_B^{-2})$. The variance $\operatorname{Var} X^\varepsilon(t)$ is continuous in $\varepsilon$ (Lemma 3(iii)) and tends to $\operatorname{Var} x_0(t) = m_2 > 0$. Hence
$$
\gamma_1[F_{\mathrm{ramp}}(t)] = \frac{K(t)}{m_2^{3/2}\, N_B} + O(N_B^{-2}) \longrightarrow 0 .
\tag{S1.20}
$$

(b) Fix a protocol and a finite tuple of times. The centred force $\mathring F_{q} = N_B^{-1/2} \sum_j (X_j^\varepsilon - \mathbb{E} X^\varepsilon)$ is a triangular array with independent, identically distributed rows ($\varepsilon = N_B^{-1/2}$ in row $N_B$). By Lemma 3(iii) the covariance of $X^\varepsilon$ at the chosen times is continuous in $\varepsilon$ and tends to $C_0(t_a, t_b)$, and the same Grönwall bounds give fourth moments bounded uniformly for $|\varepsilon| \leq 1$. Then $N_B\, \mathbb{E}|N_B^{-1/2}(X - \mathbb{E}X)|^4 = O(N_B^{-1}) \to 0$, which is Lyapunov's condition, and the multivariate Lindeberg–Feller central limit theorem gives convergence of the finite-dimensional laws to the centred Gaussian with covariance $C_0$. $C_0$ is computed from the unforced Gibbs trajectory, so it is the same for every protocol. The deterministic mean, $\mathbb{E} F_q(t) = \sqrt{N_B}\, \mathbb{E} X^\varepsilon(t) \to \mathbb{E}\, y_1(t)$, is the linear (fluctuation–dissipation) response and is absorbed by $M$. The Grönwall constants depend on bounds for $q$ and its derivatives, which is why the statement is made protocol by protocol and tuple by tuple, and not uniformly over $\mathcal{X}$. $\square$

## S1.5 What is not claimed {#sec:S1-not}

- No numerical value of $\delta$ or of $N_0(t)$; no uniform threshold in $t$.
- No statement that any particular numerical time, including $t_\star = 0.5$ used in Section 6, lies inside $(0, \delta)$.
- No topological or closure statement about membership in $\mathcal{E}_2^{\pm}$, and no claim that the finite-$N_B$ effect stays observable as $N_B$ grows.
- No escape from $\mathcal{E}_{\mathrm{univ}}$: model $\mathcal{D}$ is representable there.
- No shared $\mathcal{E}_1$ representation uniformly over the full clamp class $\mathcal{X}$.

# S2. Small-time consistency check {#sec:S2}

Lemma 4 gives the leading behaviour $K(t) = 3c(t) = 3 c_7 t^7 + O(t^8)$ with $c_7 = - \frac{\operatorname{Var}(x_0^2)}{28 \pi^{3}}$. This supplement compares the full first-order coefficient $K(t)$, computed numerically, with the leading term $3 c_7 t^7$ at four short times. The computation was written for this build and shares only the model definition with the code behind Section 6.

**Method.** For each initial condition $z_0 = (a, b)$ we integrate the unforced oscillator together with the response equation (S1.7) for the ramp protocol, and evaluate
$$
c(t) = \mathbb{E}\!\left[x_0(t)^2\, y_1(t)\right] - \mathbb{E}\!\left[x_0(t)^2\right] \mathbb{E}\!\left[y_1(t)\right]
\tag{S2.1}
$$
by quadrature over the Gibbs law at $\beta = 1$. Using the variational equation directly avoids the cancellation of a finite difference in $\varepsilon$. Two independent combinations are used: a probabilists' Gauss–Hermite tensor grid with the quartic Gibbs factor in the weights, integrated by a fixed-step fourth-order Runge–Kutta scheme at two grid sizes and two step sizes (primary); and a Gauss–Legendre tensor grid with the full Gibbs weight, integrated by an adaptive eighth-order Dormand–Prince scheme (method B). As a third, semi-analytic comparison, the exact series $\sum_{k=7}^{ 14 } c_k t^k$ is summed with the coefficients produced by computer algebra. The constant $c_7$ uses $\operatorname{Var}(x_0^2)$ from a high-precision quadrature of the Gibbs marginal, which lies inside the certified enclosure recorded with the proof.

**Result.** The ratio $K(t)/(3c_7t^7)$ approaches one as $t \to 0$, as Lemma 4 requires:

Table S2.1: Numerical first-order coefficient against the leading small-time term. "Rel. spread" is the largest relative difference in $c(t)$ between all runs of both methods.

| $t$ | $K(t)$ numerical | $3C_7t^7$ | ratio | ratio (method B) | ratio (series to $t^{14}$) | rel. spread |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $0.1$ | $-1.05257\times 10^{-10}$ | $-1.08203\times 10^{-10}$ | $0.972776$ | $0.972776$ | $0.972776$ | $8\times 10^{-6}$ |
| $0.2$ | $-1.30084\times 10^{-8}$ | $-1.38500\times 10^{-8}$ | $0.939232$ | $0.939232$ | $0.939232$ | $7\times 10^{-6}$ |
| $0.25$ | $-6.07788\times 10^{-8}$ | $-6.60419\times 10^{-8}$ | $0.920306$ | $0.920306$ | $0.920306$ | $6\times 10^{-6}$ |
| $0.5$ | $-6.83470\times 10^{-6}$ | $-8.45337\times 10^{-6}$ | $0.808518$ | $0.808517$ | $0.808500$ | $1\times 10^{-6}$ |

The departure from one is linear in $t$ at leading order: the exact next coefficient gives $c_8/c_7 = - \frac{3}{4 \pi}$.

**Symbolic cross-check.** The coefficients $c_k$ were recomputed by an independent order-by-order recursion in exact arithmetic, with Gibbs moments reduced to $m_2$ through (S1.9). They vanish for $k \leq 6$, and every coefficient from $t^7$ through $t^{ 14 }$ agrees exactly with the computer-algebra output recorded with the proof.

# S3. Mechanism map {#sec:S3}

This supplement records which effects of a non-trivial protocol a shared signed-affine model can absorb, and at which order in $1/N_B$ each enters the force law of model $\mathcal{D}$.

**Expansion and parity.** Expand the driven oscillator as $X^\varepsilon_q = x_0 + \varepsilon y_1 + \varepsilon^2 y_2 + \varepsilon^3 y_3 + \dots$, where $\ddot y_1 + (1 + 3x_0^2)\, y_1 = q(t)$, $\ddot y_2 + (1 + 3x_0^2)\, y_2 = -3x_0 y_1^2$, and so on, all from zero initial data. By induction $y_k$ is even in $x_0$ for odd $k$ and odd in $x_0$ for even $k$, and $y_k$ is homogeneous of degree $k$ in $q$. Gibbs expectations of $x_0$-odd functionals vanish.

**Order of each effect.** Combining the exact identity (S1.10) with parity gives the following map. Only the third-cumulant row is proved in this work (Lemma 3); the other rows follow from the same expansion *assuming* it holds to all orders in $L^p$ on the finite horizon, which is plausible but not proved here.

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

**Physical mechanism.** The first-order response obeys a linear oscillator equation whose stiffness $1 + 3x_0^2$ is set by the oscillator's own state. Oscillators that are instantaneously stiffer, with larger $x_0^2$ and typically higher energy, respond less to the ramp. The response $y_1$ is therefore negatively correlated with $x_0^2$, which is the content of $c(t) < 0$, and this correlation between the random part of the force and the amplitude of the response skews the force distribution. Equivalently, back-reaction couples the *shape* of the force law to the protocol, not only its location and scale.

**What does not escape.** A harmonic bath coupled to the system through a nonlinear function $A(q)$ with $A'(q) = 1 + q^2$ produces the force $F_q(t) = M_t[q] + A'(q(t))\, \xi(t)$, with $\xi$ the free bath force and $M$ a deterministic memory term. This lies exactly in $\mathcal{E}_2^{\pm}$ (it escapes $\mathcal{E}_1$, because the variance depends on the protocol). History-dependent noise amplitude, the usual multiplicative response, is therefore not the effect reported in the main text.

# S4. Competitor classes: proofs {#sec:S4}

This supplement proves the statements about the competitor classes used in Section 3. The setting is a clamped protocol family on $[0, T]$ with one shared environment preparation and a causal environment: the law of the force on $[0, t]$ depends on $q$ only through $q_{[0,t]}$.

**Proposition S4.1 (a single protocol never discriminates).** Fix one protocol: a potential $V$, a drive $u$, deterministic initial data $(q_0, \dot q_0)$ and a horizon $[0, T]$ for $m\ddot q = -V'(q) + u(t) + F_{\mathrm{env}}(t)$, and suppose the equation has a unique solution for every admissible forcing path $f$, with a measurable solution map $q = \Phi(q_0, \dot q_0, f)$. Define the realised environment force $F_{\mathrm{env}} = m \ddot q + V'(q) - u$. Then the additive exogenous model with no memory and $\operatorname{Law}(\xi) = \operatorname{Law}(F_{\mathrm{env}})$ reproduces the reduced path law of that protocol exactly.

*Proof.* In the true system $q = \Phi(q_0, \dot q_0, F_{\mathrm{env}})$ pathwise; in the model $q = \Phi(q_0, \dot q_0, \xi)$. Equal input laws give equal push-forward laws. $\square$ With random initial data the same construction requires $\xi$ to be jointly distributed with the initial data as $F_{\mathrm{env}}$ is; the conclusion is unchanged. Every discriminating statement must therefore compare one shared model across several protocols.

**Proposition S4.2 (characterisation of $\mathcal{E}_1$).** Assume $\mathbb{E} F_q(t)^2 < \infty$. A family lies in $\mathcal{E}_1$ if and only if the finite-dimensional laws of the centred force $\mathring F_q$ are the same for all clamps (equivalently, equal to those of the reference protocol).

*Proof.* If $F_q = M[q] + \xi$, then for a clamped $q$ the number $M_t[q]$ is deterministic, so $\mathring F_q = \xi - \mathbb{E}\xi$ for every $q$. Conversely, set $\xi = \mathring F_{\mathrm{ref}}$ and $M_t[q] = \mathbb{E} F_q(t)$, which is causal by causality of the environment. $\square$

**Proposition S4.3 (characterisation of $\mathcal{E}_2^{\pm}$).** Assume $\mathbb{E} F_q(t)^2 < \infty$. A family lies in $\mathcal{E}_2^{\pm}$ if and only if (i) the degeneracy set $D_q = D$ is common to all clamps, and (ii) there is one shared deterministic causal sign functional $S_t : q_{[0,t]} \mapsto \{\pm 1\}$ such that, with $s_q(t) = S_t[q_{[0,t]}]$, the finite-dimensional laws of $s_q Z_q$ off $D$ are common to all clamps.

*Proof.* ($\Rightarrow$) For a clamped $q$, $F_q(t) = m_q(t) + g_q(t)\, \xi(t)$ with deterministic causal $m_q, g_q$ and $g_q(t) \neq 0$. Then $\operatorname{Var} F_q(t) = g_q(t)^2 \operatorname{Var}\xi(t)$, so $D_q = \{t : \operatorname{Var}\xi(t) = 0\}$ for every $q$, and off $D$, $Z_q(t) = \operatorname{sgn}(g_q(t))\, Z_\xi(t)$. Put $S_t[q_{[0,t]}] = \operatorname{sgn} G_t[q]$, a functional of the prefix because $G$ is causal; then $s_q Z_q = Z_\xi$ has a protocol-independent law.
($\Leftarrow$) Let $\mathcal{L}$ be the common law of $s_q Z_q$ off $D$; let $\xi$ have finite-dimensional laws $\mathcal{L}$ off $D$ and $\xi = 0$ on $D$. Put $M_t[q] = \mathbb{E} F_q(t)$, and $G_t[q] = S_t[q_{[0,t]}]\, \operatorname{sd} F_q(t)$ off $D$, $G_t[q] = 1$ on $D$, so that $G \neq 0$ everywhere; both are causal. Off $D$, $M + G\xi$ has the finite-dimensional laws of $\mathbb{E} F_q + \operatorname{sd} F_q\, s_q (s_q Z_q) = F_q$ because $s_q^2 = 1$; on $D$ both sides equal $\mathbb{E} F_q$. $\square$

The statement is about finite-dimensional distributions; it is upgraded to path laws only when the force processes have continuous (or càdlàg) versions. Prefix consistency is essential: a family can satisfy the reflection condition at every finite tuple of times separately and still fail (ii), because the per-tuple sign choices need not be causal. A finite family of protocols can prove escape but can never prove membership.

**Proposition S4.4 (strict ladder).** $\mathcal{E}_1 \subsetneq \mathcal{E}_2^{\pm} \subsetneq \mathcal{E}_{\mathrm{univ}}$.

*Proof.* Inclusions: take $G \equiv 1$; and take $U = \xi$, $\mathfrak{F}_t[q, U] = M_t[q] + G_t[q]\, U(t)$. Strictness, with $\xi(t)$ independent standard normal on a time grid: (a) $F_q(t) = (1 + q(t)^2)\, \xi(t)$ lies in $\mathcal{E}_2^{\pm}$ but not in $\mathcal{E}_1$, because $\operatorname{Var} F_q(t) = (1 + q(t)^2)^2$ depends on $q$ while Proposition S4.2 requires a protocol-invariant centred law. (b) $F_q(t) = \xi(t) + q(t)\left(\xi(t)^2 - 1\right)$ lies in $\mathcal{E}_{\mathrm{univ}}$; its variance is $1 + 2q^2$ and its third central moment is $6q + 8q^3$ with $q = q(t)$, so $|\gamma_1|$ vanishes when $q(t) = 0$ and not otherwise. Since $|\gamma_1|$ is invariant under signed-affine maps, the family is not in $\mathcal{E}_2^{\pm}$. $\square$

**Proposition S4.5 (universal upper bound).** Let the environment state $Y \in \mathbb{R}^d$ obey $\dot Y = B(Y, q(t))$ with $B$ locally Lipschitz in $Y$ and continuous in $q$, with no blow-up on $[0, T]$ for admissible clamps; let the force be $F = C(Y, q)$ with $C$ measurable, and the initial state $Y(0) = \Psi(q(0), U)$ for one fixed map $\Psi$ and one exogenous random object $U$. Then $F_q(t) = C(\mathcal{Y}_t[q, U], q(t))$ with $\mathcal{Y}$ the solution flow, the pair $(\operatorname{Law} U, \mathfrak{F})$ is shared across clamps, and $\mathfrak{F}$ is causal in $q$. Hence every such environment lies in $\mathcal{E}_{\mathrm{univ}}$.

*Proof.* Existence and uniqueness follow from the Picard–Lindelöf theorem and the no-blow-up hypothesis; two clamps that agree on $[0, t]$ give the same solution on $[0, t]$ by uniqueness, so $\mathcal{Y}_t$ depends only on $q_{[0,t]}$; continuous dependence on initial data and measurability of $\Psi$ give measurability in $U$; and $B$, $C$, $\Psi$, $\operatorname{Law} U$ belong to the environment, not to the protocol. $\square$ Reciprocal, energy-absorbing back-reaction is included, and model $\mathcal{D}$ is of this type. A continuous-time statement for general stochastic environments is not claimed, and quantum environments are out of scope.

# S5. Numerical tables {#sec:S5}

All entries are generated from machine-readable output: the authoritative numerical output of the finite-$N_B$ computation of Section 6, and, for Table S5.5, the independent small-time computation of Supplement S2 together with the marginal quadrature below. None is transcribed by hand. Times are fixed in advance; none is claimed to lie inside the theorem's window.

**Gibbs marginal.** High-precision quadrature of $\rho(x) \propto e^{-x^2/2 - x^4/4}$ gives $m_2 = 0.467919916974$, $m_4 = 0.532080083026$ and $\operatorname{Var}(x_0^2) = m_4 - m_2^2 = 0.313131034326$, so that $c_7 = -3.60677\times 10^{-4}$. The variance lies inside the certified enclosure $0.3131310343256930878\ldots$ recorded with the proof. On the numerical grid, $m_2 + m_4 - 1 = 6.7\times 10^{-16}$, and the independent one-dimensional quadrature gives $m_2 = 0.4679199170$ and $m_4 = 0.5320800830$.

Table S5.1: Ramp protocol at $t_\star = 0.5$: single-oscillator and force cumulants. $\kappa_3(F) = N_B^{-1/2}\kappa_3(X^\varepsilon)$ and $\operatorname{Var} F = \operatorname{Var} X^\varepsilon$ by the exact identity (S1.10).

| $N_B$ | $\varepsilon$ | $\kappa_3(X^\varepsilon)$ | $\mathrm{Var}\,X^\varepsilon$ | $\kappa_3(F)$ | $\gamma_1(F)$ | $N_B\,\gamma_1$ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 4 | $0.5000$ | $-3.417347\times 10^{-6}$ | $0.4679199048$ | $-1.708674\times 10^{-6}$ | $-5.338286\times 10^{-6}$ | $-2.135314464\times 10^{-5}$ |
| 8 | $0.3536$ | $-2.416429\times 10^{-6}$ | $0.4679199050$ | $-8.543368\times 10^{-7}$ | $-2.669143\times 10^{-6}$ | $-2.135314464\times 10^{-5}$ |
| 16 | $0.2500$ | $-1.708674\times 10^{-6}$ | $0.4679199050$ | $-4.271684\times 10^{-7}$ | $-1.334572\times 10^{-6}$ | $-2.135314464\times 10^{-5}$ |
| 32 | $0.1768$ | $-1.208215\times 10^{-6}$ | $0.4679199051$ | $-2.135842\times 10^{-7}$ | $-6.672858\times 10^{-7}$ | $-2.135314464\times 10^{-5}$ |
| 64 | $0.1250$ | $-8.543368\times 10^{-7}$ | $0.4679199051$ | $-1.067921\times 10^{-7}$ | $-3.336429\times 10^{-7}$ | $-2.135314464\times 10^{-5}$ |
| 128 | $0.0884$ | $-6.041074\times 10^{-7}$ | $0.4679199051$ | $-5.339605\times 10^{-8}$ | $-1.668214\times 10^{-7}$ | $-2.135314464\times 10^{-5}$ |

Table S5.2: All fixed times. The relative spread is $(\max - \min)/|\mathrm{mean}|$ of $N_B\gamma_1$ over the bath-size grid.

| $t$ | $\gamma_1$, $N_B=4$ | $\gamma_1$, $N_B=128$ | $N_B\gamma_1$, $N_B=4$ | rel. spread of $N_B\gamma_1$ |
| ---: | ---: | ---: | ---: | ---: |
| $0.5$ | $-5.33829\times 10^{-6}$ | $-1.66821\times 10^{-7}$ | $-2.1353145\times 10^{-5}$ | $1.7\times 10^{-10}$ |
| $0.25$ | $-4.74717\times 10^{-8}$ | $-1.48349\times 10^{-9}$ | $-1.8988671\times 10^{-7}$ | $1.8\times 10^{-8}$ |
| $0.75$ | $-7.66741\times 10^{-5}$ | $-2.39607\times 10^{-6}$ | $-3.0669660\times 10^{-4}$ | $7.1\times 10^{-9}$ |
| $1.0$ | $-4.64191\times 10^{-4}$ | $-1.45060\times 10^{-5}$ | $-0.0018567633$ | $1.4\times 10^{-7}$ |

Table S5.3: Reference-protocol stationarity control (Gibbs invariance under the unforced flow).

| $t$ | $\mathbb{E}\,x(t)$ | $\mathrm{Var}\,x(t)$ | $\kappa_3[x(t)]$ |
| ---: | ---: | ---: | ---: |
| $0.0$ | $0$ | $0.4679199170$ | $5.6\times 10^{-17}$ |
| $0.25$ | $5.6\times 10^{-17}$ | $0.4679199128$ | $-7.8\times 10^{-17}$ |
| $0.5$ | $0$ | $0.4679199051$ | $0$ |
| $0.75$ | $0$ | $0.4679199058$ | $0$ |
| $1.0$ | $-1.4\times 10^{-17}$ | $0.4679199137$ | $2.6\times 10^{-17}$ |

Table S5.4: Sign-reversal control at $t_\star = 0.5$: the third cumulant is odd in the coupling.

| $N_B$ | $\kappa_3(X^{+\varepsilon})$ | $\kappa_3(X^{-\varepsilon})$ | sum | ratio |
| ---: | ---: | ---: | ---: | ---: |
| 4 | $-3.41734737\times 10^{-6}$ | $3.41734737\times 10^{-6}$ | $-7.8\times 10^{-17}$ | $-0.999999999977$ |
| 16 | $-1.70867368\times 10^{-6}$ | $1.70867368\times 10^{-6}$ | $-5.6\times 10^{-17}$ | $-0.999999999967$ |

Table S5.5: Leading-order prediction against finite-$N_B$ values. The prediction $K(t)/m_2^{3/2}$ uses the independent small-time code of Supplement S2.

| $t$ | $N_B\gamma_1$ at $N_B=128$ | $K(t)/m_2^{3/2}$ (independent) | rel. difference |
| ---: | ---: | ---: | ---: |
| $0.25$ | $-1.89886713\times 10^{-7}$ | $-1.89886709\times 10^{-7}$ | $2.0\times 10^{-8}$ |
| $0.5$ | $-2.13531446\times 10^{-5}$ | $-2.13531474\times 10^{-5}$ | $1.3\times 10^{-7}$ |

# S6. Methods and provenance {#sec:S6}

**Finite-$N_B$ computation (Section 6).** By the exact single-oscillator reduction, every bath size requires only the driven single-oscillator process at $\varepsilon = N_B^{-1/2}$. Gibbs expectations over $(x_0, p_0)$ are computed by deterministic tensor Gauss–Legendre quadrature on $[-6, 6]^2$ with $240$ nodes per dimension and the Gibbs weight, normalised on the grid. Every node pair is evolved separately with a fixed-step fourth-order Runge–Kutta integrator of step $5\times 10^{-4}$. The force cumulants then follow from (S1.10). Only the output at this reference resolution is available in machine-readable form, and only that output is used in this manuscript. A resolution ladder in grid size and step size is reported alongside the original computation, but not as machine-readable output.

**Verification history.** Two earlier attempts at this illustration failed and are reported rather than hidden. A Monte Carlo design could not detect the signal: at the very short time it used, the third cumulant lay many orders of magnitude below the sampling noise. A first deterministic quadrature passed its convergence tests but evolved the wrong set of node pairs; the error was exposed because the reference-protocol variance was not stationary and violated the exact moment identity. Convergence alone did not detect it. The computation used here passes both controls, and its values were reproduced by a separately written implementation using a different integrator and grid. That reproduction is internal, not external.

**Small-time check (Supplement S2).** Written for this build; methods as described in Supplement S2.

**Build provenance.** This manuscript is compiled, not typed. Every number is drawn from machine-readable output or computed by a build script, and every figure and table is generated from the same sources. A build manifest traces each definition, lemma, theorem and load-bearing equation to its source, and each printed value to its origin. The build fails if a placeholder is unresolved, if a scientific number appears in the source text, or if a value lacks provenance.

[AI-USE DISCLOSURE — research: proof development, code, numerical verification]
