import hashlib
from random import random, randint
from vic_roads import VicRoads
from vehicles import Car, Bike, Tram
from ride_manager import uber

transport_authority = VicRoads()


class UserAlreadyExists(Exception):
    def __init__(self, email, *args: object) -> None:
        super().__init__(*args)
        print(f'An user with {email} already exists cannot create.')


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        user_exists = False
        with open('users.text', 'r') as file:
            if email in file.read():
                user_exists = True
                # raise UserAlreadyExists(email)
        file.close()
        if (user_exists == False):
            with open('users.text', 'a') as file:
                file.write(f"{email} {pwd_encrypted}\n")
            file.close()
            # print(f"{email} User Created Successfully")

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
        self.__trip_history = []

    # Setter
    def set_location(self, location):
        self.__location = location

    # Getter
    def get_location(self):
        return self.__location

    def get_balance(self):
        return self.__balance

    def request_trip(self, destination):
        pass

    def get_trip_history(self):
        return self.__trip_history

    def start_trip(self, fare, trip_info):
        self.__balance -= fare
        self.__trip_history.append(trip_info)


# A driver is a user so inheritance concept of OOPS
class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        super().__init__(name, email, password)
        # Private attributes
        self.location = location
        self.license = license
        self.verified = transport_authority.validate_license(email, license)
        self.__balance = 0
        self.__trip_history = []

    def driving_test(self):
        result = transport_authority.driving_test(self.email)
        if result == False:
            self.license = None
        else:
            self.license = result
            self.verified = True

    def register_vehicle(self, vehicle_type, vehicle_id, rate):
        if (self.verified):
            self.vehicle = None
            if vehicle_type == 'car':
                self.vehicle = Car(vehicle_id, vehicle_type, rate, self)
            elif vehicle_type == 'bike':
                self.vehicle = Bike(vehicle_id, vehicle_type, rate, self)
            else:
                self.vehicle = Tram(vehicle_id, vehicle_type, rate, self)
            uber.add_vehicle(vehicle_type, self.vehicle)
        else:
            # print("You cannot register a vehicle, please verify yourself first")
            pass

    def get_trip_history(self):
        return self.__trip_history

    def start_trip(self, destination, fare, trip_info):
        self.__balance += fare
        self.location = destination
        self.__trip_history.append(trip_info)

    def get_balance(self):
        return self.__balance


passenger1 = Passenger("Passenger1", "passenger1@gmail.com",
                       "abc1", randint(0, 40), randint(1, 1000))
passenger2 = Passenger("Passenger2", "passenger2@gmail.com",
                       "abc2", randint(0, 40), randint(1, 1000))

passenger3 = Passenger("Passenger23", "passenger3@gmail.com",
                       "abc3", randint(0, 40), randint(1, 1000))


for i in range(1, 100):
    driver1 = Driver(f"Driver{i}", f"driver{i}@gmail.com",
                     f"drive{i}", randint(0, 100), randint(1000, 9999))
    driver1.driving_test()
    driver1.register_vehicle('car', randint(10000, 99999), 10)


# print(uber.get_available_vehicles('car'))
# print(uber.get_available_vehicles('bike'))
# print(uber.get_available_vehicles('tram'))

uber.find_vehicle(passenger1, 'car', randint(1, 200))
uber.find_vehicle(passenger1, 'car', randint(1, 200))
uber.find_vehicle(passenger1, 'car', randint(1, 200))
uber.find_vehicle(passenger1, 'car', randint(1, 200))
uber.find_vehicle(passenger1, 'car', randint(1, 200))

print(passenger1.get_trip_history())
print(uber.total_income())
