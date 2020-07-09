import random

from core.Data import Data
from core.utils.Singleton import Singleton
from core.utils.ValuesRatioLister import ValuesRatioLister


class CardService(Singleton):

    def __get_data(self):
        return self.__data

    def __set_data(self, data):
        self.__data = data

    data = property(__get_data, __set_data)

    def __get_values_ratio_lister(self) -> ValuesRatioLister:
        return self.__values_ratio_lister

    def __set_values_ratio_lister(self, values_ratio_lister: ValuesRatioLister):
        self.__values_ratio_lister = values_ratio_lister

    values_ratio_lister = property(__get_values_ratio_lister, __set_values_ratio_lister)

    def __get_deck_index(self):
        return self.__deck_index

    def __set_deck_index(self, deck_index):
        self.__deck_index = deck_index

    deck_index = property(__get_deck_index, __set_deck_index)

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

    def get_card_index_randomly(self):
        # TODO : Get card depend to all cards validation_level
        vl_present_list = self.__get_validation_levels_present_in_cards()
        vl_ratio_list = self.__values_ratio_lister.get_values_ratio_list(vl_present_list)
        vl_select = vl_ratio_list[round(random.uniform(0, len(vl_ratio_list) - 1))]
        cards = self.__data.box.decks[self.deck_index].cards
        return cards[0]

    def __get_validation_levels_present_in_cards(self):
        result = []
        vl_list = [card.validation_level for card in self.__data.box.decks[self.deck_index].cards]

        [result.append(vl) for vl in vl_list if vl not in result]

        return result
