def trungvi(a,b,c):
    tv=None
    if a<=b<=c or a>=b>=c:
        tv=b
    elif a<=b<c or a>=b>=c:
        tv=c
    else:
        tv=a
    return tv
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
trungvi=trungvi(a,b,c)
print("gia tri trung vi cua "+str(a)+str(", ")+str(b)+str(", ")+str( c)+str(" la: ")+str(trungvi))