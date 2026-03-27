"""Flashcard Class"""

class Flashcard():

    def __init__(self, word, definition) -> None:
        self.word = word
        self.definition = definition

    def check_answer(self) -> bool:
        answer = input('Did you get the answer correct (y/n): ')
        if 'y' in answer.lower():
            return True
        return False
