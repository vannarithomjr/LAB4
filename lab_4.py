"""
This program allows a user three tries to guess the correct answer to the question
question = "What is the capital of California?". The answer is "Sacramento".

We first set max_tries = 3. Then we create a loop to iterate three times. For each iteration,
we ask the user for the answer (user input). Then based on the anmswer the user gives, we check
to see if the user input matcjes the answer. If so, print "Correct!", then terminate the loop with a break statement.

If the user could not guess the correct answer within the max_tries, then print
"You have used up your allotment of guesses." then print "The correct answer is 'Sacramento'".
"""


def main():
    question = "What is the capital of California?"
    answer1 = "Sacramento"
    answer2 = "sacramento"
    ask(question, answer1, answer2)

def ask(question, answer1, answer2, tries = 3):
    while tries > 0:
        user_answer = input(question)
        
        if (user_answer == answer1 or user_answer == answer2) and (tries == 3):
            print("Amazing! You got it at the first try. You must be a guru of Geography.")
            break
        elif (user_answer == answer1 or user_answer == answer2) and (tries <3):
            print("Good job! You got it right before you run out of attmempts")
            break

        elif (user_answer != answer1 or user_answer != answer2) and tries > 1:
            tries = tries - 1
            print("Clearly, geography is not your thing. You still have", tries, "more attempts.")

        elif (user_answer != answer1 or user_answer != answer2) and (tries == 1):
            print("I am sorry my friend. You have burned out all of your  attempts and failed as an Californian Citizen.")

main()