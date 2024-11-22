#Q3 create a reverse number guessing number that allows user to enter secret number
#use random to guess the number. ouput jow many tries it takes

from random import randint

attempts = 0

userSecret = int(input("Enter a number: "))
myGuess = 0

while myGuess != userSecret:
    myGuess = randint(1, 100)
    attempts += 1

print("it took me", attempts, "attempts to guess your number")

print("it took me {0} attempts to guess the number".format(attempts))
