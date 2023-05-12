def hex2int(chuyenthanhchu):
    try:
        return int(chuyenthanhchu, 16)
    except ValueError:
        print("Lỗi: chuỗi không hợp lệ!")
        return None

def int2hex(chusothaplucphan):
    if chusothaplucphan < 0 or chusothaplucphan > 15:
        print("Lỗi: số không hợp lệ!")
        return None
    else:
        return hex(chusothaplucphan)[2:].upper()
print(hex2int(input()))

