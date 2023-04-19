so_ngay_nghi = int(input(""))
if so_ngay_nghi == 0:
    xep_loai = "Xếp loại A"
elif so_ngay_nghi < 2:
    xep_loai = "Xếp loại B"
elif so_ngay_nghi < 4:
    xep_loai = "Xep loai C"
else:
    xep_loai = "Xếp loại D"
print(xep_loai)