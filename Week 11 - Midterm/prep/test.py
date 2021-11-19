from bst import BST

def buildTestTree():
    bst = BST()
    bst.insert(5)
    bst.insert(2)
    bst.insert(4)
    bst.insert(12)
    bst.insert(9)
    bst.insert(15)
    bst.insert(7)
    bst.insert(10)
    print(bst)
    print("==============")
    print(bst.depth(5))
    print(bst.depth(2))
    print(bst.depth(10))
    print(bst.depth(11))
    print(bst.depth(1))
    bst.printPretty()

if "__main__" == __name__:
    buildTestTree()
