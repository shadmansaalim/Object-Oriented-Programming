from abc import ABC, abstractmethod


# Abstract Base Class
class AbstractAnimalClass(ABC):
    @abstractmethod
    def eat(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def move(self):
        print("Moving around")


class Monkey(AbstractAnimalClass):
    def __init__(self) -> None:
        super().__init__()
        self.__name = "B Monkey"

    def sing(self):
        print("Monkey singing")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def eat(self):
        print("Eating Banana")

    def move(self):
        print("Haning on tree branches")
        super().move()


m = Monkey()
print(m)
m.move()


print(m.name)
m.name = "ABC Monkey"
print(m.name)
