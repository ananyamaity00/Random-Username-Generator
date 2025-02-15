import random
import string

def load_words(filename):
    """Load words from a file into a list."""
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"File {filename} not found. Using default words.")
        return []

def generate_username(adjectives, nouns, add_number=True, add_special_char=True, length=None):
    """Generate a random username with optional constraints."""
    if length and length < 4:
        print("Error: Username length is too short!")
        return None
    
    while True:
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        username = adjective + noun
        
        if add_number:
            username += str(random.randint(10, 99))
        
        if add_special_char:
            username += random.choice(string.punctuation)
        
        if length and len(username) > length:
            continue  # Retry if the username is too long
        
        return username

def save_to_file(username, filename="usernames.txt"):
    """Save the generated username to a file."""
    with open(filename, "a") as file:
        file.write(username + "\n")
    print(f"Username saved to {filename}.")

def main():
    adjectives = load_words("adjectives.txt") or ["Cool", "Happy", "Fast", "Brave", "Mighty"]
    nouns = load_words("nouns.txt") or ["Tiger", "Dragon", "Eagle", "Lion", "Panther"]
    
    print("Welcome to the Random Username Generator!")
    add_number = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    add_special_char = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    
    length = input("Enter desired username length (or press Enter to skip): ").strip()
    length = int(length) if length.isdigit() else None
    
    username = generate_username(adjectives, nouns, add_number, add_special_char, length)
    
    if username:
        print("Generated Username:", username)
        save_option = input("Would you like to save this username? (yes/no): ").strip().lower()
        if save_option == "yes":
            save_to_file(username)
    else:
        print("Failed to generate a username. Try again with different options.")

if __name__ == "__main__":
    main()
