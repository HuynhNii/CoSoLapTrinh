x=int(input())
n=int(input())

L=[]
dem=0
while dem<n:
    a=int(input(""))
    L=L+[a]
    dem+=1
def search(L,x):
        for i in range(len(L)):
            if x==L[i]:
                return i
        return None

k=search(L,x)

print(k)
    