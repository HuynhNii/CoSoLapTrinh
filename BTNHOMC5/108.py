N=[]
Z=[]
P=[]
while True:
    n=input("")
    if n==" ":
        break
    n = int(n)
    if n<0:
        N.append(n)
    elif n==0:
        Z.append(n)
    elif n>0:
        P.append(n)
        
Kq=[]
Kq.extend(N)
Kq.extend(Z)
Kq.extend(P)  

for n in Kq:
    print(n)     
        
        