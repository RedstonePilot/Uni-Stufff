def string_pattern(size):
    """Returns a pattern based on the number entered

    Args:
        size (int): width of the pattern

    Raises:
        ValueError: If size is less than or equal to 2

    Returns:
        string: string of the pattern to be printed out. 
        Each line has a "new line character" at the end
    """
    if size <= 2:
        raise ValueError("Size must be larger than or equal to 3")

    output = [f"+{'-'*(size-2)}+\n"]
    for i in range(1, size//2):
        output.append(f"{'-'*(i)}+{'-'*(size-(2+i*2))}+{'-'*(i)}\n")

    first_half = output.copy()
    first_half.reverse()
    if size % 2 == 1:
        output.append(f"{'-'*(size//2)}+{'-'*(size//2)}\n")

    output += first_half
    return "".join(output)


if __name__ == "__main__":

    print(string_pattern(3))
