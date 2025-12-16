from random import randint


WELCOME_MESSAGE = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def is_prime(random_number):
    if random_number < 2:
        return False
    if random_number == 2:
        return True
    if random_number % 2 == 0:
        return False
    i = 3
    while i * i <= random_number:
        if random_number % i == 0:
            return False
        i += 2
    return True


def generate_prime_question():
    random_number = randint(1, 100)
    question = str(random_number)
    correct_answer = "yes" if is_prime(random_number) else "no"
    return question, correct_answer
