import numpy as np
from scipy import integrate
D=1.0
U=lambda z: z**2/2+z**4/4
def moments(lam):
    w=lambda z: np.exp(-(U(z)-D*lam*z)/D)   # kappa q z / D = lam z  (D=1)
    Z=integrate.quad(w,-np.inf,np.inf,epsabs=1e-14,epsrel=1e-13)[0]
    m=lambda p: integrate.quad(lambda z: z**p*w(z),-np.inf,np.inf,epsabs=1e-14,epsrel=1e-13)[0]/Z
    mu=m(1); c=lambda p: integrate.quad(lambda z:(z-mu)**p*w(z),-np.inf,np.inf,epsabs=1e-14,epsrel=1e-13)[0]/Z
    v=c(2); k3=c(3); k4=c(4)-3*v*v
    sd=np.sqrt(v)
    clip=integrate.quad(lambda z: np.clip((z-mu)/sd,-1,1)*w(z),-np.inf,np.inf,epsabs=1e-14,epsrel=1e-13,limit=200)[0]/Z
    # best tanh(c H3) not needed; also LP-optimal-type piecewise linear? just clip(a) scan
    best=max((abs(integrate.quad(lambda z: np.clip((z-mu)/sd,-a,a)*w(z),-np.inf,np.inf,epsabs=1e-14,epsrel=1e-13,limit=200)[0]/Z)/max(a,1.0),a) for a in np.linspace(0.2,3,57))
    return dict(mu=mu,var=v,k3=k3,k4=k4,g1=k3/v**1.5,Eclip1=clip,bound_clip1=0.5*abs(clip),best_clip=best)
for lam in (0.0,0.5,1.0):
    r=moments(lam); print(lam, {k:(round(v,8) if not isinstance(v,tuple) else (round(v[0]/2,6),round(v[1],3))) for k,v in r.items()})
