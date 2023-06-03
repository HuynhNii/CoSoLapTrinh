n = int(input())
L = []
for i in range(n):
    a=int(input())
    L=L+[a]
x=0
y=0
z=0
for i in L:
    if i > 0:
        x+=1
    if i % 2==0:
        y+=i
        z+=1
print(x)
if  y > 0:
    print(y/z)
else:
    print("TBC=0")