from typing import Any


class LinkedNode:
    _slots_ = "value", "link"

    def __init__(self, value, link=None):
        """ Create a new node and optionally link it to an existing one.
            param value: the value to be stored in the new node
            param link: the node linked to this one
        """
        self.value = value
        self.link = link

    def __str__(self) -> str:
        """ Return a string representation of the contents of
            this node. The link is not included.
        """
        return str(self.value)

    def __repr__(self) -> str:
        """ Return a string that, if evaluated, would recreate
            this node and the node to which it is linked.
            This function should not be called for a circular
            list.
        """
        return "LinkedNode(" + repr(self.value) + "," + \
               repr(self.link) + ")"
