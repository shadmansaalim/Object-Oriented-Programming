import hashlib


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('users.text', 'w') as file:
            file.write(f"{email} {pwd_encrypted}")
        file.close()
        print(f"{email} User Created Successfully")


saalim = User("Saalim Shadman", "abc123@gmail.com", "123456@")
