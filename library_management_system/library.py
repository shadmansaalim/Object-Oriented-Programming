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
                print("Book borrowed successfully")
                return

        print(f"We don't have the book {book_name} in our library.")
        return

    def return_book(self, book_name, user):
        for book in self.books_collection:
            if book == book_name:
                if book in user.borrowed_books:
                    self.books_collection[book] += 1
                    user.books_borrowed.remove(book_name)
                    user.books_returned.append(book_name)
                    print("Thank you for returning the book to library ")
                    return
                else:
                    print("You never borrowed this book, please check.")

        print("This book is not from our library, please check.")
        return

    def get_available_books(self):
        available_books = []
        for book in self.books_collection:
            if (self.books_collection[book] > 0):
                available_books.append(book)

        return available_books

    def donate_book(self, book_name, quantity):
        print("Thanks for donating, we added the book in our library")
        for book in self.books_collection:
            if book == book_name:
                self.books_collection[book] += quantity
                return
        self.books_collection[book_name] = quantity


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
            users_list.append(current_user)
    else:
        print("OPTIONS")
        print("_________")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Show the books that I am borrowing from library now")
        print("4. Show the books that I have returned to library in the past")
        print("5. Show the books available in library")
        print("6. Donate a book in library")
        print("7. Logout")
        opt = int(input("Select Option : "))

        if (opt == 1):
            book_name = input(
                "Book Name that you want to borrow from library : ")
            my_library.borrow_book(book_name, current_user)
        elif (opt == 2):
            book_name = input(
                "Book Name that you want to return to library : ")
            my_library.return_book(book_name, current_user)
        elif opt == 3:
            print(current_user.books_borrowed)
        elif opt == 4:
            print(current_user.books_returned)
        elif opt == 5:
            available_books = my_library.get_available_books()
            print(available_books)
        elif opt == 6:
            book_name = input("Name of the book you want to donate : ")
            quantity = int(
                input(f"Number of {book_name} books you want to donate : "))
            my_library.donate_book(book_name, quantity)
        elif opt == 7:
            current_user = None
        print("\n")
