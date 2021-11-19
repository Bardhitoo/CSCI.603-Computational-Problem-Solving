"""
sort.py

This code is taken from the selection sort code shared by the professor Maria Cepeda. It has been modified to our needs.

Authors:
    Bardh Rushiti
    Prakhar Gupta

id: br3004, pg9349

This program is for CSCI -603 Assignment Week5

This program implements selection sort
"""


def _findMinIndex(data, mark):
    """
        A helper routine for selectionSort which finds the index
        of the smallest value in data at the mark index or greater.
        :param data: a list of data
        :param mark: an index which is in range 0..len(data)-1 inclusive
        :return: An index which is in range 0..len(data)-1 inclusive
    """

    # assume the minimum value is at initial mark position
    minIndex = mark

    # loop over the remaining positions greater than the mark
    for mark in range(mark + 1, len(data)):
        # if a smaller value is found, record its index
        if data[mark] < data[minIndex]:
            minIndex = mark
    return minIndex


def manual_sort(data):
    """
        Perform an in-place selection sort of data.
        :param data: The data to be sorted
        :return: None
    """
    for mark in range(len(data) - 1):
        minIndex = _findMinIndex(data, mark)
        # swap the element at marker with the min index
        data[mark], data[minIndex] = data[minIndex], data[mark]
