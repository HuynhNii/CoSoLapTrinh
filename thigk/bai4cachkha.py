n = int(input())
S = 0
p = 1  

if n >= 0 and n <= 1000000:
    for i in range(1, n):
        if i % 3 == 0 and i % 5 != 0:
            S += 1
            
    i = 1
    while S > 0:
        if i % 3 == 0 and i % 5 != 0:
            if S == 1:
                print(i)
            else:
                print(i, end=', ')
            S -= 1
        i += 1

    print()
    print(S)
    print(i)  