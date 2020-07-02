import random;

from core.Data import Data
from core.classes.Box import Box
from core.classes.Card import Card
from core.classes.Deck import Deck


class DataDummiesLoader:

    def box_load(self):
        box = Box("test box", [])
        count_deck = round(random.uniform(1, 5))
        for number_deck in range(count_deck):
            box.decks.append(self.deck_load(number_deck))
        return box

    def deck_load(self, nb_deck: int):
        new_deck = Deck("deck" + str(nb_deck), [])
        count_card = round(random.uniform(1, 10))
        for nb_card in range(count_card):
            new_deck.cards.append(self.deck_card(nb_card))
        return new_deck

    def deck_card(self, nb_card):
        new_card = Card("title" + str(nb_card), "question" + str(nb_card), "answser" + str(nb_card))
        new_card.validation_level = round(random.uniform(0, 5))
        return new_card
