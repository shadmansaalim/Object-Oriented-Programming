# Laptop, Phone, Watch, Tablet

class Laptop:
    def __init__(self, brand, price, color, storage) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.storage = storage

    def run(self):
        print("Running the Laptop")

    def purchase(self, amount):
        if amount < self.price:
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
