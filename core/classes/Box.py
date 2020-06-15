
class Box:
    def __init__(self, name, decks):
        self.name = name
        self.decks = {}
        self.decks = decks

    def _get_name(self):
        return self.name

    def _get_decks(self):
        return self.decks

    def add_deck(self, deck):
        self.decks[deck._get_name()] = deck

    def delete_deck(self, deck):
        self.decks.pop(deck._get_name())