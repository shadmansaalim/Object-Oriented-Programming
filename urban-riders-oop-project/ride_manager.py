class RideManager:
    def __init__(self) -> None:
        print("Ride Manager Activated")
        self.__available_vehicles = {"car": [], "bike": [], "tram": []}

    def add_vehicle(self, vehicle_type, vehicle):
        self.__available_vehicles[vehicle_type].append(vehicle)

    def get_available_vehicles(self, vehicle_type):
        return self.__available_vehicles[vehicle_type]

    def find_vehicle(self, passenger, vehicle_type, destination):
        available_vehicles = len(self.__available_vehicles[vehicle_type])
        if (available_vehicles == 0):
            print(f"Sorry no {vehicle_type}s are available right now")
            return False

        for vehicle in self.__available_vehicles[vehicle_type]:
            passenger_location = passenger.get_location()
            vehicle_location = vehicle.driver.location
            distance = abs(passenger_location - vehicle_location)
            if distance < 30 and vehicle.available == True:
                fare = vehicle.rate * distance
                if passenger.get_balance() < fare:
                    print("Insufficient balance to start the trip")
                    return False
                # Making the vehicle unavailable
                vehicle.available = False
                # Removing the vehicle from available list
                self.__available_vehicles[vehicle_type].remove(vehicle)
                # Starting the trip
                passenger.start_trip(fare)
                print(f"Found a {vehicle_type} match for you for fare ${fare}")
                return True


uber = RideManager()
