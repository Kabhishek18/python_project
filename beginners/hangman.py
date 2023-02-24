import random

# Define a list of words
words = ["python", "java", "javascript", "ruby", "php", "swift", "kotlin", "scala", "perl"]

# Select a random word from the list
word = random.choice(words)

# Initialize variables
guesses = []
max_attempts = 6
attempts = 0

# Loop until the player wins or runs out of attempts
while attempts < max_attempts:
    # Print the current state of the word
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_ "
    print(display_word)

    # Ask the player for a guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    # Check if the guess is correct
    if guess in word:
        guesses.append(guess)
        print("Correct!")
    else:
        attempts += 1
        print("Incorrect. Attempts left:", max_attempts - attempts)

    # Check if the player has won
    if all(letter in guesses for letter in word):
        print("Congratulations! You have guessed the word:", word)
        break

# Check if the player has lost
if attempts == max_attempts:
    print("Sorry, you have run out of attempts. The word was:", word)
