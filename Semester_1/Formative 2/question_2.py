def common_values(lst1, lst2):
    """Returns the set of values contained in both lists

    Args:
        lst1 (list): The first list to compare  
        lst2 (list): The second list to compare

    Returns:
        list: Returns the list of values present in both lists
              or empty list if none exist
              The list will contain on duplicate items(set)
    """
    return list(set([val for val in lst1 if val in lst2]))
    # only add to the list if its in val 2
