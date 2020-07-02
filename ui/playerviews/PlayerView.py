# coding:utf-8
import tkinter
import tkinter.font as tkFont


class PlayerView(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.app = master
        self.clear()
        self.player_controller = PlayerController()
        self.create_view()

    def create_view(self):
        self.fontTitle = tkFont.Font(family="Lucida Grande", size=20)
        self.title = tkinter.Label(text="AnkiLike - Player Mode", font=self.fontTitle)
        self.title.pack()

        self.str_line = "_"*20
        self.line = tkinter.Label(text=self.str_line, font=self.fontTitle)
        self.line.pack()

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
