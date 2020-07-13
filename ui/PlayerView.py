# coding:utf-8
import tkinter
import tkinter.font as tkFont
from tkinter import END

from core.Data import Data
from core.services.DeckService import DeckService
from ui.PlayerController import PlayerController


class PlayerView(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.app = master
        self.clear()
        self.data = Data()
        self.player_controller = PlayerController(DeckService(self.data))

        self.str_line = "_" * 20
        self.fontTitle = tkFont.Font(family="Lucida Grande", size=20)
        self.line = tkinter.Label(text=self.str_line, font=self.fontTitle)
        self.title = tkinter.Label(text="AnkiLike - Player Mode", font=self.fontTitle)

        self.list_decks = tkinter.Listbox()

        self.play_deck_button = tkinter.Button(text="Play deck", command=self._call_play_button)
        self.error_deck_no_card_label = tkinter.Label(text="The deck has no card", font=("Lucida Grande", 15), fg="red")

        self.stat_deck_button = tkinter.Button(text="Stats of deck", command=self._call_stat)

        self.create_view()

    def _call_stat(self):
        if self.list_decks.curselection() != ():
            current_deck_index = self.list_decks.index(self.list_decks.curselection())
            if self.data.box.decks[current_deck_index].cards:
                self.player_controller.stats(self.app, current_deck_index)
            else:
                self.error_deck_no_card_label.config(text="The deck '{}' has no card".format(self.data.box.decks[current_deck_index].name))
                self.error_deck_no_card_label.pack()

    def _call_play_button(self):
        if self.list_decks.curselection() != ():
            current_deck_index = self.list_decks.index(self.list_decks.curselection())
            if self.data.box.decks[current_deck_index].cards:
                self.player_controller.play(self.app, current_deck_index)
            else:
                self.error_deck_no_card_label.config(text="The deck '{}' has no card".format(self.data.box.decks[current_deck_index].name))
                self.error_deck_no_card_label.pack()

    def create_view(self):
        self.title.pack()
        self.line.pack()
        if self.data.box.decks is not None:
            [self.list_decks.insert(END, deck.name) for deck in self.data.box.decks]
        self.list_decks.pack(pady=15)

        self.play_deck_button.pack(pady=10)
        self.stat_deck_button.pack(pady=10)

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
