import tkinter as tk


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