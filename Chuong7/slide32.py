def checkstring(st1,st2,st3):
    return st1.startswith(st2) or st1.endswith(st3)

st1=input()
st2=input()
st3=input()
print(checkstring(st1,st2,st3))