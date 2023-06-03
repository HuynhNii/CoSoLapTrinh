def remove_outliers(L, n):
    L = sorted(L)[n:-n]
    return L

if __name__ == '__main__':
    L = input("Nhập danh sách các giá trị, cách nhau bởi dấu phẩy: ").split(',')
    L = [float(x.strip()) for x in L]
    if len(L) < 4:
        print("Lỗi: cần ít nhất 4 giá trị để loại bỏ cực đoan")
    else:
        new_L = remove_outliers(L, 2)
        print("Danh sách đã loại bỏ giá trị cực đoan:", new_L)
        print("Danh sách ban đầu:", L)