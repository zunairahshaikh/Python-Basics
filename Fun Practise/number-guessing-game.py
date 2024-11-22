#Q2 create a number guessing game use random to create a secret number
#output how many tries user takes to guess

from random import randint

secretnum = randint(1,100)

userGuess = int(input("guess a number between 1 and 100: "))

while userGuess != secretnum:
    print("oops! wrong answer")
    print()
    continuePlay = input("Do you want to continue playing? ")
    if continuePlay != "yes":
        print(f"my number was {secretnum}")
        break
    else:
        userGuess = int(input("guess a number between 1 and 100: "))
