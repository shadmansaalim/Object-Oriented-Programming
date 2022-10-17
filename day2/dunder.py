# Dunder
# Magic Method
# Special Method
class Person:
    def __init__(self, name, age, cash):
        self.name = name
        self.age = age
        self.cash = cash

    def __add__(self, other):
        return self.cash + other.cash


saalim = Person('Saalim', 21, 5000)
ibnul = Person('Ibnul', 2, 1000)

print(saalim + ibnul)
