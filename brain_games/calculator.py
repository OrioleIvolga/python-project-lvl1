from random import randint
from random import choice
import prompt
from brain_games.welcome_guy import welcome_guy


def calculator(name):
    print("What is the result of the expression?")
    answer_right = 0
    operand = ["+", "-", "*"]
    while answer_right < 3:
        random_a = randint(1, 100)
        random_b = randint(1, 100)
        random_operand = choice(operand)
        print(
            f"Question: {random_a}"
            f" {random_operand} {random_b}"
        )
        answer = prompt.string("Your answer: ")
        if random_operand == "+":
            correct_answer = random_a + random_b
        elif random_operand == "-":
            correct_answer = random_a - random_b
        else:
            correct_answer = random_a * random_b
        if int(answer) == correct_answer:
            print("Correct!")
            answer_right += 1
        else:
            print(
                f"`{answer}` is wrong answer ;(."
                f" Correct answer was `{correct_answer}`.\n"
                f"Let`s try again, {name}!"
            )
            break

    if answer_right == 3:
        print(f"Congratulation, {name}")


def main():
    print("Welcome to the Brain Games!")
    name = welcome_guy()
    calculator(name)
