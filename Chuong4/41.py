def nhap():
    n=int(input("n="))
    return n
def giaithua(n):
    if n==0:
        return 1
    elif n<0:
        return False
    else:
        return n*giaithua(n-1)
def inkq(n,X):
    print(n,"!=",X,sep="")
n=nhap()
X=giaithua(n)
inkq(n,X)