
import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''

    all_chars = lower + upper + numbers + special_chars

    if not all_chars:
        raise ValueError("At least one character set must be selected!")

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password
length=18
length = int(input("Enter password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
print(f"Generated password: {password}")
