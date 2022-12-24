import prompt


NUM_OF_ROUNDS = 3


def play_brain_game(generate_task_func):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    i = NUM_OF_ROUNDS
    while i > 0:
        task_answer = generate_task_func()
        user_answer = prompt.string('Your answer: ')
        result = check_answer(user_answer, task_answer)
        print_conclusion(result, user_name, user_answer, task_answer)
        if result is False:
            break
        i -= 1
    else:
        print(f'Congratulations, {user_name}!')


def check_answer(user_answer, task_answer):
    return True if user_answer == str(task_answer) else False


def print_conclusion(is_user_answer_correct, user_name, u_ans, t_ans):
    if is_user_answer_correct:
        print('Correct!')
    else:
        print(f"'{u_ans}' is wrong answer ;(. Correct answer was '{t_ans}'.")
        print(f"Let's try again, {user_name}!")


def print_game_over(user_name):
    print(f'Congratulations, {user_name}!')
