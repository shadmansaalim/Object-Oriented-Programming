class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if (amount > self.balance):
            return f"You don't have enough balance --> Your Balance : {self.balance}"
        elif (amount < self.min_withdraw):
            return f'You need to withdraw minimum {self.min_withdraw}$'
        elif (amount > self.max_withdraw):
            return f'You can withdraw up to {self.max_withdraw}$'
        else:
            self.balance -= amount
            return f'Withdrawn Successfully, Your current balance : {self.balance}'

    def deposit(self, amount):
        self.balance += amount


nab_bank = Bank(8000)
reply = nab_bank.withdraw(1000)
print(nab_bank.get_balance())
nab_bank.deposit(500)
print(nab_bank.get_balance())
