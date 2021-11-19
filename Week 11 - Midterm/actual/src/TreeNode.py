"""
This is an implementation of a n-ary tree node.
@author: CS RIT
"""
from typing import Any


class TreeNode:
    __slots__ = 'value', 'children', 'parent'
    value: Any
    children: list['TreeNode']

    def __init__(self, value: Any, parent: Any = None) -> None:
        self.value = value
        self.parent = parent
        self.children = []

    def __str__(self) -> str:  # do not modify
        return str(self.value)

    def __repr__(self) -> str:  # do not modify
        return self._getStringRep(0)

    def _getStringRep(self, depth: int) -> str:  # do not modify
        ret = self.value
        for c in self.children:
            ret += "\n" + "    " * depth + "+---" + (c._getStringRep(depth + 1))
        return ret

    def __eq__(self, other) -> bool:  # do not modify
        if type(self) != type(other):
            return False
        return self.value == other.value
