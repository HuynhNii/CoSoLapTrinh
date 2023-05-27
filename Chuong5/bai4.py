n=int(input())

L=[]
dem=0
while dem<n:
    a=int(input(""))
    L=L+[a]
    dem+=1

def count(L):
        dem=0
        for x in L:
            dem=dem+1
        return dem


soluong=count(L)

print(soluong)
