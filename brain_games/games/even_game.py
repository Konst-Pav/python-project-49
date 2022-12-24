from random import randint


MIN_NUM = 1
MAX_NUM = 100
GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_even_question():
    random_num = randint(MIN_NUM, MAX_NUM)
    number_is_even = is_even(random_num)
    if number_is_even:
        answer = 'yes'
    else:
        answer = 'no'
    question = random_num
    question_and_answer = (question, answer)
    return question_and_answer


def is_even(number):
    return number % 2 == 0
