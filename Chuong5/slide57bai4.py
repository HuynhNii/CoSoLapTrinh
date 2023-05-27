x=int(input())
k=int(input())
n=int(input())
L=[]
def count(L):
    return len(L)
for i in range(n):
    num = int(input("Nhập số nguyên: "))
    L.append(num)

print(count(L))