from random import randint, choice
from ride_manager import uber
from user import Passenger, Driver

# Creating Passenger Instances
passenger1 = Passenger("Passenger1", "passenger1@gmail.com",
                       "abc1", randint(0, 40), randint(1, 1000))
passenger2 = Passenger("Passenger2", "passenger2@gmail.com",
                       "abc2", randint(0, 40), randint(1, 1000))

passenger3 = Passenger("Passenger3", "passenger3@gmail.com",
                       "abc3", randint(0, 40), randint(1, 1000))


# Creating Driver Instances
for i in range(1, 100):
    driver1 = Driver(f"Driver{i}", f"driver{i}@gmail.com",
                     f"drive{i}", randint(0, 100), randint(1000, 9999))
    driver1.driving_test()
    driver1.register_vehicle(
        choice(['car', 'bike', 'tram']), randint(10000, 99999), 10)


# print(uber.get_available_vehicles('car'))
# print(uber.get_available_vehicles('bike'))
# print(uber.get_available_vehicles('tram'))

uber.find_vehicle(passenger1, choice(['car', 'bike', 'tram']), randint(1, 200))
uber.find_vehicle(passenger1, choice(['car', 'bike', 'tram']), randint(1, 200))
uber.find_vehicle(passenger1, choice(['car', 'bike', 'tram']), randint(1, 200))


print(passenger1.get_trip_history())
print(uber.total_income())
