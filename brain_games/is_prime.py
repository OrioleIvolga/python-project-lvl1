from random import randint
import prompt
from brain_games.welcome_guy import welcome_guy


def is_prime(name):
    print("Answer `yes` if given number is prime. Otherwise answer `no`.")
    answer_right = 0
    while answer_right < 3:
        random_number = randint(1, 100)
        print("Question: " + str(random_number))
        answer = prompt.string("Your answer: ")
        a = 2
        while random_number % a != 0:
            a += 1
        if random_number == a:
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
        print(f"Congratulation, {name}")


def main():
    print("Welcome to the Brain Games!")
    name = welcome_guy()
    is_prime(name)
