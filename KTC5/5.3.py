n = int(input("n="))
L = []
for i in range(n):
    x=int(input())
    L=L+[x]
a=0
b=0
c=0
for i in L:
    if i > 0:
        a+=1
    if i % 2==0:
        b+=i
        c+=1
print("SND=",a,sep="")
if  b> 0:
    print("TBC=", b/c,sep="")
else:
    print("TBC=0")