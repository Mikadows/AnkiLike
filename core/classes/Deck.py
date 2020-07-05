class Deck:
    def __init__(self, name, cards):
        self._name = name
        self.cards = cards

    def _get_name(self):
        return self._name

    def _set_name(self, name):
        self._name = name

    name = property(_get_name, _set_name)

    def _get_cards(self):
        return self.cards

    def add_card(self, card):
        self.cards.append(card)

    def del_card(self, card):
        self.cards.remove(card)
