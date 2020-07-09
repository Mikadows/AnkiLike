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

    def get_random_list(self):
        """
        this function return integer list that contains that
        allocates values according to the ratio
        """
        result = []
        available_cases = self.__list_len
        for i in range(len(self.__values)):
            cases_to_take = round(available_cases * self.__ratio)
            if available_cases - cases_to_take <= 1:
                if cases_to_take > 1:
                    cases_to_take -= 1

            result += [self.__values[i]] * cases_to_take
            available_cases -= cases_to_take
            if i == len(self.__values) - 1:
                result += [self.__values[i]] * available_cases

        return result
