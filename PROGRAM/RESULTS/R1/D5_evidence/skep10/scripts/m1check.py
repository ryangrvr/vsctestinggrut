import numpy as np
from scipy.optimize import linprog
def std(vals, probs):
    vals=np.array(vals,float); probs=np.array(probs,float)
    m=(vals*probs).sum(); v=((vals-m)**2*probs).sum()
    return (vals-m)/np.sqrt(v), probs
def dbl(x,p,y,q):
    # W1 with cost min(|x-y|,2)
    n,m=len(x),len(y)
    C=np.minimum(np.abs(x[:,None]-y[None,:]),2.0).ravel()
    A=[];b=[]
    for i in range(n):
        r=np.zeros(n*m); r[i*m:(i+1)*m]=1; A.append(r); b.append(p[i])
    for j in range(m):
        r=np.zeros(n*m); r[j::m]=1; A.append(r); b.append(q[j])
    res=linprog(C,A_eq=np.array(A),b_eq=np.array(b),bounds=(0,None),method='highs')
    return res.fun
def dual_dbl(x,p,y,q):
    # sup E_p f - E_q f over |f|<=1, Lip<=1 on support points (extension exists on R)
    pts=np.unique(np.concatenate([x,y])); k=len(pts)
    w=np.zeros(k)
    for xi,pi in zip(x,p): w[np.searchsorted(pts,xi)]+=pi
    for yi,qi in zip(y,q): w[np.searchsorted(pts,yi)]-=qi
    A=[];b=[]
    for i in range(k-1):
        d=pts[i+1]-pts[i]
        r=np.zeros(k); r[i+1]=1; r[i]=-1; A.append(r); b.append(d); A.append(-r); b.append(d)
    res=linprog(-w,A_ub=np.array(A),b_ub=np.array(b),bounds=[(-1,1)]*k,method='highs')
    return -res.fun
for p in [0.25,0.1]:
    x0,p0=std([-1,1],[.5,.5])
    vals=[-1,0,1,2]; pr=[.5*(1-p),.5*p,.5*(1-p),.5*p]
    x1,p1=std(vals,pr)
    dq=min(dbl(x0,p0,x1,p1),dbl(x0,p0,-x1,p1))
    dq2=min(dual_dbl(x0,p0,x1,p1),dual_dbl(x0,p0,-x1,p1))
    k3=p*(1-p)*(1-2*p); g=k3/(1+p*(1-p))**1.5
    print(p,'dq',dq,dq2,'eps_R',dq/2,'gamma',g)
