class Card:
    def __init__(self, title, question, answer, validation_level=1):
        self.title = title
        self.question = question
        self.answer = answer
        self.validation_level = validation_level
