#import necessary library
import random

# Create the number to be guessed
intAns = (random.randint(10,20))

# Initialise vars
intGuess = 1
intCount = 0

# Set Guess limit var
totCount = 5

while intGuess != 0:
    # Get input from user
    intGuess = int(input("Enter Guess or 0 to exit: "))

    # Increment count variable
    intCount += 1

    if intCount < totCount:
        # main testing sequence
        if intGuess == 0:
            break
        elif intGuess < intAns:
            print(f"Your guess = {intGuess} is Too LOW, try again")
        elif intGuess > intAns:
            print(f"Your guess = {intGuess} is Too HIGH, try again")
        else:
            print(f"Your guess = {intGuess} is Correct")
            break
    else:
        print("You have run out of Guesses!")
        intGuess = 0

print("Goodbye")
