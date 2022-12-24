from random import randint
from random import choice


MIN_NUM = 1
MAX_NUM = 10


def generate_calc_question():
    random_num_1 = randint(MIN_NUM, MAX_NUM)
    random_num_2 = randint(MIN_NUM, MAX_NUM)
    math_operation = choice(['+', '-', '*'])
    result = calculate_expression(random_num_1, random_num_2, math_operation)
    print('What is the result of the expression?')
    print(f'Question: {random_num_1} {math_operation} {random_num_2}')
    return result


def calculate_expression(a, b, math_operation):
    expression = {'+': a + b, '-': a - b, '*': a * b}
    if math_operation in expression:
        result = expression[math_operation]
    else:
        result = expression['+']
    return result
