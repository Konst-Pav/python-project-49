#!/usr/bin/env python3
import prompt


def play_brain_game(gen_task, user_name, num_of_rounds):
    i = num_of_rounds
    while i > 0:
        task_answer = gen_task()
        # print(f'!!! Answer {task_answer}')
        user_answer = get_answer()
        result = check_answer(user_answer, task_answer)
        print_result(result, user_name, user_answer, task_answer)
        if result is False:
            break
        i -= 1
        task_answer = 0
    else:
        print_game_over(user_name)


def get_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def check_answer(user_answer, task_answer):
    return True if user_answer == str(task_answer) else False


def print_result(is_user_answer_correct, user_name, user_answer, task_answer):
    if is_user_answer_correct:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{task_answer}'.")
        print("Let's try again, {user_name}!")


def print_game_over(user_name):
    print(f'Congratulations, {user_name}!')
