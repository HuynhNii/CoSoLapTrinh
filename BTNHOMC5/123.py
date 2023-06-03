precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

operators = []
postfix = []

expression = input("Enter an infix expression: ")
tokens = expression.split()

for token in tokens:
    if token.isdigit():
        postfix.append(token)
    elif token in "+-*/^":
        while operators and operators[-1] != "(" and precedence[token] <= precedence.get(operators[-1], 0):
            postfix.append(operators.pop())
        operators.append(token)
    elif token == "(":
        operators.append(token)
    elif token == ")":
        while operators[-1] != "(":
            postfix.append(operators.pop())
        operators.pop()

while operators:
    postfix.append(operators.pop())

print("The equivalent postfix expression is:")
print(" ".join(postfix))
