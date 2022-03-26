#!/usr/bin/env python


from random import randint
import prompt
from brain_games.welcome_user import welcome_user
from brain_games.welcome_user import name


def main():
    print("Welcome to the Brain Games!")
    welcome_user()

print("Answer `yes` if the number is even, otherwise answer `no`.")

def evev_uneven():
    answer_right = 0
    answer_wrong = 0
    while answer_right == 3:
        if answer_wrong == 1:
            break
        random_number = randint(1, 100)
        print("Quection: " + str(random_number))
        answer = prompt.string("")
        if random_number %2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"
        if answer == correct_answer:
            print("Correct!")
            answer_right += 1
        else:
            print(f"`{answer}` is wrong answer ;(. Correct answer was `{correct_answer}`")
            answer_wrong += 1
    print("Congratulation, " + name)


if __name__ == "__main__":
    main()
    evev_uneven()
