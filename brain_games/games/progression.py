from random import randint
from brain_games import engine

WELCOME_MESSAGE = "What number is missing in progression?"
START_RANDOM_RANGE_FOR_PROGRESSION_START = 1
END_RANDOM_RANGE_FOR_PROGRESSION_START = 100
START_RANDOM_RANGE_FOR_PROGRESSION_STEP = 1
END_RANDOM_RANGE_FOR_PROGRESSION_STEP = 10
START_RANDOM_RANGE_FOR_PROGRESSION_LEN = 5
END_RANDOM_RANGE_FOR_PROGRESSION_LEN = 10


def progression():
    progression = generate_progression()
    index = randint(0, len(progression) - 1)
    correct_answer = progression[index]
    correct_answer = str(correct_answer)
    progression_for_quest = progression.copy()
    progression_for_quest[index] = ".."
    question = ' '.join([str(a) for a in progression_for_quest])
    return (question, correct_answer)


def generate_progression():
    progression_start = randint(START_RANDOM_RANGE_FOR_PROGRESSION_START,
                                END_RANDOM_RANGE_FOR_PROGRESSION_START
                                )
    progression_step = randint(START_RANDOM_RANGE_FOR_PROGRESSION_STEP,
                               END_RANDOM_RANGE_FOR_PROGRESSION_STEP
                               )
    progression_len = randint(START_RANDOM_RANGE_FOR_PROGRESSION_LEN,
                              END_RANDOM_RANGE_FOR_PROGRESSION_LEN
                              )
    progression_end = progression_start + progression_len * progression_step
    progression = list(range(progression_start,
                             progression_end,
                             progression_step
                             )
                       )
    return progression


def main():
    engine.play_game(progression, WELCOME_MESSAGE)
