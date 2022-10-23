class Vehicle:
    def __init__(self, name, license, price) -> None:
        self.name = name
        self.license = license
        self.price = price

    def start(self):
        print(f"{self.name} Started")


class Bus(Vehicle):
    def __init__(self, name, license, price, seat, ticket_price) -> None:
        super().__init__(name, license, price)
        self.seat = seat
        self.available_seats = seat
        self.ticket_price = ticket_price

    def sell_ticket(self, customer_name, quantity, amount):
        self.available_seats -= quantity
        remaining = amount - self.ticket_price*quantity
        if remaining >= 0:
            return Ticket(customer_name)
        return "No ticket for you, you provided less than ticket price"


class LuxuryBus(Bus):
    def __init__(self, name, license, price, seat, ticket_price) -> None:
        super().__init__(name, license, price, seat, ticket_price)


class MiniBus(Bus):
    def __init__(self, name, license, price, seat, ticket_price) -> None:
        super().__init__(name, license, price, seat, ticket_price)


class Ticket:
    def __init__(self, owner) -> None:
        self.owner = owner


mini = MiniBus("Mini 001", "MELB123", 60000, 50, 100)
print(mini.name)
