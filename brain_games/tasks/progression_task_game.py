from random import randint


MIN_NUM = 1
MAX_NUM = 100


def gen_progr_task():
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
    print('What number is missing in the progression?')
    print(f'Question: {str_progression}')
    return missing_element


def gen_progression(start_progression, step, length):
    progression = [start_progression]
    while length >= 0:
        progression.append(progression[-1] + step)
        length -= 1
    return progression
