from random import randint


MIN_NUM = 1
MAX_NUM = 100
GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game():
    random_num = randint(MIN_NUM, MAX_NUM)
    number_is_even = is_even(random_num)
    if number_is_even:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_num, correct_answer


def is_even(number):
    return number % 2 == 0
