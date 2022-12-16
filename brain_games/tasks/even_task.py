#!/usr/bin/env python3
from random import randint


MIN_NUM = 1
MAX_NUM = 100


def gen_even_task():
    number = randint(MIN_NUM, MAX_NUM)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {number}')
    return 'yes' if (number / 2) == int(number / 2) else 'no'
