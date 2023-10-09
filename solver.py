import sys
from words import load_words
from caesarcipher import CaesarCipher

WORDS = load_words()


def user_input():
    encrpyted_text = input("Please enter the string: ")

    final_text = decrypt(encrpyted_text)

    print(final_text)


def file_input(file_location):
    solves = []

    for line in open(file_location, "r"):
        try:
            final_text = decrypt(line.strip())
        except:
            final_text = "UNABLE TO SOLVE"
        solves.append(final_text)

    f = open("solves.txt", "w")
    f.write("\n".join(solves) + "\n")
    f.close()


def decrypt(encrpyt_text):
    offset = 1
    decrpyted = False

    CORRECT_PERCENTAGE = 0.75

    while not decrpyted:
        offset -= 1

        decrypt_text = CaesarCipher(encrpyt_text, offset=offset).decoded

        working_text = decrypt_text.replace(".", "")
        working_text = working_text.replace(",", "")

        words_in_text = working_text.split()
        num_valid = 0
        for word in words_in_text:
            if word.lower() in WORDS:
                num_valid += 1

        if num_valid / len(words_in_text) >= CORRECT_PERCENTAGE:
            decrpyted = True

        if offset < -1000:
            raise Exception("Couldn't find solution")

    return decrypt_text


if __name__ == "__main__":
    if len(sys.argv) == 1:
        user_input()
    elif len(sys.argv) == 2:
        file_input(sys.argv[1])
    else:
        print("Either give no input to input or give file")
