class Card():
    def __init__(self, title, question, answer, validation_level=0):
        self._title = title
        self._question = question
        self._answer = answer
        self._validation_level = validation_level

    def __str__(self):
        return "\n        title : " + str(self.title) + "\n        question : " + str(self.question) + "\n        answer : " + str(self.answer) + "\n        validation_level : " + str(self.validation_level)

    def _get_title(self):
        return self._title

    def _set_title(self, title):
        self._title = title

    title = property(_get_title, _set_title)

    def _get_question(self):
        return self._question

    def _set_question(self, question):
        self._question = question

    question = property(_get_question, _set_question)

    def _get_answer(self):
        return self._answer

    def _set_answer(self, answer):
        self._answer = answer

    answer = property(_get_answer, _set_answer)

    def _get_validation_level(self):
        return self._validation_level

    def _set_validation_level(self, validation_level):
        self._validation_level = validation_level

    validation_level = property(_get_validation_level, _set_validation_level)
