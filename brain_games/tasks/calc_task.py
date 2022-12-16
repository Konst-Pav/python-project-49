#!/usr/bin/env python3
from random import randint


MIN_NUM = 1
MAX_NUM = 10


def gen_calc_task():
    a = randint(MIN_NUM, MAX_NUM)
    b = randint(MIN_NUM, MAX_NUM)
    math_op = [[a + b, '+'], [a - b, '-'], [a * b, '*']]
    r_ind = randint(0, len(math_op) - 1)
    result = math_op[r_ind][0]
    print('What is the result of the expression?')
    print(f'Question: {a} {math_op[r_ind][1]} {b}')
    return result
