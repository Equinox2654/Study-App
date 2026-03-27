"""Adds Text Decoration"""

def white_space(string) -> str:
    return f'\n{string}\n'

def question(string) -> str:
    return f'Question: {string}'

def answer(string) -> str:
    return f'Answer: {string}'

def end_of_set(num) -> str:
    return f'Well Done. You got {num} answers correct.'

def option(string, option_char) -> str:
    return f'{option_char.upper()}. {string}'
