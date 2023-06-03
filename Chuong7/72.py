'''m=input()
n=m.split()
l=[]
for i in range(len(n)):
    if i==0:
        l.append(n[0].title())
    else:
        l.append(n[i].lower())
s=[".",",",":",";"]
h=l.copy().copy()
for i in range (len((l))):
    if l[i] in s:
        h[i-1] = h[i-1]+h[i]
        del (h[i])
print(*h)'''
def clean_string(input_string):
    # Xóa khoảng trắng ở đầu và cuối chuỗi
    cleaned_string = input_string.strip()

    # Chuyển chữ cái đầu tiên thành chữ hoa
    cleaned_string = cleaned_string.capitalize()

    # Xóa khoảng trắng trước dấu câu
    punctuation_marks = [",", ";", ":", "."]
    for mark in punctuation_marks:
        cleaned_string = cleaned_string.replace(" " + mark, mark)

    # Xóa khoảng trắng dư thừa giữa các từ
    cleaned_string = " ".join(cleaned_string.split())

    # Thêm khoảng trắng vào trước dấu câu nếu cần
    for mark in punctuation_marks:
        cleaned_string = cleaned_string.replace(mark, " " + mark)

    return cleaned_string

# Nhập chuỗi từ người dùng
input_string = input()

# Làm sạch chuỗi ký tự
cleaned_string = clean_string(input_string)

# In nội dung chuỗi sau khi xử lý
print("Chuỗi sau khi xử lý:", cleaned_string)