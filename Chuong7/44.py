while True:    
    str=input()
    if len(str)<8 or str.islower() or str.isupper() or str.isnumeric() or str.isalpha():
        print("Khong hop le")
    else:
        print("Hop le")
        break
