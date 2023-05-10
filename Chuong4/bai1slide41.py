def is_prime(n):
    """Hàm kiểm tra xem một số nguyên n có phải là số nguyên tố hay không"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_integer():
    """Hàm nhập một số nguyên từ bàn phím và trả về giá trị đó"""
    while True:
        try:
            n = int(input("n="))
            if 2 <= n <= 100:
                return n
            else:
                print("Số bạn vừa nhập không nằm trong khoảng từ 2 đến 100.")
        except ValueError:
            print("Số bạn vừa nhập không hợp lệ.")


def main():
    """Hàm chính của chương trình"""
    n = get_integer()
    if is_prime(n):
        print(f"{n} la SNT")
    else:
        print(f"{n} khong la SNT")


if __name__ == '__main__':
    main()