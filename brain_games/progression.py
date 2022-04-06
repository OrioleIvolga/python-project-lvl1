from random import randint
import prompt
from brain_games.welcome_guy import welcome_guy


def progression(name):
    print("What number is missing in progression?")
    answer_right = 0
    while answer_right < 3:
        progr_start = randint(1, 100)
        progr_step = randint(1, 10)
        progr_len = randint(5, 10)
        progr_end = progr_start + (progr_len - 1) * progr_step
        progr = list(range(progr_start, progr_end, progr_step))
        index = randint(0, progr_len - 1)
        correct_answer = progr[index]
        progr_for_quest = progr
        progr_for_quest[index] = ".."
        print(f"Question: {progr_for_quest}")
        answer = prompt.string("Your answer: ")
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
        print(f"Congratulations, {name}!")


def main():
    print("Welcome to the Brain Games!")
    name = welcome_guy()
    progression(name)
