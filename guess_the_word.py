# Shahla Zarisfi
# CIS256 Fall 2025
# EX 4
import random
import string

# Choose a random word from the word list
def choose_word(words, rng=None):
    rng = rng or random
    return rng.choice(words)

# Show guessed letters in the word
def reveal_letters(secret, current, guess):
    result = ""
    for s, c in zip(secret, current):
        result += guess if s.lower() == guess else c
    return result

# Check if player guessed all letters
def is_word_guessed(masked):
    return "_" not in masked

# Make sure the guess is one letter (a–z)
def normalize_guess(raw):
    raw = raw.strip().lower()
    if len(raw) == 1 and raw in string.ascii_lowercase:
        return raw
    return None

# Main game loop
def play_game():
    word_list = ["apple", "orange", "mango", "grape", "apricot"]
    secret = choose_word(word_list)
    masked = "_" * len(secret)
    attempts = 6
    guessed = set()

    print("Welcome to Guess the Word!")
    print(masked)

    while attempts > 0 and not is_word_guessed(masked):
        raw = input("Guess one letter: ")
        guess = normalize_guess(raw)

        if not guess:
            print("Enter one letter (a-z).")
            continue
        if guess in guessed:
            print("Already guessed.")
            continue

        guessed.add(guess)

        if guess in secret:
            masked = reveal_letters(secret, masked, guess)
            print("Good guess:", masked)
        else:
            attempts -= 1
            print("Wrong guess. Attempts left:", attempts)

    if is_word_guessed(masked):
        print("You guessed the word:", secret)
    else:
        print("Out of tries! The word was:", secret)

# Run the game
if __name__ == "__main__":
    play_game()