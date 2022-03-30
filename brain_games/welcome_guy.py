import prompt


def welcome_guy():
    name = prompt.string("May I have yuor name? ")
    print("Hello, " + name + "!")
    return name
