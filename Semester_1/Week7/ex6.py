

def iselfish(word, elf="elf"):
    if len(elf) == 0:
        return True
    if len(word) == 0:
        return False
    if word[0] in elf:
        elf = elf.replace(word[0], "", 1)
        print("remove", word[0], elf)
    return iselfish(word[1:], elf)


def something_ish(word, pattern):
    if len(pattern) == 0:
        return True
    if len(word) == 0:
        return False
    if word[0] in pattern:
        pattern = pattern.replace(word[0], "", 1)
        print("remove", word[0], pattern)
    return something_ish(word[1:], pattern)


def test_something_ish():
    assert something_ish("programming", "prog") == True
    assert something_ish("python", "pyt") == True
    assert something_ish("java", "jv") == True
    assert something_ish("ruby", "rb") == True
    assert something_ish("javascript", "jvs") == False
    assert something_ish("swift", "swf") == True
    assert something_ish("kotlin", "ktl") == True
    assert something_ish("typescript", "tsc") == False
    assert something_ish("csharp", "csh") == True
    assert something_ish("golang", "gol") == True
