# Dunder
# Magic Method
# Special Method
class Person:
    def __init__(self, name, age, cash, height=65):
        self.name = name
        self.age = age
        self.cash = cash
        self.height = height

    def __add__(self, other):
        return self.cash + other.cash

    def __call__(self):
        print(
            f'Person name is {self.name} with age of {self.age}. {self.name} has ${self.cash}')

    def __eq__(self, other):
        return self.age == other.age

    def __len__(self):
        return self.height


saalim = Person('Saalim', 21, 5000, 72)
ibnul = Person('Ibnul', 21, 1000)

print(saalim + ibnul)

saalim()

is_age_equal = saalim == ibnul
print(is_age_equal)

print(len(saalim))
