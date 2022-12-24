#!/usr/bin/env python3
from brain_games import game_starter
from brain_games.games.even_game import generate_even_question


def main():
    game_starter.play_brain_game(generate_even_question)


if __name__ == '__main__':
    main()
