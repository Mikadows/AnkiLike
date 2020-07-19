import unittest

from core.utils.ValuesRatioLister import ValuesRatioLister


class ValuesRatioListerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.__cardSelector = ValuesRatioLister(1 / 2)

    def test_get_list_validations_should_return_default_list_length_100(self):
        result = self.__cardSelector.get_values_ratio_list([-1])

        self.assertEqual(len(result), 100)

    def test_get_list_validations_should_return_list_length_define_in_parameter(self):
        result = self.__cardSelector.get_values_ratio_list([-1], 176)

        self.assertEqual(len(result), 176)

    def test_get_list_validations_should_return_list_lower_number_when_ratio_is_1(self):
        self.__cardSelector.ratio = 1
        
        result = self.__cardSelector.get_values_ratio_list([-1, 0, 4])

        self.assertEqual(len([vl for vl in result if vl == -1]), 100)

    def test_get_list_validations_should_return_list_same_number_when_cards_only_have_same_validation_level(self):
        result = self.__cardSelector.get_values_ratio_list([0])
        self.assertEqual(len([vl for vl in result if vl == 0]), 100)

        result = self.__cardSelector.get_values_ratio_list([1])
        self.assertEqual(len([vl for vl in result if vl == 1]), 100)

    def test_get_list_validations_should_return_50_cards_when_ratio_half_and_2_different_validation_level(self):
        result = self.__cardSelector.get_values_ratio_list([-1, 0])

        self.assertEqual(len([number for number in result if number == -1]), 50)
        self.assertEqual(len([number for number in result if number == 0]), 50)

    def test_get_list_validations_should_return_50_cards_when_ratio_half_and_2_not_successive_validation_level(self):
        result = self.__cardSelector.get_values_ratio_list([-1, 1])

        self.assertEqual(len([number for number in result if number == -1]), 50)
        self.assertEqual(len([number for number in result if number == 0]), 0)
        self.assertEqual(len([number for number in result if number == 1]), 50)

    def test_get_list_validations_should_return_two_thirds_lower_validation_level_and_manage_same_way_for_rest(self):
        self.__cardSelector.ratio = 3 / 4

        result = self.__cardSelector.get_values_ratio_list([-1, 0, 2])

        self.assertEqual(len([number for number in result if number == -1]), 75)
        self.assertEqual(len([number for number in result if number == 0]), 19)
        self.assertEqual(len([number for number in result if number == 1]), 0)
        self.assertEqual(len([number for number in result if number == 2]), 6)

    def test_get_list_validations_should_return_al_least_one_case(self):
        self.__cardSelector.ratio = 2 / 3

        result = self.__cardSelector.get_values_ratio_list([-1, 0, 1, 2, 3, 4])

        self.assertEqual(len([number for number in result if number == -1]), 67)
        self.assertEqual(len([number for number in result if number == 0]), 22)
        self.assertEqual(len([number for number in result if number == 1]), 7)
        self.assertEqual(len([number for number in result if number == 2]), 2)
        self.assertEqual(len([number for number in result if number == 3]), 1)
        self.assertEqual(len([number for number in result if number == 4]), 1)

    def test_get_list_validations_should_return_only_validation_level_max_when_cards_contain_not_below_level(self):
        self.__cardSelector.ratio = 5 / 6

        result = self.__cardSelector.get_values_ratio_list([4])

        self.assertEqual(len([number for number in result if number == -1]), 0)
        self.assertEqual(len([number for number in result if number == 0]), 0)
        self.assertEqual(len([number for number in result if number == 1]), 0)
        self.assertEqual(len([number for number in result if number == 2]), 0)
        self.assertEqual(len([number for number in result if number == 3]), 0)
        self.assertEqual(len([number for number in result if number == 4]), 100)
