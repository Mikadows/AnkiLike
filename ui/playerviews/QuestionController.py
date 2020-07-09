from core.Data import Data
from core.classes.Card import Card
from core.services import CardService
from core.utils.ValuesRatioLister import ValuesRatioLister


class QuestionController:
    def __init__(self, deck_index: int, card_service: CardService, last_card: Card):
        self.deck_index = deck_index
        self.card_service = card_service
        self.card_service.data = Data()
        self.card_service.values_ratio_lister = ValuesRatioLister(2/3)
        self.card_service.deck_index = deck_index
        self.card_service.current_card = last_card

    def __get_current_card(self):
        return self._current_card

    def __set_current_card(self, current_card):
        self._current_card = current_card

    current_card = property(__get_current_card, __set_current_card)

    def draw_card(self):
        self.current_card = self.card_service.get_card_randomly()
        return self.current_card

    def update_card_validation_level(self, is_validate: bool, master=None):
        current_card_index = self.card_service.data.box.decks[self.deck_index].cards.index(self.current_card)
        self.card_service.update_validation_level(self.deck_index, current_card_index, is_validate)
        from ui.playerviews.QuestionView import QuestionView
        QuestionView(self.deck_index, master, last_card=self.card_service.current_card)
