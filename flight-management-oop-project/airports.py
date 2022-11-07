import csv
from math import radians, sin, cos, sqrt, atan2
from airport import Airport


class Airports:
    def __init__(self) -> None:
        self.airports = None
        self.load_airport_data('./data/airport.csv')

    def load_airport_data(self, file_path):
        airports = {}
        currency_rates = {}
        country_currency = {}

        with open('./data/currencyrates.csv', 'r') as file:
            lines = csv.reader(file)
            for line in lines:
                currency_short_form = line[1]
                currency_rate = line[2]
                currency_rates[currency_short_form] = currency_rate
        file.close()

        with open('./data/countrycurrency.csv', 'r') as file:
            lines = csv.reader(file)
            for line in lines:
                country_name = line[0]
                currency_alphabetic_code = line[1]
                country_currency[country_name] = currency_alphabetic_code
        file.close()

        # Creation of Airport
        with open(file_path, 'r', encoding="utf8") as file:
            lines = csv.reader(file)

            try:
                for line in lines:
                    airport_code = line[4]
                    airport_name = line[1]
                    airport_city = line[2]
                    airport_country = line[3]
                    airport_lat = line[6]
                    airport_long = line[7]

                    currency = country_currency[airport_country]
                    airport_rate = currency_rates[currency]

                    # Using airport_code as dictionary key for each airport as the it is unique
                    airports[airport_code] = Airport(
                        airport_code, airport_name, airport_city, airport_country, airport_lat, airport_long, airport_rate)
            except KeyError as e:
                print(e)

        self.airports = airports
        file.close()

    # Calculating distance between two gps location
    def get_distance_between_airports(self, lat1, long1, lat2, long2):
        radius = 6371  # KM
        lat_diff = radians(lat1 - lat2)
        long_diff = radians(long1 - long2)
        a = (sin(lat_diff / 2) * sin(lat_diff / 2) +
             cos(radians(lat1)) * cos(radians(lat2)) *
             sin(long_diff / 2) * sin(long_diff / 2))
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = radius * c
        return distance


Airports()
