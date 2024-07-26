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

class Library: #class to hold books
    def __init__(self):
        self.books = []
    def add_book(self, book): #method to add books
        self.books.append(book)
    def display_books(self): #method to display books
        for book in self.books:
            book.display_info()    
    def get_book_by_title(self, title): #method for titles
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
#instance of Library class    
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()