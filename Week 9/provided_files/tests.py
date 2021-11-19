"""
file: tests.py
description: Verify the chained hash map class implementation
language: python3
author: br3004@rit.edu Bardh Rushiti
author: pg9349@rit.edu Prakhar Gupta
"""

__author__ = ["NAME", "NAME"]

from hashmap import HashMap


def print_map(a_map):
    for word, counter in a_map:  # uses the iter method
        print(word, counter, end=" ")
    print()


def test0():
    table = HashMap(initial_num_buckets=10)
    table.add("to", 1)
    table.add("do", 1)
    table.add("is", 1)
    table.add("to", 2)
    table.add("be", 1)

    print_map(table)

    print("'to' in table?", table.contains("to"))
    print("'to' appears", table.get("to"), "times")
    table.remove("to")
    print("'to' in table?", table.contains("to"))

    print_map(table)


def test3():
    """
        Demonstrating  working of the HashMap with
         add and remove functionality along with get and contains

         We have also shown the ability of iterate through the HashMap

        :return:None
    """
    print("")
    print("Test 3")
    hm = HashMap(initial_num_buckets=20, load_limit=0.3)
    hm.add("lad", "English")
    hm.add("adl", "Englih")
    hm.add("dal", "Eng")
    hm.add("be", "Greek")
    hm.add("be", "Greek")
    hm.add("beb", "Germand")

    hm.add("xxx", "Hindi")

    print("Is lad present ? ", hm.contains("lad"))
    print("lad value is = ", hm.get("lad"))

    for i in hm:
        print(i)

    print()
    print("Removing dal")
    hm.remove("dal")

    for i in hm:
        print(i)


def test1():
    """
    Demonstrating adding to HashMap as well as when trying to remove if a key which
    is not present is given code throws a keyerror.


    :return:None
    """
    print("")
    print("Test 1")
    hm = HashMap(initial_num_buckets=20, load_limit=0.3)
    hm.add("abc", 123)
    hm.add("xyz", 345)

    print("Trying to remove pqr which is not in our hash map")
    try:
        hm.remove("pqr")
    except KeyError:
        print('Caught key error exception ' +
              'key value not found')


def test2():
    """
    Demonstrating adding to HashMap as well as when trying to remove from the HashMap
    along with the change of bucket size i.e it will shrink or will increase

    :return:None
    """
    print("")
    print("Test 2")
    hm = HashMap(initial_num_buckets=10, load_limit=0.2)  # keeping low load limit for testing
    print("Initial size")
    print("Buckets = " + str(hm.initial_num_buckets) + "Load factor = " + str(hm.load_factor))
    hm.add("abc", 98)
    print("Adding 1 element")
    print("Buckets = " + str(hm.initial_num_buckets) + "Load factor = " + str(hm.load_factor))
    # This will lead to doubling of the size af the buckets

    hm.add("xyz", 99)
    print("Adding 1 element")
    print("Buckets = " + str(hm.initial_num_buckets) + "Load factor = " + str(
        hm.load_factor))
    hm.add("Marks in this assignment", 100)
    print("Adding 1 element")
    print("Buckets = " + str(hm.initial_num_buckets) + "Load factor = " + str(hm.load_factor))

    # This will lead to shrinking of size by half
    print("Removing 1 element")
    hm.remove("abc")
    print("Buckets = " + str(hm.initial_num_buckets) + "Load factor = " + str(
        hm.load_factor))


def test4():
    pass


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
