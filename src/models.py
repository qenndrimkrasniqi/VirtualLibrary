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
