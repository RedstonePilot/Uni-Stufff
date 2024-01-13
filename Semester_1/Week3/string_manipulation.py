string = input("Enter a string: ").lower()
new_string = []
next_cap = True
for char in string:
    if char == " ":
        next_cap = True
    else:
        if next_cap == True:
            new_string.append(char.upper())
        else:
            new_string.append(char)
        next_cap = False

print("".join(new_string))
