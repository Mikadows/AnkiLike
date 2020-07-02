from core.Data import Data


class PlayerController:
    def __init__(self, data: Data):
        self.data = data

    def play(self, selected_deck: str):
        print(selected_deck)
