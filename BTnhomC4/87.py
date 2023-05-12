def Chuoigiua(a,b):
    if len(a) >= b:
        return a  

    Trai = (b - len(a)) // 2
    Phai =b - len(a) - Trai
    return ' ' * Trai + a + ' ' * Phai

chuoi = "Xin chào, thế giới!"
chieu_rong = 10
chuoi_can = Chuoigiua(chuoi, chieu_rong)
print(chuoi_can)