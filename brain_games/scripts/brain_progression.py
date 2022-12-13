#!/usr/bin/env python3
import prompt
from random import randint

number_of_correct_answers = 3


def game():
    user_name = welcome_user()
    correct_answers_left = number_of_correct_answers
    while correct_answers_left > 0:
        task_answer = generate_task()
        user_answer = get_answer()
        result = check_answer(user_answer, task_answer)
        print_result(result, user_name, user_answer, task_answer)
        if result:
            correct_answers_left -= 1
        else:
            correct_answers_left = number_of_correct_answers
    print_game_over(user_name)


def welcome_user():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def generate_task():
    start_progr = randint(1, 100)
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


def get_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def check_answer(user_answer, task_answer):
    return True if user_answer == str(task_answer) else False


def print_result(is_user_answer_correct, user_name, user_answer, task_answer):
    if is_user_answer_correct:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{task_answer}'.\nLet's try again, {user_name}!")


def print_game_over(user_name):
    print(f'Congratulations, {user_name}!')


def main():
    game()


if __name__ == '__main__':
    main()
