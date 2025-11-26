from brain_games.cli import welcome_user
import prompt


OUTPUT_CORRECT_ANSWER = "Correct!"
MAX_RIGHT_ANSWERS_COUNT = 3


def play_game(get_question_and_answer, welcome_message):
    name = welcome_user()
    print(welcome_message)
    answer_right = 0
    while answer_right < MAX_RIGHT_ANSWERS_COUNT:
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print(OUTPUT_CORRECT_ANSWER)
            answer_right += 1
        else:
            output_wrong_answer = (f"`{answer}` is wrong answer ;(."
                                   f" Correct answer was `{correct_answer}`.\n"
                                   f"Let's try again, {name}!")
            print(output_wrong_answer)
            return

    if answer_right == 3:
        print(f"Congratulations, {name}!")
