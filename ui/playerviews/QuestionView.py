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
        self.title.pack()
        self.line.pack()

        self.frame_menu = tkinter.LabelFrame(self.app, text="Question")
        self.frame_menu.pack(pady=20)

        self.back_btn = tkinter.Button(self.frame_menu, text="Back", command=self.load_back_view)

        self.deck_name = tkinter.Label(self.frame_menu, text="Deck name : " + deck.name, font=("Lucida Grande", 15))

        self.current_card = self.question_controller.draw_card()
        self.current_content = tkinter.Label(self.frame_menu, text=self.current_card.question, font=("Lucida Grande", 15))
        self.button_show_answer = tkinter.Button(self.frame_menu, text="Show Answer", command=self._call_show_answer)

        self._create_player_deck_view()

    def _create_player_deck_view(self):
        self.deck_name.pack()
        # self.current_content.pack()

    def _call_show_answer(self):
        # self.current_content.config()
        print("answer")

    def load_back_view(self):
        PlayerView(self.app)

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
