def Thaythe(n, x):
    new_n=[n[i] for i in range(len(n))]
    for i in range(len(new_n)):
        if new_n[i]==5:
            new_n[i]=x
    print(*new_n, sep=", ")
n = []
for i in range(10):
    So = int(input())
    n+=[So]  
x = int(input("x="))
Thaythe(n, x)
