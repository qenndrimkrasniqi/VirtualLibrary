import os
import tkinter as tk

from models import Library, Librarian


def create_search_frame(window):
    frame = tk.Frame(master=window)
    frame.pack()

    label_names = ['Title', 'Author', 'Genre']
    for indx, label_name in enumerate(label_names):
        tk.Label(master=frame, text=label_name, width=20).grid(row=0, column=indx)

    for indx in range(len(label_names)):
        tk.Entry(master=frame, width=20).grid(row=1, column=indx)

    tk.Button(master=frame, text="Search", width=15).grid(row=1, column=3)

    return ""


def create_results_frame(window):
    frame = tk.Frame(master=window)
    frame.pack()

    label_names = ['Title', 'Author', 'Genre', 'Floor', 'Shelf']
    for indx, label_name in enumerate(label_names):
        tk.Label(master=frame, text=label_name, width=15).grid(row=0, column=indx)

    return frame


def create_window():
    window = tk.Tk()

    create_search_frame(window)
    results_frm = create_results_frame(window)

    return window, results_frm


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

