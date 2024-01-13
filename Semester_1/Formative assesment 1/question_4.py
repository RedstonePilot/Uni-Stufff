def encrypt(message, shifts, alphabet):
    """encrypts a message given a list of shifts and a alphabet of allowed letters


    Args:
        message (str): a string containing the message to be encrypted
        shifts (list of ints): a list of integers that dictate what the shift is for each letter        
        alphabet (string): a string of allowable ordered letters

    Returns:
        str: returns a string of the encrypted message
        None: if the message and shift length are diffrent
              if the message contains non alphabetic charachters
              if the shifts are negative or larger than the size of the alphabet 
    """
    if not (message.isalpha() and len(shifts) == len(message) and max(shifts) < len(alphabet) and min(shifts) > 0):
        return None
    new_word = ""
    for char, shift in zip(message, shifts):
        if char not in alphabet:
            return None
        new_word += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
    return new_word


print(encrypt("BABY", [2, 1, 1, 3], "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
