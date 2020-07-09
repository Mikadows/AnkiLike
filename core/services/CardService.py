import random

from core.Data import Data
from core.utils.ValuesRatioLister import ValuesRatioLister


class CardService:

    def __init__(self, data: Data, values_ratio_lister: ValuesRatioLister):
        self._data = data
        self.__values_ratio_lister = values_ratio_lister

    def _get_data(self):
        return self._data

    def _set_data(self, data):
        self._data = data

    data = property(_get_data, _set_data)

    def update_validation_level(self, deck_index: int, card_index: int, is_validate: bool):
        current_box = self.data.box
        current_card = current_box.decks[deck_index].cards[card_index]
        if not is_validate:
            current_card.validation_level = -1
        elif current_card.validation_level == -1:
            current_card.validation_level = 1
        elif current_card.validation_level < 4:
            current_card.validation_level += 1
        current_box.decks[deck_index].cards[card_index] = current_card
        self.data.box = current_box

    def get_card_index_randomly(self, deck_index):
        # TODO : Get card depend to all cards validation_level
        cards = self._data.box.decks[deck_index].cards
        return round(random.uniform(0, len(cards) - 1))

    # def __get_validation_levels_present_in_cards(self):
    #     result = []
    #     vl_list = [card.validation_level for card in self.__values.cards]
    #
    #     [result.append(vl) for vl in vl_list if vl not in result]
    #
    #     return result
