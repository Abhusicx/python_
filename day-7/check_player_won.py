import random 

word=["ritik", "pooja", "sourav"]

chosen_word=random.choice(word)
word_length=len(chosen_word)

placeholder=""
for position in range(word_length):
    placeholder+="_"

print(placeholder)

game_over=False
correct_word=[]
while not game_over:

    guess=input("enter guess:\n")

    display=""
    for letter in chosen_word:
        if letter == guess:
            display+=guess
            correct_word.append(guess)
        elif letter in correct_word:
            display+=letter
        else:
            display+="_"

    print(display)

    if display==chosen_word:
        game_over=True
        print("you won")
