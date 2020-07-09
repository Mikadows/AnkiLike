from core.classes.Deck import Deck


class ValuesRatioLister:

    def __init__(self, values, ratio: float, list_len=100):
        self.__values = values
        self.__ratio = ratio
        self.__list_len = list_len

    def __get_values(self):
        return self.__values

    def __set_values(self, deck: Deck):
        self.__values = deck

    values = property(__get_values, __set_values)

    def __get_ratio(self):
        return self.__ratio

    def __set_ratio(self, ratio):
        self.__ratio = ratio

    ratio = property(__get_ratio, __set_ratio)

    def get_random_list(self, int_values, available_cases=100):
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
            result += self.get_random_list(int_values, available_cases - cases_to_take)

        return result
