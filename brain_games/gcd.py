from random import randint
import math
import prompt
from brain_games.welcome_guy import welcome_guy


def gcd(name):
    print("Find the gratest common divisor of given numbers.")
    answer_right = 0
    while answer_right < 3:
        random_a = randint(1, 100)
        random_b = randint(1, 100)
        gcd = math.gcd(random_a, random_b)
        print("Question: " + str(random_a) + " " + str(random_b))
        answer = prompt.string("Your answer: ")
        if int(answer) == gcd:
            print("Correct!")
            answer_right += 1
        else:
            print(
                f"`{answer}` is wrong answer ;(."
                f" Correct answer was `{gcd}`.\n"
                f"Let`s try again, {name}!"
            )
            break

    if answer_right == 3:
        print(f"Congratulations, {name}!")


def main():
    print("Welcome to the Brain Games!")
    name = welcome_guy()
    gcd(name)
