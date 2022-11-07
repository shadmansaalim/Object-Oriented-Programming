import csv


class Airports:
    def __init__(self) -> None:
        self.airports = None
        self.load_airport_data('./data/airport.csv')

    def load_airport_data(self, file_path):
        airports = {}
        with open(file_path, 'r') as file:
            lines = csv.reader(file)
            for line in lines:
                print(line)
        file.close()


Airports()
