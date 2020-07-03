from core.Data import Data
from core.services import DeckService


class PlayerController:
    def __init__(self, deck_service: DeckService):
        self.deck_service = deck_service

    def play(self, master=None, index: int = -1):
        from ui.playerviews.QuestionView import QuestionView
        QuestionView(self.deck_service.find_deck_by_index(index), index, master)
