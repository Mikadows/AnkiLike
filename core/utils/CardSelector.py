from core.classes.Deck import Deck


class CardSelector:

    def __init__(self, deck: Deck, ratio: float):
        self.__deck = deck
        self.__ratio = ratio

    def __get_deck(self):
        return self.__deck

    def __set_deck(self, deck: Deck):
        self.__deck = deck

    deck = property(__get_deck, __set_deck)

    def __get_ratio(self):
        return self.__ratio

    def __set_ratio(self, ratio):
        self.__ratio = ratio

    ratio = property(__get_ratio, __set_ratio)

    def get_list_validations(self):
        result = []
        available_cases = 100
        validation_levels = self.__get_validation_levels_present_in_cards()
        for i in range(len(validation_levels)):
            cases_to_take = round(available_cases * self.__ratio)
            if available_cases - cases_to_take <= 1:
                if cases_to_take > 1:
                    cases_to_take -= 1

            result += [validation_levels[i]] * cases_to_take
            available_cases -= cases_to_take
            if i == len(validation_levels) - 1:
                result += [validation_levels[i]] * available_cases

        return result

    def __get_validation_levels_present_in_cards(self):
        result = []
        vl_list = [card.validation_level for card in self.__deck.cards]

        [result.append(vl) for vl in vl_list if vl not in result]

        return result
