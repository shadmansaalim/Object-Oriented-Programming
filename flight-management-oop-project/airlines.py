import csv
from aircraft import Aircraft


class Airlines:
    def __init__(self) -> None:
        self.aircrafts = None
        self.load_aircrafts_data('./data/aircraft.csv')

    def load_aircrafts_data(self, file_path):
        aircrafts = {}
        with open(file_path, 'r') as file:
            lines = csv.reader(file)
            # Ignoring the header with next method
            header = next(lines)

            # Creating aircrafts
            for line in lines:
                aircraft_code = line[0]
                aircraft_make = line[3]
                aircraft_category = line[1]
                aircraft_range = line[4]

                aircrafts[aircraft_code] = Aircraft(
                    aircraft_make, aircraft_code, aircraft_category, aircraft_range)
        self.aircrafts = aircrafts
        file.close()

    def get_aircraft(self, aircraft_code):
        return self.aircrafts[aircraft_code]

    def get_aircraft_by_distance(self, distance):
        aircraft = None
        for aircraft in self.aircrafts.values():
            if aircraft.flight_range < distance:
                return aircraft


Airlines()
