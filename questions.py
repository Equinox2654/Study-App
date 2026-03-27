from classes.flashcard import Flashcard
from classes.multiple_choice import Multiple_Choice_Question
from classes.true_false import True_False

test = {
    'flashcards': {
        'test1': Flashcard('test', 'answer'),
    },
    'multiple_choice': {
        'test1': Multiple_Choice_Question('What is test', 'wrong', 'right', 'wrong', 'wrong', 'b'),
    },
    'tf': {
        'test1': True_False('test1', 't'),
    },
}
