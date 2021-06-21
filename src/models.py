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


class Shelf:

    def __init__(self, source_path, number, genre):
        self.source_path = source_path
        self.number = number
        self.genre = genre
        self.books = []
        self.get_books()

    def __str__(self):
        return f"{self.number}. {self.genre}"

    def get_books(self):
        books = os.listdir(self.source_path)
        for book_name in books:
            book_path = os.path.join(self.source_path, book_name)
            number = int(book_name.split(".")[0])
            title = book_name.split("-")[0].split(".")[-1].strip()
            author = book_name.split("-")[-1].split(".")[0].strip()

            book = Book(book_path, number, title, author, self.genre)
            self.books.append(book)


class Floor:
    def __init__(self, source_path, number):
        self.source_path = source_path
        self.number = number
        self.shelves = []
        self.get_shelves()

    def __str__(self):
        return f"{self.number}"

    def get_shelves(self):
        shelves = os.listdir(self.source_path)
        for shelf_name in shelves:
            shelf_path = os.path.join(self.source_path, shelf_name)
            genre = shelf_name.split('-')[1].strip()
            number = int(shelf_name.split('.')[0])
            shelf = Shelf(shelf_path, number, genre)
            self.shelves.append(shelf)


class Library:
    def __init__(self, source_path, name, location):
        self.source_path = source_path
        self.name = name
        self.location = location
        self.floors = list()
        self.get_floors()

    def __str__(self):
        return self.name

    def get_floors(self):
        floors = os.listdir(self.source_path)
        for floor in floors:
            floor_path = os.path.join(self.source_path, floor)
            floor_number = int(floor.split('.')[0])
            floor = Floor(floor_path, floor_number)
            self.floors.append(floor)


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
