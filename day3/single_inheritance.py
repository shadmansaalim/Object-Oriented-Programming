# Inheritance

# Base class,  will have only the common attributes and methods
class Device:
    def __init__(self, brand, price, color) -> None:
        self.brand = brand
        self.price = price
        self.color = color

    def repair(self):
        print("Ready to repair")

# Here after Laptop in bracket we are giving the Device class name which is telling the laptop class to inherit from Device class


class Laptop(Device):
    def __init__(self, brand, price, color, storage) -> None:
        # This line helps to initialise the base class attribute for particular this class
        super().__init__(brand, price, color)
        self.storage = storage

    def __repr__(self) -> str:
        return f"{self.brand} {self.__class__.__name__} : Price ${self.price} : Color {self.color}"

    def run(self):
        print("Running the Laptop")

    def purchase(self, amount, discount):
        if amount < (self.price - (self.price * discount/100)):
            return f"Please add ${self.price - amount} more to purchase {self.brand} {self.__class__.__name__}"
        else:
            print(f"{self.brand} {self.__class__.__name__} purchased successfully")
            return amount - self.price


class Phone:
    def __init__(self, brand, price, color, camera, sim_count) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.camera = camera
        self.sim_count = sim_count

    def __repr__(self) -> str:
        return f"{self.brand} {self.__class__.__name__} : Price ${self.price} : Color {self.color}"

    def is_dual_sim(self):
        return self.sim_count > 1

    def purchase(self, amount):
        if amount < self.price:
            return f"Please add ${self.price - amount} more to purchase {self.brand} {self.__class__.__name__}"
        else:
            print(f"{self.brand} {self.__class__.__name__} purchased successfully")
            return amount - self.price


class Watch:
    def __init__(self, brand, price, color, watch_type) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.watch_type = watch_type

    def is_digital(self):
        return self.watch_type == "digital"

    def purchase(self, amount):
        if amount < self.price:
            return f"Please add ${self.price - amount} more to purchase {self.brand} {self.__class__.__name__}"
        else:
            print(f"{self.brand} {self.__class__.__name__} purchased successfully")
            return amount - self.price


class Manager:
    def __init__(self, name, salary, experience, designation) -> None:
        pass

    def withdraw_salary(self):
        pass

    def calc_total_sales(self):
        pass

    def handle_customer_complaints(self):
        pass


class SalesPerson:
    def __init__(self, name, salary, experience, designation, commission) -> None:
        pass

    def withdraw_salary(self):
        pass

    def handle_customer(self):
        pass


mac = Laptop("Apple Mac", 2000, "Grey", "1TB")
hp = Laptop("HP", 1200, "Black", "256GB")

print(mac)
print(hp)

iPhone = Phone("Apple", 1899, "Purple", "48MXP", 1)
samsung = Phone("Samsung", 1199, "Black", "100MXP", 2)

print(iPhone)
print(samsung)

# Getting this repair method in laptop class because of inheritance from Device class
mac.repair()


print(mac.brand)
