class RideManager:
    def __init__(self) -> None:
        print("Ride Manager Activated")
        self.__income = 0
        self.__available_vehicles = {"car": [], "bike": [], "tram": []}
        self.__trip_history = []

    def add_vehicle(self, vehicle_type, vehicle):
        self.__available_vehicles[vehicle_type].append(vehicle)

    def get_available_vehicles(self, vehicle_type):
        return self.__available_vehicles[vehicle_type]

    def total_income(self):
        return self.__income

    def trip_history(self):
        return self.__trip_history

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

                 # Storing trip history
                trip_info = {}
                trip_info['vehicle_type'] = vehicle_type
                trip_info['passenger'] = passenger.name
                trip_info['driver'] = vehicle.driver.name
                trip_info['from'] = passenger_location
                trip_info['to'] = destination
                trip_info['fare'] = fare

                self.__trip_history.append(trip_info)

                # Making the vehicle unavailable
                vehicle.available = False
                # Removing the vehicle from available list
                self.__available_vehicles[vehicle_type].remove(vehicle)

                # Starting the trip
                passenger.start_trip(fare, trip_info)

                # Giving 80% of the fare to driver and 20% to uber
                vehicle.driver.start_trip(
                    passenger_location, destination, fare*0.8, trip_info)
                self.__income += fare*0.2

                print(
                    f"Found a {vehicle_type} match for you for ${fare}. You will be assisted by {vehicle.driver.name}")
                return True


uber = RideManager()
