danhsach=[]
def CountRange(danhsach, minimum, maximum):
    dem = 0
    for i in danhsach:
        if minimum<=i<maximum:
            dem+=1
    return dem
x=int(input('So luong phan tu trong danh sach: '))
for j in range(x):
    so=input('Nhap danh sach: ')
    danhsach+=[so]
minimum=input('Gia tri toi thieu: ')
maximum=input('Gia tri toi da: ')
count = CountRange(danhsach, minimum, maximum)
print('So phan tu trong khoang:',count)