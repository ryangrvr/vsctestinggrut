from math import comb, log2, floor, log
def delta_len(n):  # Elias-delta length of positive integer n
    L = floor(log2(n)) + 1
    return (L - 1) + 2*floor(log2(L)) + 1
def ell(n): return delta_len(n+1)
def real_lit(p, exp): return p + ell(abs(exp)) + 1
print("real literal p=10 exp0/3/10:", real_lit(10,0), real_lit(10,3), real_lit(10,10))
print("real literal p=16 exp10:", real_lit(16,10))
# tuning price on log scale over [1e-3,1e3]
R = log(1e6)
for w in [0.05, 0.01, 0.001]:
    print("tuning bits window(ln)=",w, round(log2(R/w),2))
# credit
N=48
for cJ in [1,2,3]:
    for pi in [6, 7.99, 2.58]:
        G = N*(pi+log2(5)+1)
        bJ = N*10*cJ
        print(f"cJ={cJ} Pi={pi}: bJ={bJ} G={G:.0f} total={bJ+G:.0f} ; G with T/carrier once={N*pi+log2(5)+1:.0f} total={bJ+N*pi+log2(5)+1:.0f}")
# IP-13
for Nn,k in [(47,1),(47,4),(100,10),(1000,10),(1000,100),(10000,1000)]:
    print("IP-13 N,k",Nn,k, round(log2(comb(Nn,k)),1))
# partitions
for n in [2,3,4,5,6,7,8,16]:
    print("n",n,"log2(2^n-2)=",round(log2(2**n-2),2))
