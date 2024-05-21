import random


# asking if the player wants to see the instructions.


def yes_no(question):
    while True:
        answer = input(question).lower()
        if answer == "yes" or answer == "Yes":
            return "yes"
        elif answer == "no" or answer == "No":
            return "you said no"
        else:
            print("Please answer with yes or no")


# instructions.


def instructions():
    print('''

    🔥🔥🔥Welcome to Basic facts maths game!🔥🔥🔥

    to play you will be asked how many questions you want to be in the quiz.
    Then you will answer the questions.

    once you have answered all your questions you can check your
    results and see what you got wrong

        good luck!
          ''')


# game title
print()
print("➖basic facts maths game➕")
print()

# if the player said yes then it prints what's in def instructions.
want_instructions = yes_no("Do you want to read the instructions? ")
if want_instructions == "yes":
    instructions()




# asks player how many questions they will get.
number_of_questions = int(input(f"how many questions would you like? "))
print(f"you will get {number_of_questions} questions on your quiz ")
print()


# asks what difficulty the player wants
def difficulty(question):
    while True:
        answer = input(question).lower()
        if answer == "easy" or answer == "Easy":
            return "easy"
        elif answer == "normal" or answer == "Normal":
            return "normal"
        elif answer == "hard" or answer == "Hard":
            return "hard"
        else:
            print("please type in either easy, normal or hard")


want_difficulty = difficulty("select your difficulty of easy, normal or hard: ")

print()
print("press enter to start your quiz ")
input()


# makes the easy questions
def easy_questions():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-'])
    question = f"What is {num1} {operator} {num2}? "
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 / num2
    return question, answer

# finds out if the players answer is correct then adds it to a score


def easy():
    score = 0

    for _ in range(number_of_questions):
        question, correct_answer = easy_questions()
        user_answer = input(question)
        if float(user_answer) == correct_answer:
            score += 1
            print("Correct!")
        else:
            print("that one was not correct")
            print(f"the correct answer was {correct_answer}")
    print(f"You got {score} out of {number_of_questions}.")

# makes the normal questions


def normal_questions():
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    operator = random.choice(['+', '-'])
    question = f"What is {num1} {operator} {num2}? "
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 / num2
    return question, answer

# finds out if the players answer is correct then adds it to a score


def normal():
    score = 0

    for _ in range(number_of_questions):
        question, correct_answer = normal_questions()
        user_answer = input(question)
        if float(user_answer) == correct_answer:
            score += 1
            print("Correct!")
        else:
            print("that one was not correct")
            print(f"the correct answer was {correct_answer}")
    print(f"You got {score} out of {number_of_questions}.")

# makes the hard questions


def hard_questions():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)  # gets two random numbers from 1 to 100
    operator = random.choice(['+', '-'])  # gets either plus or minus
    question = f"What is {num1} {operator} {num2}? "  # creates the question
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 / num2
    return question, answer

# finds out if the players answer is correct then adds it to a score


def hard():
    score = 0  # puts the players score to zero

    for _ in range(number_of_questions):
        question, correct_answer = hard_questions()
        user_answer = input(question)
        if float(user_answer) == correct_answer:
            score += 1
            print("Correct!")  # if the player got the question correct then
            # it will add one to his score
        else:
            print("that one was not correct")
            print(f"the correct answer was {correct_answer}")  # if the player got the question
            # wrong then it will tell him the correct answer
    print(f"You got {score} out of {number_of_questions}.")


if want_difficulty == 'easy':  # if the player said easy then it will
    # run the dif called easy
    easy()
elif want_difficulty == 'normal':  # if the player said normal then it will run the dif called normal
    normal()
elif want_difficulty == 'hard':  # if the player said hard then it will run the dif called hard
    hard()
