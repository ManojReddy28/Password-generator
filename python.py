import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Change the desired length of the password
password_length = 12  # You can modify this to generate a password of your desired length
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)