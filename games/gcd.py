from random import randint
import math
from games import engine

WELCOME_MASSAGE = "Find the gratest common divisor of given numbers."


def gcd():
    random_a = randint(1, 100)
    random_b = randint(1, 100)
    gcd = math.gcd(random_a, random_b)
    question = str(random_a) + " " + str(random_b)
    correct_answer = str(gcd)
    return (correct_answer, question)


def main():
    engine.alg_game(gcd, WELCOME_MASSAGE)
