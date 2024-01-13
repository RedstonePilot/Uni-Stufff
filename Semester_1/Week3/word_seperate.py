import string
upper = string.ascii_uppercase
camel_case = input("Etner a string: ")

new_list = []
buffer = []
for char in camel_case:
    if char in upper:
        new_list.append("".join(buffer))
        buffer = []
        buffer.append(char)
    else:
        buffer.append(char)
    
new_list.append("".join(buffer))
new_list.pop(0)
print(new_list)