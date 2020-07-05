# coding:utf-8
import tkinter
import tkinter.font as tkFont
import tkinter.ttk as ttk

from core.Data import Data
from core.services.DeckService import DeckService
from ui.CreatorView import CreatorView
from ui.creatorviews.UpdateCard import UpdateCard


class UpdateCardSelector(tkinter.Frame):
    def __init__(self, deck, master=None):
        super().__init__(master)
        self.app = master
        self.selectedDeck = deck
        self.data = Data()
        self.deckService = DeckService(Data())
        self.clear()

        self.fontTitle = tkFont.Font(family="Lucida Grande", size=20)
        self.title = tkinter.Label(text="AnkiLike - Creator Mode", font=self.fontTitle)
        self.str_line = "_"*20
        self.line = tkinter.Label(text=self.str_line, font=self.fontTitle)
        self.frame_menu = tkinter.LabelFrame(self.app, text="Update card")
        self.form_one = tkinter.Frame(self.frame_menu)
        self.label_choose = tkinter.Label(self.form_one, text="Choose card : ")
        self.tst = ttk.Combobox(self.form_one)
        self.tst['values'] = [c.title for c in self.selectedDeck._get_cards()]
        self.update_btn = tkinter.Button(self.frame_menu, text="Update", command=self.update)
        self.back_btn = tkinter.Button(self.frame_menu, text="Back", command=self.load_back_view)

        self.create_view()

    def create_view(self):
        self.title.pack()
        self.line.pack()
        self.frame_menu.pack(pady=20)
        self.form_one.pack()
        self.label_choose.pack(side="left", pady=15, padx=30)
        self.tst.pack(pady=15, padx=5)
        self.update_btn.pack(pady=10)
        self.back_btn.pack(padx=100, pady=25)

    def update(self):
        card_name = self.tst.get()
        for c in self.selectedDeck._get_cards():
            if c.title == card_name:
                UpdateCard(self.selectedDeck, c, master=self.app)
        return

    def load_back_view(self):
        from ui.creatorviews.CardManagement import CardManagement
        CardManagement(self.selectedDeck, self.app)

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
