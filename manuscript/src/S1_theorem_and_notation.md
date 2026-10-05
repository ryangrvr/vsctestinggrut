# S1. Theorem and notation sheet {#sec:S1}

This supplement states the main result and every lemma it uses, defines each symbol exactly once, and gives complete proofs of Theorem 1 and of its lemmas, written to be worked through line by line; Proposition 1 is proved in Supplement S4, and the class-hierarchy propositions in Supplement S3. Every load-bearing definition, equation and statement carries an entry in the build manifest that traces it to the proof record (file, commit, section). Throughout this supplement $m_2$ is kept symbolic; its numerical value appears only in Section 6 and Supplement S5.

**How to read the proof.** The argument has one idea and four supporting facts. The idea: a shared signed-affine modulation of one exogenous process cannot change the *absolute* standardised skewness of the force, so if one protocol has zero skewness and another has non-zero skewness, no such shared representation exists. The four facts are: (i) an exact identity that turns cumulants of the bath force into cumulants of a single oscillator (Lemma 1); (ii) a symmetry that makes the reference protocol's skewness vanish exactly (Lemma 2); (iii) a first-order expansion of the ramp protocol's third cumulant in $1/N_B$ with a controlled remainder (Lemma 3); and (iv) a small-time computation showing that the first-order coefficient is strictly negative (Lemma 4). Lemma 5 makes sure the standardisation is legitimate, and Lemma 6 is the precise form of the idea.

## S1.1 Notation {#sec:S1-notation}

| Symbol | Meaning |
| :---------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $\mathcal{D}$ | the model of Definition 1 (finite Duffing bath, reciprocal coupling) |
| $t$, $T$ | time; the horizon is $[0, T]$ with $T = 2\pi$ |
| $M$, $p_q$, $V$ | mass, momentum and potential of the system coordinate; $M$ denotes the mass only in @eq:S1-H, and the location functional $M_t[q]$ everywhere else |
| $H$, $H_{\mathrm{int}}$ | parent Hamiltonian @eq:S1-H and its coupling term, $H_{\mathrm{int}} = -N_B^{-1/2}\, q \sum_j x_j$ |
| $q(t)$ | prescribed (clamped) trajectory of the system coordinate; a *protocol* |
| $\mathcal{X}$ | class of admissible clamps (Definition 2) |
| $q_{\mathrm{ref}}$, $q_{\mathrm{ramp}}$ | reference protocol and ramp protocol (Definition 2) |
| $s(u)$ | smooth ramp polynomial used by $q_{\mathrm{ramp}}$ |
| $N_B$ | number of bath oscillators (bath size) |
| $\varepsilon$ | coupling per oscillator, $\varepsilon = N_B^{-1/2}$ |
| $x_j, p_j$ | position and momentum of bath oscillator $j \in \{1, \dots, N_B\}$ |
| $H_0(x,p)$ | single-oscillator energy, @eq:S1-H0 |
| $\beta$ | inverse temperature; $\beta = 1$ throughout |
| $\rho$ | single-oscillator Gibbs law at $\beta = 1$, @eq:S1-gibbs |
| $z_0 = (a, b)$ | initial position and momentum of one oscillator, drawn from $\rho$ |
| $E_0$ | initial energy $H_0(z_0)$ |
| $X^{\varepsilon}_q(t)$ | position at time $t$ of one oscillator driven by $\varepsilon q$ |
| $x_0(t)$ | unforced trajectory, $X^{0}_q(t)$ (it does not depend on $q$); not an oscillator label |
| $y_1(t)$ | first-order response $\partial_\varepsilon X^\varepsilon_q(t)\rvert_{\varepsilon = 0}$ for the ramp protocol |
| $F_q(t)$ | interventional environment force under protocol $q$, @eq:S1-force |
| $\mathring F_q(t)$, $Z_q(t)$ | centred and standardised force (Definition 3) |
| $m_k$ | Gibbs moment $\mathbb{E}[a^k]$ of the initial position |
| $\operatorname{Var}(x_0^2)$ | $m_4 - m_2^2$, the variance of $a^2$ (equal to that of $x_0(t)^2$ for every $t$) |
| $\kappa_n$ | joint cumulant of order $n$; $\kappa_2$ is the (co)variance |
| $\gamma_1[Y]$ | standardised skewness $\kappa_3(Y) / \operatorname{Var}(Y)^{3/2}$ |
| $c(t)$ | $\operatorname{Cov}(x_0(t)^2, y_1(t))$, @eq:S1-c-def |
| $K(t)$ | $3c(t)$, the first-order coefficient of the third cumulant |
| $c_k$ | Taylor coefficient of $t^k$ in $c(t)$ |
| $\alpha_k$, $\eta_k$ | Taylor coefficients of $t^k$ in $x_0(t)$ and $y_1(t)$ |
| $\Lambda$ | constant in the order-eight Taylor remainder of $c(t)$ |
| $\Theta(t)$ | constant in the order-three remainder of the third cumulant in $\varepsilon$ |
| $Q$, $c_Q$ | bound for a clamp, $|q| \leq Q$, and the energy constant $c_Q = \sqrt{2}\, Q \pi$ (Lemma 3) |
| $R_N(t)$ | remainder in the first-order expansion @eq:S1-kappa3 |
| $D_8(z_0)$ | bound on the eighth time derivative in the proof of Lemma 4 |
| $\delta$, $N_0(t)$ | existential time window and bath-size threshold of Theorem 1 |
| $\mathcal{H}$ | harmonic baths with coupling linear in bath and system coordinates (Definition 4) |
| $\mathcal{E}_1$, $\mathcal{E}_2^{\pm}$, $\mathcal{E}_{\mathrm{univ}}$ | competitor classes (Definition 4) |
| $M_t[q]$, $G_t[q]$, $\xi$ | deterministic location, signed scale, shared exogenous process |
| $s_q(t)$ | sign assigned to protocol $q$ at time $t$ by the shared sign functional $S_t$ |
| $U$, $\mathfrak{F}$ | exogenous random object and causal functional of $\mathcal{E}_{\mathrm{univ}}$ (Definition 4) |
| $Y$, $B$, $C$, $\Psi$ | state, drift, force map and initial-state map of a deterministic causal environment (Definition 4) |
| $p_0$ | initial momentum coordinate, $p_0 = b$; also written $\dot x_0(0)$ |
| $S_t$ | shared causal sign functional (Definition 4) |
| $D_q$ | degeneracy set $\{t : \operatorname{Var} F_q(t) = 0\}$ |
| $C_0(t_a, t_b)$ | reservoir-limit covariance $\langle x_0(t_a)\, x_0(t_b) \rangle_{\mathrm{Gibbs}}$, @eq:S1-C0 |

## S1.2 Definitions {#sec:S1-defs}

<!-- M:def.model -->
**Definition 1 (model $\mathcal{D}$).** A system coordinate $q$ with momentum $p_q$ and mass $M$ is coupled reciprocally to $N_B$ identical Duffing oscillators,
$$
H = \frac{p_q^2}{2M} + V(q) + \sum_{j=1}^{N_B} \left[ \frac{p_j^2}{2} + \frac{x_j^2}{2} + \frac{x_j^4}{4} \right] - \frac{1}{\sqrt{N_B}}\, q \sum_{j=1}^{N_B} x_j, \qquad V(q) = \frac{q^2}{2} + \frac{q^4}{4}.
$$ {#eq:S1-H}
The system potential $V$ only defines the autonomous parent model; it plays no role once $q$ is clamped. Under a clamp the oscillators obey
$$
\ddot x_j + x_j + x_j^3 = \varepsilon\, q(t), \qquad \varepsilon = N_B^{-1/2},
$$ {#eq:S1-clamp}
and the environment force on the clamped coordinate is
$$
F_q(t) = -\frac{\partial H_{\mathrm{int}}}{\partial q} = \frac{1}{\sqrt{N_B}} \sum_{j=1}^{N_B} x_j(t).
$$ {#eq:S1-force}
The single coupling term produces both the force on the bath ($+\varepsilon q$ per oscillator) and the force on the system, so the coupling is reciprocal. With
$$
H_0(x, p) = \frac{p^2}{2} + \frac{x^2}{2} + \frac{x^4}{4},
$$ {#eq:S1-H0}
the preparation is the same for every protocol: at $q(0) = 0$ the coupling vanishes, and the pairs $(x_j(0), p_j(0))$ are independent and identically distributed with law
$$
\rho(x, p) \propto e^{-\beta H_0(x, p)}, \qquad \beta = 1.
$$ {#eq:S1-gibbs}

<!-- M:def.clamp_class -->
**Definition 2 (clamps and protocols).** The admissible clamps $\mathcal{X}$ are the prescribed trajectories $q : [0, T] \to \mathbb{R}$ that are $C^2$, satisfy $q(0) = \dot q(0) = 0$, have bounded $q$, $\dot q$, $\ddot q$, and are applied to the one fixed preparation @eq:S1-gibbs. Two members of $\mathcal{X}$ are used:
$$
q_{\mathrm{ref}}(t) \equiv 0, \qquad
q_{\mathrm{ramp}}(t) = \begin{cases} s(t/\pi), & 0 \leq t \leq \pi, \\ 1, & \pi < t \leq 2\pi, \end{cases} \qquad s(u) = 10u^3 - 15u^4 + 6u^5 .
$$ {#eq:S1-protocols}
Only the restriction of $q_{\mathrm{ramp}}$ to $[0, \pi]$, where it is the polynomial $s(t/\pi)$, enters Theorem 1; the plateau is part of the protocol's definition and enters only the statements on $[0, 2\pi]$ (Lemmas 3 and 5 and Proposition 1), not Theorem 1 or the numerical illustration, whose times all lie in $[0, \pi]$.

<!-- M:def.standardised -->
**Definition 3 (centred and standardised force; degeneracy set).** For a protocol $q$ and a time $t$, $\mathring F_q(t) = F_q(t) - \mathbb{E} F_q(t)$. The degeneracy set is $D_q = \{ t : \operatorname{Var} F_q(t) = 0 \}$, and for $t \notin D_q$ the standardised force is $Z_q(t) = \mathring F_q(t) / \operatorname{sd} F_q(t)$.

<!-- M:def.classes -->
**Definition 4 (competitor classes).** Every class below is a single model shared by *all* protocols in $\mathcal{X}$: its objects may depend on the prescribed path up to the current time, $q_{[0,t]}$, but not on a protocol label, and no Gaussian, Markov, finite-memory or stationarity restriction is imposed.

- $\mathcal{E}_1$ (additive exogenous): $F_q(t) = M_t[q] + \xi(t)$, with $M$ an arbitrary deterministic causal functional and $\xi$ one exogenous process whose law does not depend on $q$.
<!-- M:def.e2pm -->
- $\mathcal{E}_2^{\pm}$ (shared signed-affine exogenous): $F_q(t) = M_t[q] + G_t[q]\, \xi(t)$, with $M$ an arbitrary deterministic causal functional, $G$ an arbitrary deterministic causal functional with $G_t[q] \in \mathbb{R} \setminus \{0\}$ (a *signed causal scale*: sign changes are allowed, zero is not), and $\xi$ one exogenous process with one protocol-independent path law. Equivalently — under clamping, finite second moments and environment causality (the law of $F_q$ on $[0, t]$ depends on $q$ only through $q_{[0,t]}$), and at the level of finite-dimensional distributions — $\mathcal{E}_2^{\pm}$ membership holds exactly when (i) the degeneracy set $D_q = D$ is common to all $q$, and (ii) there is one shared deterministic causal sign functional $S_t : q_{[0,t]} \mapsto \{+1, -1\}$ such that, with $s_q(t) = S_t[q_{[0,t]}]$, the finite-dimensional laws of $s_q Z_q$ off $D$ are the same for every $q \in \mathcal{X}$. *Prefix consistency* is part of membership: if $q_{[0,t]} = q'_{[0,t]}$ then $s_q(t) = s_{q'}(t)$.
- $\mathcal{E}_{\mathrm{univ}}$ (universal causal exogenous): $F_q(t) = \mathfrak{F}_t[q, U]$, with $U$ one exogenous random object of protocol-independent law and $\mathfrak{F}$ an arbitrary deterministic functional that is causal in $q$.

<!-- M:prop.ladder -->
The harmonic class $\mathcal{H}$ (harmonic baths coupled linearly in the bath and system coordinates, with counterterm and a free-force law independent of the system's initial state) sits at the bottom, and the ladder $\mathcal{H} \subset \mathcal{E}_1 \subsetneq \mathcal{E}_2^{\pm} \subsetneq \mathcal{E}_{\mathrm{univ}}$ holds, with both inclusions among the $\mathcal{E}$-classes strict (Supplement S3).
<!-- M:prop.upper -->
Every classical, deterministic, causal environment whose state obeys $\dot Y = B(Y, q)$ with force $C(Y, q)$ and initial state $\Psi(q(0), U)$ — with $B$ jointly continuous and locally Lipschitz in $Y$, locally uniformly in $q$, $C$ measurable, and no blow-up on $[0, T]$ — lies in $\mathcal{E}_{\mathrm{univ}}$ (Proposition S3.7); model $\mathcal{D}$ is of this type (Lemma 3(i)). The question is therefore whether it lies in $\mathcal{E}_2^{\pm}$.

<!-- M:def.c -->
**Definition 5 (response objects).** Write $X^{\varepsilon}_q(t)$ for the position of one oscillator obeying @eq:S1-clamp from $z_0 = (a, b) \sim \rho$, and $x_0(t) = X^{0}_q(t)$ for the unforced trajectory. For the ramp protocol the first-order response $y_1 = \partial_\varepsilon X^\varepsilon\rvert_{\varepsilon=0}$ solves
$$
\ddot y_1 + \left(1 + 3 x_0^2\right) y_1 = q_{\mathrm{ramp}}(t), \qquad y_1(0) = \dot y_1(0) = 0,
$$ {#eq:S1-y1}
and we set
$$
c(t) = \operatorname{Cov}\!\left(x_0(t)^2,\, y_1(t)\right) = \mathbb{E}\!\left[\left(x_0(t)^2 - m_2\right) y_1(t)\right], \qquad K(t) = 3\, c(t).
$$ {#eq:S1-c-def}
The second form of $c(t)$ uses $\mathbb{E}\, x_0(t)^2 = m_2$ for every $t$, which holds because the Gibbs law is invariant under the unforced flow.

<!-- M:eq.moment_identity -->
**Gibbs moments.** Integration by parts against $e^{-a^2/2 - a^4/4}$ (the boundary terms vanish) gives
$$
m_{k+1} + m_{k+3} = k\, m_{k-1}, \qquad \text{in particular} \qquad m_2 + m_4 = 1, \quad \operatorname{Var}(x_0^2) = m_4 - m_2^2 = 1 - m_2 - m_2^2 .
$$ {#eq:S1-moments}
Odd moments vanish by symmetry, and the momentum $b$ is standard normal and independent of $a$.

## S1.3 Statements {#sec:S1-statements}

{{include:thm_main}}

<!-- M:lem.cumulant_identity -->
**Lemma 1 (exact cumulant identity).** Under any clamp $q$ and for every finite $N_B$, $F_q = \varepsilon \sum_{j} X_j$ with $X_1, \dots, X_{N_B}$ independent copies of the process $X^{\varepsilon}_q$. Consequently, for every order $n$ and every finite tuple of times,
$$
\kappa_n\!\left(F_q(t_1), \dots, F_q(t_n)\right) = N_B^{\,1 - n/2}\; \kappa_n\!\left(X^\varepsilon_q(t_1), \dots, X^\varepsilon_q(t_n)\right).
$$ {#eq:S1-star}

<!-- M:lem.parity -->
**Lemma 2 (reference parity).** Under the reference protocol, $\kappa_3(F_{\mathrm{ref}}(t)) = 0$ exactly for every $t$ and every $N_B$, and $\operatorname{Var} F_{\mathrm{ref}}(t) = m_2 > 0$.

<!-- M:lem.first_order -->
**Lemma 3 (first-order third cumulant).** Let $q = q_{\mathrm{ramp}}$, so that $|q| \leq 1$ on $[0, 2\pi]$, and let $|\varepsilon| \leq 1$. Then (i) for each $z_0$ the clamped solution exists on $[0, 2\pi]$ and is $C^\infty$ in $(z_0, \varepsilon)$; (ii) $y_1$ solves @eq:S1-y1; (iii) every moment $\mathbb{E}\big[\prod_{i \leq 3} \partial_\varepsilon^{k_i} X^\varepsilon(t_i)\big]$ with $t_i \in [0, 2\pi]$ and $\sum_i k_i \leq 3$ is finite, uniformly in $|\varepsilon| \leq 1$, and differentiation in $\varepsilon$ commutes with $\mathbb{E}$ up to third order; (iv) $\kappa_3(X^\varepsilon(t))$ is an odd $C^3$ function of $\varepsilon$ with derivative $K(t)$ at $\varepsilon = 0$. Hence for each fixed $t \in [0, 2\pi]$ there is $\Theta(t) < \infty$ with
$$
\kappa_3\!\left(F_{\mathrm{ramp}}(t)\right) = \frac{K(t)}{N_B} + R_N(t), \qquad |R_N(t)| \leq \Theta(t)\, N_B^{-2} .
$$ {#eq:S1-kappa3}
Parts (i) and (iii), and their proofs, hold verbatim for any clamp with $|q| \leq Q$ on $[0, 2\pi]$, with constants depending on $Q$ and on the bounds for the derivatives of $q$; parts (ii) and (iv) are statements about the ramp protocol's response $y_1$ and its coefficient $K(t)$.

<!-- M:lem.small_time -->
**Lemma 4 (small-time sign).** The Taylor coefficients of $c(t)$ satisfy $c_0 = c_1 = \dots = c_6 = 0$ and
$$
c(t) = {{sym.C7}}\; t^7 + O(t^8), \qquad\text{more precisely}\quad \left| c(t) - c_7 t^7 \right| \leq \Lambda\, t^8 \ \text{ on } [0, 1], \quad c_7 = {{sym.C7}} .
$$ {#eq:S1-c-small}
Since $\operatorname{Var}(x_0^2) > 0$, $c_7 < 0$, and there exists $\delta \in (0, 1]$ such that $c(t) < 0$, hence $K(t) = 3c(t) < 0$, for every $0 < t < \delta$.

<!-- M:lem.variance -->
**Lemma 5 (positive variances).** For every $N_B$ and every $t \in [0, 2\pi]$, $\operatorname{Var} F_{\mathrm{ramp}}(t) = \operatorname{Var} X^\varepsilon(t)$ is finite and strictly positive.

<!-- M:lem.e2pm_necessity -->
**Lemma 6 (an invariant of $\mathcal{E}_2^{\pm}$).** If a force family lies in $\mathcal{E}_2^{\pm}$ and $\mathbb{E}\,|F_q(t)|^3 < \infty$ for one protocol (hence, by the shared representation, for every protocol), then at every time $t$ outside the common degeneracy set the absolute standardised skewness $|\gamma_1[F_q(t)]|$ takes the same value for every protocol $q$.

<!-- M:prop.reservoir -->
**Proposition 1 (reservoir limit; $\mathcal{E}_1$-type, finite-dimensional).** (a) For each fixed $t \in (0, \delta)$, $|\gamma_1[F_{\mathrm{ramp}}(t)]| = O(N_B^{-1})$ and tends to zero as $N_B \to \infty$. (b) For the reference and ramp protocols, and for any separately fixed admissible bounded clamp for which the moment estimates of Lemma 3 hold, and for each finite tuple of times in $[0, 2\pi]$, the centred force $\mathring F_{q}$ converges in finite-dimensional distribution, as $N_B \to \infty$, to the centred Gaussian law with covariance
$$
C_0(t_a, t_b) = \left\langle x_0(t_a)\, x_0(t_b) \right\rangle_{\mathrm{Gibbs}},
$$ {#eq:S1-C0}
which is the same for every such protocol. No statement is made that one shared $\mathcal{E}_1$ representation holds uniformly over the whole infinite clamp class $\mathcal{X}$.

## S1.4 Proofs {#sec:S1-proofs}

### Proof of Lemma 1 {#sec:S1-proof-1}

<!-- M:proof.lem1 -->
*Step 1 (independence).* Under a clamp, every oscillator obeys the same deterministic equation @eq:S1-clamp, driven by the same prescribed $\varepsilon q(t)$, from independent and identically distributed initial data. The solution map $z_0 \mapsto X^\varepsilon_q(t; z_0)$ is deterministic, so the trajectories are independent copies of one process, and $F_q = \varepsilon \sum_j X_j$ exactly. No approximation is involved.

*Step 2 (cumulant generating function).* For the vector $(F_q(t_1), \dots, F_q(t_n))$, independence gives
$\log \mathbb{E}\exp\big(\sum_a \theta_a F_q(t_a)\big) = N_B \log \mathbb{E} \exp\big(\varepsilon \sum_a \theta_a X(t_a)\big)$.
Differentiating $n$ times in $\theta$ at zero brings down $\varepsilon^n$, so $\kappa_n(F) = N_B \varepsilon^n \kappa_n(X) = N_B^{1 - n/2} \kappa_n(X)$. $\square$

*Why it matters.* For $n = 2$ the force variance equals the single-oscillator variance, so the force fluctuation is of order one at every bath size; for $n = 3$ the force cumulant is $N_B^{-1/2}$ times the single-oscillator cumulant. Everything below is about one oscillator.

### Proof of Lemma 2 {#sec:S1-proof-2}

<!-- M:proof.lem2 -->
The unforced vector field $(\dot x, \dot p) = (p, -x - x^3)$ is odd, so $(x, p) \mapsto (-x, -p)$ maps solutions to solutions, and $\rho$ is even. Hence $x_0(t)$ has a law symmetric about zero at every $t$, $\mathbb{E}\, x_0(t) = 0$, and $\kappa_3(x_0(t)) = 0$. By Lemma 1, $\kappa_3(F_{\mathrm{ref}}(t)) = N_B^{-1/2} \cdot 0 = 0$. The Gibbs law is invariant under the Hamiltonian flow, so $\operatorname{Var} F_{\mathrm{ref}}(t) = \operatorname{Var} x_0(t) = m_2$, and $m_2 > 0$ because $a^2 \geq 0$ is not almost surely zero. $\square$

### Proof of Lemma 3 {#sec:S1-proof-3}

<!-- M:proof.lem3 -->
*Step 1 (energy bound and global existence).* Along the forced flow $\mathrm{d}H_0/\mathrm{d}t = \varepsilon q p$, so $\mathrm{d}\sqrt{H_0}/\mathrm{d}t = \varepsilon q p / (2\sqrt{H_0}) \leq |\varepsilon| Q / \sqrt{2}$. Hence $\sqrt{H_0(t)} \leq \sqrt{E_0} + c_Q$ on $[0, 2\pi]$ with $c_Q = \sqrt{2}\, Q \pi$. Orbits stay in a compact set, so solutions are global on $[0, 2\pi]$, and because the vector field is polynomial in $(z, \varepsilon)$ the flow is $C^\infty$ in $(z_0, \varepsilon)$. This is (i).

*Step 2 (variational equation).* Differentiating @eq:S1-clamp in $\varepsilon$ at $\varepsilon = 0$ gives @eq:S1-y1. The initial data do not depend on $\varepsilon$, because the preparation precedes the protocol and the coupling vanishes at $t = 0$; hence $y_1(0) = \dot y_1(0) = 0$. This is (ii).

*Step 3 (moment bounds).* Let $w_k = \partial_\varepsilon^k z$. Each $w_k$ solves a linear equation $\dot w_k = A(t) w_k + f_k$ from zero, with $A = \begin{pmatrix} 0 & 1 \\ -1 - 3x^2 & 0 \end{pmatrix}$, $f_1 = (0, q)$, and, for $k = 2, 3$, inhomogeneities $f_k$ that are polynomials in $x$ and the lower-order $w_j^{x}$ obtained by differentiating $-x^3$ (for example $f_2 = (0, -6x (w_1^{x})^2)$). Since $x^4/4 \leq H_0$, $x^2 \leq 2\sqrt{H_0} \leq 2(\sqrt{E_0} + c_Q)$, so $\|A(t)\|$ and $|x|$ are bounded by a constant of the form $\mathrm{const} \cdot (1 + \sqrt{E_0})$. Grönwall's inequality on $[0, 2\pi]$ then bounds every $|w_k|$, $k \leq 3$, and $|X^\varepsilon|$ by $P(E_0)\, e^{\lambda \sqrt{E_0}}$ for a polynomial $P$ and a constant $\lambda$, uniformly in $|\varepsilon| \leq 1$.

*Step 4 (integrability).* Under $\rho$, $E_0 = H_0(z_0)$ and $e^{-E_0 + \lambda\sqrt{E_0}} \leq e^{\lambda^2/2} e^{-E_0/2}$; the phase-space area of $\{H_0 \leq e\}$ grows polynomially in $e$. So $\mathbb{E}[P(E_0) e^{\lambda \sqrt{E_0}}] < \infty$, and dominated convergence allows differentiating under $\mathbb{E}$ up to third order, with continuous derivatives. This is (iii).

*Step 5 (oddness).* The map $(x, p, \varepsilon) \mapsto (-x, -p, -\varepsilon)$ maps solutions to solutions and $\rho$ is even, so $(X^{-\varepsilon}(t))_t$ has the law of $(-X^{\varepsilon}(t))_t$. Hence $\kappa_3(X^{-\varepsilon}) = -\kappa_3(X^\varepsilon)$: the third cumulant is odd in $\varepsilon$, vanishes at $\varepsilon = 0$, and $\mathbb{E}\, x_0 = 0$.

*Step 6 (the derivative is $K$).* Write $\kappa_3(X) = \mathbb{E} X^3 - 3\, \mathbb{E} X\, \mathbb{E} X^2 + 2 (\mathbb{E} X)^3$ at one time $t$. Differentiate at $\varepsilon = 0$ using (iii) and $\partial_\varepsilon X\rvert_0 = y_1$: the first term gives $3\,\mathbb{E}[x_0^2 y_1]$; the second gives $-3\,\mathbb{E}[y_1]\, \mathbb{E}[x_0^2]$, because the other term carries the factor $\mathbb{E}\, x_0 = 0$; the third vanishes for the same reason. So
$\partial_\varepsilon \kappa_3(X^\varepsilon(t))\rvert_{\varepsilon=0} = 3\left(\mathbb{E}[x_0^2 y_1] - \mathbb{E}[x_0^2]\, \mathbb{E}[y_1]\right) = 3 c(t) = K(t)$.
(For three distinct times the same computation gives the symmetric sum of three such covariances; Theorem 1 needs only the one-time case.)

*Step 7 (Taylor in $\varepsilon$ and conversion to $N_B$).* Being $C^3$ and odd, $\kappa_3(X^\varepsilon(t)) = \varepsilon K(t) + R_3(\varepsilon)$ with $|R_3(\varepsilon)| \leq \Theta(t)\, |\varepsilon|^3$, where $\Theta(t) = \sup_{|\varepsilon| \leq 1} |\partial_\varepsilon^3 \kappa_3| / 6 < \infty$ by (iii). Lemma 1 with $n = 3$ and $\varepsilon = N_B^{-1/2}$ gives $\kappa_3(F_{\mathrm{ramp}}(t)) = N_B^{-1/2} \kappa_3(X^\varepsilon(t)) = K(t)/N_B + N_B^{-1/2} R_3(N_B^{-1/2})$, and the last term is bounded by $\Theta(t) N_B^{-2}$. $\square$

*Remark.* $\Theta(t)$ is finite but enormous (it comes from Grönwall); it certifies the *order* of the remainder, not its size at any particular $N_B$.

### Proof of Lemma 4 {#sec:S1-proof-4}

<!-- M:proof.lem4 -->
*Step 1 (pathwise smoothness).* For fixed $z_0$, $x_0$ solves a polynomial ODE and $y_1$ solves the linear ODE @eq:S1-y1 with polynomial forcing $s(t/\pi)$ on $[0, 1] \subset [0, \pi]$. Both are $C^\infty$, hence so is $g(t; z_0) = (x_0(t)^2 - m_2)\, y_1(t)$, and $c(t) = \mathbb{E}\, g(t; z_0)$.

*Step 2 (a derivative bound on $[0, 1]$).* Energy conservation gives $x_0^2 \leq 2\sqrt{E_0}$ and $p_0^2 \leq 2E_0$. With $k(t) = 1 + 3x_0^2 \leq \bar k = 1 + 6\sqrt{E_0}$ and $|q_{\mathrm{ramp}}| \leq 1$, Grönwall gives $|y_1|, |\dot y_1| \leq e^{1 + \bar k}$ on $[0, 1]$. Every time derivative of order at most eight of $x_0, \dot x_0, y_1, \dot y_1$ is, by repeated use of the equations, a polynomial in $(x_0, p_0, y_1, \dot y_1)$ and in derivatives of $q_{\mathrm{ramp}}$, which are bounded on $[0, 1]$. So $\sup_{[0,1]} |\partial_t^8 g(\cdot\,; z_0)| \leq D_8(z_0) = P(E_0)\, e^{1 + \bar k}$ for a polynomial $P$.

*Step 3 (integrability).* Because $-E_0 + 6\sqrt{E_0} \leq -E_0/2 + \max_{u \geq 0}\left(6u - u^2/2\right)$ and phase-space volume grows polynomially in $E_0$, $D_8$ is $\rho$-integrable; likewise $|\partial_t^k g(0; z_0)|$ is a polynomial in $z_0$ for $k \leq 7$.

*Step 4 (Taylor first, expectation second).* For each $z_0$, $g(t) = \sum_{k=0}^{7} g^{(k)}(0)\, t^k/k! + r(t; z_0)$ with $|r| \leq D_8(z_0)\, t^8/8!$. Take expectations of this pointwise identity; every term is integrable, so no interchange of derivative and expectation is needed:
$$
c(t) = \sum_{k=0}^{7} c_k\, t^k + R(t), \qquad |R(t)| \leq \Lambda\, t^8, \qquad c_k = \frac{\mathbb{E}[g^{(k)}(0)]}{k!}, \qquad \Lambda = \frac{\mathbb{E} D_8}{8!} < \infty .
$$ {#eq:S1-taylor}

*Step 5 (the coefficients).* Expand $x_0(t) = \sum_k \alpha_k t^k$ and $y_1(t) = \sum_k \eta_k t^k$. The equations give the recursions
$$
(k+2)(k+1)\, \alpha_{k+2} = -\alpha_k - \left(x_0^3\right)_k, \qquad (k+2)(k+1)\, \eta_{k+2} = -\eta_k - 3\left(x_0^2 y_1\right)_k + q_k ,
$$ {#eq:S1-recursion}
with $\alpha_0 = a$, $\alpha_1 = b$, $\eta_0 = \eta_1 = 0$, where $(\cdot)_k$ denotes the coefficient of $t^k$ and $q_k$ those of $s(t/\pi)$: $q_3 = {{sym.q3}}$, $q_4 = {{sym.q4}}$, $q_5 = {{sym.q5}}$, all others zero through the orders needed. Because $\eta_j = 0$ for $j \leq 4$, the first non-zero response coefficients are forced by $q$ alone until the $x_0^2 y_1$ term switches on:
$$
\eta_5 = {{sym.y1_b5}}, \qquad \eta_6 = {{sym.y1_b6}}, \qquad \eta_7 = {{sym.y1_b7}} .
$$ {#eq:S1-eta}
Writing $x_0(t)^2 = \sum_i d_i t^i$, one has $d_0 = a^2$, $d_1 = 2ab$ and, using $\alpha_2 = {{sym.x0_a2}}$, $d_2 = {{sym.x0sq_d2}}$. The coefficient of $t^n$ in $c(t) = \mathbb{E}[x_0^2 y_1] - m_2\, \mathbb{E}[y_1]$ is
$$
c_n = \operatorname{Cov}(a^2, \eta_n) + \sum_{i=1}^{n} \mathbb{E}\left[d_i\, \eta_{n-i}\right].
$$ {#eq:S1-cn}

- For $n \leq 4$ every $\eta_j$ that appears vanishes, so $c_0 = \dots = c_4 = 0$.
- $c_5 = \operatorname{Cov}(a^2, \eta_5) = 0$ and $c_6 = \operatorname{Cov}(a^2, \eta_6) + \eta_5\, \mathbb{E}[2ab] = 0$, because $\eta_5, \eta_6$ are constants and $\mathbb{E}[ab] = \mathbb{E} a\, \mathbb{E} b = 0$.
- For $n = 7$ only $i \leq 2$ can contribute. The $i = 1$ term is $\eta_6 \mathbb{E}[2ab] = 0$. The $i = 2$ term is $\eta_5\, \mathbb{E}[b^2 - a^2 - a^4] = \eta_5 (1 - m_2 - m_4) = 0$ by @eq:S1-moments. What remains is $\operatorname{Cov}(a^2, \eta_7)$; only the $a^2$ part of $\eta_7$ (coefficient ${{sym.y1_b7_a2coef}}$) is random, so
$$
c_7 = \left({{sym.y1_b7_a2coef}}\right) \operatorname{Var}(a^2) = {{sym.C7}} = {{sym.C7_in_m2}} .
$$ {#eq:S1-c7}
The constant parts of $\eta_7$, including the $\pi^{-5}$ term, cancel between $\mathbb{E}[a^2 \eta_7]$ and $m_2\, \mathbb{E}[\eta_7]$; this cancellation is a useful arithmetic check. The same coefficients, through $t^{ {{sym.order_max}} }$, are produced by an exact computer-algebra recursion (Supplement S2).

*Step 6 (sign).* $a$ has a strictly positive density, so $a^2$ is not almost surely constant and $\operatorname{Var}(x_0^2) = \operatorname{Var}(a^2) > 0$; hence $c_7 < 0$. No numerical value of $m_2$ is needed.

*Step 7 (the window).* Put $\delta = \min(1, |c_7| / (2\Lambda))$. For $0 < t < \delta$, @eq:S1-taylor gives $c(t) \leq c_7 t^7 + \Lambda t^8 = t^7 (c_7 + \Lambda t) < t^7 c_7 / 2 < 0$. $\square$

*Remarks.* $\delta$ is existential, because $\Lambda$ is an existence bound that is not computed. No complex-time radius and no all-orders expansion is used.

### Proof of Lemma 5 {#sec:S1-proof-5}

<!-- M:proof.lem5 -->
By Lemma 1 with $n = 2$, $\operatorname{Var} F_{\mathrm{ramp}}(t) = \operatorname{Var} X^\varepsilon(t)$, which is finite by Lemma 3(iii). The time-$t$ map $z_0 \mapsto z(t; z_0, \varepsilon)$ of the smooth global flow is a $C^1$ diffeomorphism of $\mathbb{R}^2$, and $\rho$ has a density. A diffeomorphism carries a law with a density to a law with a density, so $(x, p)(t)$ has a density, $x(t)$ is not almost surely constant, and the variance is strictly positive. $\square$

### Proof of Lemma 6 {#sec:S1-proof-6}

<!-- M:proof.lem6 -->
Suppose $F_q(t) = M_t[q] + G_t[q]\, \xi(t)$ with one shared law for $\xi$. For a clamped protocol, $M_t[q]$ and $G_t[q]$ are deterministic numbers, and $G_t[q] \neq 0$. Then $\operatorname{Var} F_q(t) = G_t[q]^2 \operatorname{Var}\xi(t)$, so the degeneracy set is that of $\xi$ for every $q$, and off it
$$
\kappa_3(F_q(t)) = G_t[q]^3\, \kappa_3(\xi(t)), \qquad \gamma_1[F_q(t)] = \operatorname{sgn}\!\left(G_t[q]\right) \gamma_1[\xi(t)].
$$ {#eq:S1-g1-invariant}
Hence $|\gamma_1[F_q(t)]| = |\gamma_1[\xi(t)]|$ for every $q$. $\square$

*Why the absolute value.* The sign of $G$ is allowed to depend on the protocol (that is what "signed" means), and a sign flip reverses the skewness. The absolute standardised skewness is invariant under every deterministic location shift, rescaling and sign flip, so it is exactly the kind of quantity that a shared signed-affine model must hold fixed across protocols. This is the one-time case of the reflection-orbit criterion for $\mathcal{E}_2^{\pm}$.

### Proof of Theorem 1 {#sec:S1-proof-thm}

<!-- M:proof.thm -->
Take $\delta$ from Lemma 4 and fix $t \in (0, \delta)$.

1. *Non-zero first-order coefficient.* By Lemma 4, $K(t) = 3c(t) < 0$.
2. *Threshold.* With $\Theta(t)$ from Lemma 3, set $N_0(t) = \lfloor \Theta(t)/|K(t)| \rfloor + 1$, a finite integer. For every $N_B \geq N_0(t)$ we have $N_B > \Theta(t)/|K(t)|$, so $|R_N(t)| \leq \Theta(t) N_B^{-2} < |K(t)| N_B^{-1}$, and @eq:S1-kappa3 gives $\kappa_3(F_{\mathrm{ramp}}(t)) \neq 0$ with the sign of $K(t)$, that is, negative.
3. *Standardisation is legitimate.* By Lemma 5, $0 < \operatorname{Var} F_{\mathrm{ramp}}(t) < \infty$, so $\gamma_1[F_{\mathrm{ramp}}(t)] < 0$. By Lemma 2, $\operatorname{Var} F_{\mathrm{ref}}(t) = m_2 > 0$ and $\gamma_1[F_{\mathrm{ref}}(t)] = 0$. In particular $t$ is a non-degenerate time for both protocols, so the conclusion below is not a degeneracy artefact.
4. *Contradiction.* If the two force laws had a common $\mathcal{E}_2^{\pm}$ representation, Lemma 6 would give $|\gamma_1[F_{\mathrm{ramp}}(t)]| = |\gamma_1[F_{\mathrm{ref}}(t)]| = 0$, contradicting step 3.

Hence no common $\mathcal{E}_2^{\pm}$ representation exists for $N_B \geq N_0(t)$; a fortiori the whole interventional family over $\mathcal{X}$ lies outside $\mathcal{E}_2^{\pm}$. The witness is a violation at a single non-degenerate time: the standardised law of the ramp protocol lies outside every reflection image of the reference law. $\square$

*Quantifiers, made explicit.* $\exists\, \delta > 0$ such that $\forall$ fixed $t \in (0, \delta)$, $\exists\, N_0(t) < \infty$ such that $\forall N_B \geq N_0(t)$: $\kappa_3(F_{\mathrm{ramp}}(t)) \neq 0$. The threshold depends on $t$ because $\Theta(t)$ does; no uniform $N_0$ over the interval is claimed. Nothing in the proof uses a numerically chosen time.

### Proof of Proposition 1 {#sec:S1-proof-prop}

The proof, which uses Lemmas 1–3, the window $\delta$ of Lemma 4 for the domain of part (a), and a standard multivariate central limit theorem, is given in Supplement S4. Part (a) reads, explicitly,
$$
\gamma_1[F_{\mathrm{ramp}}(t)] = \frac{K(t)}{m_2^{3/2}\, N_B} + o(N_B^{-1}) \longrightarrow 0 .
$$ {#eq:S1-g1-rate}

## S1.5 What is not claimed {#sec:S1-not}

<!-- M:scope.not_claimed -->
- No numerical value of $\delta$ or of $N_0(t)$; no uniform threshold in $t$.
- No statement that any particular numerical time, including $t_\star = 0.5$ used in Section 6, lies inside $(0, \delta)$.
- No topological or closure statement about membership in $\mathcal{E}_2^{\pm}$, and no claim that the finite-$N_B$ effect stays observable as $N_B$ grows.
- No escape from $\mathcal{E}_{\mathrm{univ}}$: model $\mathcal{D}$ is representable there.
- No shared $\mathcal{E}_1$ representation uniformly over the full clamp class $\mathcal{X}$.
