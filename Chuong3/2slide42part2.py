n = int(input("n="))
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print(n, "la SNT")
else:
    print(n, "khong la SNT")