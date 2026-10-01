#Here I define the variable and inputs
user_name = input("What is your name? ")
destination = input("Where are you going? " )
distance = float(input("How far is the trip in miles? "))
vehicle_mpg = float(input("What is your vehicle mpg? "))
gas_price = float(input("How much is gas per gallon? "))
number_of_travelers = int(input("How many travelers? "))

#Here are the calculations for the totals
round_trip = distance * 2
total_gallons = round_trip / vehicle_mpg
gas_cost = total_gallons*gas_price
traveler_cost = gas_cost/number_of_travelers

#Here is where I print a summary for the traveler
print("Trip Summary")
print()
print("Traveler Name: " + user_name.upper())
print()
print("Destination: " + destination.upper())
print()
print("Total Cost: $" + f"{gas_cost:.2f}")
print()
print("Cost per Traveler: $" + f"{traveler_cost:.2f}")

