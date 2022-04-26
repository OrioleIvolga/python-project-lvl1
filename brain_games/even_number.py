from random import randint
from brain_games import engine


def even_uneven():
    print("Answer `yes` if the number is even, otherwise answer `no`.")
    random_number = randint(1, 100)
    question = str(random_number)
    if random_number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return (correct_answer, question)


def main():
    engine.alg_game(even_uneven)
