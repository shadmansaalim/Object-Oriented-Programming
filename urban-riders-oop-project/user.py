import hashlib
from random import random, randint
from re import I
from vic_roads import VicRoads
from vehicles import Car, Bike, Tram
from ride_manager import uber
from os.path import exists

transport_authority = VicRoads()


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        file_exists = exists("users.text")
        with open('users.text', 'r+') as file:
            if (file_exists):
                lines = file.readlines()
                for line in lines:
                    if email in line:
                        return False
            file.write(f"{email} {pwd_encrypted}\n")
        file.close()
        print(f"{email} User Created Successfully")

    @staticmethod
    def login(email, password):
        stored_pass = ""
        with open('users.text', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_pass = line.split(' ')[1]
                    break
        file.close()
        if (len(stored_pass)):
            hashed_pwd = hashlib.md5(password.encode()).hexdigest()
            if (hashed_pwd == stored_pass):
                print(f"Successfully Logged In {email}")
                return True
            else:
                print("Invalid Password")
        else:
            print(f"No user exists with email {email}")
        return False


# A passenger is a user so inheritance concept of OOPS
class Passenger(User):
    def __init__(self, name, email, password, location, balance) -> None:
        super().__init__(name, email, password)
        # Private attributes
        self.__location = location
        self.__balance = balance

    # Setter
    def set_location(self, location):
        self.__location = location

    # Getter
    def get_location(self):
        return self.__location

    def request_trip(self, destination):
        pass

    def start_trip(self, fare):
        self.__balance -= fare
        pass


# A driver is a user so inheritance concept of OOPS
class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        super().__init__(name, email, password)
        # Private attributes
        self.location = location
        self.license = license
        self.verified = transport_authority.validate_license(email, license)
        self.__balance = 0

    def driving_test(self):
        result = transport_authority.driving_test(self.email)
        if result != False:
            self.license = result
            self.verified = True

    def register_vehicle(self, vehicle_type, vehicle_id, rate):
        if (self.verified):
            new_vehicle = None
            if vehicle_type == 'car':
                new_vehicle = Car(vehicle_id, vehicle_type, rate, self)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(vehicle_id, vehicle_type, rate, self)
            else:
                new_vehicle = Tram(vehicle_id, vehicle_type, rate, self)
            uber.add_vehicle(vehicle_type, new_vehicle)
        else:
            print("You cannot register a vehicle, please verify yourself first")

    def start_trip(self, destination, fare):
        self.__balance += fare
        self.location = destination

    def check_balance(self):
        return self.__balance


passenger1 = Passenger("Passenger1", "passenger1@gmail.com",
                       "abc1", randint(0, 40), 5000)
passenger2 = Passenger("Passenger2", "passenger2@gmail.com",
                       "abc2", randint(0, 40), 3000)

passenger3 = Passenger("Passenger23", "passenger3@gmail.com",
                       "abc3", randint(0, 40), 6000)


driver1 = Driver("Driver1", "driver1@gmail.com",
                 "drive1", randint(0, 40), 4345)
driver1.driving_test()
driver1.register_vehicle('car', 3213, 10)


driver2 = Driver("Driver2", "driver2@gmail.com",
                 "drive2", randint(0, 40), 5465)
driver2.driving_test()
driver2.register_vehicle('car', 345213, 10)


driver3 = Driver("Driver3", "driver3@gmail.com",
                 "drive3", randint(0, 40), 932932)
driver3.driving_test()
driver3.register_vehicle('bike', 9313, 10)


driver4 = Driver("Driver4", "driver4@gmail.com",
                 "drive4", randint(0, 40), 9984)
driver4.driving_test()
driver4.register_vehicle('tram', 34213, 10)

# print(uber.get_available_vehicles('car'))
# print(uber.get_available_vehicles('bike'))
# print(uber.get_available_vehicles('tram'))

uber.find_vehicle(passenger1, 'car', 90)