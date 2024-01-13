grid = []
for _ in range(4):
    numbers = input("enter 4 digits (0..4) separated by a space: ")
    split_numbers = numbers.split(" ")
    grid.append(split_numbers)

for i in range(4):
    print("+-+-+-+-+")
    buffer = ["|"]
    for num in grid[i]:
        if num == "0":
            buffer.append(" ")
        else:
            buffer.append(num)
        buffer.append("|")
    print("".join(buffer))
print("+-+-+-+-+")
