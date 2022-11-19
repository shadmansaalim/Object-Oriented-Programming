class Bike:
    def __init__(self, driver, rate) -> None:
        self.rate = rate
        self.driver = driver

    def get_fare(self, distance):
        return self.rate * distance


class Car:
    def __init__(self, driver, rate) -> None:
        self.rate = rate
        self.driver = driver

    def get_fare(self, distance):
        return self.rate * distance


class Tram:
    def __init__(self, driver, rate) -> None:
        self.rate = rate
        self.driver = driver

    def get_fare(self, distance):
        return self.rate * distance


def Factory(vehicle_type):
    vehicles = {
        'car': Car,
        'bike': Bike,
        'tram': Tram
    }
    return vehicles[vehicle_type]()
