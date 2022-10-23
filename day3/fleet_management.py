class Bus:
    company = "Melbourne City Bus"

    def __init__(self, license, route, driver) -> None:
        self.license = license
        self.route = route
        self.driver = driver
        self.trips = []

    def start_trip(self, start_time):
        self.trips.append(start_time)


class Driver:
    def __init__(self, name, phone, license, address, pay) -> None:
        self.name = name
        self.phone = phone
        self.license = license
        self.address = address
        self.pay = pay

    def drive(self, start, end):
        pass

    def take_vacation(self):
        pass

    def withdraw_salary(self):
        pass


class Passenger:
    def __init__(self, name, phone, destination) -> None:
        self.name = name
        self.phone = phone
        self.destination = destination

    def purchase_ticket(self, destination, amount):
        pass


class Manager:
    def __init__(self, name, phone, department) -> None:
        self.name = name
        self.phone = phone
        self.department = department


class Counter:
    def __init__(self, manager, location) -> None:
        pass
