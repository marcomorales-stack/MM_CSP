# MM, 7th, Number Guessing Game

import random

# Range: 1 to 101
# Attemps: 6
secret_number = random.randint(1, 101)

print("I'm thinking of a number between 1 and 101")
print("You have 6 tries to guess it!")

guesses_used = 0
guess = 0
while True:
    if guesses_used > 6:
        print(f"you lost, the number was {secret_number}")
        break
    guess = int(input("Guess a number. "))
    if guess == secret_number:
        print(f"You won. The number was {secret_number}")
        break
    elif guess > secret_number:
        print("Too high")
        guesses_used += 1
        print(f"Your attempt {guesses_used}")
    elif guess < secret_number:
        print("Too low")
        guesses_used += 1
        print(f"Your attempt {guesses_used}")
    else:
        print("guess a NUMBER")


