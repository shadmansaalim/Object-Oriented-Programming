import csv
from airport import Airport


class Airports:
    def __init__(self) -> None:
        self.airports = None
        self.load_airport_data('./data/airport.csv')

    def load_airport_data(self, file_path):
        airports = {}
        with open(file_path, 'r', encoding="utf8") as file:
            lines = csv.reader(file)
            for line in lines:
                airport_code = line[4]
                airport_name = line[1]
                airport_city = line[2]
                airport_country = line[3]
                airport_lat = line[6]
                airport_long = line[7]
                airport_rate = 0
                # Using airport_code as dictionary key for each airport as the it is unique
                airports[airport_code] = Airport(
                    airport_code, airport_name, airport_city, airport_country, airport_lat, airport_long, airport_rate)
        self.airports = airports
        file.close()
