class User:
    def __init__(self, f_name, l_name):
        self.first = f_name
        self.last = l_name
        self.email = f'{f_name.lower()}{l_name.lower()}coding@user.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @full_name.setter
    def full_name(self, value):
        self.first = value.split(' ')[0]
        self.last = value.split(' ')[1]

    @full_name.deleter
    def full_name(self):
        del self.first
        del self.last

    def get_email(self):
        return self.email


saalim = User('Saalim', 'Shadman')
print(saalim.first)
print(saalim.last)
print(saalim.email)

print(saalim.get_email())

# Because of adding @property on top of full_name method the method is now treated as attributes like first,last,email
print(saalim.full_name)

# Setter
saalim.full_name = 'Stephen Hawking'

print(saalim.full_name)

del saalim.full_name
