def ktra(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True
def Timso(n):
    so = n + 1
    while True:
        if ktra(so):
            return so
        else:
            so += 1

n = int(input('n='))
print("SNT dau tien lon hon", n, "la:", Timso(n))