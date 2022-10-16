class Phone:
    manufacturer = 'China'

    # Constructor that initializes an object
    def __init__(self, brand, price, color):
        # self is like this in C++
        self.brand = brand
        self.price = price
        self.color = color

    def send_sms(self, text, number):
        sms = f'Sending : {text} to Phone {number}'
        return sms


my_phone = Phone('Apple', '1899', 'Purple')
print(my_phone.brand, my_phone.manufacturer)

her_phone = Phone('Samsung', '1599', 'Black')
print(her_phone.brand, her_phone.manufacturer)
