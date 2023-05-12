def priority(n):
    if n == "+" or n == "-":
        return 1
    elif n == "*" or n == "/":
        return 2
    elif n == "^":
        return 3
    else:
        return -1

if __name__ == "__main__":
    n = input("Nhập một toán tử (+, -, *, /, ^): ")
    p = priority(n)
    if p != -1:
        print(f"Ưu tiên của toán tử {n} là {p}.")
    else:
        print("Đầu vào không phải là toán tử hợp lệ.")