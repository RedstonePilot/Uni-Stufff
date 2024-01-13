def divisors(n):
    """returns all factors of a number"""
    return [d for d in range(1, n+1) if n % d == 0]


def sum_digits(number):
    """retuns the sum of all digits"""
    summation = 0
    while number > 0:
        summation += number % 10
        number //= 10

    return summation


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))
