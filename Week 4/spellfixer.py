"""
spellfixer.py

Author: Bardh Rushiti,
        Prakhar Gupta

id: br3004,
    pg9349

This program is for CSCI -603 Assignment Week4

It checks for 3 minor writing errors.
"""

import re
from ritcs.mutable_str import mutable_str


def read_user_input():
    """
    Reads input from user. Checks user input for ending file, if not ending, it checks the input and
    separates its into an array of words.

    :return: userInputArray
    """
    user_input = input("\nPlease input the word(s) to correct: ")
    if user_input == "!*!":
        print("Bye!")
        exit(0)
    user_input = re.sub(r'[^\w\s]', '', user_input.lower())
    user_input_array = user_input.lower().replace(" ", ",").split(",")
    user_input_array = [i for i in user_input_array if i]
    return user_input_array


def adj_chars(mutable_word, words, keyboard):
    """
    Checks word errors for adjacent keyboard letters. If the word is on the dictionary after the adjacent switch,
    returns the word

    :param mutable_word:  (mutable_str) words to check for error
    :param words:         (set)         set with the words from dictionary
    :param keyboard:      (dictionary)  adjacent words in keyboard

    :return: (mutable_word, True/False) true if it is has fixed the word, else false. If true returns fixed word, else
                                        returns as it was
    """
    if str(mutable_word) not in words:
        for char in mutable_word:
            for keyboard_letter in keyboard[char]:
                ms_word = mutable_str(mutable_word)
                ms_word[ms_word.index(char)] = keyboard_letter

                if str(ms_word) in words:
                    # If the word is found, return the word, True
                    return ms_word, True
        return mutable_word, False
    else:
        # If the word is not found, return the word, True
        return mutable_word, True


def remove_char(mutable_word, words):
    """
    Checks word errors of an additional letter (addd -> add)

    :param mutable_word:  (mutable_str) words to check for error
    :param words:         (set)         set with the words from dictionary

    :return: (mutable_word, True/False) true if it is has fixed the word, else false. If true returns fixed word, else
                                        returns as it was
    """
    for letter_id in range(len(mutable_word)):

        ms_word = mutable_str(mutable_word)
        del ms_word[letter_id]
        if str(ms_word) in words:
            return ms_word, True

    return mutable_word, False


def replace_char(mutable_word, words):
    """
    Checks word errors of an additional letter.

    :param mutable_word:  (mutable_str) words to check for error
    :param words:         (set)         set with the words from dictionary

    :return: (mutable_word, True/False) true if it is has fixed the word, else false. If true returns fixed word, else
                                        returns as it was
    """
    for letter_id in mutable_word:
        for j in range(ord('a'), ord('z') + 1):
            ms_word = mutable_str(mutable_word)
            ms_word[ms_word.index(letter_id)] = chr(j)
            if str(ms_word) in words:
                return ms_word, 1
    return mutable_word, 0


def correct_word(word, words, keyboard):
    """
    Checks word for 3 types of error, adjacent, remove, and replace errors.

    :param word:          (mutable_str) words to check for error
    :param words:         (set)         set with the words from dictionary
    :param keyboard:      (dictionary)  adjacent words in keyboard
    """
    adjacent_chars, found_letter_adjacent = adj_chars(word, words, keyboard)
    if found_letter_adjacent:
        print(f"{adjacent_chars} ", end="")
    else:
        removed_letter, found_letter_removed = remove_char(word, words)
        if found_letter_removed:
            print(f"{removed_letter} ", end="")
        else:
            replaced_letter, found_letter_replaced = replace_char(word, words)
            if found_letter_replaced:
                print(f"{replaced_letter} ", end="")


def read_keyboard(path, dict_flag=False):
    """
    Loads keyboard/ words file in a dictionary/ set respectively.

    :param path:          (str)         path to keyboard/ words file
    :param dict_flag:     (bool)        flag for return type
    """
    words = []
    i = 0
    with open(path) as f:
        for line in f:
            words.append(line.strip())
            i += 1

    if dict_flag:

        word_dict = {}
        for i in words:
            x = i.split(" ")
            word_dict[x[0]] = []
            for j in x[1:]:
                word_dict[x[0]].append(j)

        return word_dict

    else:
        x = []
        for i in words:
            x.append(i.lower())
        set_x = set(x)

        return set_x


def main():
    """
    Main function
    """
    words = read_keyboard('words.txt')
    keyboard = read_keyboard('keyboard.txt', True)

    print("Welcome To Spell Fixer")
    while (True):
        user_input_array = read_user_input()

        for word in user_input_array:
            ms_word = mutable_str(word)
            correct_word(ms_word, words, keyboard)


if __name__ == '__main__':
    main()
