from LinkedNode import *
from typing import Any


class Zone:
    """
    Queue.py
    Modified by: Bardh, Prakhar
    description: A linked queue (FIFO) implementation
    """
    __slots__ = "front", "back", "zone_number", "passenger_limit", "num_passenger"
    front: LinkedNode
    back: LinkedNode

    def __init__(self, zone_number: int, passenger_limit: int) -> None:
        """
        Create a new empty queue.
        """
        self.front = None
        self.back = None
        self.zone_number = zone_number
        self.passenger_limit = passenger_limit
        self.num_passenger = 0

    def __str__(self) -> str:
        """
        Return a string representation of the contents of
        this queue, oldest value first.
        """
        result = "Zone Number: " + str(self.zone_number) + "\n\t-------------------------------------------"
        counter = 1
        n = self.front
        while n != None:
            result += "\n\n\t\t" + str(counter) + " " + str(n.value)
            counter += 1
            n = n.link
        return result

    def __len__(self):
        """
        Returns the length of queue
        """
        return self.num_passenger

    def is_empty(self) -> bool:
        """
        Checks if the zone (queue) is empty
        """
        return self.front == None

    def enqueue(self, newValue: Any) -> None:
        """
        Adds new value to the queueu.

        :param newValue: the value to be added in the queue
        """
        newNode = LinkedNode(newValue)
        if self.front == None:
            self.front = newNode
        else:
            self.back.link = newNode
        self.back = newNode

        self.num_passenger += 1

    def dequeue(self) -> None:
        """
        Removes the first value from the queue
        """
        self.num_passenger -= 1
        self.front = self.front.link
        if self.front is None:
            self.back = None
        # self.num_passenger =- 1

    def peek(self) -> Any:
        """
        Returns the value of the link in the start.
        """
        assert not self.is_empty(), "peek on empty queue"
        return self.front.value

    insert = enqueue
    remove = dequeue
