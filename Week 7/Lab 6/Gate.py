from Zone import *
from Passenger import *


class Gate:
    """
    Gate class that contains the information
    """
    __slots__ = "zones", "n_zones", "gate_nr", "passenger_limit", "gate_tracker"

    def __init__(self, gate_nr: int, n_zones: int, passenger_limit: int):
        """
        Class constructor for the gate

        :param zones:           the list with 4 zones (queues) in the plane
        :param n_zones:         the number of zones in the gate
        :param passenger_limit: the passenger limit
        """
        self.gate_tracker = 1
        self.gate_nr = gate_nr
        self.n_zones = n_zones
        self.passenger_limit = passenger_limit

        self.zones = []
        for i in range(1, n_zones + 1):
            self.zones.append(Zone(i, passenger_limit))

    def __str__(self):
        """
        Return a string representation of the contents of
        the gate with all the zones inside
        """
        print(f"Gate  {self.gate_nr}")
        for i in range(len(self.zones)):
            print("\t", str(self.zones[i]), "\n")
        return ""

    def is_empty(self):
        """
        Checks if any of the zones is empty is empty
        """
        flag = True
        for i in range(0, self.n_zones):
            if not (self.zones[i].is_empty()):
                flag = False
        return flag

    def add_passenger(self, passenger: Passenger):
        """
        Adds passengers to the gate.

        :param passenger: the passenger to be added to the gate (in the corresponding zone)

        """
        gate = int(passenger.ticket_number[0])
        self.zones[gate - 1].enqueue(passenger)
