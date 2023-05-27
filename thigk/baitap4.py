n=int(input())
if n<10:
    print("0")
if n>=10:
    a=n%10
    b=n%100
    c=b//10
    print(a+c)