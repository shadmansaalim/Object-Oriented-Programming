class Shopping:
    mall = 'Melbourne Central'
    hours = []

    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total = 0

    def opening_hour(cls, day):
        return cls.mall

    # This means this function doesn't depend on any property of this class
    @staticmethod
    def calc_item_total(x, y):
        return x*y

    def add_to_total(self, amount):
        self.total += amount

    def add_to_cart(self, item, price, quantity):
        self.items.append(item)
        item_total = self.calc_item_total(price, quantity)
        self.add_to_total(item_total)

    def checkout(self):
        pass


# Can do this because this is a static method means this function inside class can be treated as normal function that is outside
# print(Shopping.calc_item_total(43, 342))

# Cannot do this
# print(Shopping.add_to_total(1))

my_shopping = Shopping('Mark Zucku')
my_shopping.add_to_total(450)
print(my_shopping.total)
