from brain_games.welcome_guy import welcome_guy


general_greeting = "Welcome to the Brain Games!"
output_correct_answ = "Correct!"
output_wrong_answ = (f"`{answer}` is wrong answer ;(."
                    f" Correct answer was `{correct_answer}`.\n"
                    f"Let's try again, {name}!")
congratulations = "Congratulations, "


def alg_game(function):
	print(general_greeting)
	welcome_guy()
	answer_right = 0
	while answer_right < 3:
		function()
		print(f"Question: {question}")
		answer = prompt.string("Your answer: ")
		if answer == correct_answer:
			print(output_correct_answ)
            answer_right += 1
        else:
            print(output_wrong_answ)
            break

    if answer_right == 3:
        print(f"{congratulations}{name}!")


def main():
    name = welcome_guy()
    alg_game(function)