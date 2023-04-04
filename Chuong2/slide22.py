gia_niem_yet = float(input("Nhap Gia niem yet: "))
chiet_khau = float(input("Nhap Chiet khau: "))
VAT= (gia_niem_yet - chiet_khau)*0.01
gia_ban = gia_niem_yet - chiet_khau + VAT
print("Gia ban:", gia_ban)