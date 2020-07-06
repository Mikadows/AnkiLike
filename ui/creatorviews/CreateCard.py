# coding:utf-8
import tkinter
import tkinter.font as tkFont
import tkinter.ttk as ttk


from core.Data import Data
from core.classes.Card import Card
from core.classes.Deck import Deck
from core.services.DeckService import DeckService
from ui.CreatorView import CreatorView


class CreateCard(tkinter.Frame):
    def __init__(self, selectedDeck, master=None):
        super().__init__(master)
        self.selectedDeck = selectedDeck
        self.app = master
        self.clear()

        self.deckService = DeckService(Data())

        self.fontTitle = tkFont.Font(family="Lucida Grande", size=20)
        self.title = tkinter.Label(text="AnkiLike - Creator Mode", font=self.fontTitle)
        self.str_line = "_" * 20
        self.str_deck = tkinter.Label(text="Add card to deck : "+self.selectedDeck.name)
        self.line = tkinter.Label(text=self.str_line, font=self.fontTitle)
        self.frame_menu = tkinter.LabelFrame(self.app, text="Create card")
        self.form_one = tkinter.Frame(self.frame_menu)
        self.form_two = tkinter.Frame(self.frame_menu)
        self.form_three = tkinter.Frame(self.frame_menu)

        self.label_title = tkinter.Label(self.form_one, text="Title : ")
        self.var_title_entry = tkinter.StringVar()
        self.title_entry = tkinter.Entry(self.form_one, textvariable=self.var_title_entry)

        self.label_quest = tkinter.Label(self.form_two, text="Question : ")
        self.var_quest_entry = tkinter.StringVar()
        self.quest_entry = tkinter.Entry(self.form_two, textvariable=self.var_quest_entry)

        self.label_answer = tkinter.Label(self.form_three, text="Answer : ")
        self.var_answer_entry = tkinter.StringVar()
        self.answer_entry = tkinter.Entry(self.form_three, textvariable=self.var_answer_entry)

        self.save_btn = tkinter.Button(self.frame_menu, text="Save", command=self.save_card)
        self.back_btn = tkinter.Button(self.frame_menu, text="Back", command=self.load_back_view)
        self.error_text = tkinter.StringVar()
        self.error_label = tkinter.Label(self.app, textvariable=self.error_text)

        self.create_view()

    def create_view(self):
        self.title.pack()
        self.line.pack()
        self.str_deck.pack()
        self.frame_menu.pack(pady=20)
        self.form_one.pack()
        self.form_two.pack()
        self.form_three.pack()
        self.label_title.pack(side="left")
        self.title_entry.pack(pady=10)
        self.label_quest.pack(side="left")
        self.quest_entry.pack(pady=10)
        self.label_answer.pack(side="left")
        self.answer_entry.pack(pady=10)
        self.save_btn.pack(pady=10)
        self.back_btn.pack(padx=100, pady=25)
        self.error_label.pack(pady=40)

    def save_card(self):
        if not self.var_title_entry.get() or not self.var_quest_entry.get() or not self.var_answer_entry.get():
            self.error_text.set("Error : you need to complete every field")
            return

        card = Card(self.var_title_entry.get(), self.var_quest_entry.get(), self.var_answer_entry.get())
        self.deckService.add_card_to_deck(self.selectedDeck, card)
        self.load_back_view()

    def load_back_view(self):
        from ui.creatorviews.CardManagement import CardManagement
        CardManagement(self.selectedDeck, master=self.app)

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
