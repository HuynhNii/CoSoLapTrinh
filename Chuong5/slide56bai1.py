x=int(input())
k=int(input())
n=int(input())
L=[]
def add(L,x,k):
    if k>len(L):
        L.append(x)
    else:
        L.insert(k, x)
for i in range(n):
    nhap=int(input())
    L.append(nhap)
add(L, x, k)
print(L)

