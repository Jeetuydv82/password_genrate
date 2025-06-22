import random
import string

def generate_password():
    print("Welcome to the Password Generator!")
    # Get desired password length from user
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ask user about complexity
    print("\nInclude the following in the password:")
    use_uppercase = input("Uppercase letters (Y/N)? ").strip().lower() == 'y'
    use_digits = input("Numbers (Y/N)? ").strip().lower() == 'y'
    use_symbols = input("Symbols (Y/N)? ").strip().lower() == 'y'

    # Combine selected character sets
    characters = lowercase
    if use_uppercase:
        characters += uppercase
    if use_digits:
        characters += digits
    if use_symbols:
        characters += symbols

    # Make sure we have characters to choose from
    if not characters:
        print("You must select at least one character type!")
        return

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    print("\nGenerated Password:", password)
# Run the password generator
generate_password()
