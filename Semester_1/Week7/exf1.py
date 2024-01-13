def print_all(numbers):
    if len(numbers) < 2:
        return numbers[0]
    print(numbers[0])
    numbers.pop(0)
    return print_all(numbers)


def rev_print_all(numbers):
    print(numbers)
    if len(numbers) < 1:
        return numbers[-1]
    print(numbers[-1])
    numbers.pop(len(numbers)-1)
    return print_all(numbers)


rev_print_all([1, 2, 3])
