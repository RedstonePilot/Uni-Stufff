def map_list(li1, li2):
    """returns a dict from 2 lists"""
    dico = {}
    for a, b in zip(li1, li2):
        dico[a] = b
    return dico


print(map_list(["one", "two"], [1, 2]))
