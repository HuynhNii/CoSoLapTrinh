def isInteger(s):
    s = s.strip()
    if len(s) == 0:  
        return False
    if s[0] in ["+", "-"]:  
        if len(s) == 1:  
            return False
        return s[1:].isdigit()  
    return s.isdigit()  

if __name__ == "__main__":
    s = input("Nhập một chuỗi: ")
    if isInteger(s):
        print("Chuỗi đại diện cho một số nguyên hợp lệ.")
    else:
        print("Chuỗi không đại diện cho một số nguyên hợp lệ.")