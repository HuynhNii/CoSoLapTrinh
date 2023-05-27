def Input():
    n = int(input("n="))
    L = []
    for i in range(n):
        k=int(input())
        L=L+[k]
    x = int(input("x="))
    return L, x

def FirstAndLast(L):
    a = [L[0], L[-1]]
    print(a)
    return a
def Search(L,x):
    if x in L:
        print(True)
        return True
    else:
        print(False)
        return False
L, x = Input()
FirstAndLast(L)
Search(L,x)