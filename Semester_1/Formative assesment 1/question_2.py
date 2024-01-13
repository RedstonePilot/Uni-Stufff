def time_to_seconds(time):
    """Takes the time in HH:MM:SS and returns the respective number of seconds

    Args:
        time (str): A string in the form of HH:MM:SS or MM:SS if there are no hours


    Returns:
        int: returns the integer number of seconds that the time represents
        None: if the time is in the wrong format
    """
    if not (time.count(":") in [1, 2] and len(time) == (2 + 3*time.count(":"))):
        return None

    if time.count(":") == 2:
        if int(time[:2]) > 99 or time[:2] == "00" or int(time[3:5]) > 59 or int(time[-2:]) > 59:
            return None
    else:
        if int(time[:2]) > 59 or int(time[-2:]) > 59:
            return None

    new_format = 0
    scale_factor = [1, 60, 3600]
    split_list = time.split(":")
    split_list.reverse()
    for component, scale in zip(scale_factor, split_list):
        new_format += int(component)*int(scale)
    return new_format


time_to_seconds("10:60")
