import prompt


def welcome_user():
    name = prompt.string("May I have yuor name? ")
    print("Hello, " + name + "!")