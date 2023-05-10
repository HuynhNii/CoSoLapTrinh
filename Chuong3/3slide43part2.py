n=int(input("n="))
for i in range(1,10000):
    if n<10:
        print(n, "co 1 chu so")
        break
    elif 10<=n<100:
        print(n, "co 2 chu so")
        break
    elif 100<=n<1000:
        print(n, "co 3 chu so")
        break
    else:
        print(n, "co 4 chu so")
        break