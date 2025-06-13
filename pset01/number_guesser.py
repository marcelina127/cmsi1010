import random

def number_guesser():
    print("Welcome to number guesser, friend! Guess a number between 1 and 1,000.")
    print("Type 'bye' or 'exit' to quit the game.")

    while True:
        number = random.randint(1, 1000)
        attempts = 0

        while True:
            guess = input("Your guess: ").strip().lower()

            if guess in ['bye', 'exit']:
                print("Thanks for playing! Goodbye.")
                return

            if not guess.isdigit():
                print("Please enter a valid number.")
                continue

            guess = int(guess)
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
                break


number_guesser()