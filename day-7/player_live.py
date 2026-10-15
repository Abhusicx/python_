import random

word = ["ritik", "pooja", "sourav"]
chosen_word = random.choice(word)
word_len = len(chosen_word)

placeholder = ""
for position in range(word_len):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []
lives = 5

while not game_over:

    guess = input("enter guess: ")
    lives -= 1

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("you win")

    elif lives == 0:
        game_over = True
        print("you lose")