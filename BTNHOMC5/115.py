def Nhap():
    dong=str(input('Nhap dong van ban: '))
    return dong
def dich(dong):
    nguyenam = ('aeiou')
    a=dong.split(" ")
    latin = ""
    for i in a:
        if i[0] in nguyenam:
            latin += i + "way" + " "
        else:
            b=0
            for letter in i:
                if letter not in nguyenam: 
                    b+=1
                    continue
                else: 
                    break
            latin += i[b:] + i[:b] + "ay" + " "
    return latin
def inkq(kq):
    print('Dich sang tieng Latin la: ',kq)

dong=Nhap()
kq=dich(dong)
inkq(kq)