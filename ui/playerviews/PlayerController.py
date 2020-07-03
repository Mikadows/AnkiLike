from core.Data import Data
from core.services import DeckService
from ui.playerviews.QuestionView import QuestionView


class PlayerController:
    def __init__(self, data: Data, deck_service: DeckService):
        self.data = data
        self.deck_service = deck_service

    def play(self, master=None, index: int = -1):
        QuestionView(self.deck_service.find_deck_by_index(index), master)
