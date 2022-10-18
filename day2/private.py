class User:
    def __init__(self, name, password, phone):
        self.name = name

        # Private attributes by adding two underscores
        self.__password = password
        self.__phone = phone

    # Method Private
    def __get_password(self):
        print(self.__password)

    def user_login(self, name, password):
        if (name == self.name and password == self.__password):
            return True
        return False


saalim = User('Saalim Shadman', 'DSA-OOPS', '123456789')

# This will work as attribute is public
print(saalim.name)

# These will not work as the attributes are initialized as private

# print(saalim.password)
# print(saalim.phone)


print(saalim.user_login('Saalim Shadman', 'DSA'))
