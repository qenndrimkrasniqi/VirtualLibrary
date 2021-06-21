import os


class Book:
    def __init__(self, source_path, number, title, author, genre):
        self.source_path = source_path
        self.number = number
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"{self.number}. {self.title} - {self.author}"


class Librarian:
    def __init__(self, name, library):
        self.name = name
        self.library = library

    def __str__(self):
        return self.name

    def get_books(self, title=None, author=None, genre=None):
        books = []
        for floor in self.library.floors:
            for shelf in floor.shelves:
                for book in shelf.books:
                    if title == book.title:
                        books.append((book, floor.number, shelf.number))
                    elif author == book.author:
                        books.append((book, floor.number, shelf.number))
                    elif genre == book.genre:
                        books.append((book, floor.number, shelf.number))
        return books
