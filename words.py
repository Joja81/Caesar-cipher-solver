FILE_LOCATION = "words.txt"


def load_words():
    words = {}
    for line in open(FILE_LOCATION, "r"):
        words[line.lower().strip()] = True
    return words
