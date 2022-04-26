from brain_games.welcome_guy import welcome_guy
import prompt


general_greeting = "Welcome to the Brain Games!"
output_correct_answ = "Correct!"
congratulations = "Congratulations, "


def alg_game(function):
    print(general_greeting)
    name = welcome_guy()
    answer_right = 0
    while answer_right < 3:
        correct_answer, question = function()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print(output_correct_answ)
            answer_right += 1
        else:
            output_wrong_answ = (f"`{answer}` is wrong answer ;(."
                                 f" Correct answer was `{correct_answer}`.\n"
                                 f"Let's try again, {name}!")
            print(output_wrong_answ)
            break

    if answer_right == 3:
        print(f"{congratulations}{name}!")


def main():
    alg_game()
