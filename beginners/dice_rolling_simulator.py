import random #random module to generate random numbers. 

min_val = 1  # Minimum value of the dice
max_val = 6  # Maximum value of the dice

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dice...")
    print("The numbers are...")
    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))

    roll_again = input("Do you want to roll the dice again? (yes or no): ")
