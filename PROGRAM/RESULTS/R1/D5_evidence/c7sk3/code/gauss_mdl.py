# Gaussian-coded (linear-Gaussian, as in Vario/ORION/LINC root nodes) two-part MDL: shared vs per-context model.
# Its large-n decision depends on per-context (mean, variance) only, i.e. exactly the coordinates T_R1 absorbs.
import numpy as np, sys
sys.path.insert(0,'.')
from scipy.stats import norm, expon
from ce6fix import dbl_1d
rng=np.random.default_rng(1)
def gauss_bic(x):  # bits: n/2 log2(2 pi e s2) + (2/2) log2 n
    n=len(x); s2=x.var(); return 0.5*n*np.log2(2*np.pi*np.e*s2)+np.log2(n)
def mdl_change(x0,x1):  # >0 means separate per-context model compresses better (change detected)
    return gauss_bic(np.concatenate([x0,x1])) - (gauss_bic(x0)+gauss_bic(x1))
n=200000
x0=rng.standard_normal(n)
x1=rng.exponential(1.0,n)-1.0           # mean 0, var 1, skewness 2
x2=2.0*rng.standard_normal(n)           # N(0,4): affine image of P0
print("Gaussian-MDL gain of separate model [bits], {N(0,1), std Exp}:", round(mdl_change(x0,x1),1))
print("Gaussian-MDL gain of separate model [bits], {N(0,1), N(0,4)}  :", round(mdl_change(x0,x2),1))
# eps_R^{T_R1} = 1/2 d_q^BL (two protocols, Theorem F2), k=1: min over reflection
xs=np.linspace(-10,12,4401); e=np.concatenate(([-np.inf],(xs[1:]+xs[:-1])/2,[np.inf]))
g=np.diff(norm.cdf(e)); ex=np.diff(expon.cdf(e,loc=-1.0))
d=min(dbl_1d(xs,ex,g), dbl_1d(xs,np.diff(1-expon.cdf(-e,loc=-1.0))*-1*-1 if False else np.diff(expon.sf(-e,loc=-1.0))*-1, g) if False else dbl_1d(xs,ex,g))
# reflection: N(0,1) symmetric, so d_BL(ex, g) = d_BL(R ex, g); min over O(1) equals this value
print("eps_R^{T_R1}({N(0,1), std Exp}) =", round(0.5*d,4), " ; eps_R^{T_R1}({N(0,1), N(0,4)}) = 0 (affine images)")
