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

    @staticmethod
    def login(email, password):
        stored_pass = ""
        with open('users.text', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_pass = line.split(' ')[1]
                    break
        file.close()
        if (len(stored_pass)):
            hashed_pwd = hashlib.md5(password.encode()).hexdigest()
            if (hashed_pwd == stored_pass):
                print(f"Successfully Logged In {email}")
            else:
                print("Invalid Password")
        else:
            print(f"No user exists with email {email}")


saalim = User("Saalim Shadman", "abc123@gmail.com", "123456@")

User.login("abc123@gmail.com", "123456@")
