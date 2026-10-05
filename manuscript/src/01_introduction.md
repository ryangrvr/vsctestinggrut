# 1. Introduction {#sec:intro}

A standard route from microscopic dynamics to a reduced equation of motion eliminates the environment and keeps its effect as a memory kernel plus a random force [CITATION NEEDED: generalized Langevin equation from a harmonic bath with linear coupling (Zwanzig; Caldeira–Leggett)] [CITATION NEEDED: Mori–Zwanzig projection-operator formalism]. When the bath is harmonic and the coupling is linear in both the bath and system coordinates, the reduced path law is exactly that of a generalized Langevin equation driven by an exogenous force whose law does not depend on the system's history. Reduced data then identify the effective forcing law but not whether the environment "reacts": an exogenous noise with the right law and memory reproduces everything.

That indistinguishability depends on what is compared. For a *single* experimental protocol nothing can be distinguished at all: whatever force the environment exerts, an exogenous process with exactly that law, and no memory, reproduces the reduced path (Supplement S3). Any meaningful comparison must therefore fix one environment and probe it with a *family* of interventions, and ask whether one shared exogenous description serves the whole family.

We adopt that interventional setting. The system coordinate is clamped to prescribed trajectories, all starting from one common environment preparation, and the environment force needed to hold each trajectory is the observable. The competitor descriptions form a nested ladder (Section 3), from the harmonic class, through additive exogenous forcing with arbitrary deterministic causal memory and the shared signed-affine class $\mathcal{E}_2^{\pm}$ (an arbitrary deterministic causal scale whose *sign* may change), up to an arbitrary causal transformation of one exogenous random object. The top class contains every classical deterministic causal environment of the type considered here (a finite-dimensional state, well posed on $[0, T]$; Supplement S3), so back-reaction as such can never be identified at that level. The informative question is whether back-reaction leaves the shared signed-affine class.

Our main result (Theorem 1) answers this for a concrete model: a finite bath of $N_B$ Duffing oscillators coupled reciprocally, with strength $N_B^{-1/2}$, to the clamped coordinate. For each fixed sufficiently small time, and every sufficiently large finite $N_B$, the force law under a smooth ramp protocol has non-zero standardised skewness while the reference (at-rest) protocol has exactly zero third cumulant. Since the absolute standardised skewness is invariant under every deterministic location, scale and sign modulation, no shared signed-affine exogenous process can represent both. The leading coefficient is explicit, $K(t) = 3c(t)$ with $c(t) = {{sym.C7}}\, t^7 + O(t^8)$, and the witness decays as $O(N_B^{-1})$; in the reservoir limit the centred force laws of the fixed protocols converge to one common Gaussian law (Section 5).

<!-- M:intro.contributions -->
**Contributions.**

1. A process-level formulation, for interventional environment forces, of the established location-scale noise class [1] [CITATION NEEDED: location-scale / conditional-transformation regression literature]: one shared exogenous path law modulated by deterministic causal location and by a deterministic causal scale that may change sign but not vanish, with prefix-consistent signs and a common degeneracy set across the whole intervention family, and its exact characterisation under clamping.
2. An explicit-witness non-representability theorem: for a finite reciprocal Duffing bath, the reference and ramp protocols admit no common $\mathcal{E}_2^{\pm}$ representation for each fixed short time and every sufficiently large finite $N_B$, with an explicit negative leading coefficient of the third-cumulant witness.
3. A quantified mesoscopic scope: the witness scales as $1/N_B$ and disappears in the reservoir limit, where the known Gaussian linear-response description is recovered for the fixed protocols, at the level of finite-dimensional force laws.

<!-- M:intro.ingredients -->
**What is established and what is added.** The table separates ingredients that are already known, which we credit, from what this work contributes.

Table 1: Established ingredients and the contribution of this work.

| Established ingredients | Contribution here |
| :-------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| Harmonic baths with linear coupling give exact generalized Langevin equations with exogenous noise [CITATION NEEDED: generalized Langevin equation from a harmonic bath with linear coupling (Zwanzig; Caldeira–Leggett)] | The harmonic class placed at the bottom of a proved ladder of shared interventional classes (Supplement S3) |
| Anharmonic environments produce non-Gaussian forces; Gaussian or Markovian embeddings can fail [CITATION NEEDED: generalized Langevin equations with non-Gaussian orthogonal forces, Kiefer et al., arXiv:2505.15665 — full bibliographic details to be verified] | A protocol-dependent change of standardised force shape proved for one fixed environment across an intervention family (Theorem 1) |
| Influence-functional treatments organise anharmonic corrections around linear response [2] [3]; finite baths depart from ideal fluctuation–dissipation behaviour [4] | The finite-bath departure tied to a defined competitor class, with an explicit $1/N_B$ rate and leading coefficient |
| Location-scale noise models with fixed standardised shape, and their causal identifiability [1] [CITATION NEEDED: location-scale / conditional-transformation regression literature] | A shared *process* across interventions with prefix-consistent signed scale, and a non-representability result rather than an identifiability result within the class |
| Identifiability of interventional stochastic differential equations [CITATION NEEDED: identifiability of interventional stochastic differential equations, Zweig et al., arXiv:2505.15987 — full bibliographic details to be verified] | A constructive Hamiltonian counterexample to shared signed-affine representation |
| Gaussian, linear-response reservoir recovery for weakly coupled environments [2] [3] [CITATION NEEDED: Caldeira–Leggett-type linear-response universality], via central-limit behaviour [CITATION NEEDED: multivariate Lindeberg–Feller central limit theorem, standard probability text] | The quantified $O(1/N_B)$ disappearance of the $\mathcal{E}_2^{\pm}$ witness into that known limit, stated for the fixed protocols at the level of finite-dimensional force laws |

<!-- M:intro.dictionary -->
**A dictionary.** The competitor class has a direct counterpart in causal modelling. At a single time and a fixed protocol history, the form @eq:e2pm is the location-scale noise model $Y = f(X) + g(X) N$ of [1], under the identification below. What has no static counterpart is the shared *process* across an intervention family, the prefix-consistent sign, and the common degeneracy set.

Table 2: Causal-modelling and physics vocabulary used in this paper.

| causal modelling | this paper |
| :------------------------------------------------------------ | :------------------------------------------------------------------------------------------------ |
| intervention | clamp protocol $q \in \mathcal{X}$ applied to one fixed environment preparation |
| covariate $X$ | protocol history $q_{[0,t]}$ |
| response $Y$ | interventional environment force $F_q(t)$ |
| location function $f(X)$ | deterministic causal response $M_t[q]$ |
| scale function $g(X)$ | signed causal scale $G_t[q] \neq 0$ |
| noise $N$, independent of $X$ | shared exogenous process $\xi$ with protocol-independent law |
| standardised residual | standardised force $Z_q(t)$ |
| model membership | representability of the force family in $\mathcal{E}_1$ or $\mathcal{E}_2^{\pm}$ |

**Outline.** Section 2 defines model $\mathcal{D}$ and the protocols, Section 3 the competitor classes, Section 4 states and explains Theorem 1, Section 5 the reservoir limit, Section 6 a deterministic numerical illustration, and Section 7 discusses scope and limitations. Supplement S1 contains the statements, the notation table and the proofs of Theorem 1 and its lemmas; S2 a small-time consistency check; S3 the proved class hierarchy and mechanism map; S4 the reservoir-limit proof; S5 the numerical methods, convergence and tables; S6 a second numerical code path and reproducibility.
