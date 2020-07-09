from core.classes.Deck import Deck


class ValuesRatioLister:

    def __init__(self, ratio: float):
        self.__ratio = ratio

    def __get_ratio(self):
        return self.__ratio

    def __set_ratio(self, ratio):
        self.__ratio = ratio

    ratio = property(__get_ratio, __set_ratio)

    def get_values_ratio_list(self, int_values, available_cases=100):
        """
        this function return integer list that contains that
        allocates values according to the ratio
        """
        result = []

        if not int_values:
            return None
        if len(int_values) == 1:
            return [int_values[0]] * available_cases

        cases_to_take = round(available_cases * self.__ratio)
        if available_cases - cases_to_take <= 1:
            if cases_to_take > 1:
                cases_to_take -= 1
        result += [int_values[0]] * cases_to_take

        if len(int_values) > 1:
            int_values.pop(0)
            result += self.get_values_ratio_list(int_values, available_cases - cases_to_take)

        return result
