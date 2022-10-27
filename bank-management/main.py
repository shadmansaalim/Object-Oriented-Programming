"""Manages Bank Account"""


class Account:
    acc_id = 1

    def __init__(self, name, age, gov_id, balance) -> None:
        self.name = name
        self.age = age
        self.gov_id = gov_id
        self.balance = balance
        self.account_id = Account.acc_id

        # Update acc id
        Account.acc_id += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


acc_1 = Account("Saalim Shadman", 99, 101, 1000)
acc_2 = Account("Ibnul Azraf", 10, 24323, 420)

print(acc_1.account_id)
print(acc_2.account_id)
