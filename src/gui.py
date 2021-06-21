import tkinter as tk


def create_search_frame(window):
    frame = tk.Frame(master=window)
    frame.pack()

    label_names = ['Title', 'Author', 'Genre']
    for indx, label_name in enumerate(label_names):
        tk.Label(master=frame, text=label_name, width=20).grid(row=0, column=indx)

    title_entr = tk.Entry(master=frame, width=20)
    title_entr.grid(row=1, column=0)

    author_entr = tk.Entry(master=frame, width=20)
    author_entr.grid(row=1, column=1)

    genre_entr = tk.Entry(master=frame, width=20)
    genre_entr.grid(row=1, column=2)

    search_btn = tk.Button(master=frame, text="Search", width=15)
    search_btn.grid(row=1, column=3)

    return title_entr, author_entr, genre_entr, search_btn


def create_results_frame(window):
    frame = tk.Frame(master=window)
    frame.pack()

    label_names = ['Title', 'Author', 'Genre', 'Floor', 'Shelf']
    for indx, label_name in enumerate(label_names):
        tk.Label(master=frame, text=label_name, width=15).grid(row=0, column=indx)

    return frame


def create_window():
    window = tk.Tk()

    title_entr, author_entr, genre_entr, search_btn = create_search_frame(window)
    results_frm = create_results_frame(window)

    return window, results_frm, title_entr, author_entr, genre_entr, search_btn


def destroy_table_body(results_frame):
    for widget in results_frame.winfo_children():
        if widget['text'] not in ['Title', 'Author', 'Genre', 'Floor', 'Shelf']:
            widget.destroy()


def populate_table(result, frm_results):
    for indx, item in enumerate(result):
        book, floor, shelf = item
        tk.Label(master=frm_results, text=book.title).grid(row=indx+1, column=0)
        tk.Label(master=frm_results, text=book.author).grid(row=indx + 1, column=1)
        tk.Label(master=frm_results, text=book.genre).grid(row=indx + 1, column=2)
        tk.Label(master=frm_results, text=floor).grid(row=indx + 1, column=3)
        tk.Label(master=frm_results, text=shelf).grid(row=indx + 1, column=4)

