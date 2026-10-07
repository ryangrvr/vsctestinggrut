"""Stage-3 evaluation kit, item (b): NR-4 law-ablation harness and responsibility map.

Charter: PROGRAM/STAGE3/STAGE3_CHARTER.md §18 NR-4 (CR-1 re-freeze 0b414e6; G2-12 item 5;
G2-13 items 1–2, CR-4). This module runs a supplied pipeline under supplied law variants.
It contains no law and evaluates none: the variants (K, K_empty, K_S, single-clause
deletions) are inputs, and they are constructed by the auditor, never by the card author
(G2-13 item 2).

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
  - the decoupled-corner set is computed ONCE, under the full law K: Ξ is excluded iff its
    K-image and the K-image of decouple(Ξ) are both defined and every lock observable
    agrees within ρ_abl. The identical set is removed from numerator and denominator for
    K, K_empty, K_S, every single-clause deletion and the responsibility map (G2-13
    item 1). A variant therefore cannot empty its own denominator;
  - if every point is excluded, the verdict is VOID (hostile default: ℛ★ not GENERATED).
    The harness never reports a fraction of 0 over an empty domain: every run's fraction
    is then None and every responsibility entry is 'VOID', never True or False;
  - builder note, for owner confirmation: a lock-fiber instance with no non-excluded
    weight (all points excluded, as in the checked kit, or zero remaining weight, added
    after review) is skipped in the every-instance clause and in the per-fiber
    responsibility report;
  - responsibility[c] is True iff ℛ★'s overall fraction under K − c is below 1/Q_min (the
    NR-4 "appears" sentence); responsibility_lock_fiber[c] lists the lock-fiber instances
    on which that fraction is below 1/Q_min (reported for Q4's "on some lock-fiber
    instance"; read by the auditor);
  - internal copies of law clauses inside components (PC-6) must already be removed by
    the supplied variant; the harness cannot detect them.
"""
from fractions import Fraction


def rho_abl(W_width, p_star=10):
    return {k: Fraction(v) / 2 ** p_star for k, v in W_width.items()}


def _excluded(K, xi, pipeline, decouple, rho):
    a = pipeline(K, xi)
    b = pipeline(K, decouple(xi))
    if a is None or b is None:
        return False
    return all(abs(a[k] - b[k]) <= rho[k] for k in rho)


def exclusion_mask(K, points, pipeline, decouple, W_width, p_star=10):
    """The decoupled-corner set, computed once under the full law K (G2-13 item 1)."""
    rho = rho_abl(W_width, p_star)
    return [_excluded(K, pt['xi'], pipeline, decouple, rho) for pt in points]


def appearance(law, points, pipeline, holds, W_width, mask, p_star=10):
    """Reference-measure fraction of Dom_gate, with the K-computed decoupled corners
    (`mask`) removed, on which ℛ★ appears under `law`, overall and per lock-fiber
    instance; plus the excluded fraction."""
    rho = rho_abl(W_width, p_star)
    tot = Fraction(0)
    num, den, excl = Fraction(0), Fraction(0), Fraction(0)
    fib = {}
    for pt, out in zip(points, mask):
        w = Fraction(pt['w'])
        tot += w
        if out:
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
    frac = num / den if den else None          # never 0 over an empty domain
    fib_frac = {i: n / d for i, (n, d) in fib.items() if d}
    return {'fraction': frac, 'per_fiber': fib_frac, 'empty': den == 0,
            'excluded_fraction': excl / tot if tot else Fraction(0)}


def nr4(K, K_empty, K_S, deletions, points, pipeline, decouple, holds, W_width,
        Q_min, p_star=10):
    """NR-4 for X = ℛ★ (threshold 1/Q_min). deletions: {clause name: law with that clause
    deleted}. Returns the verdict, every fraction, the excluded fractions and the
    responsibility map {clause: True if deleting it removes ℛ★}."""
    thr = Fraction(1, Q_min)
    mask = exclusion_mask(K, points, pipeline, decouple, W_width, p_star)
    run = {name: appearance(law, points, pipeline, holds, W_width, mask, p_star)
           for name, law in [('K', K), ('K_empty', K_empty), ('K_S', K_S)]}

    def appears(r):
        if r['fraction'] is not None and r['fraction'] >= thr:
            return True
        return bool(r['per_fiber']) and all(f >= thr for f in r['per_fiber'].values())

    if run['K']['empty']:
        # every point is a decoupled corner under K: ℛ★ is never shown off the decoupled
        # family (kit reading 3; hostile default). The mask is shared, so no variant can
        # reach an empty denominator unless K does.
        verdict = 'VOID: every point excluded (hostile default: not GENERATED)'
    elif appears(run['K_empty']):
        verdict = 'RELOCATED'
    elif appears(run['K_S']):
        verdict = 'STANDARD-IMPLIED'
    else:
        verdict = 'NOT-RELOCATED-BY-NR-4'
    resp, resp_fiber = {}, {}
    for c, law in deletions.items():
        r = appearance(law, points, pipeline, holds, W_width, mask, p_star)
        run['K-' + c] = r
        if r['empty']:                          # shared mask: empty iff K is empty (VOID)
            resp[c] = resp_fiber[c] = 'VOID'
        else:
            resp[c] = r['fraction'] < thr
            resp_fiber[c] = sorted(i for i, f in r['per_fiber'].items() if f < thr)
    return {'verdict': verdict, 'runs': run, 'responsibility': resp,
            'responsibility_lock_fiber': resp_fiber,
            'excluded_fraction_reported': {k: r['excluded_fraction'] for k, r in run.items()}}
