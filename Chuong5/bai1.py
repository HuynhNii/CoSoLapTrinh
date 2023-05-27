x=int(input(""))
k=int(input(""))
n=int(input(""))

L=[]
dem=0
while dem<n:
    a=int(input(""))
    L=L+[a]
    dem+=1
def add(L,x,k):
  L=L[:k] + [x] + L[k:]
  return L
L=add(L,x,k)

print(L)