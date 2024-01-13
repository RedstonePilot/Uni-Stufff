def check_level(level):
    """Recursive function to see if a level is do-able

    Args:
        level (list): List of the level, 0 is bomb
                      And number is how far the pad can launch you

    Returns:
        Bool: True if the level is possible or False if not
    """
    if len(level) <= 1:  # success
        return True
    if level[-1] == 0 or level[0] == 0:  # currently impossible or dead
        return False

    return True in [check_level(level[i+1:]) if i < len(level)
                    else True for i in range(level[0])]
