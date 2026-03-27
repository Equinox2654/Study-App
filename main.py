from sys import argv
from sys import exit
from time import sleep
import questions
import decorations
import builtins

original_print = builtins.print

def print(message) -> None:
    sleep(0.1)
    original_print(decorations.white_space(message))

def get_dict_of_question(question_type) -> dict:
    match argv[1]:
        case 'test':
            return questions.test[question_type]
        case _:
            return {}

def create_flashcards() -> dict:
    if argv[1] == None:
        raise Exception("Try main.py <dictionary_name>")
    return get_dict_of_question('flashcards')

def create_multiple_choice() -> dict:
    if argv[1] == None:
        raise Exception("Try main.py <dictionary_name>")
    return get_dict_of_question('multiple_choice')
     
def create_true_false() -> dict:
    if argv[1] == None:
        raise Exception("Try main.py <dictionary_name>")
    return get_dict_of_question('tf')

def use_flashcards(flashcards: dict) -> None:
    num_correct: int = 0
    for flashcard in flashcards:
        card = flashcards[flashcard]
        print(decorations.question(card.word))
        input('Define this word: ')
        print(decorations.answer(card.definition))
        if card.check_answer():
            num_correct += 1
            print("Good Job")
        else:
            print("Maybe Next Tsudo apt install libc6:i386 libncurses5:i386 libstdc++6:i386sudo apt install libc6:i386 libncurses5:i386 libstdc++6:i386sudo apt install libc6:i386 libncurses5:i386 libstdc++6:i386ime")
    print(f"Well Done. You got {num_correct} answers correct.")

def use_multiple_choice(multi_questions: dict) -> None:
    num_correct: int = 0
    for question in multi_questions:
        ques = multi_questions[question]
        print(decorations.question(ques.question))
        print(decorations.option(ques.option1, 'a'))
        print(decorations.option(ques.option2, 'b'))
        print(decorations.option(ques.option3, 'c'))
        print(decorations.option(ques.option4, 'd'))
        answer = input("What is your answer: ")
        if answer.lower() == ques.answer:
            print("Correct")
            num_correct += 1
        else:
            print(f'Incorrect. The correct answer is {ques.answer.upper()}')
    print(decorations.end_of_set(num_correct))

def use_tf(true_false: dict) -> None:
    num_correct = 0
    print("Identify whether the following questions are true or false.")
    for tf in true_false:
        question = true_false[tf]
        print(decorations.question(question.question))
        answer = input("What is your answer (t/f): ")
        if answer.lower() == question.answer:
            num_correct += 1
            print("Correct")
        else:
            print(f'Incorrect. The correct answer is {question.answer.upper()}')
    print(decorations.end_of_set(num_correct))

def main():
    flashcards = create_flashcards()
    multiple_choice_test = create_multiple_choice()
    tf = create_true_false()
    while True:
        print("A. Study Flashcards")
        print("B. Practice Multiple Choice Questions")
        print("C. Practice True of False Questions")
        print("D. Do a Practice Test (Does Not Work Yet)")
        print("To Quit pres 'q'")
        choice = input("What would you like to do: ")
        match choice:
            case 'A' | 'a':
                use_flashcards(flashcards)
            case 'B' | 'b':
                use_multiple_choice(multiple_choice_test)
            case 'C' | 'c':
                use_tf(tf)
            case 'D' | 'd':
                print("This options is currently unsupported.")
            case 'Q' | 'q':
                print("Quitting Program")
                exit()
            case _:
                print("Try Again")
                pass

if argv[0] == 'main.py':
    main()
