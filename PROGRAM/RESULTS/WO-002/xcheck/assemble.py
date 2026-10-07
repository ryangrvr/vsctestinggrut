import json, glob, os, numpy as np
import mpmath as mp
D = os.path.dirname(os.path.abspath(__file__))
os.chdir(D)
R = {os.path.basename(f)[4:-5]: json.load(open(f)) for f in sorted(glob.glob('res_*.json'))}
prim_key = 'trap_0.06_400'
sec_key = 'trap_0.08_400'
prim = R[prim_key]

mp.mp.dps = 40
f = lambda k: mp.quad(lambda x: x**k * mp.exp(-x**2/2 - x**4/4), [-mp.inf, 0, mp.inf])
Z = f(0); m2x = f(2)/Z; m4x = f(4)/Z

def arr(d):
    return np.array(list(d.values()))

def stack(r):
    out = {}
    for tag in ('P1', 'P2'):
        out[tag + '_K'] = arr(r[tag]['K'])
        out[tag + '_C2'] = np.array(r[tag]['C2'])
        out[tag + '_A'] = arr(r[tag]['A'])
        out[tag + '_drho'] = arr(r[tag]['drho'])
        out[tag + '_C2nl'] = np.array(r[tag]['nl']['C2_rich_1e-2_5e-3'])
        out[tag + '_Knl'] = np.array(r[tag]['nl']['K_rich_1e-2_5e-3'])
    out['rho'] = np.array(r['rho'])
    out['m2'] = np.array([r['m2']])
    return out

P = stack(prim)
spreads = {}
for k, r in R.items():
    if k == prim_key:
        continue
    s = stack(r)
    spreads[k] = {
        'nodes': r['nodes'], 'runtime_s': r['runtime_s'],
        'm2_minus_exact': r['m2'] - float(m2x),
        'max|K-K_prim|': max(float(np.max(np.abs(s[t + '_K'] - P[t + '_K']))) for t in ('P1', 'P2')),
        'max|C2-C2_prim|': max(float(np.max(np.abs(s[t + '_C2'] - P[t + '_C2']))) for t in ('P1', 'P2')),
        'max|A-A_prim|': max(float(np.max(np.abs(s[t + '_A'] - P[t + '_A']))) for t in ('P1', 'P2')),
        'max|drho-drho_prim|': max(float(np.max(np.abs(s[t + '_drho'] - P[t + '_drho']))) for t in ('P1', 'P2')),
        'max|rho-rho_prim|': float(np.max(np.abs(s['rho'] - P['rho']))),
        'max|K-K_archA06|': r['archive']['max_abs_dev'],
        'max|K_nlRich-K_var|(same rule)': max(r[t]['nl']['maxdiff_K_rich_vs_var'] for t in ('P1', 'P2')),
        'max|C2_nlRich-C2_var|(same rule)': max(r[t]['nl']['maxdiff_C2_rich_vs_var'] for t in ('P1', 'P2')),
    }

out = {
    'primary_rule': 'trapezoid h=0.06 on [-4.5,4.5]x[-8.5,8.5] (nodes with rel. weight<1e-30 pruned), fixed-step RK8 (DOP853 tableau) 400 steps per pi',
    'm2': prim['m2'], 'm4': prim['m4'], 'm2+m4-1': prim['m2+m4-1'],
    'm2_exact_mpmath': float(m2x), 'm4_exact_mpmath': float(m4x), 'm2_exact_minus_quad': float(m2x) - prim['m2'],
    'stationarity_dev(E x0(t_a)^2 - m2)': prim['stationarity_dev'],
    'rho': prim['rho'],
    'E_x0_max': prim['E_x0'], 'kappa3_x0_max': prim['k3_x0_max'],
}
for tag in ('P1', 'P2'):
    t = prim[tag]
    out[tag] = {
        'K': t['K'],
        'K_minus_archive_K_A06': prim['archive'][tag],
        'C2_variational': t['C2'],
        'C2_nonlinear_richardson(1e-2,5e-3)': t['nl']['C2_rich_1e-2_5e-3'],
        'C2_nonlinear_richardson3(1e-2,5e-3,2.5e-3)': t['nl']['C2_rich3'],
        'K_nonlinear_richardson(1e-2,5e-3)': {kk: t['nl']['K_rich_1e-2_5e-3'][int(i)][int(j)][int(l)]
            for kk, (i, j, l) in zip(t['K'].keys(), [(a, b, c) for a in range(3) for b in range(a, 3) for c in range(b, 3)])},
        'max|K_nl_rich - K_var|': t['nl']['maxdiff_K_rich_vs_var'],
        'max|K_nl_rich3 - K_var|': t['nl']['maxdiff_K_rich3_vs_var'],
        'max|C2_nl_rich - C2_var|': t['nl']['maxdiff_C2_rich_vs_var'],
        'max|C2_nl_rich3 - C2_var|': t['nl']['maxdiff_C2_rich3_vs_var'],
        'A': t['A'],
        'drho': t['drho'],
        'parity_max|Cov(x0_a,y1_b)|': t['parity_max'],
    }
out['max_abs_dev_K_vs_archive_K_A06'] = prim['archive']['max_abs_dev']
out['quadrature_and_integrator_spreads_vs_primary'] = spreads
out['runtime_primary_s'] = prim['runtime_s']
out['runtime_total_s'] = sum(r['runtime_s'] for r in R.values())
json.dump(out, open('xcheck_results.json', 'w'), indent=1, default=float)
print(json.dumps(out, indent=1, default=float))
