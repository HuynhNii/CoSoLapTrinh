number=[]
for i in range(10):
    a=int(input())
    number=number+[a]
x=int(input('x='))
def CauA():
    for j in range(len(number)):
        if number[j]==5:
            number[j]=x
    for h in number:
        print(h,end=', ')
    return number
def CauB(number):
    v=0
    while v<len(number):
        if number[v]==x:
            del(number[v])
        else:v+=1
    l=0
    while l<len(number):
        print(number[l],end=', ')
        l+=1
print('Cau a:')
number=CauA()
print()
print('Cau b:')
CauB(number)