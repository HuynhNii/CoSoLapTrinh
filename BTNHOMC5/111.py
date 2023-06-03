import string

def xoa_dau_cau(text):
    dau_cau = string.punctuation.replace("'", "")
    tu = text.split()
    tu_da_xoa = []
    
    for tu in tu:
        tu_da_xoa = ""
        while len(tu) > 0 and tu[0] in dau_cau:
            tu = tu[1:]
        while len(tu) > 0 and tu[-1] in dau_cau:
            tu = tu[:-1]
        if tu:
            tu_da_xoa.append(tu)
    return tu_da_xoa

van_ban = input()
van_ban_da_xoa = xoa_dau_cau(van_ban)
print(van_ban_da_xoa)