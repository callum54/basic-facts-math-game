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

print()
print("➖basic facts maths game➕")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# if the player said yes then it prints what's in def instructions.
if want_instructions == "yes":
    instructions()

# asks player how many questions they will get.
number_of_questions = int(input(f"how many questions would you like? "))
print(f"you will get {number_of_questions} questions on your test ")
print()
print("press enter to continue ")
input()

# gets two random numbers
number = random.randint(1,100)
number_2 = random.randint(1,100)

print(f" {number} + {number_2} ")

