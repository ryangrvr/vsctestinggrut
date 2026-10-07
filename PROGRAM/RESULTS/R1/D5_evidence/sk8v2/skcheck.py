import numpy as np, mpmath as mp
mp.mp.dps = 30
# (1) exact skewness of (Z+1)^3, Z~N(0,1), via exact Gaussian moments
def mom(k):  # E Z^k
    return 0 if k%2 else float(mp.fac2(k-1)) if k>0 else 1
from math import comb
def raw(p, shift):  # E (Z+shift)^p
    return sum(comb(p,j)*shift**(p-j)*mom(j) for j in range(p+1))
def skew_cube(shift):
    m1=raw(3,shift); m2=raw(6,shift); m3=raw(9,shift)
    var=m2-m1**2; mu3=m3-3*m1*m2+2*m1**3
    return mu3/var**1.5
print("skew Z^3 =", skew_cube(0), " skew (Z+1)^3 =", skew_cube(1))
# (2) contamination: limit of E cos(W_eta) vs E cos(N(0,1)) - exact closed forms
for eta in [1e-2,1e-4,1e-6]:
    c=eta**-0.5; m=eta*c; s=np.sqrt((1-eta)+eta*c**2-m**2)
    Ecos=(1-eta)*np.exp(-0.5/s**2)*np.cos(m/s)+eta*np.cos((c-m)/s)   # E cos((Z-m)/s)=cos(m/s)exp(-1/(2s^2))
    print(eta, "gap", abs(Ecos-np.exp(-0.5)), "eps_R lower", abs(Ecos-np.exp(-0.5))/2)
print("limit", np.exp(-0.25)-np.exp(-0.5))
# (3) square vs triangle on circle radius sqrt2: both whitened, same O(2)-symmetrization, different orbits
r=np.sqrt(2)
P=np.array([[r*np.cos(t),r*np.sin(t)] for t in np.arange(4)*np.pi/2])
Q=np.array([[r*np.cos(t),r*np.sin(t)] for t in np.arange(3)*2*np.pi/3])
for name,X in [("P",P),("Q",Q)]:
    print(name,"mean",X.mean(0).round(12),"cov",(X.T@X/len(X)).round(12).tolist())
# lower bound on min_O d_BL(P,O#Q): use test f(x)=max(0,1-|x-p|/rho) summed over P atoms? compute brute-force over O grid with LP-free bound:
# f_O(x) = sum_{p in P} max(0, 1 - |x-p|/rho)*? ; simpler: d_BL >= |E_P g - E_{OQ} g| for g = max over p of bump, Lip=1/rho -> scale by rho
rho=0.5
def g(x): # bump at P-atoms, sup<=1, Lip<=1/rho ; normalized f=rho*g has ||f||_BL<=max(rho,1)<=1
    return max(0.0,1-min(np.linalg.norm(x-p) for p in P)/rho)
best=1e9
for th in np.linspace(0,2*np.pi,3601):
    for refl in [1,-1]:
        O=np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])@np.diag([1,refl])
        val=rho*(np.mean([g(p) for p in P])-np.mean([g(O@q) for q in Q]))
        best=min(best,val)
print("min over O-grid of rho*(E_P g - E_OQ g) =", best, "(>0 => d_q^BL(P,Q)>0 on grid; exact positivity follows from distinct atom counts)")
