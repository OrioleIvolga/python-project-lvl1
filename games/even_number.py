from random import randint
from games import engine


WELCOME_MASSAGE = "Answer `yes` if the number is even, otherwise answer `no`."


def even_uneven():
    random_number = randint(1, 100)
    question = str(random_number)
    correct_answer = check_even(random_number)
    return(question, correct_answer)


def check_even(random_number):
    if random_number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return (correct_answer)


def main():
    engine.alg_game(even_uneven, WELCOME_MASSAGE)
