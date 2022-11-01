from abc import ABC, abstractmethod


# Abstract class
class Vehicle(ABC):
    speeds = {"car": 30, "bike": 50, "tram": 40}

    def __init__(self, vehicle_id, vehicle_type, rate, driver) -> None:
        super().__init__()
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.driver = driver
        self.available = True
        self.speed = self.speeds[vehicle_type]

    @abstractmethod
    def start_driving(self):
        pass

    @abstractmethod
    def trip_completed(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_id, vehicle_type, rate, driver) -> None:
        super().__init__(vehicle_id, vehicle_type, rate, driver)

    def start_driving(self):
        self.available = False
        print(f"{self.vehicle_type} {self.vehicle_id} STARTED")

    def trip_completed(self):
        self.available = True
        print(f"{self.vehicle_type} {self.vehicle_id} COMPLETED")


class Bike(Vehicle):
    def __init__(self, vehicle_id, vehicle_type, rate, driver) -> None:
        super().__init__(vehicle_id, vehicle_type, rate, driver)

    def start_driving(self):
        self.available = False
        print(f"{self.vehicle_type} {self.vehicle_id} STARTED")

    def trip_completed(self):
        self.available = True
        print(f"{self.vehicle_type} {self.vehicle_id} COMPLETED")


class Tram(Vehicle):
    def __init__(self, vehicle_id, vehicle_type, rate, driver) -> None:
        super().__init__(vehicle_id, vehicle_type, rate, driver)

    def start_driving(self):
        self.available = False
        print(f"{self.vehicle_type} {self.vehicle_id} STARTED")

    def trip_completed(self):
        self.available = True
        print(f"{self.vehicle_type} {self.vehicle_id} COMPLETED")
