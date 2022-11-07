class Aircraft:
    def __init__(self, make, code, category, flight_range) -> None:
        self.make = make
        self.code = code
        self.category = category
        self.flight_range = flight_range

    def get_make(self):
        return self.make

    # Dunder
    def __repr__(self) -> str:
        return f'Aircraft make: {self.make} code: {self.code} category: {self.category} range: {self.flight_range}'
