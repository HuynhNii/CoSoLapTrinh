def chamhoi(danhsach):
    if sorted(danhsach)==danhsach:
        return True
    elif sorted(danhsach,key=float,reverse=True)==danhsach:
        return True
    return False
def main():
    danhsach=[]
    b=False
    while not b:
        number = input('Nhap vao danh sach: ')
        if number!='':
            danhsach+=[number]
        else:
            b=True
    print(chamhoi(danhsach))
 
if __name__ == '__main__':
    main()