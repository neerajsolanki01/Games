import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        guess = input("Take a guess: ")
        attempts += 1

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    print("Thanks for playing!")

guess_the_number()
