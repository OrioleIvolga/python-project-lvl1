from random import randint
import prompt
from brain_games import engine


def progression(name):
    print("What number is missing in progression?")
    progr_start = randint(1, 100)
    progr_step = randint(1, 10)
    progr_len = randint(5, 10)
    progr_end = progr_start + progr_len * progr_step
    progr = list(range(progr_start, progr_end, progr_step))
    index = randint(0, progr_len - 1)
    correct_answer = progr[index]
    correct_answer = str(correct_answer)
    progr_for_quest = progr
    progr_for_quest[index] = ".."
    question = ' '.join([str(a) for a in progr_for_quest])


def main():
    engine.alg_game(progression)
