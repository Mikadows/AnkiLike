import unittest

from core.classes.Card import Card
from core.classes.Deck import Deck
from core.utils.CardSelector import CardSelector


class CardSelectorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.__max_validation_level = 4
        deck = self.create_deck_with_define_cards_validation_level([5])
        self.__cardSelector = CardSelector(deck, 1 / 2)

    def test_get_list_validations_should_return_list_length_100(self):

        result = self.__cardSelector.get_list_validations()

        self.assertEqual(len(result), 100)

    def test_get_list_validations_should_return_list_same_number_when_cards_only_minus_one_validation_level(self):
        deck = self.__cardSelector.deck
        self.assertTrue(all(map(lambda card: card.validation_level == -1, deck.cards)))

        result = self.__cardSelector.get_list_validations()

        self.assertTrue(all(map(lambda number: number == -1, result)))

    def test_get_list_validations_should_return_list_same_number_when_cards_only_have_same_validation_level(self):
        self.__cardSelector.deck = self.create_deck_with_define_cards_validation_level([0, 4])
        result = self.__cardSelector.get_list_validations()
        self.assertTrue(all(map(lambda number: number == 0, result)))

        self.__cardSelector.deck = self.create_deck_with_define_cards_validation_level([0, 0, 3])
        result = self.__cardSelector.get_list_validations()
        self.assertTrue(all(map(lambda number: number == 1, result)))

    def test_get_list_validations_should_return_50_cards_when_ratio_half_and_2_different_validation_level(self):
        self.__cardSelector.deck = self.create_deck_with_define_cards_validation_level([2, 4])

        result = self.__cardSelector.get_list_validations()

        self.assertEqual(len([number for number in result if number == -1]), 50)
        self.assertEqual(len([number for number in result if number == 0]), 50)

    def test_get_list_validations_should_return_50_cards_when_ratio_half_and_2_not_successive_validation_level(self):
        self.__cardSelector.deck = self.create_deck_with_define_cards_validation_level([2, 0, 4])

        result = self.__cardSelector.get_list_validations()

        self.assertEqual(len([number for number in result if number == -1]), 50)
        self.assertEqual(len([number for number in result if number == 0]), 0)
        self.assertEqual(len([number for number in result if number == 1]), 50)

    def test_get_list_validations_should_return_two_thirds_lower_validation_level_and_manage_same_way_for_rest(self):
        self.__cardSelector.deck = self.create_deck_with_define_cards_validation_level([3, 1, 0, 4])
        self.__cardSelector.ratio = 3 / 4

        result = self.__cardSelector.get_list_validations()

        self.assertEqual(len([number for number in result if number == -1]), 75)
        self.assertEqual(len([number for number in result if number == 0]), 19)
        self.assertEqual(len([number for number in result if number == 1]), 0)
        self.assertEqual(len([number for number in result if number == 2]), 6)

    def test_get_list_validations_should_return_al_least_one_case(self):
        self.__cardSelector.deck = self.create_deck_with_define_cards_validation_level([3, 1, 2, 7, 4, 4])
        self.__cardSelector.ratio = 2 / 3

        result = self.__cardSelector.get_list_validations()

        self.assertEqual(len([number for number in result if number == -1]), 67)
        self.assertEqual(len([number for number in result if number == 0]), 22)
        self.assertEqual(len([number for number in result if number == 1]), 7)
        self.assertEqual(len([number for number in result if number == 2]), 2)
        self.assertEqual(len([number for number in result if number == 3]), 1)
        self.assertEqual(len([number for number in result if number == 4]), 1)

    def test_get_list_validations_should_return_only_validation_level_max_when_cards_contain_not_below_level(self):
        self.__cardSelector.deck = self.create_deck_with_define_cards_validation_level([0, 0, 0, 0, 0, 4])
        self.__cardSelector.ratio = 5 / 6

        result = self.__cardSelector.get_list_validations()

        self.assertEqual(len([number for number in result if number == -1]), 0)
        self.assertEqual(len([number for number in result if number == 0]), 0)
        self.assertEqual(len([number for number in result if number == 1]), 0)
        self.assertEqual(len([number for number in result if number == 2]), 0)
        self.assertEqual(len([number for number in result if number == 3]), 0)
        self.assertEqual(len([number for number in result if number == 4]), 100)

    def create_deck_with_define_cards_validation_level(self, levels) -> Deck:
        list_cards = []
        validation_level = -1

        for i in range(len(levels)):
            if validation_level > self.__max_validation_level:
                break
            for y in range(levels[i]):
                title = 'title_{}_{}'.format(y, validation_level)
                question = 'question_{}_{}'.format(y, validation_level)
                answer = 'answer_{}_{}'.format(y, validation_level)
                card = Card(title, question, answer, validation_level)
                list_cards.append(card)
            validation_level += 1

        return Deck('current_deck', list_cards)
