from abc import ABC, abstractmethod


# Abstract class
class Vehicles(ABC):
    speeds = {"car": 30, "bike": 50, "tram": 40}

    def __init__(self, vehicle_type, rate, driver) -> None:
        super().__init__()
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.driver = driver
        self.speed = self.speeds[vehicle_type]

    @abstractmethod
    def start_driving(self):
        pass

    @abstractmethod
    def trip_completed(self):
        pass
