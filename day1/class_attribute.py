class Shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


buyer_one = Shop('Saalim Shadman')
buyer_one.add_to_cart('T-Shirt')
print(buyer_one.cart)

buyer_two = Shop('Ibnul Azraf')
buyer_two.add_to_cart('Shoe')
print(buyer_two.cart)
