def is_power(a, b):
    if a == b:
        return True
    if a < b:
        return False
    return is_power(a/b, b)


def test_is_power():
    assert is_power(8, 2) == True
    assert is_power(27, 3) == True
    assert is_power(81, 3) == True
    assert is_power(16, 4) == True
    assert is_power(100, 10) == True
    assert is_power(18, 3) == False
    assert is_power(30, 5) == False
    assert is_power(1, 1) == True
    assert is_power(0, 1) == False
    assert is_power(1, 0) == False
    assert is_power(0, 0) == False
