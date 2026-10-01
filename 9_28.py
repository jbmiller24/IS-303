import random

guess = 0
num_guesses = 0

def one_play(s):
    #Get and validate user input
    guess = int(input("Guess a number between 1 and 100: "))
    while not (guess>= 1 and guess <= 100):
        guess = int(input("Invalid number. Please try again: "))

    num_guesses += 1

    #Determine the need of guess adjustment
    if guess > solution:
        print("Lower")
    elif guess < solution:
        print("Higher")
    elif guess == solution:
        print("You got it right!")

print("Welcome to the Higher/Lower Game")

#Get a random number for the user to guess
solution = random.randint(1,100)

while guess!= solution:
    one_play(solution)

#Loop

print(f"It took you {num_guesses} guesses!")