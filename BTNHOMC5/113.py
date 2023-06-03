def danh_sach(a):
    if len(a) == 1:
        return a[0]
    elif len(a) == 2:
        return ' and '.join(a)
    else:
        return ' , '.join(a[:-1]) +',and '+ a[-1]
a = []
while True:
    b = input()
    if b == '':
        break
    a=a+[b]
ds = danh_sach(a)
print(ds)
