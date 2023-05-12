import random
def passrandom():
    length = random.randint(7, 10)
    password = ""
    for i in range(length):
        password += chr(random.randint(33, 126))
    return password
print(passrandom())