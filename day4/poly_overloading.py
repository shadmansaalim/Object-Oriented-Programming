# print(max(12, 323, 43, 12, 3, 1323, 43, 231, 32))
# print(max([32, 32, 12, 3, 124, 43433]))
# print(max('A', 'B', 'Z'))


"""Method Overloading"""


def add(num1, num2, num3=0):
    return num1 + num2 + num3


print(add(12, 13))
print(add(12, 13, 50))


def add2(*args, **kwargs):
    pass


"""Operator Overloading"""
print(12 + 13)
print("Hello" + "Dev")


class Account:
    def __init__(self, holder, balance) -> None:
        self.holder = holder
        self.__balance = balance

    def __add__(self, other):
        return self.__balance + other.__balance


my_acc = Account("Saalim Shadman", 1000)
her_acc = Account("XYZ", 50000)

# This will work only because of the dunder magic method inside Account class
print(my_acc + her_acc)
