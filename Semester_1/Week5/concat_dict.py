def concat_dict(dict1, dict2):
    """concatinates 2 dicts"""
    for key, value in dict2.items():
        if key in dict1:
            tmp = [dict1[key], value]
            dict1[key] = tmp
    return dict1


dictionary1 = {"one": 1, "two": 2, "three": 3, "five": 5}

dictionary2 = {"two": "200", "four": 4, "five": "005"}

print(concat_dict(dictionary1, dictionary2))
