# coding:utf-8
import tkinter


class PlayerView(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.app = master
        self.clear()
        self.create_view()

    def create_view(self):
        self.title = tkinter.Label(text="AnkiLike - Player Mode")
        self.title.pack()

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
