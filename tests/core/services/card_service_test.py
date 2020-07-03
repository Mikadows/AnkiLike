import unittest
import mock as mock

from core.Data import Data
from core.classes.Box import Box
from core.classes.Card import Card
from core.classes.Deck import Deck
from core.services.CardService import CardService


class CardServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cards = []
        for i in range(5):
            self.cards.append(Card("card" + str(i), "question", "answer", i))
        self.deck = Deck("deck name to test card service", self.cards)
        self.data = Data()
        self.data.box = Box("box name", [self.deck])

        self.card_service = CardService(self.data)

    def test_get_card_randomly_should_return_card(self):
        self.assertIsInstance(self.card_service.get_card_randomly(0), Card,
                              "incorrect card instance")

    @mock.patch('random.uniform')
    def test_get_card_randomly_should_retrieve_appropriate_random_value(self, random_uniform_mock):
        current_cards_len = len(self.cards)
        self.card_service.get_card_randomly(0)
        random_uniform_mock.assert_called_with(0, current_cards_len - 1)

        self.data.box.decks[0].cards.append(Card("new card", "question", "answer", 0))

        self.card_service.data = self.data

        self.card_service.get_card_randomly(0)
        random_uniform_mock.assert_called_with(0, current_cards_len)

    @mock.patch('random.uniform')
    def test_get_card_randomly_should_return_appropriate_card(self, random_uniform_mock):
        random_uniform_mock.return_value = 2

        result = self.card_service.get_card_randomly(0)

        self.assertEqual(result, self.cards[2])

