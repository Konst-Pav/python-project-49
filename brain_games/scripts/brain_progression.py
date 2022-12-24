#!/usr/bin/env python3
from brain_games import game_starter
from brain_games.games.progression_game import generate_progression_question
from brain_games.games.progression_game import GAME_RULE


def main():
    game_starter.play_brain_game(generate_progression_question, GAME_RULE)


if __name__ == '__main__':
    main()
