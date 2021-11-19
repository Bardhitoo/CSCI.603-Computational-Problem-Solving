"""
stack.py
author: James Heliotis
description: A linked stack (LIFO) implementation
"""
from typing import Any

from node import LinkedNode


class Stack:
    __slots__ = "top"
    top: LinkedNode

    def __init__(self) -> None:
        """ Create a new empty stack."""
        self.top = None

    def __str__(self) -> str:
        """ Return a string representation of the contents of
            this stack, top value first.
        """
        node = self.top
        result = "Top"
        while node is not None:
            result += " -> " + str(node.value)
            node = node.link
        result += " -> None"
        return result

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, newValue: Any) -> None:
        self.top = LinkedNode(newValue, self.top)

    def pop(self) -> None:
        assert self.top is not None
        self.top = self.top.link

    def peek(self) -> Any:
        return self.top

    insert = push
    remove = pop

def test() -> None:
    s = Stack()
    for value in 1, 2, 3:
        s.push(value)
        print(s)
    print("Popping:", s.peek())
    s.pop()
    print(s)
    for value in 15, 16:
        s.insert(value)
        print(s)
    print("Removing:", s.peek())
    s.remove()
    print(s)
    while not s.is_empty():
        print("Popping:", s.peek())
        s.pop()
        print(s)
    print("Trying one too many pops... ", end="")
    try:
        s.pop()
        print("Problem: it succeeded!")
    except Exception as e:
        print("Exception was '" + str(e) + "'")


def balanced_par(paranthesis):
    s = Stack()

    index = 0
    while index < len(paranthesis):
        if paranthesis[index] == '(':
            s.insert(paranthesis[0])
        else:
            if s.is_empty():
                return False
            else:

                s.pop()
        index += 1

    return s.is_empty()


def is_palindrome(str):
    from cs_queue import Queue
    s = Stack()
    q = Queue()

    index = 0
    while index < len(str):
        s.insert(str[index])
        q.insert(str[index])
        index += 1

    index = 0
    while index < len(str):
        if s.peek() != q.peek():
            return False
        else:
            s.pop()
            q.dequeue()
        index += 1

    return s.is_empty() and q.is_empty()


if __name__ == "__main__":
    test()