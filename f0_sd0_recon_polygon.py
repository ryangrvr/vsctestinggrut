#!/usr/bin/env python3
"""F0-SD0 Stage-1 reconnaissance (Owner Ruling 05 C4 Stage 1(ii)):
polygon zero-pattern/support reconnaissance at fixed capacity.

Part A (single system; analytic statement + numeric confirmation):
  Regular-n-gon state spaces (JGBB family) all have capacity 2, yet their
  SINGLE-SYSTEM zero structure differs by parity. For the binary facet
  measurement (e_F, u - e_F), where e_F vanishes on facet F and is scaled so
  max over the polygon is 1:
    - number of extremal states with outcome-1 impossible (e_F = 0): 2 (any n);
    - number of extremal states with outcome-2 impossible (e_F = 1):
        2 if n is even (the antipodal facet), 1 if n is odd (the opposite
        vertex).
  Analytic reason: a facet's supporting functional attains its maximum over a
  regular polygon on the antipodal FACET (two vertices) when n is even and at
  the single opposite VERTEX when n is odd. The numeric scan below confirms the
  counts for n = 3..8 (floats used only as CONFIRMATION of the stated
  combinatorial fact, tolerance 1e-9).

Part B (bipartite; exact rational):
  PR-FORCING LEMMA (exact, weights-free): any probability model whose support
  is the PR zero-pattern has every correlator equal to +/-1, hence CHSH = 4,
  for ANY weights on the support. Therefore a composite whose attainable CHSH
  is < 4 cannot realize the PR support. (Proof: in each pair context the
  support contains only sections of one fixed parity, so E = +/-1 exactly.)

  n = 4 (square = gbit; rational coordinates): the PR zero-pattern IS
  exact-support realizable. We construct the PR functional on the maximal
  tensor product and verify, in exact rationals: normalization, positivity on
  all products of extremal effects, the uniform marginals, and the exact PR
  support (8 cells with p = 1/2, 8 cells with p = 0).

Part C: what is NOT settled here (recorded UNRESOLVED): the attainable-CHSH
  values and support families for polygon composites with n != 4 (and for the
  JGBB maximally-entangled analogues) are not computed in this reconnaissance;
  by the PR-forcing lemma, any (n, composite, state-family) with attainable
  CHSH < 4 cannot realize the PR support — the per-n values are comparator
  inputs to be sourced from the JGBB full text or computed in a later stage.
"""
import math
from fractions import Fraction as Fr
from itertools import product

TOL = 1e-9

# ---------------- Part A: single-system zero structure ----------------
def polygon_vertices(n):
    return [(math.cos(2 * math.pi * i / n), math.sin(2 * math.pi * i / n)) for i in range(n)]

def facet_effect(verts, j):
    """Affine functional vanishing on edge (v_j, v_{j+1}), nonnegative on the
    polygon, scaled to max 1 over the polygon. Returns its values on vertices."""
    n = len(verts)
    (x1, y1), (x2, y2) = verts[j], verts[(j + 1) % n]
    # line through the two vertices: a x + b y = c, with polygon on side <= c
    a, b = y2 - y1, x1 - x2
    c = a * x1 + b * y1
    vals = [c - (a * x + b * y) for (x, y) in verts]   # 0 on the edge, >0 inside-side
    mx = max(vals)
    return [v / mx for v in vals]

def part_a():
    print("Part A — single-system zero structure (binary facet measurement), capacity 2 for all n:")
    rows = []
    for n in range(3, 9):
        verts = polygon_vertices(n)
        e = facet_effect(verts, 0)
        z1 = sum(1 for v in e if abs(v) < TOL)        # outcome-1 impossible
        z2 = sum(1 for v in e if abs(v - 1) < TOL)    # outcome-2 impossible
        rows.append((n, z1, z2))
        expect2 = 2 if n % 2 == 0 else 1
        ok = (z1 == 2 and z2 == expect2)
        print(f"  n={n}: outcome-1-impossible states = {z1}, outcome-2-impossible = {z2} "
              f"(expected {expect2}) {'OK' if ok else 'MISMATCH'}")
        assert ok
    print("  => at fixed capacity 2, odd and even polygon geometries have DIFFERENT")
    print("     single-system zero patterns: the parity of n is visible at support level.")

# ---------------- Part B: exact n=4 PR realization ----------------
def part_b():
    print("\nPart B — PR-forcing lemma + exact boxworld (n=4) PR realization:")
    print("  Lemma (exact): PR support => every correlator = +/-1 => CHSH = 4, any weights.")
    # Square system: states (x, y) in [-1,1]^2; unit effect u = 1.
    # Extremal nontrivial effects: e = (1+s*x)/2, (1+s*y)/2, s in {+1,-1}.
    # Measurements: A0 = x-pair, A1 = y-pair; same for Bob.
    # Bipartite PR functional on {1, xA, yA} (x) {1, xB, yB}:
    M = {('1', '1'): Fr(1),
         ('x', '1'): Fr(0), ('y', '1'): Fr(0), ('1', 'x'): Fr(0), ('1', 'y'): Fr(0),
         ('x', 'x'): Fr(1), ('x', 'y'): Fr(1), ('y', 'x'): Fr(1), ('y', 'y'): Fr(-1)}
    def omega(uA, sA, uB, sB):
        # value on product effect ((1+sA*uA)/2) (x) ((1+sB*uB)/2)
        return Fr(1, 4) * (M[('1', '1')] + sA * M[(uA, '1')] + sB * M[('1', uB)]
                           + sA * sB * M[(uA, uB)])
    cells = []
    neg = 0
    for uA in ('x', 'y'):
        for uB in ('x', 'y'):
            tot = Fr(0)
            for sA in (1, -1):
                for sB in (1, -1):
                    p = omega(uA, sA, uB, sB)
                    if p < 0:
                        neg += 1
                    tot += p
                    cells.append(((uA, uB), (sA, sB), p))
            assert tot == 1
    assert neg == 0
    half = sum(1 for _, _, p in cells if p == Fr(1, 2))
    zero = sum(1 for _, _, p in cells if p == 0)
    # PR pattern: contexts xx, xy, yx correlated (sA*sB=+1 has p=1/2), yy anticorrelated
    ok = all((p == Fr(1, 2)) == ((sA * sB == 1) if (uA, uB) != ('y', 'y') else (sA * sB == -1))
             for ((uA, uB), (sA, sB), p) in cells)
    print(f"  all 16 product-effect probabilities nonnegative: True; per-context sums = 1: True")
    print(f"  support pattern: {half} cells at exactly 1/2, {zero} cells at exactly 0; "
          f"matches PR zero-pattern: {ok}")
    assert half == 8 and zero == 8 and ok
    print("  => the PR support IS exact-support realizable on square (x) square (gbit/boxworld),")
    print("     in exact rational arithmetic. Same capacity (2) as the qubit, which cannot")
    print("     realize it (Lal / (2,2,2) enumeration: strong = PR only; PR not quantum).")

def part_c():
    print("\nPart C — UNRESOLVED at this stage (recorded):")
    print("  attainable-CHSH values / support families for polygon composites with n != 4")
    print("  (incl. JGBB maximally-entangled analogues) are not computed here; by the")
    print("  PR-forcing lemma, attainable CHSH < 4 implies the PR support is unrealizable")
    print("  for that (n, composite, state family). Per-n values: comparator inputs, to be")
    print("  sourced from the JGBB full text or computed in a later authorized stage.")

if __name__ == '__main__':
    part_a(); part_b(); part_c()
