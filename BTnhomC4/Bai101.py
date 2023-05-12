def nhap():
    a=int(input("Nhap so thu nhat: "))
    b=int(input("Nhap so thu hai: "))
    return a,b
def rutgon(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    k=a
    return k
def inkq():
    m=a//k
    n=b//k
    print(m,n)

a,b=nhap()
k=rutgon(a,b)
inkq()