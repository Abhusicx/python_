
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has Blackjack. You lose!"
    elif user_score == 0:
        return "Blackjack! You win!"
    elif user_score > 21:
        return "You went over 21. You lose!"
    elif computer_score > 21:
        return "Computer went over 21. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_input = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()

            if user_input == 'y':
                user_cards.append(deal_card())
            elif user_input == 'n':
                is_game_over = True
            else:
                print("Invalid input. Please type 'y' or 'n'.")

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, "
        f"final score: {computer_score}"
    )

    print(compare(user_score, computer_score))


while input("\nDo you want to play Blackjack? Type 'y' or 'n': ").lower() == 'y':
    play_game()
