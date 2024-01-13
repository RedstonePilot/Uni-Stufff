def game(number, order=1):
    dp = [0] * (number + 1)
    dp[1] = dp[2] = dp[4] = 1

    for i in range(5, number + 1):
        if order == 1:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 4]
        else:
            dp[i] = dp[i - 1] + dp[i - 2]

    return "First" if dp[number] != 0 else "Second", dp[number]


def test_game():
    assert game(5, 1) == ("First", 2)
    assert game(6, 1) == ("First", 4)
    assert game(7, 1) == ("Second", 0)
    assert game(8, 1) == ("First", 1)
    assert game(9, 1) == ("First", 2)
    assert game(10, 1) == ("First", 4)
    assert game(11, 1) == ("Second", 0)
    assert game(12, 1) == ("First", 1)


test_game()
