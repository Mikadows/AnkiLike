# coding:utf-8
import tkinter
import tkinter.font as tkFont
from core.Data import Data
from core.services.DeckService import DeckService


class RenameDeck(tkinter.Frame):
    def __init__(self, selectedDeck, master=None):
        super().__init__(master)
        self.selectedDeck = selectedDeck
        self.app = master
        self.clear()

        self.deckService = DeckService(Data())

        self.fontTitle = tkFont.Font(family="Lucida Grande", size=20)
        self.title = tkinter.Label(text="AnkiLike - Creator Mode", font=self.fontTitle)
        self.str_line = "_" * 20
        self.str_deck = tkinter.Label(text="Add card to deck : "+self.selectedDeck.name)
        self.line = tkinter.Label(text=self.str_line, font=self.fontTitle)
        self.frame_menu = tkinter.LabelFrame(self.app, text="Rename deck")
        self.form_one = tkinter.Frame(self.frame_menu)

        self.label_title = tkinter.Label(self.form_one, text="Deck name : ")
        self.var_title_entry = tkinter.StringVar()
        self.var_title_entry.set(self.selectedDeck.name)
        self.title_entry = tkinter.Entry(self.form_one, textvariable=self.var_title_entry)

        self.save_btn = tkinter.Button(self.frame_menu, text="Save", command=self.save_name)
        self.back_btn = tkinter.Button(self.frame_menu, text="Back", command=self.load_back_view)
        self.error_text = tkinter.StringVar()
        self.error_label = tkinter.Label(self.app, textvariable=self.error_text)

        self.create_view()

    def create_view(self):
        self.title.pack()
        self.line.pack()
        self.str_deck.pack()
        self.frame_menu.pack(pady=20)
        self.form_one.pack()
        self.label_title.pack(side="left")
        self.title_entry.pack(pady=10)
        self.save_btn.pack(pady=10)
        self.back_btn.pack(padx=100, pady=25)
        self.error_label.pack(pady=40)

    def save_name(self):
        if not self.var_title_entry.get():
            return
        self.deckService.rename_deck(self.selectedDeck, self.var_title_entry.get())
        self.load_back_view()

    def load_back_view(self):
        from ui.creatorviews.ManageDeck import ManageDeck
        ManageDeck(master=self.app)

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
