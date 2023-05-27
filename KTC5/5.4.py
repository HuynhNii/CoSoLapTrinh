n = int(input("n="))
A = []
for i in range(n):
    x=int(input())
    A=A+[x]
B = A[::-1]
print(B)
B.sort()
print(B)