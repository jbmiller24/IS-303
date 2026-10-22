
from Level67_wordle_functions import choose_word, get_guess, evaluate_guess, display_guess, has_won
# Welcome statement explains the rules to the game
print("Welcome to Mystery Wordle!")
print("Guess the five-letter word.")
print("G = correct letter and position")
print("Y = correct letter, wrong position")
print("- = letter is not in the word")

play_again = "yes"

# Starts a new game with a new secret word and resets the game variables
while play_again == "yes":
    secret_word = choose_word()
    previous_guesses = []
    won = False
    attempt = 1

    # Gives the player up to six attempts to guess the word
    while attempt <= 6:
        print("Attempt", attempt, "of 6")

        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)

        # Evaluates and displays feedback for the player's guess
        feedback = evaluate_guess(guess, secret_word)
        display_guess(guess, feedback)

        # Ends the guessing loop if the player guesses correctly
        if has_won(guess, secret_word):
            print("Congratulations! You solved the puzzle.")
            won = True
            break

        attempt = attempt + 1
    # Reveals the secret word if the player runs out of attempts
    if not won:
        print("Sorry, you ran out of attempts!")
        print("The secret word was:", secret_word)

    # Asks user if they want to play again
    play_again = input("Would you like to play again? (yes/no): ").lower()

print("Thanks for playing!")