from random import randint
from brain_games import engine


WELCOME_MASSAGE = "Answer `yes` if the number is even, otherwise answer `no`."


def even_uneven():
    random_number = randint(1, 100)
    question = str(random_number)
    correct_answer = random_number % 2 == 0 and str("yes") or str("no")
    return(question, correct_answer)


def main():
    engine.alg_game(even_uneven, WELCOME_MASSAGE)
