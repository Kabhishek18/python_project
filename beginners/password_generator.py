import random
import string

def generate_password(length):
    """Generate a random password of the specified length."""
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by choosing random characters from the set
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Get the desired length of the password from the user
length = int(input("Enter password length: "))

# Generate and print the password
password = generate_password(length)
print("Password:", password)
