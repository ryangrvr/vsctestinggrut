"""Validation of kit items (b) and (c). Run: python3 test_kit.py
Fixtures are abstract test pipelines over clause tokens; they are not laws and carry no
physics. Item (d) is validated by running sel222.py (results/sel222.json)."""
import os
import sys
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nr4_ablation import nr4, appearance  # noqa: E402
from hb_controls import eps_tlin_affine_entry, static_map_control  # noqa: E402

PTS = [{'xi': g, 'w': 1, 'fiber': 'A' if g % 2 else 'B'} for g in range(4)]
W = {'o': 1024}          # ρ_abl = 1 per observable at p★ = 10
HOLDS = lambda img, rho: abs(img['o']) <= rho['o']  # noqa: E731
DEC = lambda g: 0  # noqa: E731
FULL = frozenset({'type', 'S', 'c1', 'c2'})
VARIANTS = dict(K=FULL, K_empty=frozenset({'type'}), K_S=frozenset({'type', 'S'}),
                deletions={c: FULL - {c} for c in ('c1', 'c2')})


def run(pipe):
    return nr4(points=PTS, pipeline=pipe, decouple=DEC, holds=HOLDS, W_width=W, Q_min=4,
               **VARIANTS)


def test_relocated_when_type_alone_forces():
    r = run(lambda law, g: {'o': 0 if g else 5})
    assert r['verdict'] == 'RELOCATED'


def test_standard_implied():
    r = run(lambda law, g: {'o': 0 if ('S' in law and g) else g + 5})
    assert r['verdict'] == 'STANDARD-IMPLIED'


def test_responsibility_map():
    r = run(lambda law, g: {'o': 0 if ('c1' in law and g) else g + 5})
    assert r['verdict'] == 'NOT-RELOCATED-BY-NR-4'
    assert r['responsibility'] == {'c1': True, 'c2': False}


def test_decoupled_corner_excluded_and_reported():
    # ℛ★ holds only at the decoupled corner g = 0: without exclusion K_empty would reach
    # 1/4 = 1/Q_min and convict; with the G2-12 item 5 exclusion it does not
    pipe = lambda law, g: {'o': (0 if g else 7) if 'c1' in law else 3 * g}  # noqa: E731
    r = run(pipe)
    assert r['verdict'] == 'NOT-RELOCATED-BY-NR-4'
    assert r['runs']['K_empty']['excluded_fraction'] == Fr(1, 4)


def test_undefined_image_is_not_appearance():
    r = appearance(frozenset(), PTS, lambda law, g: None, DEC, HOLDS, W)
    assert r['fraction'] == 0 and r['excluded_fraction'] == 0


def test_all_excluded_is_void():
    r = run(lambda law, g: {'o': 0})
    assert r['verdict'].startswith('VOID')


def test_hb3_hb4_exact_zero_tlin():
    M1, M2 = [Fr(0), Fr(1)], [Fr(2), Fr(-1, 3)]
    G1, G2 = [[Fr(1), Fr(0)], [Fr(1, 2), Fr(1)]], [[Fr(3), Fr(0)], [Fr(-1), Fr(2)]]
    assert eps_tlin_affine_entry(M1, G1, M2, G2) == 0


def test_static_map_on_hb4():
    # mean-0 skewed three-point driver (a two-point law cannot show it: any map of a
    # two-point law keeps γ₁² fixed by its probabilities)
    xi = [(Fr(-1), Fr(2, 5)), (Fr(0), Fr(2, 5)), (Fr(2), Fr(1, 5))]
    r = static_map_control(xi)
    assert r['with_static_tail'] != 0      # spurious nonzero witness from the static tail
    assert r['tail_removed'] == 0          # PC-7(b) removal restores the exact zero


if __name__ == '__main__':
    for name, f in list(globals().items()):
        if name.startswith('test_'):
            f()
            print('ok', name)
