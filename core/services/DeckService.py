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

    def add_deck(self, deck):
        self.data.box.add_deck(deck)
