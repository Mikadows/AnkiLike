from core.classes.Deck import Deck


class CardSelector:

    def __init__(self, deck: Deck, ratio: float):
        self.__deck = deck
        self.__ratio = ratio

    def __get_deck(self):
        return self.__deck

    def __set_deck(self, deck: Deck):
        self.__deck = deck

    deck = property(__get_deck, __set_deck)

    def get_list_validations(self):
        cur_valid_level = self.__deck.cards[0].validation_level
        return [cur_valid_level] * 100
