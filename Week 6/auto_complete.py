"""
Autocomplete.py

Authors:
    Bardh Rushiti
    Prakhar Gupta

id: br3004, pg9349

This program is for CSCI -603 Assignment Week5

This program uses Binary and linear search as well as Selection sort to run an
autocomplete
"""

import sys

from bsearch import *
from sort import *


def auto_complete(li):
    """
        Implements the auto complete
        If user doesnot enter any thing  first element is printed.
        If a prefix was entered before it cycles to the next posssible word
        Best match word is the target word
        Also prints the matching word list for better user experience


        :param li list of legal words
        :return: None
    """

    inp = ''
    manual_sort(li)  # selection sort of the list
    print("Sorted list")
    print(li)
    print("Welcome to Auto-complete! Usage: Enter a prefix to auto-complete :")
    print("Entering nothing will print the first word in the sorted list. Enter <QUIT> to exit.")
    last_inp = li[0]
    flag = True
    counter = 0
    while inp != "<QUIT>":  ## TO run loop until user exits
        print()
        inp = input("Enter a prefix to search for:  ")
        if inp == '':
            if counter == 0:  # check for cold start i.e no prefix entered
                print("No input given printing first word")
                inp = last_inp
                counter = 1
            else:
                flag = False
                inp = last_inp
                print("Using last prefix entered")
        else:
            last_inp = inp
            flag = True
            counter = 1

        found, foundId = binSearch(li,
                                   inp)  # binary search for first element position
        if found:  # if word is found
            last_id = linearSearch(foundId, inp,
                                   li)  # linear search for last position
            focus_li = li[foundId:last_id + 1]
            print("Matching words  " + str(focus_li))
            if flag == True:  # To cycle across words in case of empty string
                print(f"Best Match: {focus_li[(foundId) % (len(focus_li))]}")
                print("Enter to switch to next matching word")

            else:
                foundId += counter
                print(f"Best Match: {focus_li[(foundId) % (len(focus_li))]}")
                print("Enter to switch to next matching word")
                counter += 1

        elif inp == "<QUIT>":
            pass
        else:
            print("No match")
    print("Exiting Auto-complete! Good bye.")


def main():
    """
        Main function to read the text file

        :param None
        :return: None
    """
    # If the number of args is not correct exit with a message,
    # else it is guaranteed to be right
    if len(sys.argv) != 2:
        exit("Usage: python3 auto_complete filename")

    # Read from command line argument and save it in a list
    li = []
    # Read from file
    with open(sys.argv[-1]) as f:
        line = f.readline().strip('\n')
        while line != '':
            li.append(line)
            line = f.readline().strip('\n')

    auto_complete(li)  # calling auto complete


if __name__ == "__main__":
    main()
