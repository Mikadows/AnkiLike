# coding:utf-8
import json

from pathlib import Path
from tkinter import messagebox

from core.classes.Box import Box
from core.classes.Card import Card
from core.classes.Deck import Deck
from core.utils.BoxEncoder import BoxEncoder


class SaveService:

    def __init__(self):
        self.save_file_path = Path("save/save.json")

    def get_json_box(self, file_path):
        box = Box("AnkiLike", list())
        if file_path.exists():
            try:
                json_data = self.get_json_from_file(file_path)
                for deck in json_data['decks']:
                    new_deck = Deck(deck['_name'], list())
                    for card in deck['cards']:
                        new_card = Card(card['_title'], card['_question'], card['_answer'], card['_validation_level'])
                        new_deck.add_card(new_card)
                    box.add_deck(new_deck)
                return box
            except:
                messagebox.showwarning("Sauvegarde", "Vos données sont corrompues ou inexistantes")
                return box
        else:
            messagebox.showwarning("Sauvegarde", "Aucune sauvegarde trouvée")
            return box

    def get_json_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data

    def save_data(self, file_path, box):
        try:
            with open(file_path, 'w') as file:
                json.dump(box, file, cls=BoxEncoder)
                messagebox.showinfo("Sauvegarde", "Vos données ont été sauvegardées")
        except:
            messagebox.showerror("Sauvegarde", "Les données n'ont pas pu être sauvegardées")


