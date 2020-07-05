class Box:

    def __init__(self, name, decks):
        self._name = name
        self.decks = []
        self.decks = decks

    def _get_name(self):
        return self._name

    def _set_name(self, name):
        self._name = name

    name = property(_get_name, _set_name)

    def _get_decks(self):
        return self.decks

    def add_deck(self, deck):
        self.decks.append(deck)

    def delete_deck(self, deck):
        try:
            self.decks.remove(deck)
        except ValueError:
            print("deck {0} is not in the decks list".format(deck.name))

    def __str__(self):
        decks = ""
        for deck in self.decks:
            decks += str(deck) + "\n"
        return "name : " + str(self.name) + "\ndecks : " + str(decks)
