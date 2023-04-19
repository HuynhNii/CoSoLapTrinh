diem_toan = float(input())
diem_ly = float(input())
diem_hoa = float(input())

diem_tb = (diem_toan*2 + diem_ly*3 + diem_hoa)/6

if diem_tb < 3:
    xep_loai="Kém"
elif diem_tb < 5:
    xep_loai="Yếu"
elif diem_tb < 6:
    xep_loai="Trung bình"
elif diem_tb < 7:
    xep_loai="Trung bình Khá"
elif diem_tb < 8:
    xep_loai="Khá"
elif diem_tb < 9:
    xep_loai="Giỏi"
else:
    xep_loai="Xuất sắc"
print(""+str(xep_loai))