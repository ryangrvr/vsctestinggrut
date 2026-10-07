# Skeptic check of analyst counterexample 6 and a corrected replacement.
# eps_R for two protocols at k=1 under T_R1 equals 1/2 d_q^BL (Theorem F2), d_q^BL = min over O in {+1,-1} of d_BL(whitened laws).
# D_KL^T (analyst's MDL-modulo-T radius) for two protocols with weights w equals inf_{s in T} JS_w(P0, s#P1) <= H(w) (information-radius identity).
import numpy as np
from scipy.optimize import linprog
from scipy.stats import norm

def dbl_1d(xs, mu, nu):
    n=len(xs); c=-(mu-nu)
    rows=[];b=[]
    for i in range(n-1):
        r=np.zeros(n); r[i]=1; r[i+1]=-1; d=xs[i+1]-xs[i]
        rows.append(r.copy()); b.append(d); rows.append(-r); b.append(d)
    res=linprog(c,A_ub=np.array(rows),b_ub=np.array(b),bounds=[(-1,1)]*n,method='highs')
    return -res.fun

def gauss_on(xs):
    edges=np.concatenate(([-np.inf],(xs[1:]+xs[:-1])/2,[np.inf]))
    return np.diff(norm.cdf(edges))

def discrete_on(xs, locs, wts):
    m=np.zeros(len(xs))
    for l,w in zip(locs,wts):
        j=np.argmin(abs(xs-l)); m[j]+=w
    return m

def whiten(locs,wts):
    mu=np.sum(locs*wts); v=np.sum(wts*(locs-mu)**2); return (locs-mu)/np.sqrt(v)

L=10.0; base=np.linspace(-L,L,2001)
def eps_vs_gauss(locs,wts):
    z=whiten(np.asarray(locs,float),np.asarray(wts,float))
    xs=np.unique(np.sort(np.concatenate((base,z))))
    nu=gauss_on(xs); mu=discrete_on(xs,z,wts)
    d=min(dbl_1d(xs,mu,nu), dbl_1d(xs,mu[::-1] if False else discrete_on(xs,-z,wts),nu))
    return 0.5*d

def JS(p,q,w0=0.5):
    w1=1-w0; m=w0*p+w1*q
    def kl(a,b):
        s=a>0; return np.sum(a[s]*np.log(a[s]/b[s]))
    return w0*kl(p,m)+w1*kl(q,m)

print("H(1/2)=log2=",np.log(2))
# (i) analyst's atom family: show D_KL^T is finite (bounded by JS with s=id) and tends to 0.
for eta in [0.1,0.01]:
    c=eta**(-1/3)
    # JS_{1/2}(N, P_eta) with s=id: continuous parts share density, atom is singular part
    w=0.5; a=eta  # P_eta = (1-a) N + a delta_c
    # M = (1 - a/2) N + (a/2) delta
    kl0=-np.log(1-a/2)                        # KL(N || M)
    kl1=(1-a)*np.log((1-a)/(1-a/2))+a*np.log(a/(a/2))   # KL(P_eta || M)
    js=0.5*kl0+0.5*kl1
    print(f"atom family eta={eta}: JS_1/2(N,P_eta) [upper bound on D_KL^T] = {js:.5f}  (finite, not infinite)")
# (ii) corrected counterexample: two families with D_KL^T = log 2 exactly (mutually singular for every affine s) but different eps_R
for h in [1.0,0.5,0.25,0.1]:
    locs=np.arange(-8,8+1e-9,h); wts=norm.pdf(locs); wts/=wts.sum()
    print(f"lattice h={h}: D_KL^T = log2 (atomic vs abs. continuous for every affine s); eps_R = {eps_vs_gauss(locs,wts):.4f}")
print(f"Rademacher: D_KL^T = log2; eps_R = {eps_vs_gauss([-1,1],[0.5,0.5]):.4f}")
