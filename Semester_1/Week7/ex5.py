def merge(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1

    if list1[0] < list2[0]:
        return [list1[0]] + merge(list1[1:], list2)
    if list2[0] < list1[0]:
        return [list2[0]] + merge(list2[1:], list1)


def test_merge():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]
    assert merge([1, 3, 5], []) == [1, 3, 5]
    assert merge([], [2, 4, 6]) == [2, 4, 6]
    assert merge([], []) == []
