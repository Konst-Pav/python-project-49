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
    a = randint(min_num, max_num)
    b = randint(min_num, max_num)
    math_op = [[a + b, '+'], [a - b, '-'], [a * b, '*']]
    r_ind = randint(0, len(math_op)-1)
    result = math_op[r_ind][0]
    print('What is the result of the expression?')
    print(f'Question: {a} {math_op[r_ind][1]} {b}')
    return result


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
