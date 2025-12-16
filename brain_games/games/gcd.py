from random import randint


WELCOME_MESSAGE = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_gcd_question():
    random_a = randint(1, 100)
    random_b = randint(1, 100)
    result = gcd(random_a, random_b)
    question = (f"{random_a} {random_b}")
    correct_answer = str(result)
    return (question, correct_answer)
