#Establish variables and import the random generator module
import random
while True:
    secret_number = random.randint(1, 100)
    guess_count = 0
    #Start the game and make the user input a number
    print("I'm thinking of a # from 1 to 100.")
    while True:
        guess = int(input("Enter your guess: "))
        #Check if number is between 1 and 100 and valid
        if guess < 1 or guess > 100:
            print("Invalid guess. Enter a number between 1 and 100.")
            continue 
        #Increases each guess by 1
        guess_count += 1
        #This loop allows user to get closer to the random number and correctly guess it
        if guess > secret_number:
            print("Lower")
        elif guess < secret_number:
            print("Higher")
        else:
            print("Correct!")
            print(f"It took you {guess_count} guesses!")
            break
    #Allows user to get feedback and play again
    if guess_count <= 3:
        print("Amazing!")
    elif guess_count >= 4 and guess_count <= 5:
        print("Impressive!")
    elif guess_count >= 6 and guess_count <=7:
        print("Good job!")
    elif guess_count >= 8 and guess_count <=9:
        print("Took a little longer, but you got there!")
    else:
        print("You need to lock in.")

    print("Would you like to play again?")
    print("Respond with Y to play again")
    response = input().lower()
    if response != "y":
        print("Thanks for playing!")
        break