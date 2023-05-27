w=int(input())
h=int(input())
mt=(input())
k=input()

if mt=='A':
    nt=0/100
if mt=='B':
    nt=10/100
if mt=='C':
    nt=20/100
if mt=='D':
    nt=29/100
if mt=='E':
    nt=35/100
else:
    nt=0

if w<=1000 and h<30000:
    if k=='y':
        n=10
    else:
        n=0
    t=w*h*nt
    S=w*h*(1+nt)+n
    print(round(S,2))