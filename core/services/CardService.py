import random

from core.Data import Data


class CardService:

    def __init__(self, data: Data):
        self._data = data

    def _get_data(self):
        return self._data

    def _set_data(self, data):
        self._data = data

    data = property(_get_data, _set_data)

    def get_card_randomly(self, deck_index):
        # TODO : Get card depend to all cards validation_level
        cards = self._data.box.decks[deck_index].cards
        random_value = random.uniform(0, len(cards) - 1)
        return cards[round(random_value)]
