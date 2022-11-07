import random

def guess(number, attempts):
    """Input guesses based on number attempts."""
    for _ in range(attempts):
        print(f"You have {attempts} attempts remaining to guess the number.")
        attempts -= 1
        guessed_number = int(input("Make a guess: "))
        if guessed_number == number:
            print(f"You got it! The answer was {number}.")
            return
        else:
            if guessed_number > number:
                print("Too high.")
            else:
                print("Too low.")
            if attempts > 0:
                print("Guess again.")
            else:
                print("You've run out of guesses. You lose.")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "hard":
    attempts = 5
elif difficulty == "easy":
    attempts = 10
else:
    attempts = 0

guess(number, attempts)
