from airit_simulation import *


def test_process_passengers():
    process_passengers('passengers_very_small.txt')
    # after this points the program ends
    # passengers_list = process_passengers('1passengers_very_small.txt')


def test_passenger():
    passengers_list = process_passengers('passengers_very_small.txt')
    for passenger in passengers_list:
        new_passenger = Passenger(passenger[0], passenger[1], passenger[2] == "True")
        print(new_passenger)


def test_gate():
    gate = Gate(gate_nr=0, n_zones=4, passenger_limit=10)
    assert gate.is_empty() == True

    # addition of passenger
    passenger = Passenger("Bardh", "1000023456", True)
    gate.add_passenger(passenger)
    assert len(gate.zones[0]) == 1


def test_zone():
    zone = Zone(zone_number=1, passenger_limit=10)
    assert zone.is_empty() == True
    assert len(zone) == 0

    passenger = Passenger("Prakhar", "20008904", False)
    zone.enqueue(passenger)
    assert zone.peek() == passenger
    assert len(zone) == 1
    assert zone.num_passenger == 1
    zone.dequeue()
    assert len(zone) == 0
    assert zone.num_passenger == 0
    assert zone.is_empty() == True


def test_airplaine():
    passenger = Passenger("Maria", "302348904", False)
    airplane = Airplane(5)
    assert airplane.is_empty() == True
    airplane.push(passenger)
    assert len(airplane) == 1
    airplane.pop()
    assert len(airplane) == 0


def test_process_inputs():
    max_pass, max_pass_aircraft = process_inputs()

    assert max_pass > 0, "max passenger should be a positive number"
    assert isinstance(max_pass, int), "max passenger should be an integer"

    assert max_pass_aircraft > 0, "max passenger in aircraft should be a positive number"
    assert isinstance(max_pass_aircraft, int), "max passenger in aircraft should be an integer"


def main():
    test_process_passengers()
    test_process_inputs()
    test_passenger()
    test_gate()
    test_zone()
    test_airplaine()
    print("\033[92mAll tests passed")


if "__main__" == __name__:
    main()
