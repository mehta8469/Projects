import random
import string

def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting random characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Example usage
password_length = 10
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
