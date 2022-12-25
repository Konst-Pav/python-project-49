from random import randint


MIN_NUM = 1
MAX_NUM = 100
GAME_RULE = 'What number is missing in the progression?'


def generate_game():
    start_progression = randint(MIN_NUM, MAX_NUM)
    step = randint(1, 10)
    progression_length = randint(5, 10)
    progression = gen_progression(start_progression, step, progression_length)
    index_missing_element = randint(0, len(progression) - 1)
    missing_element = progression[index_missing_element]
    progression[index_missing_element] = '..'
    str_progression = ''
    i = 0
    while i < len(progression):
        str_progression += str(progression[i]) + ' '
        i += 1
    correct_answer = missing_element
    question = str_progression
    return question, correct_answer


def gen_progression(start_progression, step, length):
    progression = [start_progression]
    while length >= 0:
        progression.append(progression[-1] + step)
        length -= 1
    return progression
