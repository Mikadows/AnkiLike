import tkinter
import tkinter.font as tkFont

from core.classes import Deck


class PlayerDeckView(tkinter.Frame):
    def __init__(self, deck: Deck, master=None):
        self.app = master
        self.clear()

        self.cards = deck.cards

        self.str_line = "_" * 20
        self.font_title = tkFont.Font(family="Lucida Grande", size=20)
        self.line = tkinter.Label(text=self.str_line, font=self.font_title)
        self.title = tkinter.Label(text="AnkiLike - Player Mode", font=self.font_title)

        self.deck_name = tkinter.Label(text="Deck name : " + deck.name, font=self.font_title)
        self.deck_name.config(font=("Lucida Grande", 15))

        self._create_player_deck_view()

    def _create_player_deck_view(self):
        self.title.pack()
        self.deck_name.pack()
        self.line.pack()

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
