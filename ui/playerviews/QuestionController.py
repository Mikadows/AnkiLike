from core.services import CardService


class QuestionController:
    def __init__(self, deck_index: int, card_service: CardService):
        self.deck_index = deck_index
        self.card_service = card_service


    def draw_card(self):
        return self.card_service.get_card_randomly(self.deck_index)
