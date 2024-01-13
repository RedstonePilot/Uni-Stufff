from textanalysis import sample_text
def get_words_starting_with(text,letter):
    output = []
    for word in text.split():
        test_word = word.lower()
        if test_word.startswith(letter):
            if word not in output:
                output.append(word)
    return output
print(get_words_starting_with(sample_text,"a"))

    