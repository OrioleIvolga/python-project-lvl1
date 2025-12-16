#!/usr/bin/env python


from brain_games import engine
from brain_games.games.calc import generate_question_and_answer, WELCOME_MESSAGE

def main():
    engine.play_game(generate_question_and_answer, WELCOME_MESSAGE)


if __name__ == "__main__":
    main()
