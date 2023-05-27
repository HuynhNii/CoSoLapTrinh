n = int(input("n="))
L = []
for i in range(n):
    x=int(input())
    L=L+[x]
M =[]
for x in L:
    if x not in M:
        M=M+[x]
print(M)