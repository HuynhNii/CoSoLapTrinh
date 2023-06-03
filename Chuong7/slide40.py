m=[]    
s=[]    
for i in range(4):  
    a=input("mon " + str(i+1) + ":")
    b=input("So luong:")
    m.append(a)
    s.append(b)

for i in range(4):
    print(m[i].ljust(20,"."),end="")
    print(s[i].rjust(6," "))