n=int(input())
m=int(input())
S=0
if n<=m and n>=0 and m>=0:
    for i in range(n,m):
        S=S+i
print(S)