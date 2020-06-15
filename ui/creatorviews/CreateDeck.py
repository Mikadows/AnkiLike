# coding:utf-8
import tkinter
import tkinter.font as tkFont
import tkinter.ttk as ttk

from core.classes.Deck import Deck
from ui.CreatorView import CreatorView


class CreateDeck(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.app = master
        self.clear()
        self.create_view()

    def create_view(self):
        self.fontTitle = tkFont.Font(family="Lucida Grande", size=20)
        self.title = tkinter.Label(text="AnkiLike - Creator Mode", font=self.fontTitle)
        self.title.pack()

        self.str_line = "_"*20
        self.line = tkinter.Label(text=self.str_line, font=self.fontTitle)
        self.line.pack()

        self.frame_menu = tkinter.LabelFrame(self.app, text="Create Deck")
        self.frame_menu.pack(pady=20)

        self.form_one = tkinter.Frame(self.frame_menu)
        self.form_one.pack()

        self.label_name = tkinter.Label(self.form_one, text="Name : ")
        self.label_name.pack(side="left")
        self.var_name_entry = tkinter.StringVar()
        self.name_entry = tkinter.Entry(self.form_one, textvariable=self.var_name_entry)
        self.name_entry.pack(pady=10)


        self.save_btn = tkinter.Button(self.frame_menu, text="Save", command=self.save_deck)
        self.save_btn.pack(pady=10)

        self.back_btn = tkinter.Button(self.frame_menu, text="Back", command=self.load_back_view)
        self.back_btn.pack(padx=100, pady=25)

        self.confirm_text = tkinter.StringVar()
        self.confirm_label = tkinter.Label(self.app, textvariable=self.confirm_text)
        self.confirm_label.pack(pady=40)

    def save_deck(self):
        to_validate = self.var_name_entry.get()
        if not to_validate:
            self.confirm_text.set("Error : name cannot be blank")
            return

        new_deck = Deck(self.var_name_entry.get(), "n")
        print(new_deck._get_name())
        self.load_back_view()

    def load_back_view(self):
        CreatorView(self.app)

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
