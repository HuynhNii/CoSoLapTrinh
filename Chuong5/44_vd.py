L = []
while True:
    st=input()
    if st=="":
        break
    elif st not in L:
        L=L+[st]
print(L)