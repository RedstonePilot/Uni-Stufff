def is_palindome(number):
    """Checks if the input is a palindrome

    Args:
        number (str): The charachter sequence to check

    Returns:
        bool : True if the input is a palindrome else False
    """
    return number == number[::-1]


def longest_palindromic_numbers(number, set_=set()):
    """Recursive function to find the largets palindromic number

    Args:
        number (str): string of the number you want to check
        set_ (set, optional): keeps a track of the current longest. Defaults to set().

    Returns:
        set: set of the longest palindromes
    """
    if is_palindome(number):
        set_.add(number)
        largest = 0
        for n in set_:
            largest = max(len(n), largest)
        for n in set_.copy():
            if len(n) < largest:
                set_.remove(n)
        return {number}
    longest_palindromic_numbers(number[1:])
    longest_palindromic_numbers(number[:-1])
    return set_


if __name__ == "__main__":
    print(longest_palindromic_numbers("019910"))
