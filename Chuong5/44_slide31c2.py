def Nhap():
    L=[]
    for i in range(10):
        z=int(input())
        L=L+[z]
       
    x=int(input("x="))
    return x,L


def InKQ(L):
    for x in L:
        print(x,end=", ")
   
def CauA(x,L):
    for i in range(len(L)):
        if L[i]==5:
            L[i]=x
    InKQ(L)


def CauB(x,L):
    i=0
    while i<len(L):
        if L[i]==x:
            del(L[i])
        else:
            i=i+1
    InKQ(L)
   
x,L=Nhap()
CauA(x,L)
CauB(x,L)

