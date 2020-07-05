class Card:
    def __init__(self, title, question, answer, validation_level=1):
        self.title = title
        self.question = question
        self.answer = answer
        self.validation_level = validation_level

    def __str__(self):
        return "\n        title : " + str(self.title) + "\n        question : " + str(self.question) + "\n        answer : " + str(self.answer) + "\n        validation_level : " + str(self.validation_level)
