class Airport:
    def __init__(self, code, name, city, country, lat, long, rate) -> None:
        # Public Attributes
        self.code = code
        self.name = name
        self.city = city
        self.country = country
        self.lat = lat
        self.long = long
        # Private
        self.__rate = rate

    # Getter
    def get_rate(self):
        return self.__rate

     # Setter
    def set_rate(self, amount):
        self.__rate = amount

    # Dunder
    def __repr__(self) -> str:
        return f'Airport {self.name} in {self.country} with {self.lat} latitude and {self.long} longitude having a rate of {self.rate}'
