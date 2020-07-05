class Card:
    def __init__(self, title, question, answer, validation_level=1):
        self._title = title
        self.question = question
        self.answer = answer
        self.validation_level = validation_level

    def _get_title(self):
        return self._title

    def _set_title(self, title):
        self._title = title

    title = property(_get_title, _set_title)
