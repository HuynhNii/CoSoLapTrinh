import math

def nhap():
    print("Nhap 3 so nguyen:")
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    return a,b,c

def giaipt(a,b,c):
     d= b**2-4*a*c
     
     if d<0:
        print("Phuong trinh vo nghiem")
     elif d==0:
        x=-b/(2*a)
        print("Phuong trinh co nghiem kep")
        print("x1=x2=",x,sep="")
     else:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        print("Phuong trinh co hai nghiem")
        print("x1=",x1,sep="")
        print("x2=",x2,sep="")

def inkq(x1,x2):
    print("Phuong trinh co hai nghiem")
    print("x1=",x1)
    print("x2=",x2)

a,b,c = nhap()
giaipt(a,b,c)