def shrink(signal, element):
    """Shrinks the boundaries of the forground regions

    Args:
        signal (binary list): A list of 1 and 0 with 1 represeting the foreground
        element (binary list): The list of 1 and 0 to match the signal with

    Returns:
        binary list: Returns a Shrunk list
    """

    shrunk_signal = []
    for i, bit in enumerate(signal):
        if i == len(signal)-1:
            if bit == element[0]:
                shrunk_signal.append(1)
            else:
                shrunk_signal.append(0)
        elif [bit, signal[i+1]] == element:
            shrunk_signal.append(1)
        else:
            shrunk_signal.append(0)
    return shrunk_signal


def expand(signal, element):
    """Expands the boundaries of the forground regions

    Args:
        signal (binary list): A list of 1 and 0 with 1 represeting the foreground
        element (binary list): The list of 1 and 0 to match the signal with

    Returns:
        binary list: Returns an Expanded list
    """

    expanded_signal = []
    for i, bit in enumerate(signal):
        if i == len(signal)-1:
            if bit == 1:
                expanded_signal.append(1)
            else:
                expanded_signal.append(0)
        elif 1 in [bit, signal[i+1]]:
            expanded_signal.append(1)
        else:
            expanded_signal.append(0)

    return expanded_signal


def denoise(signal, element):
    """Performs the shrink then expand operations

    Args:
        signal (binary list): A list of 1 and 0 with 1 represeting the foreground
        element (binary list): The list of 1 and 0 to match the signal with

    Returns:
        binary list: Returns the de noised list
    """
    return expand(shrink(signal, element), element)


if __name__ == "__main__":
    signal = [0, 1, 0, 0, 0, 1]
    structuring_element = [0, 0]
    print(shrink(signal, structuring_element))
    print(expand(signal, structuring_element))
