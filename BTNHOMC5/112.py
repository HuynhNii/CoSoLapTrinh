def tinh_gia_tri_trung_binh(so):
    
    if len(so) == 0:
        return 0
    
    tong = sum(so)
    gia_tri_trung_binh = tong / len(so)
    return gia_tri_trung_binh

so = []
gia_tri_trung_binh = []

while True:
    nhap_nguoi_dung = input()
    
    if nhap_nguoi_dung == "":
        break
    
    so_con = float(nhap_nguoi_dung)
    so.append(so_con)
    
    gia_tri_tb = tinh_gia_tri_trung_binh(so)
    gia_tri_trung_binh.append(gia_tri_tb)

print("Cac gia tri trung binh:")
for i, gia_tri_tb in enumerate(gia_tri_trung_binh):
    print(i+1, gia_tri_tb)