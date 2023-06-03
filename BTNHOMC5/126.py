def dsachcon(lst):
    result = [[]]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            result.append(lst[i:j])
    return result

if __name__ == '__main__':
    lst = []
    n = int(input("Nhập số phần tử của list: "))
    for i in range(n):
        x = input()
        lst.append(x)
        
    print("List đã nhập là:", lst)
    print("Các danh sách con của list là:", dsachcon(lst))

