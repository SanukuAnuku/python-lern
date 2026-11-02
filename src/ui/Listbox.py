import tkinter as tk

class Listbox(tk.Frame):
    def __init__(self, master, width, height):
        super().__init__(master, bg="green", width=width, height=height)
        self.master = master
        self.pack()

    def add_to_list(self, content):
        self.insert(0, tk.END)

    def delete_list(self):
        self.delete(0, tk.END)