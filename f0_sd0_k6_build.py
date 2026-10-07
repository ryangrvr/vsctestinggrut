#!/usr/bin/env python3
import sys
sys.setrecursionlimit(100000)
from itertools import combinations, product
from math import gcd
from functools import reduce
def add(u,v): return (u[0]+v[0], u[1]+v[1])
def sub(u,v): return (u[0]-v[0], u[1]-v[1])
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def dot(x,y): return reduce(add, (mul(a,b) for a,b in zip(x,y)))
ZERO=(0,0)
def primitive(v):
    if all(c==ZERO for c in v): return None
    while True:
        g = 0
        for a,b in v: g = gcd(g, gcd(abs(a), abs(b)))
        if g > 1: v = tuple((a//g, b//g) for a,b in v)
        if all(a % 2 == 0 for a,b in v):
            v = tuple((b, a//2) for a,b in v); continue
        break
    for a,b in v:
        if (a,b) != ZERO:
            if (a < 0) or (a == 0 and b < 0): v = tuple((-a,-b) for a,b in v)
            break
    return v
def cross(x,y):
    return primitive((sub(mul(x[1],y[2]), mul(x[2],y[1])),
                      sub(mul(x[2],y[0]), mul(x[0],y[2])),
                      sub(mul(x[0],y[1]), mul(x[1],y[0]))))
vals = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]
rays = set()
for v in product(vals, repeat=3):
    p = primitive(v)
    if p: rays.add(p)
for it in range(4):
    new = set()
    rl0 = sorted(rays)
    for x, y in combinations(rl0, 2):
        if dot(x,y) == ZERO:
            c = cross(x,y)
            if c and c not in rays: new.add(c)
    if not new: break
    rays |= new
rl = sorted(rays)
idx = {r:i for i,r in enumerate(rl)}
triads = [tuple(idx[v] for v in t) for t in
          ( (a,b,c) for a,b,c in combinations(rl,3)
            if dot(a,b)==ZERO and dot(a,c)==ZERO and dot(b,c)==ZERO )]
n = len(rl)
print(f"rays {n}, triads {len(triads)}")

ray_triads = [[] for _ in range(n)]
for ti, t in enumerate(triads):
    for r in t: ray_triads[r].append(ti)

def solve():
    color = [None]*n
    def propagate(queue):
        """returns (ok, trail) applying forced moves"""
        trail = []
        work = list(queue)
        while work:
            ti = work.pop()
            t = triads[ti]
            ones = sum(1 for i in t if color[i]==1)
            zeros = sum(1 for i in t if color[i]==0)
            if ones > 1 or zeros == 3: return False, trail
            if ones == 1:
                for i in t:
                    if color[i] is None:
                        color[i] = 0; trail.append(i)
                        work.extend(ray_triads[i])
            elif zeros == 2:
                for i in t:
                    if color[i] is None:
                        color[i] = 1; trail.append(i)
                        work.extend(ray_triads[i])
        return True, trail
    def undo(trail):
        for i in trail: color[i] = None
    def bt():
        # MRV: triad with no 1, fewest unknowns
        best, bu = None, 4
        for ti, t in enumerate(triads):
            ones = sum(1 for i in t if color[i]==1)
            if ones: continue
            unk = [i for i in t if color[i] is None]
            if not unk: return False
            if len(unk) < bu: best, bu = ti, len(unk)
        if best is None: return True  # every triad has its 1
        t = triads[best]
        for pick in [i for i in t if color[i] is None]:
            color[pick] = 1
            trail = [pick]
            ok, tr = propagate(ray_triads[pick])
            trail += tr
            if ok and bt(): return True
            undo(trail)
        return False
    return bt()

res = solve()
print("KS-colorable:", res, "(False = certified pure-triad KS set)")
if not res:
    import json
    json.dump({"rays": rl, "triads": triads}, open("ks_set.json","w"))
    print("saved ks_set.json:", n, "rays,", len(triads), "triads")
#!/usr/bin/env python3
"""Trim the certified pure-triad KS set to a smaller uncolorable core (greedy triad
removal; uncolorability re-decided exactly at each step), then build the CHTW
KS-game support. Candidate-independent."""
import json

d = json.load(open("ks_set.json"))
rays, triads = d["rays"], [tuple(t) for t in d["triads"]]

def colorable(triads, n):
    ray_triads = {}
    for ti, t in enumerate(triads):
        for r in t: ray_triads.setdefault(r, []).append(ti)
    color = {}
    def propagate(queue, trail):
        work = list(queue)
        while work:
            ti = work.pop()
            t = triads[ti]
            ones = sum(1 for i in t if color.get(i) == 1)
            zeros = sum(1 for i in t if color.get(i) == 0)
            unk = [i for i in t if i not in color]
            if ones > 1 or (ones == 0 and not unk): return False
            if ones == 1:
                for i in unk:
                    color[i] = 0; trail.append(i); work.extend(ray_triads.get(i, []))
            elif len(unk) == 1 and ones == 0:
                i = unk[0]; color[i] = 1; trail.append(i); work.extend(ray_triads.get(i, []))
        return True
    def bt():
        best, bu = None, 5
        for ti, t in enumerate(triads):
            if any(color.get(i) == 1 for i in t): continue
            unk = [i for i in t if i not in color]
            if not unk: return False
            if len(unk) < bu: best, bu = ti, len(unk)
        if best is None: return True
        for pick in [i for i in triads[best] if i not in color]:
            trail = [pick]; color[pick] = 1
            if propagate(ray_triads.get(pick, []), trail) and bt(): return True
            for i in trail: color.pop(i, None)
        return False
    return bt()

assert not colorable(triads, len(rays))
# greedy trim
cur = list(triads)
changed = True
while changed:
    changed = False
    for k in range(len(cur)):
        test = cur[:k] + cur[k+1:]
        if not colorable(test, len(rays)):
            cur = test; changed = True; break
used = sorted({r for t in cur for r in t})
print(f"trimmed core: {len(cur)} triads over {len(used)} rays; uncolorable: {not colorable(cur, len(rays))}")
remap = {r: i for i, r in enumerate(used)}
core = {"rays": [rays[r] for r in used], "triads": [[remap[r] for r in t] for t in cur]}
json.dump(core, open("ks_core.json", "w"))
print("saved ks_core.json")
