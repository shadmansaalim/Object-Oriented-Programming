class Account:
    def __init__(self, holder, init_balance) -> None:
        self.holder = holder  # Public Attribute
        self._account_number = "SS1239"  # Protected Attribute
        self.__balance = init_balance   # Private Attribute

    def deposit(self, amount):
        print(f"Adding ${amount} to your account")
        self.__balance += amount

    def withdraw(self, amount):
        print(f"Withdrawing ${amount} from your account")
        self.__balance -= amount


class StudentAccount(Account):
    def __init__(self, holder, init_balance, school) -> None:
        super().__init__(holder, init_balance)
        self.school = school


saalim = StudentAccount("Saalim", 2000, "RMIT")

# Will not work as balance is created as private now
# print(saalim.balance)
saalim.deposit(3000)
# print(saalim.balance)
