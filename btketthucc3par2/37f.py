while True:
    n=int(input())
    if n<=0:
        break
    elif n==0:
        print("0!=1")
    else:
        t=1
        for i in range(1,n+1):
            t=t*i
        print(t)