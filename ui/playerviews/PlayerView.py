# coding:utf-8
import tkinter
import tkinter.font as tkFont
from tkinter import END, ANCHOR

from core.Data import Data
from ui.playerviews.PlayerController import PlayerController


class PlayerView(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.app = master
        self.clear()
        self.data = Data()
        self.player_controller = PlayerController(self.data)

        self.str_line = "_" * 20
        self.fontTitle = tkFont.Font(family="Lucida Grande", size=20)
        self.line = tkinter.Label(text=self.str_line, font=self.fontTitle)
        self.title = tkinter.Label(text="AnkiLike - Player Mode", font=self.fontTitle)

        self.list_decks = tkinter.Listbox()

        self.play_deck_button = tkinter.Button(text="Play deck", command=self._call_play_button)

        self.create_view()

    def _call_play_button(self):
        self.player_controller.play(self.app, self.list_decks.index(self.list_decks.curselection()))

    def create_view(self):
        self.title.pack()

        self.line.pack()

        [self.list_decks.insert(END, deck.name) for deck in self.data.box.decks]
        self.list_decks.pack()

        self.play_deck_button.pack()

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
