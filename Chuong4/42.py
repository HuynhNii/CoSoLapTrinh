def nhap():
    n = int(input("n="))
    return n
def inkq(n):
    for i in range(2,n+1,2):
        print(i,end=" ")
while True:
    n=nhap()
    inkq(n)
    ch= input("\nTiep tuc khong?")
    if ch== 'K' or ch=='k':
        break