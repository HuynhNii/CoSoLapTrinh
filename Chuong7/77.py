n=str(input())
c=[]
a=0
for i in range (len(n)):
    if n[i]==":":
        a=i+1
c.append(n[a+1:])
print(*c)