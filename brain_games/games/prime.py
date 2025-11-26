from random import randint
from brain_games import engine


WELCOME_MESSAGE = ('Answer "yes" if given number is prime. '
                   'Otherwise answer "no".')


def prime_game():
    random_number = randint(1, 100)
    question = str(random_number)
    correct_answer = "yes" if check_prime(random_number) else "no"
    return(question, correct_answer)


def check_prime(random_number):
    divider_for_check = 2
    while random_number % divider_for_check != 0:
        divider_for_check += 1
    return random_number == divider_for_check


def main():
    engine.play_game(prime_game, WELCOME_MESSAGE)
