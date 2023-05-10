import random
while True:
    n=int(input("Human: "))
    if n==0:
        break
    m=random.randint(1,3)
    print("Computer:",m)
    if n==m:
        print("Result: Draw!")
    elif m==1 and n==2:
        print("Result: Computer Win!")
        continue
    elif m==2 and n==3:
        print("Result: Computer Win!")
    elif m==3 and n==1:
        print("Result: Computer Win!")
        continue
    elif n==0:
        break
    else:
        print("Result: Human Win!")
        continue