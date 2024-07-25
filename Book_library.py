"""This is a library system that keeps track of books using OOP"""
class Book:
    def __init__(self, title, author):
        self.title = title #properties
        self.author = author #properties
        self.available = True #properties
    def checkout(self): #method for the property of books
        if self.available:
            self.available = False
            return True
        else:
            return False
    def return_book(self): #method for the property of books
        self.available = True
    def display_info(self): #method for the property of books
        print(f"Book is {self.title}, written by {self.author}, and is available: {'Yes' if self.available else 'No'}")

#Class variables
book1 = Book("The Hitchhikers Guide to the Galaxy", "Douglas Adams")
book2 = Book("Malinche", "Laura Esquivel")
book3 = Book("One Day", "David Nicholls")
#Class list
books = [book1, book2, book3]

for book in books: #loop to display book info
    book.display_info()