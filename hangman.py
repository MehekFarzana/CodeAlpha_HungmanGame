import random

# List of 5 predefined words
words = ["python", "coding", "computer", "program", "hangman"]

# Select a random word
secret_word = random.choice(words)

# Store correctly guessed letters
guessed_letters = []

# Maximum incorrect guesses allowed
max_attempts = 6
incorrect_guesses = 0

print("=" * 35)
print("       WELCOME TO HANGMAN!")
print("=" * 35)
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    # Check if the player has guessed the word
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        print("You won the game!")
        break

    # Take a letter from the player
    guess = input("Enter a letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.\n")
        continue

    # Check whether the letter was already guessed
    if guess in guessed_letters:
        print("You have already guessed that letter. Try again.\n")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!\n")
    else:
        incorrect_guesses += 1
        print("Wrong guess!\n")

else:
    print("\nGame over! You ran out of attempts.")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")