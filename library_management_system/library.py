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


my_library = Library({"English": 2, "History": 5, "Math": 3})
