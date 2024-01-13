def rec_sum(digits):
    if len(digits) < 1:
        return 0
    return rec_sum(digits[1:]) + digits[0]


def test_rec_sum():
    assert rec_sum([1, 2, 3]) == 6
    assert rec_sum([4, 5, 6]) == 15
    assert rec_sum([10, 20, 30, 40]) == 100
    assert rec_sum([-1, 1]) == 0
    assert rec_sum([0, 0, 0, 0]) == 0
    assert rec_sum([]) == 0
    assert rec_sum([1]) == 1
