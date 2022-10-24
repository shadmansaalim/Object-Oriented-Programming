from abc import ABC, abstractmethod


# Abstract Base Class
class AbstractAnimalClass(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstra
    def name(self):
        pass

    @abstractmethod
    def move(self):
        print("Moving around")


class Monkey(AbstractAnimalClass):
    def sing(self):
        print("Monkey singing")

    def eat(self):
        print("Eating Banana")

    def move(self):
        print("Haning on tree branches")
        super().move()


m = Monkey()
print(m)
m.move()
