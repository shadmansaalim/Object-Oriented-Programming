class Laptop:
    def __init__(self, brand, age):
        self.brand = brand
        self.age = age

    def increase_age(self, age=1):
        self.last_age = self.age
        self.age += age

    def repair(self, life_increase=-5):
        self.increase_age(life_increase)


my_laptop = Laptop('Macbook', 20)
my_laptop.increase_age()
print(my_laptop.last_age, my_laptop.age)

my_laptop.repair()
print(my_laptop.last_age, my_laptop.age)

print(my_laptop.__dict__)
