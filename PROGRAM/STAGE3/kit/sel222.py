"""Stage-3 evaluation kit, item (d): B-SEL reproduction of the charter §2.4 values.

Reuses the SD0 enumeration code at the repository root (f0_sd0_recon_222.py, exact
rational arithmetic) and checks the frozen counts: 2961 pNS tables, 1721 local,
1232 logically contextual (992 exact-support realizable, 240 not), 8 strongly contextual
(exactly the 8 PR boxes: the PR-forcing check), and 2721 exact-support-realizable
supports. Writes results/sel222.json. Runtime about 3 minutes.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..')))
import f0_sd0_recon_222 as sd0  # noqa: E402

FROZEN = {'pNS': 2961, 'local': 1721, 'logical': 1232, 'strong': 8,
          'logical_realizable': 992, 'gap': 240, 'realizable_supports': 2721}


def run():
    sd0.SYMS = sd0.all_symmetries()
    tables = sd0.pns_tables()
    cls = {'local': [], 'logical': [], 'strong': []}
    for S in tables:
        cls[sd0.classify(S)[0]].append(S)
    real = {k: [S for S in v if sd0.exact_support_realizable(S)] for k, v in cls.items()}

    def key(S):
        return tuple(sorted((c, tuple(sorted(S[c]))) for c in sd0.CTX))
    pr_forcing = {key(S) for S in real['strong']} == {key(S) for S in sd0.pr_boxes()}
    out = {'pNS': len(tables), 'local': len(cls['local']), 'logical': len(cls['logical']),
           'strong': len(cls['strong']), 'logical_realizable': len(real['logical']),
           'gap': sum(len(cls[k]) - len(real[k]) for k in cls),
           'realizable_supports': sum(len(v) for v in real.values()),
           'local_all_realizable': len(real['local']) == len(cls['local']),
           'strong_realizable_equals_PR_boxes': pr_forcing}
    out['matches_frozen'] = all(out[k] == v for k, v in FROZEN.items()) and pr_forcing
    return out


if __name__ == '__main__':
    r = run()
    with open(os.path.join(HERE, 'results', 'sel222.json'), 'w') as f:
        json.dump(r, f, indent=2)
    print(json.dumps(r, indent=2))
    assert r['matches_frozen'], 'SEL reproduction does not match charter §2.4'
