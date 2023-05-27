n=int(input())
def ktra(k):
    if k==2:
        return True
    else:
        for i in range (2,k):
            if k%i!=0: continue
            else: return False
        if i==(k-1): return True
S=1
k=2
if n>=1 and n<=50:
    while S<n:
        if ktra(k): 
            print(str(k),end=' ')
            S=S+1
        k=k+1
    while S<=n:
        if ktra(k):
            print(str(k))
            S=S+1
        k=k+1