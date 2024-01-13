def sum_digits(num):
    if num == 0:
        return 0
    return sum_digits(num//10) + num % 10


def test_sum_digits():
    assert sum_digits(123) == 6
    assert sum_digits(456) == 15
    assert sum_digits(789) == 24
    assert sum_digits(0) == 0
    assert sum_digits(100) == 1
    assert sum_digits(1010101) == 4
    assert sum_digits(9999999) == 63
