def nhap():
    n=int(input('So luong: '))
    a=str(input('Don vi: '))
    return n,a
def quydoi(n,a):
    if a=='muong ca phe':
        x=n//3
        if x>=16:
            if x//16!=0:
                k=x//16
                l=x-(k*16)
                m=n-(l*3)-(k*16*3)
                if l==0:
                    print(k,'coc,',m,'muong ca phe.')
                if m==0:
                    print(k,'coc,',l,'muong canh.')
                if l==0 and m==0:
                    print(k,'coc.')
                if l!=0 and m!=0:
                    print(k,'coc,',l,'muong canh,',m,'muong ca phe.')
        elif x<16:
            p=n-x*3
            if p==0:
                print(x,'muong canh.')
            else:
                print(x,'muong canh,',p,'muong ca phe.')
    if a=='muong canh':
        k=n//16
        l=n-k*16
        if k!=0:
            print(k,'coc',l,'muong canh')
        else:
            print(n,'muong canh')
        
n,a=nhap()
quydoi(n,a)        