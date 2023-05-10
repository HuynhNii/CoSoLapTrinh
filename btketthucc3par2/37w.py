while True:
    n=int(input())
    if n<0:
        break
    elif n==0:
        print("0!=1")
    else:
        i=1
        t=1
        while i<=n:
            t=t*i
            i+=1
    print(t)