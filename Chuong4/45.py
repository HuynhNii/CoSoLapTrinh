print("Nhap day so:")
def LaSoNguyenTo(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def SoHopLe(x):
    return x <= 1
def NhapVaDem():
    dem = 0
    while True:
        x = int(input())
        if SoHopLe(x):
          break
        if LaSoNguyenTo(x):
            dem += 1
    return dem
def InKQ(kq):
    print("Co", kq, "so nguyen to")
kq = NhapVaDem()
InKQ(kq)