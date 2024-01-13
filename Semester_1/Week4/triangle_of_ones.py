def triangle_ones_and_zeros(rows):
    num = 1
    for i in range(rows):
        for j in range(i+1):
            if num == 1:
                print("1", end="")
                num = 0
            else:
                print("0", end="")
                num = 1
        print()

triangle_ones_and_zeros(5)