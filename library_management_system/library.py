from dbm.ndbm import library


class User:
    def __init__(self, name, id, password):
        self.name = name
        self.id = id
        self.password = password
        self.books_borrowed = []
        self.books_returned = []


class Library:
    def __init__(self, books_collection):
        self.books_collection = books_collection

    def borrow_book(self, book_name, user):
        for book in self.books_collection:
            if book == book_name:
                if book_name in user.books_borrowed:
                    print("You already have this book with you.")
                    return
                if self.books_collection[book] == 0:
                    print("Book out of stock, please come again later.")
                    return
                self.books_collection[book] -= 1
                user.books_borrowed.append(book_name)
                print("Take your book")
                return

        print(f"We don't have the book {book_name} in our library.")
        return


my_library = Library({"English": 2, "History": 5, "Math": 3})

users_list = []
current_user = None

while True:
    if current_user == None:
        print("Not Logged In - Please Login or Create an account : (L/C)")
        option = input()
        if (option == "L"):
            id = int(input("Enter your id : "))
            password = input("Enter password : ")

            user_found = False
            for user in users_list:
                if (user.id == id and user.password == password):
                    current_user = user
                    user_found = True

            if (user_found == False):
                print("No user found with given id and password")

        else:
            name = input("Enter your name : ")
            id = int(input("Enter your id : "))
            password = input("Enter your password : ")
            user = User(name, id, password)
            current_user = user
            # users_list.append(current_user)
    else:
        print("OPTIONS")
        print("_________")
        print("1. Borrow a book")
        my_library.borrow_book("English", current_user)
        print(my_library.books_collection)
        print(current_user.books_borrowed)
        break
