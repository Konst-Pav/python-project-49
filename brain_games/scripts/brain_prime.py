#!/usr/bin/env python3
from brain_games import game_starter
from brain_games.games.prime_game import generate_prime_question


def main():
    game_starter.play_brain_game(generate_prime_question)


if __name__ == '__main__':
    main()
