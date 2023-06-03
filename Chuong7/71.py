def dem_ky_tu(chuoi):
    chu_hoa = 0
    chu_thuong = 0
    chu_so = 0
    ky_tu_khac = 0

    for ky_tu in chuoi:
        if ky_tu.isupper():
            chu_hoa += 1
        elif ky_tu.islower():
            chu_thuong += 1
        elif ky_tu.isdigit():
            chu_so += 1
        else:
            ky_tu_khac += 1

    print("In hoa:",chu_hoa)
    print("In thuong:",chu_thuong)
    print("Chu so:",chu_so)
    print("Khac:",ky_tu_khac)

chuoi = input()
dem_ky_tu(chuoi)