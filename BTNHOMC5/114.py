import random
def xo_so():
    so = []
    while len(so) < 6:
        so_moi = random.randint(1, 49)
        if so_moi not in so:
            so.append(so_moi)
    so.sort()
    return so
ket_qua =xo_so()
print( ket_qua)