"""Validation of kit item (a). Run: python3 -m pytest -q PROGRAM/STAGE3/kit (or python3 test_l0_code.py)."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from l0_code import (ALPHABET, elias_delta_len, ell, L_stmt, normalize, compression_verdict,
                     coupling_credit, ip13_domain, ip5_constant)


def test_alphabet():
    assert len(ALPHABET) == 64


def test_elias_delta():
    # Standard Elias-delta lengths: 1→1, 2→4, 3→4, 4→5, 8→8, 16→9
    assert [elias_delta_len(n) for n in (1, 2, 3, 4, 8, 16)] == [1, 4, 4, 5, 8, 9]
    assert ell(0) == 1


def test_L_stmt_counts():
    # ∀x (x ∈ V → x = x): tokens forall var -> in var var = var var : 9 tokens; 5 occurrences of
    # 2 distinct variables (x, V): ceil(log2 3) = 2 bits each
    e = ('forall', 'x', ('->', ('in', 'x', 'V'), ('=', 'x', 'x')))
    assert L_stmt(e) == 6 * 9 + 5 * 2


def test_real_literal_price_depends_on_p():
    e = ('=', 'c', ('real', 3))
    assert L_stmt(e, p=16) - L_stmt(e, p=10) == 6


def test_normalize_prenex_nnf():
    e = ('not', ('forall', 'x', ('->', 'A', ('exists', 'y', 'B'))))
    n = normalize(e)
    # ¬∀x(A → ∃y B) = ∃x(A ∧ ∀y ¬B)
    assert n[0] == 'exists' and n[2][0] == 'forall'
    assert n[2][2] == ('and', 'A', ('not', 'B'))


def test_reserved_rejected():
    try:
        L_stmt(('reserved1',))
        assert False
    except ValueError:
        pass


def test_verdicts():
    # LOOKUP when ΔL ≤ 0 at p = 10
    assert compression_verdict(100, 10, {6: 90, 10: 200, 16: 220})['verdict'] == 'LOOKUP'
    # COMPRESSIVE: ΔL0 ≥ 10 at p=10 and > 0 at p=16
    assert compression_verdict(1000, 0, {6: 700, 10: 800, 16: 900})['verdict'] == 'COMPRESSIVE'
    # D_sel cannot fill the margin (§4.4, CT-86)
    v = compression_verdict(805, 10, {6: 790, 10: 800, 16: 810})
    assert v['verdict'] == 'NON-COMPRESSIVE'


def test_coupling_credit_caps():
    # 100 instances at c=1: 1000 bits; family cap with one shared constant: 10 bits
    assert coupling_credit([1] * 100, 1, 1, 100) == 1000
    assert coupling_credit([1] * 100, 1, 1, 100, c_fam=1) == 10
    # the per-instance minimum governs
    assert coupling_credit([1] * 99 + [0], 1, 1, 100) == 0


def test_ip13_bounded_with_redraws():
    a = ip13_domain(0, 160, 160, 16)
    b = ip13_domain(0, 160, 1600, 160)   # same exclusion rate with redraws: same price
    assert abs(a - b) < 1e-9


def test_ip5_exact_value():
    assert ip5_constant(12, exact_expr_len=30) == 30


if __name__ == '__main__':
    for name, f in list(globals().items()):
        if name.startswith('test_'):
            f()
            print('ok', name)
