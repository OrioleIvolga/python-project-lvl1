from random import randint
import math
from brain_games import engine


def gcd():
    print("Find the gratest common divisor of given numbers.")
    random_a = randint(1, 100)
    random_b = randint(1, 100)
    gcd = math.gcd(random_a, random_b)
    question = str(random_a) + " " + str(random_b)
    correct_answer = str(gcd)
    return (correct_answer, question)


def main():
    engine.alg_game(gcd)
