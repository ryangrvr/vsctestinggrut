#!/usr/bin/env python3
"""Harmonic control of kubo_check.py rerun on a wider x-domain (Lx = 8.5): the Lx = 4.5 rule
truncates the unit-variance harmonic Gibbs law (m2 = 0.99987), which breaks stationarity on the
quadrature measure and leaves an O(1e-4) artifact in the Kubo-side integral."""
import json, sys
import kubo_check as kc

_orig = kc.rule_trap
kc.rule_trap = lambda h, Lx=4.5, Lp=8.5, harmonic=False: _orig(h, Lx=8.5, Lp=8.5, harmonic=harmonic)
m2, Kdir, Kfdt, R, ts = kc.run(0.08, 8000, harmonic=True)
print(json.dumps({"harmonic_wide": {"m2": m2, "K_direct": Kdir, "K_kubo": Kfdt,
                                    "max_abs_R": float(abs(R).max())}}, indent=1))
