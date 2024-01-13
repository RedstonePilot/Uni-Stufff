from math import floor


def track_points(time, event_parameters):
    """Gives a score based on given parameters 

    Args:
        time (float): The time taken to complete the race
        event_parameters (tuple): paramaters from the conversion table

    Raises:
        ValueError: If the event_parameters tuple doesn't contain exactly 3 elements

    Returns:
        int: The number of points (rounded down) that an athelete has
    """
    if len(event_parameters) != 3:  # wrong format
        raise ValueError
    a, b, c = event_parameters
    if b < time:  # not returning a negative number
        return 0
    return max(0, floor(a*(b-time)**c))
