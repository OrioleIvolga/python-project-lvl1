from random import randint
from random import choice
from games import engine


WELCOME_MASSAGE = "What is the result of the expression?"
START_RANDOM_RANGE = 1
END_RANDOM_RANGE = 100


def calculator():
    operand = ["+", "-", "*"]
    random_operand = choice(operand)
    random_a = randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    random_b = randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    question = f"{random_a} {random_operand} {random_b}"
    if random_operand == "+":
        correct_answer = random_a + random_b
    elif random_operand == "-":
        correct_answer = random_a - random_b
    elif random_operand == "*":
        correct_answer = random_a * random_b
    else:
        print("Anknown simbol")
    return (question, str(correct_answer))


def main():
    engine.alg_game(calculator, WELCOME_MASSAGE)
