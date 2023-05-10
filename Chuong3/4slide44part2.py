while True:
    a=float(input("a="))
    b=float(input("b="))
    c=input("Toan tu: ")
    if c=="+":
        print(a,"+",b,"=",a+b,sep="")
    elif c=="-":
        print(a,"-",b,"=",a-b,sep="")
    elif c=="*":
        print(a,"*",b,"=",a*b,sep="")
    elif c=="/":
        if b==0:
            print("khong hop le")
        else:
            print(a,"/",b,a/b,sep="")
    d=input("Tiep tuc: ")
    if d=="x":
        continue
    elif d=="t ":
        break