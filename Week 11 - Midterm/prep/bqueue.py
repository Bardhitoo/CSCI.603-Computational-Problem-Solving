class Node:
    __slots__ = "val", "link"
    val: any
    link: "Node"

    def __init__(self, val: any, link: "Node" = None):
        self.val = val
        self.link = link


class BardhQueue:
    __slots__ = "front", "back"
    front: Node
    back: Node

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, val):
        newNode = Node(val)
        if self.front is None:
            self.front = newNode
        else:
            self.back.link = newNode
        self.back = newNode

    def dequeue(self):
        if self.front is None:
            self.back = None
            return
        self.front = self.front.link

    def peek(self):
        assert self.front is not None, "peek on empty queue"
        return self.front.val