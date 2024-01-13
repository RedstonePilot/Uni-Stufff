def seconds_to_time(time):
    """Converts a given ammount of seconds to the HH:MM:SS format


    Args:
        time (int): Taken a number of seconds as an integer

    Returns:
        string: Returns a string in the form HH:MM:SS or MM:SS if there is no hours
        None: if the time is negative, over 99:59:59
    """
    if time < 0 or time >= 360_000:
        return None

    hours = time // 3600
    mins = (time % 3600) // 60
    seconds = time % 60
    if hours:
        return f"{hours:02}:{mins:02}:{seconds:02}"
    return f"{mins:02}:{seconds:02}"
