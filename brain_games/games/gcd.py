from random import randint
import math
from brain_games import engine

WELCOME_MESSAGE = "Find the gratest common divisor of given numbers."


def gcd():
    random_a = randint(1, 100)
    random_b = randint(1, 100)
    gcd = math.gcd(random_a, random_b)
    question = (f"{random_a} {random_b}")
    correct_answer = str(gcd)
    return (question, correct_answer)


def main():
    engine.alg_game(gcd, WELCOME_MESSAGE)
