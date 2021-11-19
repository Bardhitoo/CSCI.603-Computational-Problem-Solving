"""
linkedlist.py

A Linked List interface and implementation in Python
This version uses a cursor. Using indices is inherently inefficient and
hides the strengths of the linked list.
Cursors, immutable, are created by list methods.

author: CS RIT
"""
from typing import Any

class LinkedNode:

    __slots__ = "value", "link"
    value: Any
    link: 'LinkedNode'

    def __init__( self, value: str, link: 'LinkedNode' = None ) -> None:
        """ Create a new node and optionally link it to an existing one.
            param value: the value to be stored in the new node
            param link: the node linked to this one
        """
        self.value = value
        self.link = link

    def __str__(self) -> str:
        return str(self.value)


class LinkedList:

    __slots__ = 'front', 'size'
    front: LinkedNode
    size: int

    def __init__( self ) -> None:
        """ Create an empty list.
        """
        self.front = None
        self.size = 0

    def append( self, new_value: Any ) -> None:
        """ Add value to the end of the list.
            List is modified.
            :param new_value: the value to add
            :return: None
        """
        node = self.front
        newNode = LinkedNode( new_value )
        if node == None:
            self.front = newNode
        else:
            while node.link != None:
                node = node.link
            node.link = newNode
        self.size +=1

    def prepend( self, new_value: Any ) -> None:
        """ Add value to the beginning of the list.
            List is modified.
            :param new_value: the value to add
            :return: None
        """
        self.front = LinkedNode( new_value, self.front )
        self.size += 1

    def start( self ) -> LinkedNode:
        """ Generate a cursor that refers to the beginning of the list.
            List is unchanged.
            :return: a cursor, possibly 'off' if list is empty
        """
        return self.front

    def is_off( self, cursor: LinkedNode ) -> bool:
        """ Is the cursor off the list?
            :param cursor: the cursor (list position) to be tested
            :return: True iff the cursor is not at a valid location in the list.
        """
        return cursor == None

    def get_value( self, cursor: LinkedNode ) -> Any:
        """ Get the value at the location indicated by the cursor.
            List is unchanged.
            :pre: not self.is_off( cursor );
                            raises ValueError in event of violation
            :param cursor: the list position of the desired value
            :return: value stored at cursor's location
        """
        if self.is_off( cursor ):
            raise ValueError()
        return cursor.value

    def next_loc( self, cursor: LinkedNode ) -> LinkedNode:
        """ Create a new cursor to the next position in the list, or
            'off' if cursor is at the last position.
            List is unmodified.
            :pre: not self.is_off( cursor )
                            raises ValueError in event of violation
            :param cursor: the list position
            :return: the new cursor
        """
        if self.is_off( cursor ):
            raise ValueError()
        return cursor.link

    def __str__(self) -> str:
        """ Returns the content of the list in one single line, first to last """
        result = '['
        cursor = self.start()
        while not self.is_off(cursor):
            result += str(self.get_value(cursor))
            cursor = self.next_loc(cursor)
            if not self.is_off(cursor): result += ", "
        result += "]"
        return result

def print_list( seq: LinkedList, msg: str ) -> None:
    """ Print the contents of a list on a single line, first to last.
    """
    print("%s\n===============\n[%d] " % (msg, seq.size), end="")
    print(seq)
    print()

def test() -> None:
    # Create a list.
    seq = LinkedList()
    print_list( seq, "START" )

    # Add values using append.
    for even in 4, 6:
        seq.append( even )

    # Prepend a value
    seq.prepend( 2 )
    print_list( seq, "EVENS" )


if __name__ == "__main__":
    test()

