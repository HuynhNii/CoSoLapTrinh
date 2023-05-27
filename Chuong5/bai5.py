x=int(input())
y=int(input())
n=int(input())
L=[]
dem=0
while dem<n:
    a=int(input(""))
    L=L+[a]
    dem+=1
y=int(input())
def replace(L, x, y):
    for i in range(len(L)):
        if (x==L[i]):
            L[i]=y
    return L

L=replace(L, x, y)
print(L)