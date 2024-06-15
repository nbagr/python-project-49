import random

RULE = 'What number is missing in the progression?'


def get_progression():
    first_number = random.randint(0, 10)
    progression_size = random.randint(5, 10)
    step = random.randint(1, 10)

    progression = [first_number + step * i for i in range(progression_size)]
    return progression


def get_content():
    progression = get_progression()

    last_index = len(progression) - 1
    random_index = random.randint(0, last_index)

    correct_answer = str(progression[random_index])

    progression[random_index] = '..'
    question = ' '.join(map(str, progression))

    return question, correct_answer
