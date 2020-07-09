import unittest
from unittest.mock import MagicMock

from core.Data import Data
from core.classes.Box import Box
from core.classes.Card import Card
from core.classes.Deck import Deck
from core.services.CardService import CardService
from tests.test_helpers.DeckCreateHelper import DeckCreateHelper


class CardServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cards = []
        for i in range(5):
            self.cards.append(Card("card" + str(i), "question", "answer", i))
        self.deck = Deck("deck name to test card service", self.cards)
        self.data = Data()
        self.data.box = Box("box name", [self.deck])
        self.mock_values_ratio_lister = MagicMock()

        self.card_service = CardService()
        self.card_service.data = self.data
        self.card_service.deck_index = 0
        self.card_service.values_ratio_lister = self.mock_values_ratio_lister

        self.deck_create_helper = DeckCreateHelper(4)

    def test_update_validation_level_should_update_card_validation_level(self):
        current_validation_level = self.data.box.decks[0].cards[0].validation_level
        self.assertEqual(current_validation_level, 0)

        self.card_service.update_validation_level(0, 0, True)

        self.assertGreater(self.data.box.decks[0].cards[0].validation_level, current_validation_level)
        self.assertEqual(self.data.box.decks[0].cards[0].validation_level, current_validation_level + 1)

    def test_update_validation_level_should_put_to_minus1_when_card_is_not_validate(self):
        self.data.box.decks[0].cards[0].validation_level = 4

        self.card_service.update_validation_level(0, 0, False)

        self.assertEqual(self.data.box.decks[0].cards[0].validation_level, -1)

    def test_update_validation_level_should_not_update_when_validation_level_is_highest(self):
        self.data.box.decks[0].cards[0].validation_level = 4

        self.card_service.update_validation_level(0, 0, True)

        self.assertEqual(self.data.box.decks[0].cards[0].validation_level, 4)

    def test_update_validation_level_should_update_to_1_when_validation_level_is_minus1(self):
        self.data.box.decks[0].cards[0].validation_level = -1

        self.card_service.update_validation_level(0, 0, True)

        self.assertEqual(self.data.box.decks[0].cards[0].validation_level, 1)

    def test_get_card_randomly_should_return_card(self):
        self.mock_values_ratio_lister.get_values_ratio_list.return_value = [0] * 100
        self.assertIsInstance(self.card_service.get_card_randomly(), Card,
                              "incorrect type")

    # @mock.patch('random.uniform')
    # def test_get_card_randomly_should_retrieve_appropriate_random_value_depend_to_ratio_list(self, random_uniform_mock):
    #     self.mock_values_ratio_lister.get_values_ratio_list.return_value = [0] * 100
    #     random_uniform_mock.return_value = 2
    #
    #     self.card_service.get_card_randomly()
    #     random_uniform_mock.assert_called_with(0, 99)
    #
    # @mock.patch('random.uniform')
    # @mock.patch('random.choice')
    # def test_get_card_randomly_should_retrieve_appropriate_random_value_depend_to_ratio_list(self, random_uniform_mock):
    #     self.mock_values_ratio_lister.get_values_ratio_list.return_value = [0] * 100
    #     random_uniform_mock.return_value = 2
    #
    #     self.card_service.get_card_randomly()
    #     random_uniform_mock.assert_called_with(0, 99)
    #
    # @mock.patch('random.uniform')
    # @mock.patch('random.choice')
    # def test_get_card_randomly_should_return_card_with_validation_zero_when_one_card_in_deck(self, uniform_mock, choice_mock):
    #     self.mock_values_ratio_lister.get_values_ratio_list.side_effect = [[0] * 100, 0]
    #     self.data.box.decks[0] = self.deck_create_helper.create_deck_with_define_cards_validation_level([0, 2])
    #     self.cards = self.data.box.decks[0].cards
    #
    #     uniform_mock.return_value = 2
    #     choice_mock.return_value = 1
    #
    #     self.card_service.get_card_randomly()
    #
    #     choice_mock.assert_called_with(0, 99)

    # @mock.patch('random.uniform')
    # def test_get_card_randomly_should_return_card_
