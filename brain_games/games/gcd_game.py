from random import randint
from math import gcd


MIN_NUM = 1
MAX_NUM = 100


def generate_gcd_question():
    random_num_1 = randint(MIN_NUM, MAX_NUM)
    random_num_2 = randint(MIN_NUM, MAX_NUM)
    max_divisor = gcd(random_num_1, random_num_2)
    print('Find the greatest common divisor of given numbers.')
    print(f'Question: {random_num_1} {random_num_2}')
    return max_divisor
