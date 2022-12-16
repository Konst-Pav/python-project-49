#!/usr/bin/env python3
from brain_games import welcome_user
from brain_games import game
from brain_games.tasks.calc_task import gen_calc_task


NUMBER_OF_ROUNDS = 3


def main():
    user_name = welcome_user.get_user_name()
    game.play_brain_game(gen_calc_task, user_name, NUMBER_OF_ROUNDS)


if __name__ == '__main__':
    main()
