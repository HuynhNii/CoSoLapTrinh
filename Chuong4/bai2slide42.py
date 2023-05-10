def is_prime(number):
    """Hàm kiểm tra xem một số nguyên có phải là số nguyên tố hay không"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def print_first_n_primes(n):
    """Hàm in ra n số nguyên tố đầu tiên"""
    count = 0
    i = 2
    while count < n:
        if is_prime(i):
            print(i, end=' ')
            count += 1
        i += 1


def main():
    """Hàm chính của chương trình"""
    n = int(input("n="))
    print_first_n_primes(n)


if __name__ == '__main__':
    main()