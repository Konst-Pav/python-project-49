#!/usr/bin/env python3
import prompt
from random import randint


min_num = 1
max_num = 100
number_of_correct_answers = 3


def game():
    user_name = welcome_user()
    correct_answers_left = number_of_correct_answers
    while correct_answers_left > 0:
        random_number = generate_task()
        user_answer = get_answer()
        result = check_answer(user_answer, random_number)
        print_result(result, user_name, user_answer, random_number)
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
    number = randint(min_num, max_num)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {number}')
    return number


def get_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def check_answer(user_answer, number):
    return True if user_answer == correct_answer(is_even(number)) else False


def print_result(is_user_answer_correct, user_name, user_answer, random_number):
    if is_user_answer_correct:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer(is_even(random_number))}'.\nLet's try again, {user_name}!")


def print_game_over(user_name):
    print(f'Congratulations, {user_name}!')


def correct_answer(answer):
    return 'yes' if answer else 'no'


def is_even(number):
    return (number / 2) == int(number / 2)


def main():
    game()


if __name__ == '__main__':
    main()
