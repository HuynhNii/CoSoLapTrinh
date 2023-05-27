x=int(input())
k=int(input())
n=int(input())
L=[]
"""def delete(L, x):
    i=0
    while i<len(L):
        if L[i]==x:
            del L[i]
        else:
            i+=1
L = delete(L, x)
print(L)"""
def delete(L, x):
    i = 0
    while i < len(L):
        if L[i] == x:
            del L[i]
        else:
            i += 1

x = int(input("x: "))
k = int(input("k: "))

n = int(input("n: "))
L = []
for i in range(n):
    L.append(int(input("Nhập số nguyên : ")))

delete(L, x)

print(L)
