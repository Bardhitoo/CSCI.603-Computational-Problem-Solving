"""
bsearch.py
Authors:
    Bardh Rushiti
    Prakhar Gupta

id: br3004, pg9349

This program is for CSCI -603 Assignment Week5

This program implements Binary and linear search
"""


def isPrefix(prefix, word):
    """
        Checks if the word has the same prefix
        :param prefix:  the prefix that we are looking for
        :param word:    the full word
        :return:        true if found, else false
    """
    if word[:len(prefix)] == prefix:
        return True
    else:
        return False


def linearSearch(start_index, prefix, li):
    """
        Finds the last index that matches the prefix in the given list
        :param start_index:     starting index of the game
        :param prefix:          prefix that we are looking for
        :param li:              the list to search the prefix in
        :return:
    """
    last = -1
    for i in range(start_index, len(li)):
        if isPrefix(prefix, li[i]):
            last = i
        elif li[i] > prefix:
            return last

    return last


def _binSearchRec(data, val, left, right):
    """
        Searches the value in the data given
        :param data:        the data to look for
        :param val:         the value we're looking for
        :param left:        the right limit
        :param right:       the left index
        :return:            True/ False, index of the word (-1 if it isnt found)
    """
    if left > right:
        return False, -1
    mid = (left + right) // 2
    if isPrefix(val, data[mid]):
        found, ind = True, mid
        found_in_left, new_ind = _binSearchRec(data, val, left, mid - 1)
        if found_in_left:
            return found_in_left, new_ind
        else:
            return found, ind

    elif data[mid] > val:
        return _binSearchRec(data, val, left, mid - 1)
    else:
        return _binSearchRec(data, val, mid + 1, right)


def binSearch(data, val):
    """
        Helper function for binary search tree
        :param data:    data to look in
        :param val:     value we're looking for
    """
    return _binSearchRec(data, val, 0, len(data) - 1)
