from Zone import *


class Airplane:
    """
    Airplane class that contains the information top, has_carry_ons, has_no_carry_ons
    """
    __slots__ = "top", "has_carry_ons", "has_no_carry_ons", "passenger_counter"
    top: LinkedNode
    has_carry_ons: Zone
    has_no_carry_ons: Zone
    passenger_counter: int

    def __init__(self, limit: int) -> None:
        """
        Class constructor for the Airplane

        :param limit:   the limit of the passengers in the plane
        """
        self.top = None
        self.passenger_counter = 0
        self.has_carry_ons = Zone(45, limit)
        self.has_no_carry_ons = Zone(45, limit)

    def __str__(self) -> str:
        """
        Return a string representation of the contents of
        this stack, top value first.
        """
        result = "Stack["
        n = self.top
        while n != None:
            result += " " + str(n.value)
            n = n.link
        result += " ]"
        return result

    def __len__(self):
        """
        Returns the length of queue
        """
        return self.passenger_counter

    def deboard(self):
        """
        Deboards the passengers from the plane.
        """
        while not self.is_empty():
            passenger = self.peek()
            self.pop()
            if (passenger.has_carry_on):
                self.has_carry_ons.enqueue(passenger)
            else:
                self.has_no_carry_ons.enqueue(passenger)

        print("The aircraft has landed." +
              "\nPassengers are disembarking...")
        while not (self.has_no_carry_ons.is_empty()):
            print(self.has_no_carry_ons.peek())
            self.has_no_carry_ons.dequeue()

        while not (self.has_carry_ons.is_empty()):
            print(self.has_carry_ons.peek())
            self.has_carry_ons.dequeue()

    def is_empty(self) -> bool:
        """
        Checks if the zone (queue) is empty
        """
        return self.top == None

    def push(self, newValue: Any) -> None:
        """
        Adds new value to the stack.

        :param newValue: the value to be added in the stack
        """
        self.top = LinkedNode(newValue, self.top)
        self.passenger_counter += 1

    def pop(self) -> None:
        """
        Removes the last value from the stack
        """
        assert not self.is_empty(), "Pop from empty stack"
        self.top = self.top.link
        self.passenger_counter -= 1

    def peek(self) -> Any:
        """
        Returns the value of the link at the top.
        """
        assert not self.is_empty(), "peek on empty stack"
        return self.top.value

    insert = push
    remove = pop
