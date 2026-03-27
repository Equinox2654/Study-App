"""Multiple Choice Question"""

class Multiple_Choice_Question():

    def __init__(self, question, option1, option2, option3, option4, answer) -> None:
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.answer = answer

    def give_question(self) -> None:
        print(self.question)
        print(f'A. {self.option1}')
        print(f'B. {self.option2}')
        print(f'C. {self.option3}')
        print(f'D. {self.option4}')
        answer = input("What is the answer? ")
        if answer.lower() == self.answer.lower():
            print("Correct")
            return
        print(f'Incorrect. The correct answer is {self.answer}')
