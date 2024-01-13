import string
lower = string.ascii_lowercase
plain_text = input("Enter a string: ").lower()

shift = int(input("Enter a shift: ")) %26
cipher_text = []
for char in plain_text:
    if char not in lower:
        cipher_text.append(char)
    else:
        index = lower.index(char)
        new_index = (index + shift)%26
        cipher_text.append(lower[new_index])

print("".join(cipher_text))