i=0
a=0
g=0
c=0
f=0
while True:
    x=float(input('x='))
    y=float(input('y='))
    if x=='':
        break
    d=x*y
    e=x**2
    f+=e
    c+=d
    i+=1
    a+=x
    g+=y
m=(c-(a*g)/i)/(f-(a**2)/i)
b=g/i-m*(a/i)
pt=m*x+b
print(pt)