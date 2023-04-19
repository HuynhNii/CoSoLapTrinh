a=int(input("Tieu thu="))
if (a<=100):
    print("Phai tra=",round((a*550)*1.1,1),sep="")
elif a<=150:
    print("Phai tra=",round((100*550+(a-100)*750)*1.1,1),sep="")
elif a<=200:
    print("Phai tra=",round((100*550+50*750+(a-150)*950)*1.1,1),sep="")
else:
    print("Phai tra=",round((100*550+50*750*50*950+(a-200)*1350)*1.1,1),sep="")