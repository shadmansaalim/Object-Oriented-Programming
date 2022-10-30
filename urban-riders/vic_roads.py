import random


# Transport Authority
class VicRoads:
    def __init__(self) -> None:
        self.__license = {}

    def driving_test(self, email):
        score = random.randint(0, 100)
        if score > 30:
            print("Driving test passed successfully")
            license_number = random.randint(5000, 9999)
            self.__license[email] = license_number
            return license_number
        else:
            print("FAILED! Driving Test")
            return False

    def validate_license(self, email, license):
        if email in self.__license:
            return self.__license[email] == license
        return False
