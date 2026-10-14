import random
number = random.randint(1, 100)
guess = None
print("Welcome to the Number Guessing Game!")
while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number:
        if number - guess <= 10:
            print("Close! Try a higher number.")
        else:
            print("Too low! Try again.")
    elif guess > number:
        if guess - number <= 10:
            print("Close! Try a lower number.")
        else:
            print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the correct number: {number}")