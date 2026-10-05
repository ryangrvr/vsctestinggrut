# S6. Methods and provenance {#sec:S6}

<!-- M:num.method -->
**Finite-$N_B$ computation (Section 6).** By the exact single-oscillator reduction, every bath size requires only the driven single-oscillator process at $\varepsilon = N_B^{-1/2}$. Gibbs expectations over $(x_0, p_0)$ are computed by deterministic tensor Gauss–Legendre quadrature on $[-{{num.L}}, {{num.L}}]^2$ with ${{num.nx}}$ nodes per dimension and the Gibbs weight, normalised on the grid. Every node pair is evolved separately with a fixed-step fourth-order Runge–Kutta integrator of step ${{num.dt}}$. The force cumulants then follow from @eq:S1-star. Only the output at this reference resolution is available in machine-readable form, and only that output is used in this manuscript. A resolution ladder in grid size and step size is reported alongside the original computation, but not as machine-readable output.

<!-- M:num.history -->
**Verification history.** Two earlier attempts at this illustration failed and are reported rather than hidden. A Monte Carlo design could not detect the signal: at the very short time it used, the third cumulant lay many orders of magnitude below the sampling noise. A first deterministic quadrature passed its convergence tests but evolved the wrong set of node pairs; the error was exposed because the reference-protocol variance was not stationary and violated the exact moment identity. Convergence alone did not detect it. The computation used here passes both controls, and its values were reproduced by a separately written implementation using a different integrator and grid. That reproduction is internal, not external.

<!-- M:check.t7 -->
**Small-time check (Supplement S2).** Written for this build; methods as described in Supplement S2.

<!-- M:build.provenance -->
**Build provenance.** This manuscript is compiled, not typed. Every number is drawn from machine-readable output or computed by a build script, and every figure and table is generated from the same sources. A build manifest traces each definition, lemma, theorem and load-bearing equation to its source, and each printed value to its origin. The build fails if a placeholder is unresolved, if a scientific number appears in the source text, or if a value lacks provenance.

<!-- M:disclosure.research -->
[AI-USE DISCLOSURE — research: proof development, code, numerical verification]
