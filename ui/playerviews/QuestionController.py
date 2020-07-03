from core.services import CardService


class QuestionController:
    def __init__(self, deck_index: int, card_service: CardService):
        self.deck_index = deck_index
        self.card_service = card_service

    def _get_current_card_index(self):
        return self._current_card_index

    def _set_current_card_index(self, current_card_index):
        self._current_card_index = current_card_index

    current_card_index = property(_get_current_card_index, _set_current_card_index)

    def draw_card(self):
        self.current_card_index = self.card_service.get_card_index_randomly(self.deck_index)
        return self.card_service.data.box.decks[self.deck_index].cards[self.current_card_index]

    def update_card_validation_level(self, is_validate: bool, master=None):
        self.card_service.update_validation_level(self.deck_index, self.current_card_index, is_validate)
        from ui.playerviews.QuestionView import QuestionView
        QuestionView(self.deck_index, master)
