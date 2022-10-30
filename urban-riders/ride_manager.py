class RideManager:
    def __init__(self) -> None:
        print("Ride Manager Activated")
        self.__available_vehicles = {"car": [], "bike": [], "tram": []}

    def add_vehicle(self, vehicle_type, vehicle):
        self.__available_vehicles[vehicle_type].append(vehicle)

    def get_available_vehicles(self, vehicle_type):
        return self.__available_vehicles[vehicle_type]

    def find_vehicle(self):
        pass


uber = RideManager()
