# Poly -> Many
# Morph -> Different

# Here one plus sign is acting different for different condition
print(2+8)
print("Hello" + "World")
print([1, 2] + [3, 4])


# Overriding make_sound method below

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print("Animal Sound")


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Meow Meow")


class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Bark Bark")


class Horse(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Horseeeeee oo")


tom = Cat("Tommy")
german = Dog("German")
horsy = Horse("Horsy")

tom.make_sound()
german.make_sound()
horsy.make_sound()
