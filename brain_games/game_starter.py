import prompt


NUM_OF_ROUNDS = 3
WRONG_ANSWER = 'is wrong answer ;(. Correct answer was'


def play_brain_game(game_module):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    i = NUM_OF_ROUNDS
    print(game_module.GAME_RULE)
    while i > 0:
        quastion, answer = game_module.generate_game()
        print(f'Question: {quastion}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' {WRONG_ANSWER} '{answer}'.")
            print(f"Let's try again, {user_name}!")
            break
        i -= 1
    else:
        print(f'Congratulations, {user_name}!')
