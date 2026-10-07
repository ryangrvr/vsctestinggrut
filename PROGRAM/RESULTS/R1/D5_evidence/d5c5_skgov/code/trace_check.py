import numpy as np
tau=lambda A: np.trace(A)/A.shape[0]
Sig=np.diag([1.0,3.0])
def contrast(M): return tau(M@Sig@M.T)-tau(Sig)*tau(M@M.T)
M0=np.eye(2); M1=np.diag([1.0,2.0]); M2=np.array([[1.0,0.0],[0.7,1.0]])
for name,M in [("M0",M0),("M1",M1),("M2",M2)]:
    C=M@Sig@M.T
    # whitened Gaussian law is N(0,I) for every nonsingular C -> one GL(k) orbit
    W=np.linalg.inv(np.linalg.cholesky(C))@C@np.linalg.inv(np.linalg.cholesky(C)).T
    print(name,"trace-contrast=%.4f"%contrast(M),"whitened cov == I:",np.allclose(W,np.eye(2)))
