def ispalindrome(word):
    if len(word) <= 1:
        return True
    while not word[0].isalpha():
        word = word[1:]
    while not word[-1].isalpha():
        word = word[:-1]

    if word[0].lower() != word[-1].lower():
        return False
    return ispalindrome(word[1:-1])


def rec_sum(digits):
    if len(digits) < 1:
        return 0
    return rec_sum(digits[1:]) + digits[0]


def sum_digits(num):
    if num == 0:
        return 0
    return sum_digits(num//10) + num % 10


def flatten(mlist):
    ret_list = []
    for element in mlist:
        if isinstance(element, list):
            ret_list.extend(flatten(element))
        else:
            ret_list.append(element)

    return ret_list


def merge(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1

    if list1[0] < list2[0]:
        return [list1[0]] + merge(list1[1:], list2)
    if list2[0] < list1[0]:
        return [list2[0]] + merge(list2[1:], list1)


def is_power(a, b):
    if a == b:
        return True
    if a < b:
        return False
    return is_power(a/b, b)
