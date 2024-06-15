import random
import math

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number))
    for element in range(2, (number_sqrt + 1)):
        if number % element == 0:
            return False
    return True


def get_content():
    question = random.randint(0, 50)
    correct_answer = 'yes' if is_prime(question) else 'no'

    return question, correct_answer
