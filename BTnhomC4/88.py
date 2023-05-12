def Nhap(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True

a = float(input(""))
b = float(input(""))
c = float(input(""))

if Nhap(a, b, c):
    print("Các độ dài này có thể tạo thành một tam giác.")
else:
    print("Các độ dài này không thể tạo thành một tam giác.")