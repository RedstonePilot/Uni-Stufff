WEIGHT_OF_ONE_RICE = 0.00003
def weight_of_rice():
    running_total = 0
    sum = 0
    for i in range(8):
        for j in range(8):
            if running_total == 0:
                running_total += 1
            else:
                running_total *= 2

            sum += running_total
            print(f"{running_total} grains, with a weigth of {running_total * WEIGHT_OF_ONE_RICE} kg")
    print(f"Total weight of rice: {sum * WEIGHT_OF_ONE_RICE} kg")

weight_of_rice()