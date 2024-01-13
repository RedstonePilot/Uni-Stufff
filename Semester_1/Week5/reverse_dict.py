def reverse_dict(dico):
    if len(dico) != len(set(dico)):
        return None

    keys = []
    values = []
    ret_dico = {}
    for key, value in dico.items():
        keys.append(key)
        values.append(value)
    for a, b in zip(keys, values):
        ret_dico[b] = a

    return ret_dico


print(reverse_dict({"one": 1, "two": 2, "two": "2"}))  # ignore
