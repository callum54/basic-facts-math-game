
# asking if the user wants to see the instructions
answer = input(f"Do you want to read the instructions? ")
if answer == "yes":
    print("a")
elif answer == "no":
    print("you said no")
else:
    print("please answer with yes or no")

# asks user how many questions they will get
number_of_questions = int(input(f"how many questions would you like? "))
print(f"you picked {number_of_questions}")

