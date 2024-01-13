def extractText(text, keys):
    ret = []
    keys = keys.lower()
    for word in text.split(" "):
        check = True
        for char in word:
            if not char.lower() in keys:
                check = False
                break
        if check == True:
            ret.append(word)

    return " ".join(ret)
