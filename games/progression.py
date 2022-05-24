from random import randint
from games import engine

WELCOME_MASSAGE = "What number is missing in progression?"
START_RANDOM_RANGE_FOR_PROGR_START = 1
END_RANDOM_RANGE_FOR_PROGR_START = 100
START_RANDOM_RANGE_FOR_PROGR_STEP = 1
END_RANDOM_RANGE_FOR_PROGR_STEP = 10
START_RANDOM_RANGE_FOR_PROGR_LEN = 5
END_RANDOM_RANGE_FOR_PROGR_LEN = 10


def progression():
    progr, progr_len = generatingProgression()
    index = randint(0, progr_len - 1)
    correct_answer = progr[index]
    correct_answer = str(correct_answer)
    progr_for_quest = progr
    progr_for_quest[index] = ".."
    question = ' '.join([str(a) for a in progr_for_quest])
    return (question, correct_answer)


def generatingProgression():
    progr_start = randint(START_RANDOM_RANGE_FOR_PROGR_START,
                          END_RANDOM_RANGE_FOR_PROGR_START
                          )
    progr_step = randint(START_RANDOM_RANGE_FOR_PROGR_STEP, 
                         END_RANDOM_RANGE_FOR_PROGR_STEP
                         )
    progr_len = randint(START_RANDOM_RANGE_FOR_PROGR_LEN, 
                        END_RANDOM_RANGE_FOR_PROGR_LEN
                        )
    progr_end = progr_start + progr_len * progr_step
    progr = list(range(progr_start, progr_end, progr_step))
    return(progr, progr_len)


def main():
    engine.alg_game(progression, WELCOME_MASSAGE)
