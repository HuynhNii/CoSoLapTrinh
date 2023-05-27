x=int(input())
n=int(input())

L=[]
dem=0
while dem<n:
    a=int(input(""))
    L=L+[a]
    dem+=1

def delete(L,x):
    M=[]
    for z in L:
        if x!=z:
            M.append(z)
    return M

L=delete(L,x)

print(L)