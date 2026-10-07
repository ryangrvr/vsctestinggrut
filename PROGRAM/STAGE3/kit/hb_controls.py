"""Stage-3 evaluation kit, item (c), partial: B-REC exact zeros on HB-3 and HB-4 under T_lin,
and the static-map control on HB-4 (charter §15.3, §19.3 rejection list).

Exact rational arithmetic only. Records are affine images of a shared driver ξ:
  HB-3 (C2-G):  F_a = M_a + G_a ξ, ξ standard Gaussian over k time points. The law is
                N(M_a, G_a G_aᵀ); a T_lin map carrying protocol 1 to protocol 2 exists
                iff the laws are affine images; it is t(x) = M_2 + G_2 G_1⁻¹ (x − M_1).
  HB-4 (C2-NG): the same entry with a non-Gaussian ξ (affine entry). The same t is an
                exact pathwise identity, so ε^{T_lin} = 0 for any ξ law.
  Static map:   protocol 2's record passed through s(x) = x + αx² (k = 1) before the
                interface. T_lin at k = 1 preserves γ₁² = μ₃²/μ₂³, so a γ₁² mismatch is an
                exact nonzero witness. Removing the known static tail (PC-7(b)) restores 0.
This module contains no law and no card content.
"""
from fractions import Fraction as Fr


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def inv(A):
    n = len(A)
    M = [list(map(Fr, row)) + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [v / pv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]


def tlin_witness_map(M1, G1, M2, G2):
    """Return (A, b) with t(x) = A x + b and check t∘(M1 + G1·) == M2 + G2· exactly."""
    A = matmul(G2, inv(G1))
    b = [M2[i] - sum(A[i][j] * M1[j] for j in range(len(M1))) for i in range(len(M1))]
    exact = matmul(A, G1) == [list(map(Fr, r)) for r in G2] and \
        all(b[i] + sum(A[i][j] * M1[j] for j in range(len(M1))) == M2[i] for i in range(len(M1)))
    return A, b, exact


def eps_tlin_affine_entry(M1, G1, M2, G2):
    """ε^{T_lin} for affine-entry records (HB-3 and HB-4): exactly 0 iff the witness map
    is an exact identity (G1 invertible)."""
    return Fr(0) if tlin_witness_map(M1, G1, M2, G2)[2] else None


def central_moments(law):
    """law: list of (value, prob) with Fraction entries. Returns (μ2, μ3)."""
    m = sum(p * x for x, p in law)
    return (sum(p * (x - m) ** 2 for x, p in law), sum(p * (x - m) ** 3 for x, p in law))


def gamma1_sq(law):
    m2, m3 = central_moments(law)
    return m3 * m3 / (m2 ** 3)


def push(law, f):
    return [(f(x), p) for x, p in law]


def static_map_control(xi_law, M=(Fr(0), Fr(3, 10)), G=(Fr(1), Fr(2)), alpha=Fr(1, 2)):
    """k = 1. Returns the exact γ₁² witness with the static tail present and after its
    removal with the known inverse on the range."""
    F1 = push(xi_law, lambda x: M[0] + G[0] * x)
    F2 = push(xi_law, lambda x: M[1] + G[1] * x)
    F2s = push(F2, lambda x: x + alpha * x * x)
    # the known tail is injective on the support, so its inverse on the range is exact
    assert len({y for y, _ in F2s}) == len({x for x, _ in F2})
    inverse = {y: x for (y, _), (x, _) in zip(F2s, F2)}
    removed = push(F2s, lambda y: inverse[y])
    return {'with_static_tail': gamma1_sq(F2s) - gamma1_sq(F1),
            'tail_removed': gamma1_sq(removed) - gamma1_sq(F1)}
