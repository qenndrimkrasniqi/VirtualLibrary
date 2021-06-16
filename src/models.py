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



