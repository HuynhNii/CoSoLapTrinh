giacoban=4.00
them140m=0.25
def quangduong(x):
    gia=giacoban+(x*1000//140)*them140m
    return gia
x=float(input("Nhap quang duong di duoc (km): "))
giave=quangduong(x)
print("Tong gia ve la: $"+str(giave))