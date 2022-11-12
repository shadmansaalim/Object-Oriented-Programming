class Trip:
    def __init__(self, trip_cities, aircraft, price, departure_date, route=None) -> None:
        self.trip_cities = trip_cities
        self.aircraft = aircraft
        self.price = price
        self.departure_date = departure_date
        self.trip_route = route

    def __repr__(self) -> str:
        return f'Trip : {self.trip_cities} Aircraft: {self.aircraft} Route: {self.trip_route} Price: {self.price}'
