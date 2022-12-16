#!/usr/bin/env python3
from random import randint


MIN_NUM = 1
MAX_NUM = 100


def gen_progr_task():
    start_progr = randint(MIN_NUM, MAX_NUM)
    int_step = randint(1, 10)
    progr_len = randint(5, 10)
    i = progr_len
    progr = [start_progr]
    while i >= 0:
        progr.append(progr[-1] + int_step)
        i -= 1
    ind_missing_el = randint(0, len(progr) - 1)
    missing_el = progr[ind_missing_el]
    progr[ind_missing_el] = '..'
    str_progr = ''
    i = 0
    while i < len(progr):
        str_progr += str(progr[i]) + ' '
        i += 1
    print('What number is missing in the progression?')
    print(f'Question: {str_progr}')
    return missing_el
