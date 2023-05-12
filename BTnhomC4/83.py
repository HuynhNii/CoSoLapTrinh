def soluong(x):
    p1=10.95
    p2=2.95
    if x==1:
        p=p1
    elif x>1:
        p=p1+((x-1)*2.95)
    else:
        p=0
    return p
x=int(input("So luong mat hang duoc mua: "))
phivc=soluong(x)
print("Phi va chuyen la: $"+str(phivc))