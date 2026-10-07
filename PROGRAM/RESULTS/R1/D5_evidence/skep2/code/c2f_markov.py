import numpy as np
dt=0.01; n=64
def K1(tau):
    r=np.exp(-dt/tau); i=np.arange(n)
    D=i[:,None]-i[None,:]
    return np.where(D>=0, r**np.clip(D,0,None), 0.0)
def pred_weights(K,k):
    # exact conditional expectation E[F_k | F_<k] = K[k,<k] xi_<k + E xi_k ; xi_<k = K_<k^{-1} F_<k
    A=K[:k,:k]; w=np.linalg.solve(A.T, K[k,:k])
    return w   # weights on F_0..F_{k-1}
# C2-F as implemented: single exponential
for tau in (0.05,0.20):
    K=K1(tau); r=np.exp(-dt/tau)
    # check recursion F_k = r F_{k-1} + xi_k: K[k,:] - r K[k-1,:] = e_k
    E=K[1:,:]-r*K[:-1,:]; I=np.eye(n)[1:,:]
    w=pred_weights(K,40)
    print(f"C2-F tau={tau}: max|K_k - r K_(k-1) - e_k|={np.abs(E-I).max():.2e}; weight on F_(k-1)={w[-1]:.6f} (r={r:.6f}); max|weight on F_<k-1|={np.abs(w[:-1]).max():.2e}")
# C2-F' : unit-diagonal two-exponential filter, K = (K(t1)+K(t2))/2
for taus in ((0.05,0.40),(0.02,0.20)):
    K=0.5*(K1(taus[0])+K1(taus[1]))
    for k in (10,40,63):
        w=pred_weights(K,k)
        print(f"C2-F' taus={taus} k={k}: w(F_k-1)={w[-1]:.5f}, w(F_k-2)={w[-2]:.5f}, max|w on F_<k-1|={np.abs(w[:-1]).max():.4e}, l1={np.abs(w[:-1]).sum():.4e}")
