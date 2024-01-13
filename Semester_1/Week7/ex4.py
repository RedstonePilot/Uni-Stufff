def flatten(mlist):
    ret_list = []
    for element in mlist:
        if isinstance(element, list):
            ret_list.extend(flatten(element))
        else:
            ret_list.append(element)

    return ret_list


def test_flatten():
    assert flatten([1, 2, [3, 4, [5, 6], 7], 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert flatten([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]
    assert flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert flatten([1, [2, 3], 4, [5, 6]]) == [1, 2, 3, 4, 5, 6]
    assert flatten([]) == []
    assert flatten([1, 2, 3]) == [1, 2, 3]
