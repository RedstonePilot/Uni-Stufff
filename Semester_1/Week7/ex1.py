"""Write a recursive function ispalindrome(word) that returns true if the string word is a
palindrome, false otherwise. You can start with an implementation that does not deal with
punctuation, and then refactor your code to take into account punctuation"""


def ispalindrome(word):
    if len(word) <= 1:
        return True
    while not word[0].isalpha():
        word = word[1:]
    while not word[-1].isalpha():
        word = word[:-1]

    if word[0].lower() != word[-1].lower():
        return False
    return ispalindrome(word[1:-1])
