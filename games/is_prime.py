from random import randint
from games import engine


WELCOME_MASSAGE = (f"Answer `yes` if given number is prime. "
                   f"Otherwise answer `no`.")


def is_prime():
    random_number = randint(1, 100)
    question = str(random_number)
    correct_answer = checkPrime(random_number)
    return(question, correct_answer)


def checkPrime(random_number):
    divider_for_check = 2
    while random_number % divider_for_check != 0:
        divider_for_check += 1
    if random_number == divider_for_check:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return (correct_answer)


def main():
    engine.alg_game(is_prime, WELCOME_MASSAGE)