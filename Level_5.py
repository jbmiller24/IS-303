import random
def get_player_choice():
    while True:
        player_choice = input("Enter Rock, Paper, Scissors: ").lower()

        if player_choice not in ["rock", "paper", "scissors"]:
            print(f"Sorry, {player_choice} is not a valid choice. Please try again.")
        else:
            return player_choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif player_choice == "rock" and computer_choice == "scissors":
        return "win"
    elif player_choice == "rock" and computer_choice == "paper":
        return "loss"
    elif player_choice == "paper" and computer_choice == "rock":
        return "win"
    elif player_choice == "paper" and computer_choice == "scissors":
        return "loss"
    elif player_choice == "scissors" and computer_choice == "paper":
        return "win"
    elif player_choice == "scissors" and computer_choice == "rock":
        return "loss"



#Welcome user to the game
print("Welcome to Rock Paper Scissors!")
player_wins = 0
computer_wins = 0
rounds_played = 0
while True:
    round_count = int(input("How many rounds would you like to play: "))
    if round_count % 2 == 0:
        print("Sorry the number must be an odd number. Please try again: ")
    else:
         break
while rounds_played < round_count:
    player_choice = get_player_choice()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(player_choice, computer_choice)
    print(f"The computer chose {computer_choice}")
    if result == "win":
         player_wins += 1
         rounds_played += 1
         print("You won!")
    elif result == "loss":
         rounds_played += 1
         computer_wins += 1
         print("You lost!")
    elif result == "tie":
         print("You tied! Play again.")
         

#Game Summary
print(f"Score - You: {player_wins} | Computer: {computer_wins}")
if player_wins > computer_wins:
    print("You won against the computer!!")
elif player_wins < computer_wins:
    print("You lost against the computer!!")
else:
    print("You tied with the computer!!")

print("Thanks for playing!")