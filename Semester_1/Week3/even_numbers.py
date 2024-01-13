numbers = input("Enter a series of numbers: ")
spilt_numbers = numbers.split(" ")
even = 0
even_numbers = []
for num in spilt_numbers:
    if int(num) % 2 == 0:
        if num not in even_numbers:
            even += 1
            even_numbers.append(num)

print(f"There are {even} distinct even numbers: {even_numbers}")
