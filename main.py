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

want_instructions = yes_no("Do you want to read the instructions? ")

# if the player said yes then it prints what's in def instructions.
if want_instructions == "yes":
    instructions()

# asks player how many questions they will get.
number_of_questions = int(input(f"how many questions would you like? "))
print(f"you will get {number_of_questions} questions on your quiz ")
print()

# difficulty levels


def easy():
    print("starting easy mode")
    print()
    # gets two random numbers
    number_1 = random.randint(1, 50)
    number_2 = random.randint(1, 50)

    answer_1 = number_1 + number_2

    # makes math equation and checks the players answer
    user_answer = int(input(f" {number_1} + {number_2} "))
    if user_answer == answer_1:
        print("correct!")
    else:
        print("that one was not correct")
        print(f"the correct answer was {answer_1}")


def normal():
    print("starting normal mode")
    print()
    # gets two random numbers
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)

    answer_1 = number_1 + number_2

    # makes math equation and checks the players answer
    user_answer = int(input(f" {number_1} + {number_2} "))
    if user_answer == answer_1:
        print("correct!")
    else:
        print("that one was not correct")
        print(f"the correct answer was {answer_1}")



def hard():
    print("starting hard mode")
    print()
    # gets two random numbers
    number_1 = random.randint(1, 160)
    number_2 = random.randint(1, 160)

    answer_1 = number_1 + number_2

    # makes math equation and checks the players answer
    user_answer = int(input(f" {number_1} + {number_2} "))
    if user_answer == answer_1:
        print("correct!")
    else:
        print("that one was not correct")
        print(f"the correct answer was {answer_1}")


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

if want_difficulty == "easy":
    easy()
elif want_difficulty == "normal":
    normal()
