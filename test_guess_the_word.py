# Shahla Zarisfi
# CIS256 Fall 2025
# EX 4
# # Import random for predictable testing and functions to test
import random
from guess_the_word import (
    choose_word,
    reveal_letters,
    is_word_guessed,
    normalize_guess,
)

# Test that choose_word picks a valid word from the list
def test_choose_word_is_from_list():
    words = ["apple", "orange", "mango", "grape", "apricot"]
    rng = random.Random(1)  
    picked = choose_word(words, rng=rng)
    assert picked in words  

# Test that correct guesses reveal matching letters
def test_reveal_letters_correct_guess_reveals_positions():
    secret = "apple"
    current = "_____"
    updated = reveal_letters(secret, current, "a")
    assert updated == "a____"
    updated = reveal_letters(secret, updated, "p")
    assert updated == "app__"
    updated = reveal_letters(secret, updated, "l")
    assert updated == "appl_"
    updated = reveal_letters(secret, updated, "e")
    assert updated == "apple"

# Test that wrong guesses do not change the masked word
def test_reveal_letters_wrong_guess_changes_nothing():
    secret = "mango"
    current = "_____"
    updated = reveal_letters(secret, current, "z")
    assert updated == current

# Test that is_word_guessed returns True when no underscores remain
def test_is_word_guessed_true_when_no_underscores():
    assert is_word_guessed("apple") is True

# Test that is_word_guessed returns False when underscores exist
def test_is_word_guessed_false_when_underscores_exist():
    assert is_word_guessed("app_e") is False

# Test that normalize_guess accepts one letter and lowercases it
def test_normalize_guess_accepts_single_letter_and_lowercases():
    assert normalize_guess("A") == "a"
    assert normalize_guess("  b  ") == "b"

# Test that normalize_guess rejects invalid input
def test_normalize_guess_rejects_bad_input():
    assert normalize_guess("") is None
    assert normalize_guess("ab") is None
    assert normalize_guess("1") is None
    assert normalize_guess("#") is None