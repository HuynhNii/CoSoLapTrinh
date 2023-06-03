def snt(gh):
    H = [True] * gh
    H[0] = H[1] = False
    for i in range(2, int(gh ** 0.5) + 1):
        if H[i]:
            for j in range(i**2, gh, i):
                H[j] = False
    return [i for i in range(2, gh) if H[i]]
gh = int(input("Nhập giới hạn: "))
print("Các số nguyên tố nhỏ hơn", gh, "là:")
print(snt(gh))