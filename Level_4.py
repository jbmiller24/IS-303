#create the list
expenses = []
#declare variables
small_count = 0
moderate_count = 0
large_count = 0
#create the loop for the user to put in expenses
while True:
    expense = float(input("Enter an expense or 0 to finish: "))
    #end the loop once user puts in zero
    if expense == 0:
        break
    #if user puts an invalid expense then loop to beginning
    if expense < 0:
        print("Invalid expense. Try again.")
        continue
   #add the expense to the list 
    expenses.append(expense)
    #classify each expense
    if expense < 25:
        small_count += 1
    elif expense <= 100:
        moderate_count += 1
    else:
        large_count += 1
#print out summary
print("Expense Summary")
print(f"Number of Expenses: {len(expenses)}")
print(f"Total: ${sum(expenses):,.2f}")
if len(expenses) > 0:
    print(f"Average: ${sum(expenses) / len(expenses):,.2f}")
    print(f"Smallest Expense: ${min(expenses):,.2f}")
    print(f"Largest Expense: ${max(expenses):,.2f}")
else:
    print("No expenses entered.")
print(f"Small Expenses: {small_count}")
print(f"Moderate Expenses: {moderate_count}")
print(f"Large Expenses: {large_count}")