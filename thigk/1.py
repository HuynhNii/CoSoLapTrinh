L=[]
A=[]
while True:
    n=str(input())
    if n=='':
        break
    else:
        L+=[n]
for i in L:
    if i not in A:
        A+=[i]
for i in A:
    print(i)