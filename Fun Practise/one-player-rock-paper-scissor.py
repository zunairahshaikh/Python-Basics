#Q1 create a one player rock paper scissor game using random for computer input

import random

choices = ["rock", "paper", "scissors"]

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' to exit the game.\n")

    while True:
        player_choice = input("Your choice: ").lower()

        if player_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break

      
        if player_choice not in choices:
            print("Invalid choice. Please try again.\n")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

    
        result = determine_winner(player_choice, computer_choice)
        print(f"{result}\n")


play_game()
