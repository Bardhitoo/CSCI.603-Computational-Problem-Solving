"""
CSCI-603: Trees (week 10)
Author: Sean Strout @ RIT CS

This is an implementation of a binary tree node.
"""
from typing import Any


class BTNode:
    """
    A binary tree node contains:
     :slot val: A user defined value
     :slot left: A left child (BTNode or None)
     :slot right: A right child (BTNode or None)
    """
    __slots__ = 'val', 'left', 'right'
    val: Any
    left: 'BTNode'
    right: 'BTNode'


    def __init__(self, val: Any, left: 'BTNode' = None, right: 'BTNode' = None) -> None:
        """
        Initialize a node.
        :param val: The value to store in the node
        :param left: The left child (BTNode or None)
        :param right: The right child (BTNode or None)
        :return: None
        """
        self.val = val
        self.left = left
        self.right = right


    def __inorder(self, node: "BTNode") -> str:
        """
        The recursive inorder traversal function that builds a string
        representation of the tree.
        :param node: The current node (BTNode)
        :return: A string of the tree, e.g. "1 2 5 9 "
        """
        if node is None:
            return ""
        else:
            return self.__inorder(node.left) + ' ' + str(node.val) + ' ' +self.__inorder(node.right)

    def __str__(self) -> str:
        """
        Return a string representation of the tree.  By default this will
        be a string with the values in order.
        :return:
        """
        # call the recursive helper function with the root node
        return self.__inorder(self)

def testBTNode() -> None:
    """
    A test function for BTNode.
    :return: None
    """
    left = BTNode(10)
    right = BTNode(20)
    parent = BTNode(30)
    parent.left = left
    parent.right = right
    print('parent (30):', parent.val)
    print('left (10):', parent.left.val)
    print('right (20):', parent.right.val)
    print('parent:', parent)


if __name__ == '__main__':
    testBTNode()
