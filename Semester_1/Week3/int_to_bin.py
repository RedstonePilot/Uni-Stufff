integer = int(input(("Enter an int:")))
binary = []
remainder  = 1
while integer:
    remainder = integer % 2
    integer = integer // 2
    binary.append(str(remainder))

print("".join(binary)[::-1])