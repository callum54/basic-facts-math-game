import random
import time

print()  # creates space between the top of the page
# asks for the players name
name = input("what is your name?: ")

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
    Then you will answer the questions. ''')

    time.sleep(2.5)  # time.sleep adds a 2.5, second timer before printing the next bit
    # so that the player has time to read
    print(''' 

    once you have picked how many questions you want you will get to select your difficulty ''')

    time.sleep(2.5)
    print('''
    
    easy mode
    easy mode will give you addition and subtraction questions between the numbers 1 and 10
    
    normal mode
    normal mode gives you addition, subtraction and multiplication, the numbers that you will 
    see in normal mode are between 1 and 30. all answers are rounded to 2 decimal places.
    
    hard mode
    hard mode will give you addition, subtraction, multiplication and division. the numbers
    that you will see in hard mode are between 1 and 50. remember that division and multiplication 
    are rounded to 2 decimal place. ''')

    time.sleep(3.5)
    print('''
    
    the symbol + is addition
    the symbol - is subtraction
    the symbol * is multiplication
    the symbol / is division ''')

    time.sleep(2.5)
    print('''
    once you have answered all your questions you can check your
    results and see what you got wrong. you can scroll back up to 
    read the instructions. 
    
        good luck!
          ''')


# creates space between the last line of code so the code isn't grouped together
print()

# welcomes the player
print(f"hello {name} welcome to...")

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
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    operator = random.choice(['+', '-'])
    question = f"What is {number_1} {operator} {number_2}? "
    if operator == '+':
        answer = number_1 + number_2
    elif operator == '-':
        answer = number_1 - number_2
    else:
        answer = number_1 / number_2
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
    print(f"you got {score} out of {number_of_questions}.")

# makes the normal questions


def normal_questions():
    number_1 = random.randint(1, 30)
    number_2 = random.randint(1, 30)
    operator = random.choice(['+', '-', "*"])
    question = f"What is {number_1} {operator} {number_2}? "
    if operator == '+':
        answer = number_1 + number_2
    elif operator == '-':
        answer = number_1 - number_2
    elif operator == '*':
        answer = round(number_1 * number_2, 2)
    else:
        answer = number_1 / number_2
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
      print(f"you got {score} out of {number_of_questions}.")

# makes the hard questions


def hard_questions():
    number_1 = random.randint(1, 50)
    number_2 = random.randint(1, 50)  # gets two random numbers from 1 to 100
    operator = random.choice(['+', '-', '*', '/'])  # gets either plus or minus
    question = f"What is {number_1} {operator} {number_2}? "  # creates the question
    if operator == '+':
        answer = number_1 + number_2
    elif operator == '-':
        answer = number_1 - number_2
    elif operator == '*':
        answer = round(number_1 * number_2, 2)
    else:
        answer = round(number_1 / number_2, 2)
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
    print(f"you got {score} out of {number_of_questions}.")


if want_difficulty == 'easy':  # if the player said easy then it will
    # run the dif called easy
    easy()
elif want_difficulty == 'normal':  # if the player said normal then it will run the dif called normal
    normal()
elif want_difficulty == 'hard':  # if the player said hard then it will run the dif called hard
    hard()
