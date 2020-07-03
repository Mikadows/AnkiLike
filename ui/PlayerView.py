# coding:utf-8
import tkinter
import tkinter.font as tkFont
from tkinter import END

from core.Data import Data
from core.services.DeckService import DeckService


class PlayerView(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.app = master
        self.clear()
        self.data = Data()
        self.deck_service = DeckService(self.data)

        self.str_line = "_" * 20
        self.fontTitle = tkFont.Font(family="Lucida Grande", size=20)
        self.line = tkinter.Label(text=self.str_line, font=self.fontTitle)
        self.title = tkinter.Label(text="AnkiLike - Player Mode", font=self.fontTitle)
        self.title.pack()
        self.line.pack()

        self.frame_menu = tkinter.LabelFrame(self.app, text="List Decks")
        self.frame_menu.pack(pady=20)
        self.list_decks = tkinter.Listbox(self.frame_menu)
        self.play_deck_button = tkinter.Button(self.frame_menu, text="Play deck", command=self._call_play_button)
        self.create_view()

    def _call_play_button(self):
        current_deck_index = self.list_decks.index(self.list_decks.curselection())
        current_deck = self.deck_service.find_deck_by_index(current_deck_index)
        from ui.playerviews.QuestionView import QuestionView
        QuestionView(current_deck, current_deck_index, self.app)

    def create_view(self):
        if self.data.box.decks is not None:
            [self.list_decks.insert(END, deck.name) for deck in self.data.box.decks]
        self.list_decks.pack()

        self.play_deck_button.pack()

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
