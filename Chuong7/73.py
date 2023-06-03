import re

def kiem_tra_mat_khau(mat_khau):
    if len(mat_khau) < 6 or len(mat_khau) > 17:
        return False
    if not re.search(r"[a-z]", mat_khau):
        return False
    if not re.search(r"[A-Z]", mat_khau):
        return False
    if not re.search(r"[0-9]", mat_khau):
        return False
    if not re.search(r"[$#@]", mat_khau):
        return False
    return True
mat_khau = input()
if kiem_tra_mat_khau(mat_khau):
    print(True)
else:
    print(False)
