st='''--Người---đâu-gặp---gỡ-làm-chi---
Trăm----năm-biết-có---duyên---gì--hay--không.
Ngổn-ngang---trăm-mối---bên---lòng----
----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.'''
def XuLyDong(xau):
    L=xau.split("-")    
    while "" in L:    
        L.remove("")
    return " ".join(L) 
def TienXuLy(st):
    L=st.split("\n")    
    for dong in L:
        print(XuLyDong(dong))   
TienXuLy(st)