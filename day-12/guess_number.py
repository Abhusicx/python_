import random

def set_turns(difficulty_choice):
    if difficulty_choice == 'easy':
        return 10
    elif difficulty_choice == 'hard':
        return 5
    else:
        print("Invalid difficulty entered. Defaulting to easy.")
        return 10

def check_guess(user_guess, correct_answer):
    if correct_answer > user_guess:
        print("Too low!")
        return False
    elif correct_answer < user_guess:
        print("Too high!")
        return False
    else:
        print(f"🎯 You got it! The answer was {correct_answer}.")
        return True

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
remaining_turns = set_turns(difficulty)

# Active Game Loop
game_over = False
while not game_over and remaining_turns > 0:
    print(f"You have {remaining_turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    game_over = check_guess(guess, answer)
    
    if not game_over:
        remaining_turns -= 1
        if remaining_turns == 0:
            print(f"You've run out of guesses! You lose. The answer was {answer}.")
