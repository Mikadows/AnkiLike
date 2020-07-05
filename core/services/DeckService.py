from core.Data import Data
from core.classes import Deck


class DeckService:

    def __init__(self, data: Data):
        self.data = data

    def find_deck_by_index(self, index: int):
        try:
            return self.data.box.decks[index]
        except IndexError:
            return None

    def find_deck_by_name(self, name):
        decks = [e for e in self.data.box.decks]
        for d in decks:
            if d._get_name() == name:
                return d
        return None

    def rename_deck(self, deck, name):
        pos = self.find_deck_index(deck)
        self.data.box.decks[pos].name = name

    def add_deck(self, deck):
        self.data.box.add_deck(deck)

    def add_card_to_deck(self, deck, card):
        pos = self.find_deck_index(deck)
        self.data.box.decks[pos].add_card(card)

    def find_deck_index(self, deck):
        return self.data.box.decks.index(deck)

    def delete_deck(self, deck):
        self.data.box.decks.remove(deck)
        return

    def delete_card_in_deck(self, deck, card):
        pos = self.find_deck_index(deck)
        self.data.box.decks[pos].del_card(card)