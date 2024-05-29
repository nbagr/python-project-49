import random
import math

RULE = 'Find the greatest common divisor of given numbers.'


def get_content():
    first_number = random.randint(0, 25)
    second_number = random.randint(25, 50)

    question = f'{first_number} {second_number}'
    correct_answer = str(math.gcd(first_number, second_number))
    return question, correct_answer
