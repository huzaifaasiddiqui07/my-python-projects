# ============================================
# Number Guessing Game
# Author: Huzaifa Siddiqui
# Course: Software Engineering - NED Academy
# Description: A fun guessing game where the
#              computer picks a random number
#              and the player has 3 attempts
#              to guess it correctly.
# ============================================

import random


def guess_num():
    """
    Generates a random number between 0 and 10.
    Player has 3 attempts to guess the correct number.
    """
    number = random.randint(0, 10)
    attempts = 3

    print("=" * 40)
    print("       NUMBER GUESSING GAME")
    print("=" * 40)
    print("I have picked a number between 0 and 10.")
    print(f"You have {attempts} attempts. Good luck!\n")

    while attempts > 0:
        guess = int(input(f"Attempts left: {attempts} → Enter your guess: "))

        if guess == number:
            print("\n🎉 Congratulations! You guessed it right!")
            return
        elif guess < number:
            print("Too low! Try higher.\n")
        else:
            print("Too high! Try lower.\n")

        attempts -= 1

    print(f"\n❌ You Lost! The correct number was {number}.")
    print("Better luck next time!")


# --- Main Program ---
guess_num()
