import random

RULE = 'What is the result of the expression?'
operators = '+-*'


def get_correct_answer(first_number, second_number, operator):
    if operator == '+':
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number


def get_content():
    first_number = random.randint(0, 20)
    second_number = random.randint(0, 20)
    operator = random.choice(operators)

    question = f'{first_number} {operator} {second_number}'
    correct_answer = str(
        get_correct_answer(first_number, second_number, operator))

    return question, correct_answer
