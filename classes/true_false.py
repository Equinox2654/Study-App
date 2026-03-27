"""True or False Question"""

class True_False():

    def __init__(self, question: str, answer: str) -> None:
        self.question = question
        self.answer = answer

    def give_question(self) -> None:
        print(self.question)
        answer = input('What is your answer (t/f): ')
        while answer.lower() != 't' or answer.lower() != 'f':
            print('Your response must be t/f. Not anything else.')
            answer = input('What is your answer (t/f): ')
        if answer.lower() == self.answer.lower():
            print('Correct')
            return
        print('Wrong')
