from core.classes.Card import Card
from core.classes.Deck import Deck


class DeckCreateHelper:

    def __init__(self, max_validation_level=4):
        self.max_validation_level = max_validation_level

    def create_deck_with_define_cards_validation_level(self, levels) -> Deck:
        list_cards = []
        validation_level = -1

        for i in range(len(levels)):
            if validation_level > self.max_validation_level:
                break
            for y in range(levels[i]):
                title = 'title_{}_{}'.format(y, validation_level)
                question = 'question_{}_{}'.format(y, validation_level)
                answer = 'answer_{}_{}'.format(y, validation_level)
                card = Card(title, question, answer, validation_level)
                list_cards.append(card)
            validation_level += 1

        return Deck('current_deck', list_cards)
