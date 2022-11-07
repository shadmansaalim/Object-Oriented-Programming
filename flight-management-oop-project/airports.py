import csv
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


Airports()
