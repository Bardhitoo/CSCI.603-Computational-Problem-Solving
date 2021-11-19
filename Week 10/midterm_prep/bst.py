"""
CSCI-603: Trees (week 10)
Author: Sean Strout @ RIT CS

This is an implementation of a binary search tree.
"""
import random
from typing import Any

from btnode import BTNode


class BST:
    """
    A binary search tree consists of:
    :slot root: The root node of the tree (BTNode)
    :slot size: The size of the tree (int)
    """
    __slots__ = 'root', 'size'
    root: BTNode
    size: int

    def __init__(self, root: BTNode = None) -> None:
        """
        Initialize the tree.
        :return: None
        """
        self.root = root
        self.size = 0

    def __str__(self) -> str:
        """
        Return a string representation of the tree.  By default this will
        be a string with the values in order.
        :return:
        """
        # call the recursive helper function with the root node
        return self.inorder(self.root)

    def __insert(self, val: int, node: BTNode) -> None:
        """
        The recursive helper function for inserting a new value into the tree.
        :param val: The value to insert
        :param node: The current node in the tree (BTNode)
        :return: None
        """
        if val < node.val:
            if node.left is None:
                node.left = BTNode(val)
            else:
                self.__insert(val, node.left)
        elif val > node.val:
            if node.right is None:
                node.right = BTNode(val)
            else:
                self.__insert(val, node.right)

    def insert(self, val: int) -> None:
        """
        Insert a new value into the tree
        :param val: The value to insert
        :return: None
        """
        if self.root is None:
            self.root = BTNode(val)
        else:
            self.__insert(val, self.root)
        self.size += 1

    def __contains(self, val: int, node: BTNode) -> bool:
        """
        The recursive helper function for checking if a value is in the tree.
        :param val: The value to search for
        :param node: The current node (BTNode)
        :return: True if val is present, False otherwise
        """
        if val < node.val:
            if node.left is None:
                return False
            else:
                return self.__contains(val, node.left)
        elif val > node.val:
            if node.right is None:
                return False
            else:
                return self.__contains(val, node.right)
        elif val == node.val:
            return True

    def contains(self, val: int) -> bool:
        """
        Returns whether a value is in the tree or not.
        :param val: The value to search for
        :return: True if val is present, False otherwise
        """
        # call the recursive helper function with the root node
        if self.root is None:
            return False
        elif self.root.val == val:
            return True
        else:
            return self.__contains(val, self.root)

    def __height(self, node: BTNode) -> int:
        """
        The recursive helper function for computing the height of a node
        :param node: The current node (BTNode)
        :return: The height of node (int)
        """
        if node is None:
            return -1
        else:
            return 1 + max(self.__height(node.right), self.__height(node.left))

    def height(self) -> int:
        """
        Return the height of a tree.  Recall:
            - The height of an empty tree is -1
            - The height of a tree with one node is 0
            - Otherwise the height is one plus the larger of the heights of
            the left or right children.
        :return: The height (int)
        """
        # just call the recursive helper function with the root node
        return self.__height(self.root)

    def inorder(self, node: BTNode) -> str:
        """
        The recursive inorder traversal function that builds a string
        representation of the tree.
        :param node: The current node (BTNode)
        :return: A string of the tree, e.g. "1 2 5 9 "
        """
        if node is None:
            return ""
        else:
            return self.inorder(node.left) + " " + str(node.val) + " " + self.inorder(node.right)

    def preorder(self, node: BTNode) -> str:
        """
        The recursive inorder traversal function that builds a string
        representation of the tree.
        :param node: The current node (BTNode)
        :return: A string of the tree, e.g. "1 2 5 9 "
        """
        if node is None:
            return ""
        else:
            return str(node.val) + " " + self.inorder(node.left) + " " + self.inorder(node.right)

    def postorder(self, node: BTNode) -> str:
        """
        The recursive inorder traversal function that builds a string
        representation of the tree.
        :param node: The current node (BTNode)
        :return: A string of the tree, e.g. "1 2 5 9 "
        """
        if node is None:
            return ""
        else:
            return self.inorder(node.left) + " " + self.inorder(node.right) + " " + str(node.val)


def testBST() -> None:
    # tree with a parent (20), left child (10) and right child (30)
    random.seed(42)
    t2 = BST()
    list_asd = [random.randint(0, 10) for i in range(10)]
    for val in list_asd: t2.insert(val)
    print('t2:', t2)

    # a larger tree
    t3 = BST()
    for val in (17, 5, 35, 2, 16, 29, 38, 19, 33): t3.insert(val)
    print('t3:', t3)
    print('t3 size (9):', t3.size)
    print('t3 contains 16 (True)?', t3.contains(16))
    print('t3 contains 0 (False)?', t3.contains(0))
    print('t3 height (3)?', t3.height())


if __name__ == '__main__':
    testBST()
