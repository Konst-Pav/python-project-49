import prompt


NUM_OF_ROUNDS = 3
WRONG_ANSWER = 'is wrong answer ;(. Correct answer was'


def play_brain_game(generate_task_func):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    i = NUM_OF_ROUNDS
    while i > 0:
        task_answer = generate_task_func()
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(task_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' {WRONG_ANSWER} '{task_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
        i -= 1
    else:
        print(f'Congratulations, {user_name}!')
