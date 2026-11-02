import random
import string

# SystemRndom uses the operating system's secure random source
# Which is safer for passwords than the default random generator
rng = random.SystemRandom()

MIN_LENGTH = 5
MAX_LENGTH = 25

def get_length():
    """ Ask the user for a valid password length."""
    while True:
        try:
            length = int(input(f"Enter password length({MIN_LENGTH}-{MAX_LENGTH}): "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if MIN_LENGTH <= length <= MAX_LENGTH:
            return length
        print(f"Length must be between {MIN_LENGTH} and {MAX_LENGTH}.")


def generate_password(length):
    """Build a random password containing all four character types."""
    pools = [
        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits,
        string.punctuation,
    ]

    #guarantee at least one character from each pool
    password = [rng.choice(pool) for pool in pools]

    #Fill the remaining space from all characters combined
    all_characters = "".join(pools)
    password += [rng.choice(all_characters) for _ in range(length - len(password))]

    #shuffle so the gauranteed characters are not always at the start
    rng.shuffle(password)
    return "".join(password)

def main():
    print("password Generator")

    while True:
        length = get_length()
        print(f"\nYour password: {generate_password (length)}\n")

        again = input("Generate another? (y/n): ").strip().lower()
        if again != "y":
            break

main()


