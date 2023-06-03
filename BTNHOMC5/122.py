def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isspace():
            i += 1
        elif expression[i] in "+-*/^()":
            tokens.append(expression[i])
            i += 1
        else:
            start = i
            while i < len(expression) and not expression[i].isspace() and expression[i] not in "+-*/^()":
                i += 1
            tokens.append(expression[start:i])
    return tokens

if __name__ == '__main__':
    expression = input("Nhập biểu thức toán học: ")
    tokens = tokenize(expression)
    print(tokens)
