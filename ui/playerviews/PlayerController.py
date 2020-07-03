from core.Data import Data
from ui.playerviews.QuestionView import QuestionView


class PlayerController:
    def __init__(self, data: Data):
        self.data = data

    def play(self, master=None, index: int = -1):
        decks = self.data.box.decks
        QuestionView(decks[index], master)
