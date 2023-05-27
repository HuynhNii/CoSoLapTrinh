def search(L, x):
    for i in range(len(L)):
        if L[i] == x:
            return i
    return None
x = int(input(""))
n = int(input(""))

L = []
for i in range(n):
    num = int(input())
    L.append(num)

index = search(L, x)
if index != None:
    print(index)
else:
    print('None')