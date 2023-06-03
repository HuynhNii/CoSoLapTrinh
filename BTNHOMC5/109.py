def proper_divisors(n):
    L=[]
    for i in range(1,n+1):
        if n%i==0:
            L.append(i)
    return L
# if __name__=="__main__":
n=int(input("Nhập SND:"))
print("các ước số của",n,"là:",proper_divisors(n))