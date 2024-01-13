data = [[1,2,3], [2], [1, 2, 3, 4]]
output =[]
total = 0
for row in data:
    total = 0
    for val in row:
        total += val
    output.append(total)
print(output)   