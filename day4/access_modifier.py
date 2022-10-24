# Public Protected Private
class Account:
    def __init__(self, holder) -> None:
        self._account_holder = holder


class StudentAccount(Account):
    def __init__(self, holder, balance, school) -> None:
        self.__balance = balance
        super().__init__(holder)

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient Balance"
        self.__balance -= amount
        return amount

    def deposit(self, amount):
        if amount < 0:
            return "Negative amount cannot be deposited"
        self.__balance += amount

    def get_balance(self):
        return self.__balance


saalim = StudentAccount("Saalim", 10000, "RMIT")
print(saalim.get_balance())

print(saalim._StudentAccount__balance)
