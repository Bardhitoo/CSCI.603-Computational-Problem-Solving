"""
airit_simulation.py
Authors:
    Bardh Rushiti
    Prakhar Gupta

id: br3004, pg9349

This program is for CSCI -603 Assignment Week6
"""

from typing import Any
from Passenger import *
from Airplane import *
from Gate import *
import sys


def process_passengers(file_path: str) -> list:
    """
    Reads the passengers from the file_path provided

    :param file_path:   the path to the file
    :return:            list of passengers
    """
    from os import path

    if not path.exists(file_path):
        exit(f"File not found: {file_path}")

    passenger_list = []
    with open(file_path) as f:
        lines = f.readlines()

        for line in lines:
            passenger_list.append(line.strip('\n').split(','))

    return passenger_list


def process_inputs():
    """
    Promps the user for input for variables max_pass and max_pass_aircraft

    :return:    (max_pass, max_pass_aircraft)  maximum number of passengers in gate, and maximum number of
                                               passengers in aircraft
    """
    max_pass = -1
    while not max_pass > 0:
        try:
            max_pass = int(input("Please input the maximum number of passengers allowed at airline gate: "))
        except:
            print("Please input type<int> for the maximum number of passengers at airline gate")

    max_pass_aircraft = -1
    while not max_pass_aircraft > 0:
        try:
            max_pass_aircraft = int(
                input("Please input the maximum number of passengers allowed at airline aircraft: "))
        except:
            print("Please input type<int> for the maximum number of passengers")

    return max_pass, max_pass_aircraft


def boarding_deboarding(gate, max_passengers_in_aircraft):
    """
    Functions that boards and deboards passengers from the plane

    :param gate:                            gate with passengers
    :param max_passengers_in_aircraft:      maximum number of passengers in the aircraft
    """
    while not gate.is_empty():
        nzone = 3
        print("Passengers are boarding the aircraft...")

        airplane = Airplane(max_passengers_in_aircraft)
        count = 0
        while count < max_passengers_in_aircraft:
            while not gate.zones[nzone].is_empty():
                passeng = gate.zones[nzone].peek()
                gate.zones[nzone].dequeue()
                print(passeng)

                airplane.push(passeng)
                count += 1

                if count >= max_passengers_in_aircraft:
                    break

            if nzone > 0:
                nzone -= 1
            else:
                break

        print("The aircraft is full.")
        print("Ready for taking off ...")
        airplane.deboard()


def simulation(file_path):
    """
    The part that handles the simulation to the program

    :param file_path: the file_path provided by the user
    """

    processed_passengers = process_passengers(file_path)

    print("Beginning simulation...")
    max_passengers_in_gate, max_passengers_in_aircraft = process_inputs()

    nzone = 4
    # Gate 0 has 4 zones with 10 passenger limit
    gate = Gate(gate_nr=0, n_zones=nzone,
                passenger_limit=max_passengers_in_gate)

    total_passengers = len(processed_passengers)

    limit_of_passengers_in_aircraft = total_passengers // max_passengers_in_gate

    for passenger_in_aircraft in range(0, limit_of_passengers_in_aircraft + 1):

        print("Passengers are lining up at the gate...")
        passenger_cntr = 0

        if passenger_in_aircraft < limit_of_passengers_in_aircraft:
            for passenger in processed_passengers[max_passengers_in_gate * passenger_in_aircraft:]:
                if passenger_cntr < max_passengers_in_gate:
                    # print(passenger)
                    p = Passenger(passenger[0], passenger[1], passenger[2] == "True")
                    print(p)
                    gate.add_passenger(p)

                    passenger_cntr += 1

            print("The gate is full; remaining passengers must wait.")
            boarding_deboarding(gate, max_passengers_in_aircraft)
        else:
            for passenger in processed_passengers[max_passengers_in_gate * passenger_in_aircraft:]:
                if passenger_cntr < max_passengers_in_gate:
                    p = Passenger(passenger[0], passenger[1], passenger[2] == "True")
                    gate.add_passenger(p)
                    print(p)
                    passenger_cntr += 1
            # print(gate)
            print("Last Passenger in line")
            boarding_deboarding(gate, max_passengers_in_aircraft)
            print("No more passenger")


def main():
    """
    The main function
    """
    simulation(sys.argv[1])


if __name__ == '__main__':
    main()
