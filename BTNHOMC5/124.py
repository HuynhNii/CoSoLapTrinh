def kttoantu(c):
    return c in ['+', '-', '*', '/', '^']
def douutien(tt):
    if tt == '+' or tt == '-':
        return 1
    elif tt == '*' or tt == '/':
        return 2
    elif tt == '^':
        return 3
    else:
        return 0
def chuyendoi(i):
    H = []
    K = []
    for kt in i:
        if kt.isdigit():
            H.append(kt)
        elif kttoantu(kt):
            while len(K) > 0 and kttoantu(K[-1]) and douutien(kt) <= douutien(K[-1]):
                H.append(K.pop())
            K.append(kt)
        elif kt == '(':
            K.append(kt)
        elif kt == ')':
            while len(K) > 0 and K[-1] != '(':
                H.append(K.pop())
            if len(K) > 0 and K[-1] == '(':
                K.pop()
    while len(K) > 0:
        H.append(K.pop())
    return ''.join(H)
def danhgia(chuyendoi):
    K = []
    for kt in chuyendoi:
        if kt.isdigit():
            K.append(int(kt))
        elif kttoantu(kt):
            phai = K.pop()
            trai = K.pop()
            kq = None
            if kt == '+':
                kq = trai + phai
            elif kt == '-':
                kq = trai - phai
            elif kt == '*':
                kq = trai * phai
            elif kt == '/':
                kq = trai / phai
            elif kt == '^':
                kp = trai ** phai
            K.append(kq)
    return K.pop()
if __name__ == '__main__':
    i = input('Nhap bieu thuc trung to: ')
    chuyendoi = chuyendoi(i)
    print('Bieu thuc hau to:', chuyendoi)
    kq = danhgia(chuyendoi)
    print('Ket qua:', kq)
