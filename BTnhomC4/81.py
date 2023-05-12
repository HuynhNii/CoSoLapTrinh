import math
def hypotenuse(a,b):
    return math.sqrt(a**2 + b**2)
a = float(input("a="))
b = float(input("b="))
c = hypotenuse(a,b)
print("c="+str(c))