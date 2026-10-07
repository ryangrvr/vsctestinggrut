#!/usr/bin/env python3
"""R1 definition, numerical sanity checks (Claude Code).

Checks the witness inequality of R1_DEFINITION.md, Proposition 2: for 1-D laws with
standardized versions Z ~ P, W ~ Q,

    | |g(P)| - |g(Q)| |  <=  dq(P, Q) * (m_P^2 + m_P*m_Q + m_Q^2)

where:
  g   = standardized skewness E Z^3;
  m   = ||Z||_3;
  dq  = min over s in {+1,-1} of W_3(Z, s*W).

For two empirical measures with the same number of atoms, the sorted (quantile)
coupling is optimal for every convex cost, so W_3 is exact.

Controls:
  (C1) Exact identity: the distance between a law and any signed-affine image of it
       is 0, to rounding.
  (C2) The inequality must hold on every random trial. It is a theorem, so a
       violation means a bug.
  (C3) Total variation cannot carry the bound. The analytic family
       P_eta = (1-eta) N(0,1) + eta * delta_c with c = eta^(-1/3) has
       TV(P_eta, N(0,1)) = eta -> 0, while its skewness tends to 1 (N(0,1) has
       skewness 0).
"""
import json
import math
import random

def standardize(x):
    n = len(x)
    mu = sum(x) / n
    var = sum((v - mu) ** 2 for v in x) / n
    sd = math.sqrt(var)
    return [(v - mu) / sd for v in x]

def skew(z):
    return sum(v ** 3 for v in z) / len(z)

def m3(z):
    return (sum(abs(v) ** 3 for v in z) / len(z)) ** (1 / 3)

def w3_sorted(z, w):
    a, b = sorted(z), sorted(w)
    return (sum(abs(u - v) ** 3 for u, v in zip(a, b)) / len(a)) ** (1 / 3)

def dq(z, w):
    return min(w3_sorted(z, w), w3_sorted(z, [-v for v in w]))

random.seed(20261006)
out = {}

# (C1) signed-affine invariance
x = [random.gammavariate(2.0, 1.0) for _ in range(4000)]
y = [-3.7 * v + 11.2 for v in x]
zx, zy = standardize(x), standardize(y)
out["C1_affine_invariance_dq"] = dq(zx, zy)

# (C2) inequality on random pairs of laws
gens = [
    lambda: random.gauss(0, 1),
    lambda: random.expovariate(1.0),
    lambda: random.gammavariate(0.7, 1.0),
    lambda: random.lognormvariate(0, 0.6),
    lambda: random.betavariate(2, 5),
    lambda: random.paretovariate(4.5),
    lambda: random.uniform(-1, 3),
]
worst = 0.0
trials = 0
for _ in range(300):
    g1, g2 = random.sample(gens, 2)
    n = 3000
    z = standardize([g1() for _ in range(n)])
    w = standardize([g2() for _ in range(n)])
    lhs = abs(abs(skew(z)) - abs(skew(w)))
    L = m3(z) ** 2 + m3(z) * m3(w) + m3(w) ** 2
    rhs = dq(z, w) * L
    ratio = lhs / rhs if rhs > 0 else 0.0
    worst = max(worst, ratio)
    trials += 1
out["C2_trials"] = trials
out["C2_max_lhs_over_rhs"] = worst          # must be <= 1
out["C2_inequality_holds"] = worst <= 1 + 1e-12

# (C3) the TV counterexample, analytic moments of (1-eta) N(0,1) + eta * delta_c
rows = []
for eta in (1e-1, 1e-2, 1e-3, 1e-4, 1e-6):
    c = eta ** (-1 / 3)
    m1 = eta * c
    m2 = (1 - eta) + eta * c * c
    m3_raw = eta * c ** 3
    var = m2 - m1 * m1
    k3 = m3_raw - 3 * m1 * m2 + 2 * m1 ** 3
    g = k3 / var ** 1.5
    rows.append({"eta": eta, "TV_to_N01": eta, "skewness": g})
out["C3_TV_counterexample"] = rows

print(json.dumps(out, indent=1))
json.dump(out, open(__file__.replace(".py", "_output.json"), "w"), indent=1)
