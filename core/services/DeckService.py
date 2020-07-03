from core.Data import Data
from core.utils.Singleton import Singleton


class DeckService:

    def __init__(self, data: Data):
        self.data = data

    def get_deck(self, index: int):
        return self.box.decks
