#!/usr/bin/env python


from brain_games import engine
from brain_games.games.even import generate_even_question, WELCOME_MESSAGE


def main():
    engine.play_game(generate_even_question, WELCOME_MESSAGE)

if __name__ == "__main__":
    main()
