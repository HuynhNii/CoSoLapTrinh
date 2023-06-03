def convert_strings(input_string):
    lowercase_string = input_string.lower()  
    uppercase_string = input_string.upper()  

    return lowercase_string, uppercase_string

input_string = input()

result1, result2 = convert_strings(input_string)

print(result1)
print(result2)