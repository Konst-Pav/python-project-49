from random import randint
from random import choice


MIN_NUM = 1
MAX_NUM = 10
LIST_OF_OPERATORS = ['+', '-', '*']
GAME_RULE = 'What is the result of the expression?'


def generate_calc_question():
    random_num_1 = randint(MIN_NUM, MAX_NUM)
    random_num_2 = randint(MIN_NUM, MAX_NUM)
    math_op = choice(LIST_OF_OPERATORS)
    question = str(random_num_1) + ' ' + str(math_op) + ' ' + str(random_num_2)
    answer = calculate_expression(random_num_1, random_num_2, math_op)
    question_and_answer = (question, answer)
    return question_and_answer


def calculate_expression(a, b, math_operation):
    expression = {'+': a + b, '-': a - b, '*': a * b}
    if math_operation in expression:
        result = expression[math_operation]
    else:
        result = expression['+']
    return result
