a=input().split(",")
c=[]
for i in a:
    if i not in c:
        c.append(i)
c.sort()
e=",".join(c)
print(e)