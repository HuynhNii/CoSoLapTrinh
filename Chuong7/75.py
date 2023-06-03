l=(list(map(int,input().split())))
n=int(input())
def x(n):
   for i in range (len(l)):
       if n==l[i]:return True
   return False
if x(n)==False:print("0")
else:
    for i in range (len(l)):
        if n==l[i]:print(i+1)