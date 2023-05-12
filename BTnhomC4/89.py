def Chuoi(s):
    words = s.split()
    words[0] = words[0].Chuoi()
    for i in range(1, len(words)):
        if words[i-1][-1] in [".", "!", "?"]:
            words[i] = words[i].Chuoi()
        elif words[i] == "i" and (i == len(words)-1 or words[i+1] == "") and (i == 1 or words[i-1][-1] == " "):
            words[i] = "I"
    return " ".join(words)

s = input("Nhập một chuỗi: ")
result = Chuoi(s)
print(result)