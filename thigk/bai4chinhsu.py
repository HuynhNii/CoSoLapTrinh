n = int(input())
S = 0
count = 0

if 0 <= n <= 1000000:
    for i in range(1, n):
        if i % 3 == 0 and i % 5 != 0:
            S += 1
    
    for i in range(1, n):
        if i % 3 == 0 and i % 5 != 0:
            if count == S:
                break
            if count < S:
                if count == S-1:
                    print(i)
                else:
                    print(i, end=', ')
                count += 1
                
print()
print(S)
print(count)