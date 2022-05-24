from brain_games.welcome_guy import welcome_guy
import prompt


GENERAL_GREETING = "Welcome to the Brain Games!"
OUTPUT_CORRECT_ANSWER = "Correct!"


def alg_game(function, welcom_massage):
    print(GENERAL_GREETING)
    name = welcome_guy()
    print(welcom_massage)
    answer_right = 0
    while answer_right < 3:
        question, correct_answer = function()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print(OUTPUT_CORRECT_ANSWER)
            answer_right += 1
        else:
            output_wrong_answ = (f"`{answer}` is wrong answer ;(."
                                 f" Correct answer was `{correct_answer}`.\n"
                                 f"Let's try again, {name}!")
            print(output_wrong_answ)
            break

    if answer_right == 3:
        print("Congratulations, " + name + "!")


def main():
    alg_game()
