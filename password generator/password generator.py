import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine all character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        length = int(input("Enter the length of each password: "))
        for i in range(num_passwords):
            password = generate_password(length)
            print(f"Password {i+1}: {password}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
