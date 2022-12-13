#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.simple_num import simple_num_in_range

number_of_correct_answers = 3


def game():
    user_name = welcome_user()
    correct_answers_left = number_of_correct_answers
    while correct_answers_left > 0:
        task_answer = generate_task()
        user_answer = get_answer()
        result = check_answer(user_answer, correct_answer(task_answer))
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
    max_num = 100
    r_int = randint(0, max_num)
    simple_num = simple_num_in_range(max_num)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print(f'Question: {r_int}')
    return True if r_int in simple_num else False


def get_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def check_answer(user_answer, task_answer):
    return True if user_answer == str(task_answer) else False


def correct_answer(answer):
    return 'yes' if answer else 'no'


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
