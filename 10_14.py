has_error = True

while has_error:
    try:
        number = int(input("Enter a number: "))
        print(number)

        has_error = False

    except ValueError:
        print("Invalid number. Please try again.")
    except KeyboardInterrupt:
        print("You stopped the program")
    except:
        print("You got some rando error")
        break

def withdraw(amount, balance):
    if amount > balance:
        raise Exception("Insufficient Funds")

    return balance - amount

from BankFunctions import withdraw

balance = 100

try: 
    amount = int(input("Please enter the amount you would like to withdraw: "))

    balance = withdraw(amount, balance)
except:
    print("There")