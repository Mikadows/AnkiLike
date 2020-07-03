import tkinter
import tkinter.font as tkFont

from core.Data import Data
from core.classes import Deck
from core.services.CardService import CardService
from ui.PlayerView import PlayerView
from ui.playerviews.QuestionController import QuestionController


class QuestionView(tkinter.Frame):
    def __init__(self, deck: Deck, deck_index, master=None):
        self.app = master
        self.clear()
        self.data = Data()
        self.deck_index = deck_index
        self.cards = deck.cards

        self.question_controller = QuestionController(deck_index, CardService(self.data))

        self.str_line = "_" * 20
        self.font_title = tkFont.Font(family="Lucida Grande", size=20)
        self.line = tkinter.Label(text=self.str_line, font=self.font_title)
        self.title = tkinter.Label(text="AnkiLike - Player Mode", font=self.font_title)

        self.deck_name = tkinter.Label(text="Deck name : " + deck.name, font=self.font_title)
        self.deck_name.config(font=("Lucida Grande", 15))
        self.question_title = tkinter.Label(text="Question :", font=("Lucida Grande", 15))
        self.current_card = self.question_controller.draw_card()
        self.current_content = tkinter.Label(text=self.current_card.question, font=("Lucida Grande", 20))
        self.button_show_answer = tkinter.Button(text="Show answer", command=self._call_show_answer)
        self.back_button = tkinter.Button(text="Return list decks", command=self._back_player_view)
        self._create_player_deck_view()

    def _create_player_deck_view(self):
        self.title.pack()
        self.line.pack()
        self.deck_name.pack()
        self.question_title.pack()
        self.current_content.pack()
        self.button_show_answer.pack()
        self.back_button.pack()

    def _back_player_view(self):
        PlayerView(self.app)

    def _call_show_answer(self):
        self.current_content.config()

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
