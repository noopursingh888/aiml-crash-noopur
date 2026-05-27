import random


secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7


print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")


while attempts < max_attempts:

    guess = int(input("Enter your guess: "))

    attempts += 1

    if guess == secret_number:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break

    elif guess > secret_number:
        print("Too high")

    else:
        print("Too low")

    print(f"Attempts left: {max_attempts - attempts}")


if attempts == max_attempts and guess != secret_number:
    print(f"You lost! The correct number was {secret_number}")