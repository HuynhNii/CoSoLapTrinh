def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b

while True:
    a = float(input("a="))
    b = float(input("b="))
    operator = input("Toan tu: ")

    result = calculate(a, b, operator)
    print("Kết quả:", result)

    end = input("Tiep tuc: ")
    if end.lower() == 't':
        break