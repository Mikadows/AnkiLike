
class Deck:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def _get_name(self):
        return self.name

    def _get_cards(self):
        return self.cards