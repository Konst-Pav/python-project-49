#!/usr/bin/env python3
from random import randint


MAX_NUM = 100


def gen_prime_task():
    r_int = randint(0, MAX_NUM)
    simple_num = simple_num_in_range(MAX_NUM)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print(f'Question: {r_int}')
    return 'yes' if r_int in simple_num else 'no'


def simple_num_in_range(max):
    simple_num = list_of_num(max)
    i = 0
    while i < len(simple_num):
        y = i + 1
        while y < len(simple_num):
            res = simple_num[y] / simple_num[i]
            if res == int(res):
                simple_num.pop(y)
            else:
                y += 1
        i += 1
    return simple_num


def list_of_num(max):
    l_of_num = []
    i = 2
    while i <= max:
        l_of_num.append(i)
        i += 1
    return l_of_num
