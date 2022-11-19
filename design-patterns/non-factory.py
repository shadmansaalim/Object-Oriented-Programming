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


b1 = Bike('Jawad', 5)
c1 = Car('Ahmed', 10)
t1 = Tram('Faraz', 8)

print(b1.get_fare(20))
print(c1.get_fare(20))
print(t1.get_fare(20))
