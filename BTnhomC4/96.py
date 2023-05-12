def matkhaumanh(password):
    if len(password) < 8:
        return False
    has_uppercase = False
    has_lowercase = False
    has_number = False
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_number = True
    return has_uppercase and has_lowercase and has_number
while True:
        password = input("Nhap pass: ")
        if matkhaumanh(password):
            print("Pass hop le")
            break
        else:
            print("Pass khong hop le\n Moi nhap lai")