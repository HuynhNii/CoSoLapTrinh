def nhap():
    thang=int(input('Thang: '))
    nam=int(input('Nam: '))
    return thang, nam
def ngay(thang,nam):
    if nam%4==0:
        if thang==2:
            print('Thang',thang,'nam',nam,'co 29 ngay')
        elif thang==4 or thang==6 or thang==9 or thang==11:
            print('Thang',thang,'nam',nam,'co 30 ngay')
        else:
            print('Thang',thang,'nam',nam,'co 31 ngay')
    else:
        if thang==2:
            print('Thang',thang,'nam',nam,'co 28 ngay')
        elif thang==4 or thang==6 or thang==9 or thang==11:
            print('Thang',thang,'nam',nam,'co 30 ngay')
        else:
            print('Thang',thang,'nam',nam,'co 31 ngay')

thang,nam=nhap()
ngay(thang,nam)