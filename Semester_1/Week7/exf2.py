def to_binary(number):
    if number == 0:
        return '0'
    elif number == 1:
        return '1'
    else:
        return to_binary(number // 2) + str(number % 2)


def to_den(binary):
    if binary == '':
        return 0
    else:
        return int(binary[0]) * 2**(len(binary) - 1) + to_den(binary[1:])


def test_to_den():
    assert to_den('0') == 0
    assert to_den('1') == 1
    assert to_den('10') == 2
    assert to_den('11') == 3
    assert to_den('100') == 4
    assert to_den('101') == 5
    assert to_den('110') == 6
    assert to_den('111') == 7
    assert to_den('1000') == 8
    assert to_den('1001') == 9
    assert to_den('1010') == 10
    assert to_den('1010011') == 83


test_to_den()
