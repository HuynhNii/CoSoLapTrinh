def Input():
    n = int(input("n="))
    L = []
    for i in range(n):
        t=int(input())
        L=L+[t]
    return L
def Search(L):
    max= L[0]
    min= L[0]
    for i in L:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min
def Output(max, min):
    print(max, min)
L = Input()
max, min = Search(L)
Output(max, min)