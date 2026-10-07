import numpy as np
from scipy.linalg import expm
from scipy.stats import norm
def witness(lam,tau,M,L=4.0):
    z=np.linspace(-L,L,M); h=z[1]-z[0]
    V=z**2/2+z**4/4-lam*z
    pi=np.exp(-(V-V.min())); pi/=pi.sum()
    # square-root-approximation generator, reversible wrt pi
    up=np.exp(-(V[1:]-V[:-1])/2)/h**2   # rate i->i+1
    dn=np.exp(-(V[:-1]-V[1:])/2)/h**2   # rate i+1->i
    Q=np.zeros((M,M)); i=np.arange(M-1)
    Q[i,i+1]=up; Q[i+1,i]=dn; Q[np.arange(M),np.arange(M)]=-Q.sum(1)
    P=expm(Q*tau)
    J=pi[:,None]*P
    F=np.cumsum(pi)-pi/2; N=norm.ppf(F)
    t=np.tanh(N)
    w_odd=np.sum(J*(t[:,None]**2)*t[None,:])
    w_even=np.sum(J*t[:,None]*t[None,:])
    sym=np.abs(J-J.T).max()
    return w_odd,w_even,sym
for lam in (0.0,1.0):
    for tau in (0.25,1.0):
        for M in (401,801):
            wo,we,s=witness(lam,tau,M)
            print(f"lam={lam} tau={tau} M={M}: E[tanh(N1)^2 tanh(N2)]={wo:+.5e}  E[tanh N1 tanh N2]={we:+.5e}  detailed-balance asym={s:.1e}")
# Lipschitz constant of g(n1,n2)=tanh(n1)^2 tanh(n2)
x=np.linspace(-6,6,2001); X,Y=np.meshgrid(x,x)
g1=2*np.tanh(X)/np.cosh(X)**2*np.tanh(Y); g2=np.tanh(X)**2/np.cosh(Y)**2
print("Lip bound", np.sqrt(g1**2+g2**2).max(), "analytic sqrt(1+(4/(3*sqrt3))^2)=", np.sqrt(1+(4/(3*np.sqrt(3)))**2))
