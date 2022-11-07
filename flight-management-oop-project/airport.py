class Airport:
    def __init__(self, name, country, lat, long, rate) -> None:
        self.name = name
        self.country = country
        self.lat = lat
        self.long = long
        self.rate = rate

    # Dunder
    def __repr__(self) -> str:
        return f'Airport {self.name} in {self.country} with {self.lat} latitude and {self.long} longitude having a rate of {self.rate}'
