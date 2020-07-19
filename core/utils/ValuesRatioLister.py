from core.classes.Deck import Deck


class ValuesRatioLister:

    def __init__(self, ratio: float):
        self.__ratio = ratio

    def __get_ratio(self):
        return self.__ratio

    def __set_ratio(self, ratio):
        self.__ratio = ratio

    ratio = property(__get_ratio, __set_ratio)

    def get_values_ratio_list(self, values, available_cases=100):
        """
        this function return integer list that contains that
        allocates values according to the ratio
        """
        result = []

        if not values:
            return None
        if len(values) == 1 or self.__ratio == 1:
            return [values[0]] * available_cases

        cases_to_take = round(available_cases * self.__ratio)
        if available_cases - cases_to_take <= 1:
            if cases_to_take > 1:
                cases_to_take -= 1
        result += [values[0]] * cases_to_take

        if len(values) > 1:
            values.pop(0)
            result += self.get_values_ratio_list(values, available_cases - cases_to_take)

        return result
