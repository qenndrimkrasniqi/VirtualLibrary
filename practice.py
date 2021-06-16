import os

from src.models import Book

source_path = './Data/Hivzi Sylejmani - Prishtinë/1. Floor/1. Shelf - Tragedy/1. Of Mice and Men - John Steinbeck.txt'
basename = os.path.basename(source_path)
number = int(basename.split('.')[0])
title_author = basename.split('.')[1]
title, author = title_author.split('-')

shelf = source_path.split('/')[-2]
genre = shelf.split('-')[-1]

book = Book(source_path, number, title.strip(), author.strip(), genre.strip())
print(book)