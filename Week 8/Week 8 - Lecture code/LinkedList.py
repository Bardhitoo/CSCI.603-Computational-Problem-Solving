from typing import Any
from Iterators.node import LinkedNode

class LinkedList:
    __slots__ = "front"

    def __init__(self):
        self.front = None

    def __str__(self):
        result = ''
        node = self.front
        while node is not None:
            result += str(node.value) + " "
            node = node.link
        return result

    def append(self, new_value):
        if self.front is None:
            self.prepend(new_value)
        else:
            node = self.front
            while node.link is not None:
                node = node.link
            node.link = LinkedNode(new_value)

    def prepend(self, new_value):
        self.front = LinkedNode(new_value, self.front)

    def start(self):
        return self.front

    def is_off(self, cursor):
        return cursor is None

    def get_value(self, cursor: LinkedNode) -> Any:
        if self.is_off(cursor):
            raise ValueError()
        return cursor.value

    def set_value(self, cursor: LinkedNode, new_value: Any) -> None:
        if self.is_off(cursor):
            raise ValueError()
        cursor.value = new_value

    def next_loc(self, cursor: LinkedNode) -> LinkedNode:
        if not self.is_off(cursor):
            return cursor.link
        else:
            raise ValueError()

    def insert(self, cursor: LinkedNode, new_value: Any) -> None:
        if self.front == cursor:
            self.prepend(new_value)
        else:
            node = self.front
            while node.link != cursor:
                node = node.link
            node.link = LinkedNode(new_value, cursor)

    def size(self) -> int:
        return self._size_to_end(self.front)

    def _size_to_end(self, node: LinkedNode) -> int:
        if node is None:
            return 0
        else:
            return 1 + self._size_to_end(node.link)

    def add_second(self, item):
        if self.front is None:
            raise ValueError

        newnode = LinkedNode(item, self.front.link.link)
        self.front.link = newnode
