class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.cart.append(product)

    def checkout(self, amount):
        price = 0
        for item in self.cart:
            price += item['price'] * item['quantity']

        if (amount < price):
            return f'You need to add more ${price - amount} to checkout successfully'
        elif (amount > price):
            return f'You added more ${amount - price} money mistakenly, your all items costs ${price}'
        else:
            self.cart = []
            return 'Order placed successfully'


shopping = Shopper('Apple Store')
shopping.add_to_cart('iPhone 14 pro', 1899, 2)
shopping.add_to_cart('Airpods', 200, 3)
shopping.add_to_cart('Apple Watch', 560, 5)

res = shopping.checkout(7198)
print(res)
