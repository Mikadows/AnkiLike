class Box:

    def __init__(self, name, decks):
        self._name = name
        self.decks = {}
        self.decks = decks

    def _get_name(self):
        return self._name

    def _set_name(self, name):
        self._name = name

    name = property(_get_name, _set_name)

    def _get_decks(self):
        return self.decks

    def add_deck(self, deck):
        self.decks[deck._get_name()] = deck

    def delete_deck(self, deck):
        self.decks.pop(deck._get_name())
