# 2. Model and protocols {#sec:model}

<!-- M:def.model -->
**Parent Hamiltonian.** Model $\mathcal{D}$ couples a system coordinate $q$ (momentum $p_q$, mass $M$) reciprocally to $N_B$ identical Duffing oscillators:
$$
H = \frac{p_q^2}{2M} + V(q) + \sum_{j=1}^{N_B} \left[ \frac{p_j^2}{2} + \frac{x_j^2}{2} + \frac{x_j^4}{4} \right] - \frac{1}{\sqrt{N_B}}\, q \sum_{j=1}^{N_B} x_j, \qquad V(q) = \frac{q^2}{2} + \frac{q^4}{4}.
$$ {#eq:H}
The coupling per oscillator is $\varepsilon = N_B^{-1/2}$, so the equilibrium force fluctuation is of order one at every bath size while each oscillator is perturbed only at order $\varepsilon$. The Hamiltonian is bounded below for every $N_B$, and the single coupling term produces both the force on the bath and the force on the system: the coupling is reciprocal. The system potential $V$ defines the autonomous parent model and plays no role once $q$ is clamped.

<!-- M:eq.clamp -->
**Clamped dynamics and the force.** Under a prescribed trajectory $q(t)$ each oscillator obeys
$$
\ddot x_j + x_j + x_j^3 = \frac{q(t)}{\sqrt{N_B}},
$$ {#eq:clamp}
and the environment force on the clamped coordinate is
$$
F_q(t) = -\frac{\partial H_{\mathrm{int}}}{\partial q} = \frac{1}{\sqrt{N_B}} \sum_{j=1}^{N_B} x_j(t).
$$ {#eq:force}
It is measured interventionally, as the force needed to hold the prescribed trajectory; no hidden bath variable is read.

<!-- M:eq.prep -->
**Preparation.** At $q(0) = 0$ the coupling vanishes, and the oscillators are prepared independently in the single-oscillator Gibbs law at inverse temperature $\beta = 1$,
$$
\rho(x, p) \propto e^{-\beta H_0(x,p)}, \qquad H_0(x, p) = \frac{p^2}{2} + \frac{x^2}{2} + \frac{x^4}{4}, \qquad \beta = 1 .
$$ {#eq:prep}
The preparation is the same for every protocol. We write $m_2 = \langle x^2 \rangle_{\mathrm{Gibbs}}$ and $m_4 = \langle x^4 \rangle_{\mathrm{Gibbs}}$; integration by parts gives $m_2 + m_4 = 1$, hence $\operatorname{Var}(x_0^2) = m_4 - m_2^2 = 1 - m_2 - m_2^2 > 0$. Outside Section 6 and Supplement S5, $m_2$ is kept symbolic.

<!-- M:def.protocols -->
**Protocols.** Admissible clamps are $C^2$ trajectories with $q(0) = \dot q(0) = 0$ and bounded $q, \dot q, \ddot q$ on $[0, 2\pi]$, all applied to the one preparation @eq:prep. Two are used:
$$
q_{\mathrm{ref}}(t) \equiv 0, \qquad
q_{\mathrm{ramp}}(t) = \begin{cases} s(t/\pi), & 0 \leq t \leq \pi, \\ 1, & \pi < t \leq 2\pi, \end{cases} \qquad s(u) = 10u^3 - 15u^4 + 6u^5 .
$$ {#eq:protocols}
The *reference protocol* holds the coordinate at rest; the *ramp protocol* moves it smoothly from $0$ to $1$. Theorem 1 uses only the polynomial part $s(t/\pi)$ of the ramp, at short times.

![Model, protocols and witness (schematic). (a) The clamped coordinate exerts the force $q(t)/\sqrt{N_B}$ on each of $N_B$ Duffing oscillators and receives the force $F_q$ of @eq:force. (b) The two protocols, drawn exactly from their definitions @eq:protocols; the theorem concerns a short initial time window $(0, \delta)$ whose size is existential and is not drawn to scale. (c) The witness logic: the reference protocol has zero third cumulant for every $N_B$; the ramp protocol has a non-zero third cumulant for all sufficiently large $N_B$; since the absolute standardised skewness is invariant under shared location, scale and sign modulation, the two cannot share one signed-affine exogenous representation. The panel contains no data.](figure:fig1_schematic){#fig:schematic}

**Single-oscillator reduction.** Under a clamp, all oscillators obey the same deterministic equation, driven by the same $\varepsilon q(t)$, from independent identically distributed initial data. Hence $F_q = \varepsilon \sum_j X_j$ with $X_j$ independent copies of one driven-oscillator process $X^{\varepsilon}_q$, exactly, for every finite $N_B$ (Lemma 1 of Supplement S1). We write $x_0(t)$ for the unforced trajectory ($\varepsilon = 0$) and $y_1 = \partial_\varepsilon X^\varepsilon\rvert_{\varepsilon = 0}$ for the first-order response, which solves $\ddot y_1 + (1 + 3x_0^2)\, y_1 = q(t)$ with $y_1(0) = \dot y_1(0) = 0$.
