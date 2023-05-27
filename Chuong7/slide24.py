def NhapSo(st):
    while True:
        x=input("x=")
        if x.isnumeric():
            return int(x)
        else:
            print("Khong hop le!!!")
a=NhapSo("a=")
b=NhapSo("b=")
print("a+b=",a+b)