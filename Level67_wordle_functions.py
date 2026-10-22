import random
# Selects and returns a secret word
def choose_word():
    word_list = ["PLANT", "CRANE", "SLATE", "BRICK", "MOUSE", "PLANE", "HOUSE", "CLIMB"]
    secret_word = random.choice(word_list)
    return secret_word

# Gets and validates the player’s guess     
def get_guess(previous_guesses):
    while True:
        guess = input("Enter a five-letter word: ").upper()

        if len(guess) != 5 or not guess.isalpha():
            print("Please enter exactly five letters.")
        elif guess in previous_guesses:
            print("You already used that guess. Try again.")
        else:
            return guess
        
# Compares the guess with the secret word and returns feedback.
def evaluate_guess(guess, secret_word):
    feedback = []

    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback.append("G")
        elif guess[i] in secret_word:
            feedback.append("Y")
        else:
            feedback.append("-")

    return feedback

# Displays the guess and its feedback.
def display_guess(guess, feedback):
    print("Guess: ", end="")
    for letter in guess:
        print(letter, end=" ")
    print()

    print("Feedback: ", end="")
    for result in feedback:
        print(result, end=" ")
    print()

# Determines whether the player has guessed the word.
def has_won(guess, secret_word):
    return guess == secret_word
        