import json, sys, time, numpy as np, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xcheck import *
which = sys.argv[1]
n0 = int(sys.argv[2])
method = sys.argv[3] if len(sys.argv) > 3 else 'rk8'
if which.startswith('ghx4_'):
    n = int(which.split('_')[1]); X, P, W, dr = rule_gh_x4_gw(n)
elif which.startswith('trap_'):
    h = float(which.split('_')[1]); X, P, W, dr = rule_trap(h)
elif which.startswith('freud_'):
    _, nx, npp = which.split('_')
    x, wx = freud_gauss(int(nx)); p, wp = gh_gw(int(npp)); X, P, W, dr = tensor(x, wx, p, wp)
if method == 'rk8':
    r, S = run_rule(which, X, P, W, n0)
    tag = f'{which}_{n0}'
else:
    t0 = time.time(); S, nfev = propagate_dop853(X, P, 1e-13); t1 = time.time()
    r = analyse(X, W, S); r['nodes'] = int(X.size); r['runtime_s'] = t1 - t0; r['nfev'] = nfev
    tag = f'{which}_dop853'
r['pruned_weight'] = dr
r['archive'] = compare_archive(r)
json.dump(r, open(f'res_{tag}.json', 'w'), indent=1, default=float)
print(tag, 'nodes', X.size, 'm2', r['m2'], 'maxdev_arch', r['archive']['max_abs_dev'], 'parity', r['P1']['parity_max'], r['P2']['parity_max'], 'time', r['runtime_s'], flush=True)
