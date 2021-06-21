import os

from gui import create_window, populate_table, destroy_table_body
from models import Library, Librarian


source_path = '../Data/Hivzi Sylejmani - Prishtinë'
basename = os.path.basename(source_path)
name, location = basename.split('-')

library = Library(source_path, name.strip(), location.strip())

librarian = Librarian('Sherif', library)

window, results_frm, title_entr, author_entr, genre_entr, search_btn = create_window()

def get_data(e, title, author, genre):
    books = librarian.get_books(title.get(), author.get(), genre.get())
    destroy_table_body(results_frm)
    populate_table(books, results_frm)


search_btn.bind("<Button-1>", lambda event, title=title_entr, author=author_entr, genre=genre_entr:get_data(event, title, author, genre))

window.mainloop()