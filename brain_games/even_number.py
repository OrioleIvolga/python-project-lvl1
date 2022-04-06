from random import randint
import prompt
from brain_games.welcome_guy import welcome_guy


def even_uneven(name):
    print("Answer `yes` if the number is even, otherwise answer `no`.")
    answer_right = 0
    while answer_right < 3:
        random_number = randint(1, 100)
        print("Question: " + str(random_number))
        answer = prompt.string("Your answer: ")
        if random_number % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"
        if answer == correct_answer:
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
        print(f"Congratulations, {name}")


def main():
    print("Welcome to the Brain Games!")
    name = welcome_guy()
    even_uneven(name)
