from typing import Any

class Passenger:
    """
    Passenger class that contains the information for a passenger
    """
    __slots__ = "name", "ticket_number", "has_carry_on"
    name: str
    ticket_number: str
    has_carry_on: bool

    def __init__(self, name: str, ticket_number: str, has_carry_on: bool):
        """
        Class Passenger constructor, creates a passenger with a name, ticket number and checks if they have a carry-on
        """
        self.name = name
        self.ticket_number = ticket_number
        self.has_carry_on = has_carry_on

    def __str__(self):
        """
        Return a string representation of the contents of
        this stack, top value first.
        """
        return "Name: " + self.name + "\tTicket Number: " + self.ticket_number + "\tHas carry-on? " + str(
            self.has_carry_on)
