import unittest

from core.Data import Data
from core.classes.Box import Box
from core.classes.Card import Card
from core.classes.Deck import Deck
from core.services.DeckService import DeckService


class DeckServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.card = Card("card title", "question", "answer", 1)
        self.deck = Deck("deck name", [self.card])
        self.data = Data()
        self.data.box = Box("box name", [self.deck])

        self.deck_service = DeckService(self.data)

    def test_get_deck_should_return_deck_present_in_data_box(self):
        current_decks = self.data.box.decks
        current_decks.append(Deck("2nd deck", [self.card]))
        self.data.box.decks = current_decks

        self.assertIsInstance(self.deck_service.find_deck_by_index(0), Deck,
                              "incorrect deck instance")
        self.assertEqual(self.deck_service.find_deck_by_index(0), self.deck,
                         "incorrect deck value")
        self.assertEqual(self.deck_service.find_deck_by_index(1).name, "2nd deck",
                         "incorrect deck value")

    def test_get_decks_should_not_raise_exception_when_index_out_bound_number_decks(self):
        number_deck = len(self.data.box.decks)
        try:
            self.deck_service.find_deck_by_index(number_deck)
        except IndexError:
            self.fail("deck_service.get_deck({0}) raised IndexError unexpectedly!".format(number_deck))

    def test_get_decks_should_return_None_when_index_out_bound_number_decks(self):
        number_deck = len(self.data.box.decks)
        self.assertIsNone(self.deck_service.find_deck_by_index(number_deck),
                          "deck value is not None")
