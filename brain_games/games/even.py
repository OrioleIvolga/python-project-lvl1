from random import randint


WELCOME_MESSAGE = (
    'Answer "yes" if the number is even, otherwise answer "no".'
)


def generate_even_question():
    random_number = randint(1, 100)
    question = str(random_number)
    correct_answer = "yes" if is_even(random_number) else "no"
    return (question, correct_answer)


def is_even(random_number):
    return random_number % 2 == 0
