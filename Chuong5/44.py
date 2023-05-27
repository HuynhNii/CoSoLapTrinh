L=[1,2,3,5,5,5,8,9,5]
def RemoveAll(x,L):
    while x in L:
        L.remove(x)
    return L
L=RemoveAll(5,L)
print(L)