from random import randint


WELCOME_MESSAGE = "What number is missing in the progression?"
START_RANDOM_RANGE_FOR_PROGRESSION_START = 1
END_RANDOM_RANGE_FOR_PROGRESSION_START = 100
START_RANDOM_RANGE_FOR_PROGRESSION_STEP = 1
END_RANDOM_RANGE_FOR_PROGRESSION_STEP = 10
START_RANDOM_RANGE_FOR_PROGRESSION_LEN = 5
END_RANDOM_RANGE_FOR_PROGRESSION_LEN = 10


def generate_progression_question():
    progression = generate_progression()
    index = randint(0, len(progression) - 1)
    correct_answer = str(progression[index])
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
    return [
        progression_start + i * progression_step
        for i in range(progression_len)
    ]
