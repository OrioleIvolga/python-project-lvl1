from random import randint
from brain_games import engine


WELCOME_MESSAGE = "Answer `yes` if the number is even, otherwise answer `no`."


def even_uneven():
    random_number = randint(1, 100)
    question = str(random_number)
    correct_answer = "yes" if check_even(random_number) else "no"
    return(question, correct_answer)


def check_even(random_number):
    return random_number % 2 == 0


def main():
    engine.play_game(even_uneven, WELCOME_MESSAGE)
