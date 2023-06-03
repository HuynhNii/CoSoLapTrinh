def la_so_hoan_hao(num):
    tong_uoc = sum([i for i in range(1, num) if num % i == 0])

    if tong_uoc == num:
        return True
    else:
        return False

for num in range(1, 10001):
    if la_so_hoan_hao(num):
        print(num)