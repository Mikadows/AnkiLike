import unittest

from core.utils.ValuesRatioLister import ValuesRatioLister


class ValuesRatioListerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.__cardSelector = ValuesRatioLister([-1], 1 / 2)

    def test_get_list_validations_should_return_list_length_100(self):

        result = self.__cardSelector.get_random_list([-1])

        self.assertEqual(len(result), 100)

    def test_get_list_validations_should_return_list_same_number_when_cards_only_minus_one_validation_level(self):
        result = self.__cardSelector.get_random_list([-1])

        self.assertTrue(all(map(lambda number: number == -1, result)))

    def test_get_list_validations_should_return_list_same_number_when_cards_only_have_same_validation_level(self):
        self.__cardSelector.values = [0]
        result = self.__cardSelector.get_random_list([0])
        self.assertTrue(all(map(lambda number: number == 0, result)))

        self.__cardSelector.values = [1]
        result = self.__cardSelector.get_random_list([1])
        self.assertTrue(all(map(lambda number: number == 1, result)))

    def test_get_list_validations_should_return_50_cards_when_ratio_half_and_2_different_validation_level(self):
        self.__cardSelector.values = [-1, 0]

        result = self.__cardSelector.get_random_list([-1, 0])

        self.assertEqual(len([number for number in result if number == -1]), 50)
        self.assertEqual(len([number for number in result if number == 0]), 50)

    def test_get_list_validations_should_return_50_cards_when_ratio_half_and_2_not_successive_validation_level(self):
        self.__cardSelector.values = [-1, 1]

        result = self.__cardSelector.get_random_list([-1, 1])

        self.assertEqual(len([number for number in result if number == -1]), 50)
        self.assertEqual(len([number for number in result if number == 0]), 0)
        self.assertEqual(len([number for number in result if number == 1]), 50)

    def test_get_list_validations_should_return_two_thirds_lower_validation_level_and_manage_same_way_for_rest(self):
        self.__cardSelector.values = [-1, 0, 2]
        self.__cardSelector.ratio = 3 / 4

        result = self.__cardSelector.get_random_list([-1, 0, 2])

        self.assertEqual(len([number for number in result if number == -1]), 75)
        self.assertEqual(len([number for number in result if number == 0]), 19)
        self.assertEqual(len([number for number in result if number == 1]), 0)
        self.assertEqual(len([number for number in result if number == 2]), 6)

    def test_get_list_validations_should_return_al_least_one_case(self):
        self.__cardSelector.values = [-1, 0, 1, 2, 3, 4]
        self.__cardSelector.ratio = 2 / 3

        result = self.__cardSelector.get_random_list([-1, 0, 1, 2, 3, 4])

        self.assertEqual(len([number for number in result if number == -1]), 67)
        self.assertEqual(len([number for number in result if number == 0]), 22)
        self.assertEqual(len([number for number in result if number == 1]), 7)
        self.assertEqual(len([number for number in result if number == 2]), 2)
        self.assertEqual(len([number for number in result if number == 3]), 1)
        self.assertEqual(len([number for number in result if number == 4]), 1)

    def test_get_list_validations_should_return_only_validation_level_max_when_cards_contain_not_below_level(self):
        self.__cardSelector.values = [4]
        self.__cardSelector.ratio = 5 / 6

        result = self.__cardSelector.get_random_list([4])

        self.assertEqual(len([number for number in result if number == -1]), 0)
        self.assertEqual(len([number for number in result if number == 0]), 0)
        self.assertEqual(len([number for number in result if number == 1]), 0)
        self.assertEqual(len([number for number in result if number == 2]), 0)
        self.assertEqual(len([number for number in result if number == 3]), 0)
        self.assertEqual(len([number for number in result if number == 4]), 100)
