#!/usr/bin/env python3
from random import randint


def list_of_num(max):
    l_of_num = []
    i = 2
    while i <= max:
        l_of_num.append(i)
        i += 1
    return l_of_num

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

l = simple_num_in_range(100)
print(l)
