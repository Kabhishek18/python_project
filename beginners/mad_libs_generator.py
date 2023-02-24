# Ask the user to enter words to fill in the blanks
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
adverb1 = input("Enter an adverb: ")
adjective2 = input("Enter an adjective: ")
noun2 = input("Enter a noun: ")

# Create the story using the user's input
story = f"The {adjective1} {noun1} {verb1} {adverb1} to the {adjective2} {noun2}."

# Print the story
print(story)