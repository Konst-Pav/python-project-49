#!/usr/bin/env python3
from random import randint


MIN_NUM = 1
MAX_NUM = 100


def gen_gcd_task():
    a = randint(MIN_NUM, MAX_NUM)
    b = randint(MIN_NUM, MAX_NUM)
    if a > b:
        min_n = a
    else:
        min_n = b
    while min_n > 0:
        if a / min_n == int(a / min_n) and b / min_n == int(b / min_n):
            max_divisor = min_n
            break
        min_n -= 1
    print('Find the greatest common divisor of given numbers.')
    print(f'Question: {a} {b}')
    return max_divisor
