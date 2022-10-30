class RideManager:
    def __init__(self) -> None:
        print("Ride Manager Activated")
        self.__available_vehicles = {"car": [], "bike": [], "tram": []}

    def add_vehicle(self, vehicle_type, vehicle):
        self.__available_vehicles[vehicle_type].append(vehicle)

    def match_vehicle(self):
        pass


uber = RideManager()
