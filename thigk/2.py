n=int(input())
L=[]
for i in range (n):
    n=int(input())
    L=L+[n]
for i in range(len(L)):
    x=max(L)
    y=min(L)
print(x)
print(y)