import random

print("Rock, Paper, Scissors")

your_object=input("Choose one...Rock, Paper, Scissors\n")
Object=["Rock", "Paper", "Scissor"]

if your_object=="Rock" or your_object=="Paper" or your_object=="Scissors":
    computer_object=random.choice(Object)
    print(computer_object)
else:
    print("choose from the list")