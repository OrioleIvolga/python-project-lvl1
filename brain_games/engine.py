from brain_games.cli import welcome_user
import prompt


OUTPUT_CORRECT_ANSWER = "Correct!"
MAX_RIGHT_ANSWERS_COUNT = 3


def play_game(get_question_and_answer, welcome_message):
    name = welcome_user()
    print(welcome_message)
    for _ in range(MAX_RIGHT_ANSWERS_COUNT):
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer != correct_answer:
            print (f"`{answer}` is wrong answer ;(."
                   f" Correct answer was `{correct_answer}`.\n"
                   f"Let's try again, {name}!")
            return
        print(OUTPUT_CORRECT_ANSWER)
    print(f"Congratulations, {name}!")
