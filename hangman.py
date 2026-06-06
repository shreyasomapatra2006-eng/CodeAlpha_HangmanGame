import random

WORDS = ["patient", "guide", "housemaid", "original", "algorithm"]

HANGMAN_STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""
]

MAX_WRONG = 6


def display_state(word, guessed, wrong_count):
    print(HANGMAN_STAGES[wrong_count])
    print("\nWord: ", end="")
    print(" ".join(ch if ch in guessed else "_" for ch in word))
    print(f"\nWrong guesses left: {MAX_WRONG - wrong_count}")
    if guessed - set(word):
        print(f"Incorrect letters: {', '.join(sorted(guessed - set(word)))}")


def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong_count = 0

    print("\n🎮  Welcome to Hangman!")
    print("══════════════════════")

    while True:
        display_state(word, guessed, wrong_count)

        # Win check
        if all(ch in guessed for ch in word):
            print(f"\n🎉 You won! The word was '{word}'.")
            break

        # Lose check
        if wrong_count >= MAX_WRONG:
            print(f"\n💀 Game over! The word was '{word}'.")
            break

        # Get input
        guess = input("\nEnter a letter: ").strip().lower()

        if not guess or not guess.isalpha() or len(guess) != 1:
            print("⚠  Please enter a single letter.")
            continue

        if guess in guessed:
            print(f"  You already guessed '{guess}'. Try another.")
            continue

        guessed.add(guess)

        if guess in word:
            print(f"  ✓ '{guess}' is in the word!")
        else:
            wrong_count += 1
            print(f"  ✗ '{guess}' is not in the word.")

    # Play again?
    again = input("\nPlay again? (y/n): ").strip().lower()
    if again == "y":
        play()
    else:
        print("\nThanks for playing! Goodbye. 👋\n")


if __name__ == "__main__":
    play()
