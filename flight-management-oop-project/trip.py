class Trip:
    def __init__(self, trip_cities, departure_date) -> None:
        self.trip_cities = trip_cities
        self.departure_date = departure_date
        self.aircraft = None
        self.trip_route = None
        self.cost = None

    def __repr__(self) -> str:
        return f'Trip : {self.trip_cities} Aircraft: {self.aircraft} Route: {self.trip_route} Cost: {self.cost}'
