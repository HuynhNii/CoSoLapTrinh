A = []
for i in range(10):
    x=int(input())
    A=A+[x]
B = A.copy()
for i in range(0, len(A)-1, 2):
    B[i] = A[i+1]
    B[i+1] = A[i]
print(B)