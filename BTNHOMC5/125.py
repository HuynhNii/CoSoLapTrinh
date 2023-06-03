def kiemtra(nho, lon):
    if not nho:
        return True
    for i in range(len(lon)):
        if lon[i] == nho[0]:
            if lon[i:i+len(nho)] == nho:
                return True
    return False
listlon = input("Nhập danh sách lớn hơn, các phần tử cách nhau bằng dấu phẩy: ").split(",")
listnho = input("Nhập danh sách nhỏ hơn, các phần tử cách nhau bằng dấu phẩy: ").split(",")
listlon = [int(i) for i in listlon]
listnho = [int(i) for i in listnho]
print(kiemtra(listnho, listlon))  
