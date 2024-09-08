import random
from hangman_words import words #Hangman words fetched from another python file
from hangman_art import stages  # ASCII stages for hangman

# Choose a random word
chosen_word = random.choice(words)

# Create a placeholder for the word (e.g., '_ _ _ _ _' for 'apple')
placeholder = ["_"] * len(chosen_word)

# Set the number of allowed attempts
attempts = len(chosen_word)

# Store incorrect guesses
incorrect_guesses = []


# Game start display
print("Welcome to Hangman!")
print(" ".join(placeholder))
print(f"You have {attempts} attempts remaining.")
print(stages[0])

# Continue guessing until the word is guessed or attempts run out
while attempts > 0 and "_" in placeholder:
    guess = input("Guess a letter: ").lower()

    # Check if the letter was already guessed
    if guess in incorrect_guesses or guess in placeholder:
        print(f"You already guessed '{guess}'. Try another letter.")
        continue

    # If the guessed letter is in the chosen word
    if guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                placeholder[index] = guess
        print("Good guess!")
    else:
        incorrect_guesses.append(guess)
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts remaining.")

    # Show the updated word, wrong guesses, and the current stage of the hangman
    print(" ".join(placeholder))
    print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
    print(stages[6 - attempts])  # Update hangman stage

# Game over messages
if "_" not in placeholder:
    print(f"Congratulations! You've guessed the word: {chosen_word}")
else:
    print(f"Sorry, you ran out of attempts. The word was: {chosen_word}")
