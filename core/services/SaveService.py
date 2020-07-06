# coding:utf-8
import json

from pathlib import Path
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
                    new_deck = Deck(deck['name'], list())
                    for card in deck['cards']:
                        new_card = Card(card['title'], card['question'], card['answer'], card['validation_level'])
                        new_deck.add_card(new_card)
                    box.add_deck(new_deck)
                return box
            except:
                print('Error parsing saved data')
                return box
        else:
            print('No back-up found.')
            return box

    def get_json_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data

    def save_json_to_file(self, file_path, data):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file)
            return True
        except:
            print('Can\'t save data')
            return False

    def save_data(self, data):
        with open(self.save_file_path, 'w') as file:
            json.dump(data.box, file, cls=BoxEncoder)
