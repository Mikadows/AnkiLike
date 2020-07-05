
class Deck:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def _get_name(self):
        return self.name

    def _get_cards(self):
        return self.cards

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        cards = ""
        for card in self.cards:
            cards += str(card) + "\n"
        return "\n    name : " + str(self.name) + "\n    cards : " + str(cards)