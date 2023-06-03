n=[]
a=[x for x in input().split(',')]
for i in a:
    a=int(i,2)
    if a%3==0:
        n.append(i)
print(*n,sep=',')