from random import randint
from brain_games import engine


def is_prime():
    print("Answer `yes` if given number is prime. Otherwise answer `no`.")
    random_number = randint(1, 100)
    question = str(random_number)
    a = 2
    while random_number % a != 0:
        a += 1
    if random_number == a:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return (correct_answer, question)


def main():
    engine.alg_game(is_prime)
