def chuyenthanhcoso10(so,coso):
    stp=0
    p=0
    while so>0:
        digit=so%10
        if digit>=coso:
            raise ValueError('Invalid digit for base')
        stp+=digit*(coso**p)
        so//=10
        p+=1
    return stp
def chuyenthanhbatky(stp,coso):
    so=0
    p=0
    while stp>0:
        digit=stp%coso
        so+=digit*(10**p)
        stp//=coso
        p+=1
    return so
def chuyendoi(so,tucoso,thanhcoso):
    stp=chuyenthanhcoso10(so,tucoso)
    result=chuyenthanhbatky(stp,thanhcoso)
    return result
if __name__ == '__main__':
    try:
        so=int(input('Nhap 1 so: '))
        tucoso=int(input('Nhap vao co so cua so do: '))
        thanhcoso=int(input('Nhap vao co so muon chuyen thanh: '))
        if tucoso<2 or tucoso>16 or thanhcoso<2 or thanhcoso>16:
            raise ValueError('Invalid base')
        result=chuyendoi(so,tucoso,thanhcoso)
        print(so,'trong co so',tucoso,'la',result,'trong co so',thanhcoso)
    except ValueError as e:
        print(e)