# coding:utf-8
import tkinter
import tkinter.font as tkFont
import tkinter.ttk as ttk

from core.Data import Data
from core.classes.Deck import Deck
from core.services.DeckService import DeckService
from ui.CreatorView import CreatorView
from ui.creatorviews.CardManagement import CardManagement
from ui.creatorviews.RenameDeck import RenameDeck


class ManageDeck(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.app = master
        self.clear()
        self.data = Data()
        self.deckService = DeckService(Data())

        # Nominal view
        self.fontTitle = tkFont.Font(family="Lucida Grande", size=20)
        self.title = tkinter.Label(text="AnkiLike - Creator Mode", font=self.fontTitle)
        self.str_line = "_" * 20
        self.frame_menu = tkinter.LabelFrame(self.app, text="Deck Management")
        self.line = tkinter.Label(text=self.str_line, font=self.fontTitle)
        self.form_one = tkinter.Frame(self.frame_menu)
        self.label_choose = tkinter.Label(self.form_one, text="Choose your deck : ")
        self.tst = ttk.Combobox(self.form_one)
        self.tst['values'] = [d._get_name() for d in self.data.box.decks]
        self.save_btn = tkinter.Button(self.frame_menu, text="Manage cards", command=self.manage)
        self.rename_btn = tkinter.Button(self.frame_menu, text="Rename", command=self.rename_view)
        self.back_btn = tkinter.Button(self.frame_menu, text="Back", command=self.load_back_view)

        # Rename view
        self.clear()
        self.rename_label = tkinter.Label(self.form_one, text="Name : ")
        self.var_name_entry = tkinter.StringVar()
        self.input_rename = tkinter.Entry(self.form_one, textvariable=self.var_name_entry)

        self.create_view_nominal()

    def create_view_nominal(self):
        self.title.pack()
        self.line.pack()
        self.frame_menu.pack(pady=20)
        self.form_one.pack()
        self.label_choose.pack(side="left", pady=15, padx=30)
        self.tst.pack(pady=15, padx=5)
        self.save_btn.pack(pady=10)
        self.rename_btn.pack(pady=10)
        self.back_btn.pack(padx=100, pady=25)

    def rename_view(self):
        deck = self.deckService.find_deck_by_name(self.tst.get())
        if deck:
            RenameDeck(deck, self.app)

    def manage(self):
        deck = self.deckService.find_deck_by_name(self.tst.get())
        if deck:
            CardManagement(deck, master=self.app)

    def load_back_view(self):
        CreatorView(self.app)

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
