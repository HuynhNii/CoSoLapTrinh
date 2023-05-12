import random
def biensoxe():
    if random.random() < 0.5:
        letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
        digits = ''.join(random.choices('0123456789', k=3))
        return f"{letters}{digits}"
    else:
        digits = ''.join(random.choices('0123456789', k=4))
        letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
        return f"{digits}{letters}"
print(biensoxe())