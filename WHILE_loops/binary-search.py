#Q Ask user for a  number between 1-100
# your program can ask yes or no questions (max 10)
#your program should tell the correct guess everytime

print("think of a number between 1-100")
notGuessed = True
highestnum = 101
lowestnum = 0
attempts = 0
while attempts<=10 and notGuessed:
    guess = int((highestnum+lowestnum)/2)
    answer = input(f"is your number {guess}? ")
    attempts += 1
    if answer == "yes":
        print(f"I guessed your number ({guess}) in {attempts} attempts")
        notGuessed = False
    else:
        answer = input("is your number higher than my guess? ")
        if answer == "yes":
            lowestnum = guess
        else:
            highestnum = guess
