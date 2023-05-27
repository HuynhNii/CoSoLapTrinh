n = int(input("n="))
A = []
for i in range(n):
    x=int(input())
    A=A+[x]
tong=0
for i in range(1, len(A), 2):
    tong+= A[i]
print("Tong=",tong,sep="")