from TreeNode import TreeNode
from linkedlist import LinkedList

"""
This is an implementation of a taxonomy tree.
@author: CS RIT
"""


class Tree:
    __slots__ = 'root', 'nodeLookup'
    root: TreeNode
    nodeLookup: dict[str, TreeNode]

    def __init__(self) -> None:  # do not modify
        self.root = None
        self.nodeLookup = dict()

    def __str__(self) -> str:  # do not modify
        if self.root:
            return str(self.root)
        return "[empty]"

    def __repr__(self) -> str:  # do not modify
        if self.root:
            return repr(self.root)
        return "[empty]"

    def getNodeByValue(self, value: str) -> TreeNode:  # do not modify
        return self.nodeLookup[value]

    def addRoot(self, value: str) -> None:  # do not modify
        """
        Creates a new node using the value and places it at the root
        :param value: the value of the root
        """
        assert value not in self.nodeLookup and not self.root
        node = TreeNode(value)
        self.nodeLookup[value] = node
        self.root = node

    def addChildTo(self, newChildValue: str, parentValue: str) -> None:
        """
        Creates a new node using the newChildValue and adds it to the node representing the parentValue
        :param newChildValue: The value of the new child node
        :param parentValue: The value of the intended parent

        """
        assert parentValue in self.nodeLookup and newChildValue not in self.nodeLookup
        node = TreeNode(newChildValue, parentValue)
        self.nodeLookup[newChildValue] = node
        self.getNodeByValue(parentValue).children.append(node)

    def getPathToAncestor(self, nodeValue: str, ancValue: str) -> LinkedList:
        """
         Finds the path between the node specified by nodeValue and the ancestor node specified by ancValue
        :param nodeValue: The value of the node
        :param ancValue: The value of the ancestor node
        :return: A list of nodes representing the path between the node and its ancestor
        """
        assert nodeValue in self.nodeLookup and ancValue in self.nodeLookup
        # TODO
        linkedList = LinkedList()

        node = self.getNodeByValue(nodeValue)
        ancParent = self.getNodeByValue(ancValue).parent
        linkedList.append(nodeValue)
        while node.value != ancParent and node.parent is not None:
            node = self.getNodeByValue(node.parent)
            linkedList.prepend(node.value)

        return linkedList

    def getPathToRoot(self, nodeValue: str) -> LinkedList:  # do not modify
        """
         Finds the path between the node specified by nodeValue and the root of the tree
        :param nodeValue: The value of the node
        :return: A list of nodes representing the path between the node and the root of the tree
        """
        assert nodeValue in self.nodeLookup
        return self.getPathToAncestor(nodeValue, self.root.value)

    def getLCA(self, node1Value: str, node2Value: str) -> str:
        """
        Finds the least common ancestor of the nodes specified by the two arguments
        (i.e. the first common ancestor you would encounter when moving up the tree from node1 and node2).
        :param node1Value: The value of node1
        :param node2Value: The value of node2
        :return: The value of the least common ancestor node
        """
        assert node1Value in self.nodeLookup and node2Value in self.nodeLookup
        path1 = self.getPathToRoot(node1Value)
        path2 = self.getPathToRoot(node2Value)

        cursor1 = path1.start()
        cursor2 = path2.start()

        lca = ""
        while not path1.is_off(cursor1) and not path2.is_off(cursor2) and cursor1.value == cursor2.value:
            lca = cursor1.value
            cursor1 = path1.next_loc(cursor1)
            cursor2 = path2.next_loc(cursor2)

        return lca


def test() -> None:
    t = Tree()
    t.addRoot("thing")
    # add children here
    t.addChildTo("animal", "thing")
    # TODO add the rest of nodes here
    t.addChildTo("plant", "thing")
    t.addChildTo("mammal", "animal")
    t.addChildTo("fish", "animal")
    t.addChildTo("tuna", "fish")
    t.addChildTo("dog", "mammal")
    t.addChildTo("cat", "mammal")
    t.addChildTo("human", "mammal")

    # testing part 3
    print("Testing taxonomy..........")
    print(repr(t))
    print()
    # testing part 4
    print("Testing getPathToAncestor function..........")
    # path to root
    print("getPathToRoot('animal') =", t.getPathToRoot("animal"))
    print("getPathToRoot('thing') =", t.getPathToRoot("thing"))
    print("getPathToRoot('cat') =", t.getPathToRoot("cat"))
    # path to ancestor
    print("getPathToAncestor('animal','animal') =", t.getPathToAncestor('animal', 'animal'))
    print("getPathToAncestor('dog','animal') =", t.getPathToAncestor('dog', 'animal'))
    print("getPathToAncestor('dog','mammal') =", t.getPathToAncestor('dog', 'mammal'))
    print()
    # testing part 5
    print("Testing getLCA function..........")
    # LCA
    print("LCA('animal','thing') =", t.getLCA("animal", "thing"))
    print("LCA('thing','animal') =", t.getLCA("thing", "animal"))
    print("LCA('cat','tuna') =", t.getLCA("cat", "tuna"))
    print("LCA('tuna','cat') =", t.getLCA("tuna", "cat"))
    print("LCA('tuna','mammal') =", t.getLCA("tuna", "mammal"))
    print("LCA('cat','cat') =", t.getLCA("cat", "cat"))


if __name__ == '__main__':
    test()
