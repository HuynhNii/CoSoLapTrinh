# L=[]                      C1
# LS=set()
# while True:
#     x=input("")
#     if x==" ":
#         break
#     if x not in LS:
#         L.append(x)
#         LS.add(x)
# for x in L:
#     print(x)

L=[]
while True:
    n=input("")
    if n==" ":
        break
    if n not in L:
        L.add(n)
for n in L:
    print(n)