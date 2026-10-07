import numpy as np, sys
sys.path.insert(0,'.')
from scipy.stats import norm
from ce6fix import dbl_1d, gauss_on
L=12.0
def eps_atom(eta):
    c=eta**(-1/3); m=eta*c; v=(1-eta)+eta*c*c-m*m; s=np.sqrt(v)
    atom=(c-m)/s
    xs=np.unique(np.sort(np.append(np.linspace(-L,L,2401),[atom,-atom])))
    edges=np.concatenate(([-np.inf],(xs[1:]+xs[:-1])/2,[np.inf]))
    nu=np.diff(norm.cdf(edges))
    mu=(1-eta)*np.diff(norm.cdf(edges,loc=-m/s,scale=1/s)); j=np.argmin(abs(xs-atom)); mu[j]+=eta
    d1=dbl_1d(xs,mu,nu); d2=dbl_1d(xs,mu[::-1],nu)  # xs symmetric grid incl. +-atom, so reversal = reflection
    return 0.5*min(d1,d2)
for eta in [0.1,0.05,0.02,0.01]:
    a=eta; js=0.5*(-np.log(1-a/2))+0.5*((1-a)*np.log((1-a)/(1-a/2))+a*np.log(2))
    print(f"eta={eta}: eps_R={eps_atom(eta):.4f}   D_KL^T <= {js:.4f}  (< log2 = 0.6931)")
