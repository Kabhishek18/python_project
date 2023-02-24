import random

print("Welcome to Rock, Paper, Scissors game!")

choices = ["rock", "paper", "scissors"]
play_again = "yes"

while play_again == "yes":
    # Get the user's choice
    user_choice = input("Enter your choice (rock/paper/scissors): ")

    # Get the computer's choice
    computer_choice = random.choice(choices)

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Rock beats scissors.")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Paper beats rock.")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors beats paper.")
    else:
        print("You lose! " + computer_choice + " beats " + user_choice + ".")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes or no): ")

print("Thanks for playing!")
