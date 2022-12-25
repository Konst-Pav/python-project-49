from random import randint
from math import gcd


MIN_NUM = 1
MAX_NUM = 100
GAME_RULE = 'Find the greatest common divisor of given numbers.'


def generate_game():
    random_num_1 = randint(MIN_NUM, MAX_NUM)
    random_num_2 = randint(MIN_NUM, MAX_NUM)
    question = f'{random_num_1} {random_num_2}'
    correct_answer = gcd(random_num_1, random_num_2)
    return question, correct_answer
