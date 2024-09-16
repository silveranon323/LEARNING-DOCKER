import itertools
import string

def brute_force_attack(password):
    chars = string.ascii_letters + string.digits  # Characters to attempt (letters and digits)
    password_length = len(password)  # Length of the password to guess

    # Generate combinations of possible passwords with the same length
    for attempt in itertools.product(chars, repeat=password_length):
        attempt_password = ''.join(attempt)
        print(f"Trying password: {attempt_password}")
        
        if attempt_password == password:
            print(f"Password found: {attempt_password}")
            return True

    print("Password not found.")
    return False

# Example password to crack
password = "abc123"

# Call the brute force attack function
brute_force_attack(password)
