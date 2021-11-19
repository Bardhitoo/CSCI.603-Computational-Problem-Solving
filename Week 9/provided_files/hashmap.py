"""
description: Chained Hashmap implementation
file: hashmap.py
language: python3
author: br3004@rit.edu Bardh Rushiti
author: pg9349@rit.edu Prakhar Gupta
"""

from collections.abc import Callable, Hashable
from typing import Any, Tuple, Iterator, Iterable, List


def naive_hash_func(str) -> int:
    """
    Naive hash function.
    """
    sum = 0
    for letter, power in zip(str, range(len(str))):
        sum += (ord(letter) - 97)

    return sum


def improved_hash_func(str) -> int:
    """
    Improved hash function
    """
    sum = 0
    for letter, power in zip(str, range(len(str))):
        sum += (ord(letter) - 97) * 31 ** power

    return sum


class ChainNode:
    """
    ChainNode(key: Any, value: Any, link: 'ChainNode' = None) -&gt; None
    A node to hold (key-value) pair of objects stored in a Chained Hash Map
    """
    __slots__ = "key", "value", "link"

    def __init__(self, key: Any, value: Any, link: "ChainNode" = None) -> None:
        self.key = key
        self.value = value
        self.link = link


if "__main__" == __name__:
    a = ChainNode(1, 1)
    c = 2
    a.link = ChainNode(2, 2)


class HashMap(Iterable):
    MIN_BUCKETS = 10

    __slots__ = "hash_table", "hash_func", "initial_num_buckets", "load_limit", "load_factor", "size"

    __abstractmethods__ = frozenset()

    def __init__(self, hash_func: Callable[[Hashable], int] = improved_hash_func, initial_num_buckets: int = 100,
                 load_limit: float = 0.75) -> None:
        """
        Create a new empty hash table.
        :param initial_num_buckets: starting number_of_buckets
        :param load_limit: See class documentation above.
        :param hash_func: the hash function used to compute the entry's location into the hash table
        :return: None
        """
        self.hash_func = hash_func
        self.initial_num_buckets = initial_num_buckets
        self.load_limit = load_limit

        self.hash_table = [ChainNode(None, None) for _ in range(self.initial_num_buckets)]
        self.load_factor = 0
        self.size = 0

    def __iter__(self) -> Iterator[Tuple[Hashable, Any]]:
        """
        Build an iterator.

        :return: an iterator for the current entries in the map
        """

        for node in self.hash_table:
            while node.value is not None:
                yield node.key, node.value
                node = node.link

    def add(self, key: Hashable, value: Any) -> None:
        """
        Insert a new entry into the hash table. However, if the key
        already exists, the value associated to that key is updated with the given value.
        Double the size of the table if its load_factor exceeds the load_limit.

        :param key: the key to add
        :param value: the value to add
        :return: None
        """

        index = self.hash_func(key) % self.initial_num_buckets
        node = self.hash_table[index]

        while node.key is not None and node.key != key:
            node = node.link

        # add new node
        if node.key is None:
            node.key = key
            node.value = value
            node.link = ChainNode(None, None)

            # Change the load factor only when adding on a new part in the hashtable
            self.size += 1
            self.load_factor = self.size / self.initial_num_buckets

        # update value with the same key
        elif node.key == key:
            node.value = value

        # resize hashtable and update element placement
        if self.load_factor >= self.load_limit:
            self.hash_table = self.resize_hashtable(increase_size=True)

    def resize_hashtable(self, increase_size: bool) -> List:
        """
        Resizes the hashman to the new desired size

        :param increase_size: how the codes desides is we want to shrink or
        """
        if increase_size:
            self.initial_num_buckets = self.initial_num_buckets * 2
        if not increase_size:
            self.initial_num_buckets = self.initial_num_buckets // 2

        hm = HashMap(self.hash_func, self.initial_num_buckets, self.load_limit)

        for key, val in self:
            hm.add(key, val)

        self.load_factor = self.size / self.initial_num_buckets
        return hm.hash_table

    def contains(self, key: Hashable) -> bool:
        """
        Is the given key in the hash table?

        :return: True iff key or its equivalent has been added to this table
        """
        index = self.hash_func(key) % self.initial_num_buckets
        node = self.hash_table[index]

        while node.key != key and node.key is not None:
            node = node.link

        return node.key == key

    def get(self, key: Hashable) -> Any:
        """
        Return the value associated to the given key.

        :return The value associated to the given key or None if key is not found
        """
        index = self.hash_func(key) % self.initial_num_buckets
        node = self.hash_table[index]
        while node.key is not None and node.key != key:
            node = node.link

        if node.key is None:
            return None
        else:
            return node.value

    def imbalance(self) -> float:
        """
        Computes the imbalance of the hashtable.

        :return: the average length of all non-empty chains minus 1, or 0 if hash table is empty
        """
        elem_counter, node_counter = 0, 0

        for node in self.hash_table:
            if node.key is not None:
                elem_counter += 1
                node_counter += 1

                while node.link.key is not None:
                    node_counter += 1
                    node = node.link

        try:
            return (node_counter / elem_counter) - 1
        except ZeroDivisionError:
            exit("You cannot divide by zero! Make sure there are elements in your HashMap")

    def remove(self, key: Hashable) -> None:
        """
        Remove an object from the hash table.
        Resize the table if its size has dropped below
        (1-load_factor)*current_size.

        :param key: the key to remove; assumes hashing and equality work
        :return: None
        """

        index = self.hash_func(key) % self.initial_num_buckets
        node = self.hash_table[index]
        parent = self.hash_table[index]

        # if we need to, iterate over the LinkedList
        while node.key is not None and node.key != key:
            parent = node
            node = node.link

        # check if we're removing the first element (that doesn't exist)
        if node.key is None:
            raise KeyError("Element doesn't exist.")

        # if we found what we're trying to remove
        if node.key == key:
            if node != parent:
                parent.link = node.link
                self.size -= 1
                self.load_factor = self.size / self.initial_num_buckets
            elif node.link.key is None:
                self.hash_table[index] = ChainNode(None, None)
                self.size -= 1
                self.load_factor = self.size / self.initial_num_buckets

        # resize hashmap
        if self.load_factor <= 1 - self.load_limit:
            self.hash_table = self.resize_hashtable(increase_size=False)
