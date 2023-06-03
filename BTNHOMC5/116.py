def Nhap():
    dong=str(input('Nhap dong van ban: '))
    return dong
def dich(dong):
    nguyenam = ('AEIOUaeiou')
    a=dong.split(' ')
    latin = ''
    for i in a:
        if i[0] in nguyenam:
            latin += i + 'way '
            if i[0].isupper():
                latin=latin[0].upper() + latin[1:]
        else:
            b=0
            for chu in i:
                if chu not in nguyenam: 
                    b+=1
                    continue
                else:           
                    if i[0].isupper():
                        latin+=i[b].upper() +i[b+1:]+ i[:b].lower()+ 'ay '
                    else:    
                        latin += i[b:] + i[:b] + 'ay '
                break       
    return latin
def inkq(kq):
    print('Dich sang tieng Latin la: ',kq)

dong=Nhap()
kq=dich(dong)
inkq(kq)