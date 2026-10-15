import random 

word = ['ritik', 'sourav', 'pooja']

chosen_word = random.choice(word)

print(chosen_word)

guess=input("enter letter?").lower()

for letter in chosen_word:
    if guess == letter: 
        print("right")
    else:
        print("wrong")