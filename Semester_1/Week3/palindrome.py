import string as strl
lower = strl.ascii_lowercase
string = input("Enter a string: ").lower()
for char in string:
    if char not in lower:
        string = string.replace(char,"")


flipped = string[::-1]

if flipped == string:
    print("is a palindrome")
else:
    print("Not a Palindrome")

