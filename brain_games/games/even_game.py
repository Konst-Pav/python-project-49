from random import randint


MIN_NUM = 1
MAX_NUM = 100


def generate_even_question():
    random_num = randint(MIN_NUM, MAX_NUM)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {random_num}')
    number_is_even = is_even(random_num)
    if number_is_even:
        result = 'yes'
    else:
        result = 'no'
    return result


def is_even(number):
    result = (number / 2) == int(number / 2)
    return result
