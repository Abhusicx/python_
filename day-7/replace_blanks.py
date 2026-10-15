import random

word = ["ritik", "pooja", "sourav"]

chosen_word = random.choice(word)
print(chosen_word)

word_length=len(chosen_word)

placeholder=""
for position in range(word_length):
    placeholder += "_"

print(placeholder)

guess = input("enter a guess:\n")

display=""
for letter in chosen_word:
    if letter == guess:
        display+=guess
    else:
        display+="_"

print(display)
