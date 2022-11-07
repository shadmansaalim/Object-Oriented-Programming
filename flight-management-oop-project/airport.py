class Airport:
    def __init__(self, name, country, lat, long, rate) -> None:
        # Public Attributes
        self.name = name
        self.country = country
        self.lat = lat
        self.long = long
        # Private
        self.__rate = rate

    # Getter
    def get_rate(self):
        return self.__rate

    # Dunder
    def __repr__(self) -> str:
        return f'Airport {self.name} in {self.country} with {self.lat} latitude and {self.long} longitude having a rate of {self.rate}'
