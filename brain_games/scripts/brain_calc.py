#!/usr/bin/env python3
from brain_games import game_starter
from brain_games.games.calc_game import generate_calc_question, GAME_RULE


def main():
    game_starter.play_brain_game(generate_calc_question, GAME_RULE)


if __name__ == '__main__':
    main()
