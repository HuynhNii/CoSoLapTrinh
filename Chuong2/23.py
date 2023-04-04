import math
print("Nhap hai canh ke cua tam giac vuong:")
a=int(input())
b=int(input())
c=(math.sqrt(a**2+b**2))
d=round(c, 2)
print("Canh ke thu nhat la: " + str(a)+", canh ke thu hai: " + str(b)+", co canh huyen = " + str(d))