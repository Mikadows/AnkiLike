import tkinter
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import END

from core.Data import Data
from core.services.CardService import CardService
from core.utils.ValuesRatioLister import ValuesRatioLister
from ui.PlayerView import PlayerView
from ui.playerviews.QuestionController import QuestionController


class StatsView(tkinter.Frame):
    def __init__(self, deck_index, master=None, last_card=None, **kw):
        super().__init__(master, **kw)
        self.app = master
        self.clear()
        self.data = Data()
        self.current_deck = self.data.box.decks[deck_index]
        self.deck_index = deck_index
        self.cards = self.current_deck.cards

        # set card_service
        self.card_service = CardService()

        self.question_controller = QuestionController(deck_index, self.card_service, last_card)

        self.str_line = "_" * 20
        self.font_title = tkFont.Font(family="Lucida Grande", size=20)
        self.line = tkinter.Label(text=self.str_line, font=self.font_title)
        self.title = tkinter.Label(text="AnkiLike - Player Mode", font=self.font_title)

        self.deck_name = tkinter.Label(text="Stats of deck : " + self.current_deck.name, font=self.font_title)
        self.deck_name.config(font=("Lucida Grande", 15))
        self.global_validation_percent = len([c for c in self.current_deck.cards if c.validation_level == 4])/len(self.current_deck.cards)*100
        self.tmp = "{:.1f}".format(self.global_validation_percent)
        self.varLabel = tkinter.StringVar()
        self.varLabel.set("Global validation : " + self.tmp + " %")
        print(len(self.current_deck.cards), len([c for c in self.current_deck.cards if c.validation_level == 4]))
        print(self.global_validation_percent)
        self.percent_valid_label = tkinter.Label(textvariable=self.varLabel, font=("Lucida Grande", 12), fg='green')

        self.form_one = tkinter.Frame()
        self.label_choose = tkinter.Label(self.form_one, text="Validations levels : ")
        self.validations_levels = ttk.Combobox(self.form_one)
        self.validations_levels['values'] = [n for n in range(1, 5)]
        self.show_button = tkinter.Button(self.form_one, text="Show cards", command=self._refresh_card_list)
        self.list_cards = tkinter.Listbox()
        self.varCard = tkinter.StringVar()
        self.varCard.set('...')
        self.labelCardPercent = tkinter.Label(textvariable=self.varCard)
        self.reset_button = tkinter.Button(text="Reset validation level", command=self._reset_card)
        self.back_button = tkinter.Button(text="Return list decks", command=self._back_player_view)

        self._create_stats_deck_view()

    def _create_stats_deck_view(self):
        self.title.pack()
        self.line.pack()
        self.deck_name.pack(pady=10)
        self.percent_valid_label.pack()
        self.form_one.pack()
        self.label_choose.pack()
        self.show_button.pack()
        self.validations_levels.pack()
        self.list_cards.pack()
        self.labelCardPercent.pack()
        self.reset_button.pack(pady=10)
        self.back_button.pack(pady=10)

    def _back_player_view(self):
        PlayerView(self.app)

    def _reset_card(self):
        if self.list_cards.curselection() != ():
            card = [c for c in self.current_deck.cards if c.title == self.cards_selected[self.list_cards.curselection()[0]].title]
            card[0].validation_level = 0
            self._refresh_card_list()
            self.global_validation_percent = len([c for c in self.current_deck.cards if c.validation_level == 4]) / len(self.current_deck.cards) * 100
            self.tmp = "{:.1f}".format(self.global_validation_percent)
            self.varLabel.set("Global validation : " + self.tmp + " %")

    def _refresh_card_list(self):
        self.selected_validation_level = int(self.validations_levels.get())
        self.cards_selected = [c for c in self.current_deck.cards if c.validation_level == self.selected_validation_level]
        print(self.cards_selected)
        self.list_cards.delete(0, tkinter.END)
        [self.list_cards.insert(END, c.title) for c in self.cards_selected]
        self.list_cards.pack()
        self.local_validation_percent = len([c for c in self.current_deck.cards if c.validation_level == self.selected_validation_level]) / len(self.current_deck.cards) * 100
        self.tmp2 = "{:.1f}".format(self.local_validation_percent)
        self.varCard.set("Validate : " + self.tmp2 + " %")

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
