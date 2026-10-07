"""Stage-3 evaluation kit, item (b): NR-4 law-ablation harness and responsibility map.

Charter: PROGRAM/STAGE3/STAGE3_CHARTER.md §18 NR-4 (CR-1 re-freeze 0b414e6; G2-12 item 5).
This module runs a supplied pipeline under supplied law variants. It contains no law and
evaluates none: the variants (K, K_empty, K_S, single-clause deletions) are inputs.

Interface (all supplied by the Evaluator, never by the card):
  points    list of dicts {'xi': Ξ, 'w': reference-measure weight, 'fiber': ι or None}
            drawn from Dom_gate (Dom_pre for the run).
  pipeline  pipeline(law, xi) -> dict {lock observable: value} for a defined image,
            or None when the pipeline image is undefined.
  decouple  decouple(xi) -> the same Ξ with every S–E coupling set to zero.
  holds     holds(obs, tol) -> True iff the image satisfies ℛ★ within tol per lock
            observable.
  W_width   {lock observable: |W|} (the chart width); ρ_abl = 2^(−p★)·|W| per observable.

Readings recorded in kit/README.md:
  - an undefined image does not count as ℛ★ appearing and stays in the denominator;
  - the decoupled-corner test compares Ξ with decouple(Ξ) under the same law variant;
    a point is excluded only if both images are defined and every lock observable agrees
    within ρ_abl;
  - if every point is excluded under K, the verdict is VOID (hostile default: ℛ★ not
    GENERATED), never a fraction of 0 over an empty domain;
  - internal copies of law clauses inside components (PC-6) must already be removed by
    the supplied variant; the harness cannot detect them.
"""
from fractions import Fraction


def rho_abl(W_width, p_star=10):
    return {k: Fraction(v) / 2 ** p_star for k, v in W_width.items()}


def _excluded(law, xi, pipeline, decouple, rho):
    a = pipeline(law, xi)
    b = pipeline(law, decouple(xi))
    if a is None or b is None:
        return False
    return all(abs(a[k] - b[k]) <= rho[k] for k in rho)


def appearance(law, points, pipeline, decouple, holds, W_width, p_star=10):
    """Reference-measure fraction of Dom_gate (decoupled corners removed) on which ℛ★
    appears under `law`, overall and per lock-fiber instance; plus the excluded fraction."""
    rho = rho_abl(W_width, p_star)
    tot = Fraction(0)
    num, den, excl = Fraction(0), Fraction(0), Fraction(0)
    fib = {}
    for pt in points:
        w = Fraction(pt['w'])
        tot += w
        if _excluded(law, pt['xi'], pipeline, decouple, rho):
            excl += w
            continue
        img = pipeline(law, pt['xi'])
        hit = img is not None and holds(img, rho)
        den += w
        num += w if hit else 0
        if pt.get('fiber') is not None:
            n_d = fib.setdefault(pt['fiber'], [Fraction(0), Fraction(0)])
            n_d[0] += w if hit else 0
            n_d[1] += w
    frac = num / den if den else Fraction(0)
    fib_frac = {i: (n / d if d else Fraction(0)) for i, (n, d) in fib.items()}
    return {'fraction': frac, 'per_fiber': fib_frac, 'empty': den == 0,
            'excluded_fraction': excl / tot if tot else Fraction(0)}


def nr4(K, K_empty, K_S, deletions, points, pipeline, decouple, holds, W_width,
        Q_min, p_star=10):
    """NR-4 for X = ℛ★ (threshold 1/Q_min). deletions: {clause name: law with that clause
    deleted}. Returns the verdict, every fraction, the excluded fractions and the
    responsibility map {clause: True if deleting it removes ℛ★}."""
    thr = Fraction(1, Q_min)
    run = {name: appearance(law, points, pipeline, decouple, holds, W_width, p_star)
           for name, law in [('K', K), ('K_empty', K_empty), ('K_S', K_S)]}

    def appears(r):
        if r['fraction'] >= thr:
            return True
        return bool(r['per_fiber']) and all(f >= thr for f in r['per_fiber'].values())

    if run['K']['empty']:
        # every point is a decoupled corner under K: ℛ★ is never shown off the decoupled
        # family (kit reading; hostile default)
        verdict = 'VOID: every point excluded (hostile default: not GENERATED)'
    elif appears(run['K_empty']):
        verdict = 'RELOCATED'
    elif appears(run['K_S']):
        verdict = 'STANDARD-IMPLIED'
    else:
        verdict = 'NOT-RELOCATED-BY-NR-4'
    resp = {}
    for c, law in deletions.items():
        r = appearance(law, points, pipeline, decouple, holds, W_width, p_star)
        run['K-' + c] = r
        resp[c] = r['fraction'] < thr
    return {'verdict': verdict, 'runs': run, 'responsibility': resp,
            'excluded_fraction_reported': {k: r['excluded_fraction'] for k, r in run.items()}}
