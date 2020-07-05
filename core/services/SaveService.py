# coding:utf-8
import json
import os.path

from core.classes.Box import Box
from core.classes.Card import Card
from core.classes.Deck import Deck


class SaveService:

    def get_saved_box(self):
        if os.path.isfile('save/save.json'):
            with open("save/save.json", encoding='utf-8') as file:
                decks = self.get_saved_decks(file)
                if decks is None or len(decks) < 1:
                    print('No saved decks found.')
                    return
                else:
                    return Box("AnkiLike", decks)
        else:
            print('No back-up found.')
            return

    def get_saved_decks(self, json_file):
        decks = list()
        try:
            data = json.loads(json_file.read())
            saved_decks = data['decks']
            for deck in saved_decks:
                new_deck = Deck(deck['name'], [])
                for card in deck['cards']:
                    new_card = Card(card['title'], card['question'], card['answer'], card['validation_level'])
                    new_deck.add_card(new_card)
                decks.append(new_deck)
            return decks
        except:
            print('Wrong parsing, you are going to loose all your data :).')
            return
