from random import randint
from random import choice
from brain_games import engine


def calculator():
    print("What is the result of the expression?")
    operand = ["+", "-", "*"]
    random_a = randint(1, 100)
    random_b = randint(1, 100)
    random_operand = choice(operand)
    question = f"{random_a} {random_operand} {random_b}"
    if random_operand == "+":
        correct_answer = random_a + random_b
    elif random_operand == "-":
        correct_answer = random_a - random_b
    else:
        correct_answer = random_a * random_b
    return (str(correct_answer), question)


def main():
    engine.alg_game(calculator)
