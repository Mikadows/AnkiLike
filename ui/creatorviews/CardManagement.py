# coding:utf-8
import tkinter
import tkinter.font as tkFont
from core.Data import Data
from core.services.DeckService import DeckService
from ui.creatorviews.CreateCard import CreateCard
from ui.creatorviews.DeleteCard import DeleteCard
from ui.creatorviews.UpdateCardSelector import UpdateCardSelector


class CardManagement(tkinter.Frame):
    def __init__(self, selectedDeck, master=None):
        super().__init__(master)
        self.selectedDeck = selectedDeck
        self.app = master
        self.clear()

        self.deckService = DeckService(Data())

        self.fontTitle = tkFont.Font(family="Lucida Grande", size=20)
        self.title = tkinter.Label(text="AnkiLike - Creator Mode", font=self.fontTitle)
        self.str_line = "_" * 20
        self.str_deck = tkinter.Label(text="Card management of deck : " + self.selectedDeck.name)
        self.line = tkinter.Label(text=self.str_line, font=self.fontTitle)
        self.frame_menu = tkinter.LabelFrame(self.app, text="Deck management")
        self.create_card = tkinter.Button(self.frame_menu, text="Add card", command=self.load_add_card_view)
        self.update_card = tkinter.Button(self.frame_menu, text="Update card", command=self.load_update_card_view)
        self.delete_card = tkinter.Button(self.frame_menu, text="Delete card", command=self.load_del_card_view)
        self.back_btn = tkinter.Button(self.frame_menu, text="Back", command=self.load_back_view)

        self.create_view()

    def load_add_card_view(self):
        CreateCard(self.selectedDeck, master=self.app)

    def load_update_card_view(self):
        UpdateCardSelector(self.selectedDeck, master=self.app)

    def load_del_card_view(self):
        DeleteCard(self.selectedDeck, master=self.app)

    def create_view(self):
        self.title.pack()
        self.line.pack()
        self.str_deck.pack()
        self.frame_menu.pack(pady=20)
        self.create_card.pack(pady=10)
        self.update_card.pack(pady=10)
        self.delete_card.pack(pady=10)
        self.back_btn.pack(padx=100, pady=25)

    def load_back_view(self):
        from ui.creatorviews.ManageDeck import ManageDeck
        ManageDeck(self.app)

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
