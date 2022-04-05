import prompt


def welcome_guy():
    name = prompt.string("May I have your name? ")
    print("Hello, " + name + "!")
    return name
