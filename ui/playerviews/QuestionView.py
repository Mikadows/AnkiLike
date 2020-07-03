import tkinter
import tkinter.font as tkFont

from core.Data import Data
from core.classes import Deck
from core.services.CardService import CardService
from ui.PlayerView import PlayerView
from ui.playerviews.QuestionController import QuestionController


class QuestionView(tkinter.Frame):
    def __init__(self, deck_index, master=None):
        self.app = master
        self.clear()
        self.data = Data()
        self.current_deck = self.data.box.decks[deck_index]
        self.deck_index = deck_index
        self.cards = self.current_deck.cards

        self.question_controller = QuestionController(deck_index, CardService(self.data))

        self.str_line = "_" * 20
        self.font_title = tkFont.Font(family="Lucida Grande", size=20)
        self.line = tkinter.Label(text=self.str_line, font=self.font_title)
        self.title = tkinter.Label(text="AnkiLike - Player Mode", font=self.font_title)

        self.deck_name = tkinter.Label(text="Deck name : " + self.current_deck.name, font=self.font_title)
        self.deck_name.config(font=("Lucida Grande", 15))
        self.question_title = tkinter.Label(text="Question :", font=("Lucida Grande", 15))
        self.current_card = self.question_controller.draw_card()
        self.current_content = tkinter.Label(text=self.current_card.question, font=("Lucida Grande", 20))
        self.button_validate = tkinter.Button(text="Show answer", command=self._call_show_answer)
        self.button_not_validate = tkinter.Button(text="Not Validate", command=self._call_not_validate)
        self.back_button = tkinter.Button(text="Return list decks", command=self._back_player_view)
        self._create_player_deck_view()

    def _create_player_deck_view(self):
        self.title.pack()
        self.line.pack()
        self.deck_name.pack()
        self.question_title.pack()
        self.current_content.pack()
        self.button_validate.pack()
        self.back_button.pack()

    def _back_player_view(self):
        PlayerView(self.app)

    def _call_show_answer(self):
        self.back_button.pack_forget()

        self.question_title.configure(text="Answer :")
        self.current_content.configure(text=self.current_card.answer)
        self.button_validate.configure(text="Validate", command=self._call_validate)

        self.button_not_validate.pack()
        self.back_button.pack()

    def _call_validate(self):
        self.question_controller.update_card_validation_level(True, self.app)

    def _call_not_validate(self):
        self.question_controller.update_card_validation_level(False, self.app)

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
