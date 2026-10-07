import numpy as np
from scipy import integrate, stats

phi = stats.norm.pdf
# (i) memoryless nonlinear model X = xi + c(xi^2-1), c=0.3
c = 0.3
s = np.sqrt(1 + 2*c*c)
skew_formula = (6*c + 8*c**3)/(1+2*c*c)**1.5
g = lambda x: (x + c*(x*x-1))/s
# numerical skewness
m3 = integrate.quad(lambda x: g(x)**3*phi(x), -40, 40, limit=400)[0]
m2 = integrate.quad(lambda x: g(x)**2*phi(x), -40, 40, limit=400)[0]
m1 = integrate.quad(lambda x: g(x)*phi(x), -40, 40, limit=400)[0]
clip = lambda z: np.clip(z, -1, 1)
Ef = integrate.quad(lambda x: clip(g(x))*phi(x), -40, 40, limit=400, points=[-5,-3,-1,0,1,3])[0]
print('(i) skew formula', skew_formula, 'numeric', m3, 'mean', m1, 'var', m2)
print('(i) E clip(W) =', Ef, ' bound eps_R >= 0.5*|Ef| =', 0.5*abs(Ef))
# best odd 1-D BL witness lower bound: LP over piecewise-linear odd f on grid (sup over odd f, ||f||_inf<=1, Lip<=1)
# dist_BL(W, S) = sup_odd E f(W); eps_R >= 0.5 * that. Compute via discretized LP.
from scipy.optimize import linprog
zs = np.linspace(0, 8, 1601)  # f on [0,8], odd extension; f(0)=0
h = zs[1]-zs[0]
# density of W: W = g(xi). Compute E f(W) = sum_k f(z_k) * w_k with w_k = P(W in cell around z_k) - P(W in cell around -z_k)
xs = np.linspace(-12, 12, 400001)
dx = xs[1]-xs[0]
wv = g(xs); pw = phi(xs)*dx
edges = np.concatenate([[0], (zs[:-1]+zs[1:])/2, [np.inf]])
pos = np.histogram(wv[wv>=0], bins=edges, weights=pw[wv>=0])[0]
neg = np.histogram(-wv[wv<0], bins=edges, weights=pw[wv<0])[0]
wts = pos - neg
n = len(zs)
# maximize sum wts*f  s.t. |f_k|<=1, |f_{k+1}-f_k|<=h, f_0 = 0 (odd)
A=[];b=[]
for k in range(n-1):
    row=np.zeros(n); row[k+1]=1; row[k]=-1; A.append(row); b.append(h)
    A.append(-row); b.append(h)
bounds=[(0,0)]+[(-1,1)]*(n-1)
res = linprog(-wts, A_ub=np.array(A), b_ub=np.array(b), bounds=bounds, method='highs')
print('(i) sup over odd BL f of E f(W) ~', -res.fun, ' => eps_R lower bound (F3, two protocols) ~', -res.fun/2)

# (ii) data-processing: P=N(0,1), Q=N(0,4); phi(y)=y+y^3
def kurt(sig):
    E2 = integrate.quad(lambda x: (sig*x+(sig*x)**3)**2*phi(x), -40, 40, limit=400)[0]
    E4 = integrate.quad(lambda x: (sig*x+(sig*x)**3)**4*phi(x), -40, 40, limit=400)[0]
    return E2, E4/E2**2
E2a,k1 = kurt(1.0); E2b,k2 = kurt(2.0)
print('(ii) kurtoses', k1, k2)
fe = lambda z: np.minimum(np.abs(z), 1.0)
Ea = integrate.quad(lambda x: fe((x+x**3)/np.sqrt(E2a))*phi(x), -40, 40, limit=400, points=[-1,0,1])[0]
Eb = integrate.quad(lambda x: fe((2*x+8*x**3)/np.sqrt(E2b))*phi(x), -40, 40, limit=400, points=[-1,0,1])[0]
print('(ii) E f even: P', Ea, 'Q', Eb, ' d_q^BL >=', abs(Ea-Eb))
