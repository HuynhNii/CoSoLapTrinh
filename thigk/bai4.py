n=int(input())
S=0
p=1
if n>=0 and n<=1000000:
    for i in range (1,n):
        if i%3==0 and i%5!=0:
            S=S+1
    for i in range(1,n):
        if i%3==0 and i%5!=0 and p==S:
            print(i)
            p=p+1
        elif i%3==0 and i%5!=0 and p<S:
            print(i,end=', ')
        
        
print()
print (S)
print(i)