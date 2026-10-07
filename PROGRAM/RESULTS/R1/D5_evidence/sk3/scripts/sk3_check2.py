import numpy as np
from scipy import integrate, stats, optimize
phi = stats.norm.pdf
def Emin(sig):
    E2 = sig**2 + 6*sig**4 + 15*sig**6
    s = np.sqrt(E2)
    f = lambda z: sig*z + (sig*z)**3
    z1 = optimize.brentq(lambda z: f(z)-s, 0, 10)
    inner = integrate.quad(lambda z: abs(f(z))/s*phi(z), -z1, z1, points=[0], epsabs=1e-14, epsrel=1e-13)[0]
    outer = 2*stats.norm.sf(z1)
    return inner+outer, z1, E2
a = Emin(1.0); b = Emin(2.0)
print(a, b, 'diff', a[0]-b[0])
# Monte Carlo sanity
rng = np.random.default_rng(1)
Z = rng.standard_normal(4_000_000)
for sig,E2 in [(1,22),(2,1060)]:
    W = (sig*Z+(sig*Z)**3)/np.sqrt(E2)
    print(sig, np.mean(np.minimum(abs(W),1)))
# Gauss-Hermite 200 nodes (what analyst may have used)
x,w = np.polynomial.hermite_e.hermegauss(200); w = w/w.sum()
for sig,E2 in [(1,22),(2,1060)]:
    W = (sig*x+(sig*x)**3)/np.sqrt(E2)
    print('GH200', sig, np.sum(w*np.minimum(abs(W),1)))
# also GH200 for clip in (i)
c=0.3; s=np.sqrt(1+2*c*c)
print('GH200 (i)', 0.5*abs(np.sum(w*np.clip((x+c*(x*x-1))/s,-1,1))))
