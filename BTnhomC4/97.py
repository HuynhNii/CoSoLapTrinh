import random
def dodaimatkhau():
    dodaimatkhau = random.randint(7, 10)
    matkhau = ""
    for i in range(dodaimatkhau):
        matkhau += chr(random.randint(33, 126))
    return matkhau

def chonmatkhau(matkhau):
    if len(matkhau) < 8:
        return False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    for char in matkhau:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    return has_uppercase and has_lowercase and has_digit

def matkhaumanh():
    a = 0
    while True:
        matkhau = dodaimatkhau()
        a += 1
        if chonmatkhau(matkhau):
            print("Da tao pass sau:", a,'lan thu can thiet')
            break
        return matkhau
print(matkhaumanh())