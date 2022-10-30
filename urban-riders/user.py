import hashlib
from re import I
from vic_roads import VicRoads
from vehicles import Car, Bike, Tram
from ride_manager import uber


transport_authority = VicRoads()


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('users.text', 'w') as file:
            file.write(f"{email} {pwd_encrypted}")
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
                new_vehicle = Car(vehicle_type, vehicle_id, rate, self.email)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(vehicle_type, vehicle_id, rate, self.email)
            else:
                new_vehicle = Tram(vehicle_type, vehicle_id, rate, self.email)
            uber.add_vehicle(new_vehicle)
        else:
            print("You cannot register a vehicle, please verify yourself first")

    def start_trip(self, destination, fare):
        self.__balance += fare
        self.location = destination

    def check_balance(self):
        return self.__balance


saalim = User("Saalim Shadman", "abc123@gmail.com", "123456@")
User.login("abc123@gmail.com", "123456@")

jawad = Driver("Jawad Ahmed", "jawad123@gmail.com",
               "987654321", "339 Swanston Street", 9322)

print(transport_authority.validate_license(jawad.email, jawad.license))
jawad.driving_test()
print(transport_authority.validate_license(jawad.email, jawad.license))
print(jawad.license)
